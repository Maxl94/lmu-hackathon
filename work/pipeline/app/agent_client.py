import logging
import re
import threading
import time
from collections.abc import Callable
from typing import Any, Protocol

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from app.config import Settings
from app.cost import compute_token_cost

logger = logging.getLogger(__name__)

PLACEHOLDER_GEMINI_KEYS = {"PASTE_YOUR_GEMINI_API_KEY", "AQ.Ab8RN6LZCw-"}
DISCOGS_RELEASE_URL_RE = re.compile(
    r"https?://(?:www\.)?discogs\.com/(?:[a-z]{2}/)?release/(\d+)", re.IGNORECASE
)

PROMPT = """You are a music metadata researcher. Find the track list of one specific release using Google Search.

Release (from our catalogue; it may contain typos or format hints like "(2CD)" or "(LP)"):
- barcode (EAN/UPC): {barcode}
- album title: {album}
- album artist: {artist}

Rules:
1. If a barcode is given, search for it first (MusicBrainz, Discogs, shops, label or artist pages). Then search by artist and title.
2. The barcode identifies the exact edition. Use the edition that matches it (e.g. deluxe vs. standard, 1 vs. 2 discs). Without a barcode, use hints in the title ("(2CD)", "(LP)", ...) to choose the edition.
3. Take tracks ONLY from pages that your search returned. Never write tracks from memory. If you cannot find a track list you trust, return an empty "tracks" list.
4. "Various", "VA" and similar mean a compilation. "Name, Die" means "Die Name".
5. Keep track titles exactly as written on the source and do not translate them. "disc" starts at 1; "number" is the position on that disc (for vinyl, count continuously per record: A1, A2, B1 -> 1, 2, 3). Set "length_sec" to the duration in seconds, or null if the source gives none.
6. "sources" lists the URLs of the pages you took the tracks from.

Answer with a single JSON object and nothing else (no markdown, no comments):
{{"tracks": [{{"disc": 1, "number": 1, "title": "...", "length_sec": 215}}], "sources": ["https://..."]}}
"""


class AgentTrack(BaseModel):
    disc: int = 1
    number: int
    title: str
    length_sec: int | None = None


class AgentAnswer(BaseModel):
    tracks: list[AgentTrack] = Field(default_factory=list)
    sources: list[str] = Field(default_factory=list)
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0


def _extract_token_usage(response: Any) -> tuple[int, int]:
    """Extract (input_tokens, output_tokens) from Gemini usage_metadata."""
    usage = getattr(response, "usage_metadata", None)
    if usage is None:
        return 0, 0
    input_tokens = getattr(usage, "prompt_token_count", 0) or 0
    output_tokens = (getattr(usage, "candidates_token_count", 0) or 0) + (
        getattr(usage, "thoughts_token_count", 0) or 0
    )
    return int(input_tokens), int(output_tokens)


class AgentFallbackError(Exception):
    """Raised when the Gemini agent fallback fails across all retry attempts."""


class AgentFallbackProvider(Protocol):
    @property
    def model_name(self) -> str: ...

    def research_album(self, barcode: str, album: str, artist: str) -> AgentAnswer: ...


def parse_answer(text: str) -> AgentAnswer:
    """Extract and validate a JSON AgentAnswer from raw or fenced model output."""
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    start, end = cleaned.find("{"), cleaned.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("No JSON object found in agent response.")
    return AgentAnswer.model_validate_json(cleaned[start : end + 1])


def grounding_urls(response: Any) -> list[str]:
    """Extract unique web URIs returned in Gemini Google Search grounding metadata."""
    urls: list[str] = []
    for candidate in getattr(response, "candidates", None) or []:
        metadata = getattr(candidate, "grounding_metadata", None)
        chunks = getattr(metadata, "grounding_chunks", None) if metadata else None
        for chunk in chunks or []:
            web = getattr(chunk, "web", None)
            uri = getattr(web, "uri", None) if web else None
            if uri and uri not in urls:
                urls.append(uri)
    return urls


def dedupe_and_sort_tracks(tracks: list[AgentTrack]) -> list[AgentTrack]:
    """Sort tracks by (disc, number) and drop duplicate positions keeping the first."""
    deduped: dict[tuple[int, int], AgentTrack] = {}
    for track in sorted(tracks, key=lambda t: (t.disc, t.number)):
        deduped.setdefault((track.disc, track.number), track)
    return list(deduped.values())


def extract_discogs_release_ids(sources: list[str]) -> list[int]:
    """Extract unique positive Discogs release IDs from source URLs in appearance order."""
    ids: list[int] = []
    seen: set[int] = set()
    for src in sources:
        if not src:
            continue
        match = DISCOGS_RELEASE_URL_RE.search(src)
        if not match:
            continue
        rid = int(match.group(1))
        if rid > 0 and rid not in seen:
            seen.add(rid)
            ids.append(rid)
    return ids


class GeminiAgentClient:
    """Gemini + Google Search tracklist discovery fallback client."""

    def __init__(self, settings: Settings, genai_client: Any | None = None) -> None:
        self._settings = settings
        self._model_name = settings.google_genai_model
        self._external_client = genai_client
        self._owned_client: Any | None = None
        self._client_lock = threading.Lock()

    @property
    def model_name(self) -> str:
        return self._model_name

    def _get_client(self) -> Any:
        if self._external_client is not None:
            return self._external_client
        with self._client_lock:
            if self._owned_client is None:
                api_key = (self._settings.gemini_api_key or "").strip()
                if not api_key or api_key in PLACEHOLDER_GEMINI_KEYS:
                    raise AgentFallbackError("GEMINI_API_KEY is not configured.")
                self._owned_client = genai.Client(vertexai=False, api_key=api_key)
            return self._owned_client

    def close(self) -> None:
        with self._client_lock:
            if self._owned_client is not None:
                close_fn = getattr(self._owned_client, "close", None)
                if callable(close_fn):
                    close_fn()
                self._owned_client = None

    def _restructure(self, client: Any, text: str) -> tuple[AgentAnswer, int, int]:
        if not text.strip():
            return AgentAnswer(), 0, 0
        response = client.models.generate_content(
            model=self._model_name,
            contents=(
                "Convert the following text into the JSON schema. Use only information "
                "contained in the text. If it contains no track list, return empty lists.\n\n"
                + text
            ),
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=AgentAnswer,
                temperature=0,
            ),
        )
        in_tok, out_tok = _extract_token_usage(response)
        return AgentAnswer.model_validate_json(response.text or "{}"), in_tok, out_tok

    def _research_once(
        self,
        client: Any,
        barcode: str,
        album: str,
        artist: str,
        attempt: int = 1,
        attempts: int = 1,
        on_progress: Callable[[int, int, str], None] | None = None,
    ) -> AgentAnswer:
        prompt = PROMPT.format(
            barcode=barcode if barcode not in ("", "0") else "unknown",
            album=album,
            artist=artist,
        )
        if on_progress is not None:
            on_progress(
                attempt,
                attempts,
                f"Gemini + Google Search attempt {attempt}/{attempts} ({self._model_name})",
            )
        response = client.models.generate_content(
            model=self._model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                temperature=0,
            ),
        )
        total_in, total_out = _extract_token_usage(response)
        text = getattr(response, "text", None) or ""
        try:
            answer = parse_answer(text)
        except ValueError:
            logger.info("Agent output for %r required schema restructure fallback", album)
            if on_progress is not None:
                on_progress(
                    attempt,
                    attempts,
                    f"Attempt {attempt}/{attempts}: restructuring free-text output to JSON",
                )
            answer, rest_in, rest_out = self._restructure(client, text)
            total_in += rest_in
            total_out += rest_out

        cost_usd = compute_token_cost(total_in, total_out) if (total_in > 0 or total_out > 0) else 0.0
        tracks = dedupe_and_sort_tracks(answer.tracks)
        if not tracks:
            return AgentAnswer(
                input_tokens=total_in,
                output_tokens=total_out,
                cost_usd=cost_usd,
            )

        sources = [s for s in dict.fromkeys(src.strip() for src in answer.sources if src) if s]
        if not sources:
            sources = grounding_urls(response)
        return AgentAnswer(
            tracks=tracks,
            sources=sources,
            input_tokens=total_in,
            output_tokens=total_out,
            cost_usd=cost_usd,
        )

    def research_album_with_progress(
        self,
        barcode: str,
        album: str,
        artist: str,
        on_progress: Callable[[int, int, str], None] | None = None,
    ) -> AgentAnswer:
        client = self._get_client()
        attempts = max(1, self._settings.agent_max_attempts)
        last_exc: Exception | None = None
        for attempt in range(1, attempts + 1):
            try:
                logger.info(
                    "Gemini agent research attempt %s/%s for %s - %s (barcode=%s)",
                    attempt,
                    attempts,
                    artist,
                    album,
                    barcode or "-",
                )
                return self._research_once(
                    client,
                    barcode,
                    album,
                    artist,
                    attempt=attempt,
                    attempts=attempts,
                    on_progress=on_progress,
                )
            except Exception as exc:
                last_exc = exc
                logger.warning(
                    "Gemini agent attempt %s/%s failed for %s - %s: %s",
                    attempt,
                    attempts,
                    artist,
                    album,
                    exc,
                )
                if attempt < attempts:
                    delay = 2 ** (attempt + 1)
                    if on_progress is not None:
                        on_progress(
                            attempt,
                            attempts,
                            f"Attempt {attempt}/{attempts} failed; retrying in {delay}s",
                        )
                    time.sleep(delay)
        raise AgentFallbackError(
            f"Gemini agent fallback failed after {attempts} attempt(s): {last_exc}"
        ) from last_exc

    def research_album(self, barcode: str, album: str, artist: str) -> AgentAnswer:
        return self.research_album_with_progress(barcode, album, artist, on_progress=None)
