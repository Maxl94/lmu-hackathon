from types import SimpleNamespace
from typing import Any

import pytest

from app.agent_client import (
    AgentFallbackError,
    AgentTrack,
    GeminiAgentClient,
    dedupe_and_sort_tracks,
    extract_discogs_release_ids,
    grounding_urls,
    parse_answer,
)
from app.config import Settings


class FakeModelsAPI:
    def __init__(self, responses: list[Any]) -> None:
        self._responses = list(responses)
        self.calls: list[dict[str, Any]] = []

    def generate_content(self, **kwargs: Any) -> Any:
        self.calls.append(kwargs)
        next_item = self._responses.pop(0)
        if isinstance(next_item, Exception):
            raise next_item
        return next_item


class FakeGenaiClient:
    def __init__(self, responses: list[Any]) -> None:
        self.models = FakeModelsAPI(responses)


def _make_response(text: str, uris: list[str] | None = None) -> Any:
    chunks = [SimpleNamespace(web=SimpleNamespace(uri=u)) for u in (uris or [])]
    candidate = SimpleNamespace(
        grounding_metadata=SimpleNamespace(grounding_chunks=chunks)
    )
    return SimpleNamespace(text=text, candidates=[candidate])


def test_parse_answer_raw_fenced_prose_and_errors() -> None:
    raw = '{"tracks":[{"disc":1,"number":1,"title":"Intro","length_sec":95}],"sources":["https://musicbrainz.org/1"]}'
    parsed_raw = parse_answer(raw)
    assert len(parsed_raw.tracks) == 1
    assert parsed_raw.tracks[0].title == "Intro"
    assert parsed_raw.tracks[0].length_sec == 95

    fenced = f"Here you go:\n```json\n{raw}\n```\nDone!"
    parsed_fenced = parse_answer(fenced)
    assert parsed_fenced.sources == ["https://musicbrainz.org/1"]

    with pytest.raises(ValueError):
        parse_answer("I could not find any JSON here.")

    with pytest.raises(ValueError):
        parse_answer("{not valid json}")


def test_extract_discogs_release_ids_and_dedupe() -> None:
    sources = [
        "https://musicbrainz.org/release/abc",
        "https://www.discogs.com/release/123456-Artist-Album",
        "http://discogs.com/de/release/98765-Another-Slug",
        "https://www.discogs.com/master/55555",
        "https://www.discogs.com/release/123456",
        "",
    ]
    assert extract_discogs_release_ids(sources) == [123456, 98765]


def test_dedupe_and_sort_tracks_and_grounding_urls() -> None:
    tracks = [
        AgentTrack(disc=2, number=1, title="Disc 2 First", length_sec=200),
        AgentTrack(disc=1, number=2, title="Second", length_sec=180),
        AgentTrack(disc=1, number=1, title="First", length_sec=120),
        AgentTrack(disc=1, number=1, title="Duplicate First", length_sec=999),
    ]
    cleaned = dedupe_and_sort_tracks(tracks)
    assert [(t.disc, t.number, t.title) for t in cleaned] == [
        (1, 1, "First"),
        (1, 2, "Second"),
        (2, 1, "Disc 2 First"),
    ]

    resp = SimpleNamespace(
        candidates=[
            SimpleNamespace(
                grounding_metadata=SimpleNamespace(
                    grounding_chunks=[
                        SimpleNamespace(web=SimpleNamespace(uri="https://a.example")),
                        SimpleNamespace(web=None),
                        SimpleNamespace(web=SimpleNamespace(uri="https://a.example")),
                        SimpleNamespace(web=SimpleNamespace(uri="https://b.example")),
                    ]
                )
            ),
            SimpleNamespace(grounding_metadata=None),
        ]
    )
    assert grounding_urls(resp) == ["https://a.example", "https://b.example"]
    assert grounding_urls(SimpleNamespace(candidates=None)) == []


def test_gemini_agent_client_happy_path_grounding_and_barcode_zero() -> None:
    json_without_sources = (
        '{"tracks":['
        '{"disc":1,"number":2,"title":"Track B","length_sec":null},'
        '{"disc":1,"number":1,"title":"Track A","length_sec":210}'
        '],"sources":[]}'
    )
    fake_genai = FakeGenaiClient(
        [_make_response(json_without_sources, uris=["https://source-from-grounding.test/album"])]
    )
    settings = Settings(google_genai_model="gemini-3.8-flash", gemini_api_key="real-key")
    client = GeminiAgentClient(settings, genai_client=fake_genai)

    ans = client.research_album("0", "Test Album", "Test Artist")
    assert client.model_name == "gemini-3.8-flash"
    assert [t.title for t in ans.tracks] == ["Track A", "Track B"]
    assert ans.sources == ["https://source-from-grounding.test/album"]
    sent_prompt = fake_genai.models.calls[0]["contents"]
    assert "barcode (EAN/UPC): unknown" in sent_prompt


def test_gemini_agent_client_restructure_empty_retry_and_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.agent_client.time.sleep", lambda _: None)

    # 1. Free-text answer triggers _restructure() fallback
    fake_restructure = FakeGenaiClient(
        [
            _make_response("1. Alpha (3:00)\n2. Beta"),
            _make_response(
                '{"tracks":[{"disc":1,"number":1,"title":"Alpha","length_sec":180}],'
                '"sources":["https://restructured.test"]}'
            ),
        ]
    )
    c1 = GeminiAgentClient(Settings(agent_max_attempts=2), genai_client=fake_restructure)
    ans1 = c1.research_album("1234567890123", "Album", "Artist")
    assert len(fake_restructure.models.calls) == 2
    assert ans1.tracks[0].title == "Alpha"
    assert ans1.sources == ["https://restructured.test"]

    # 2. Empty tracks returned -> empty AgentAnswer
    fake_empty = FakeGenaiClient(
        [_make_response('{"tracks":[],"sources":["https://ignored.test"]}')]
    )
    c2 = GeminiAgentClient(Settings(agent_max_attempts=1), genai_client=fake_empty)
    ans2 = c2.research_album("", "Nothing", "Nobody")
    assert ans2.tracks == []
    assert ans2.sources == []

    # 3. Transient failure followed by recovery on retry
    fake_retry = FakeGenaiClient(
        [
            RuntimeError("429 temporary"),
            _make_response(
                '{"tracks":[{"disc":1,"number":1,"title":"Recovered","length_sec":100}],'
                '"sources":["https://ok.test"]}'
            ),
        ]
    )
    c3 = GeminiAgentClient(Settings(agent_max_attempts=2), genai_client=fake_retry)
    ans3 = c3.research_album("", "Retry Album", "Retry Artist")
    assert [t.title for t in ans3.tracks] == ["Recovered"]

    # 4. Persistent failure raises AgentFallbackError
    fake_fail = FakeGenaiClient([RuntimeError("err1"), RuntimeError("err2")])
    c4 = GeminiAgentClient(Settings(agent_max_attempts=2), genai_client=fake_fail)
    with pytest.raises(AgentFallbackError):
        c4.research_album("", "Fail Album", "Fail Artist")


def test_gemini_agent_client_requires_configured_key() -> None:
    c = GeminiAgentClient(Settings(gemini_api_key=""))
    with pytest.raises(AgentFallbackError):
        c.research_album("", "Album", "Artist")


def test_gemini_agent_client_extracts_token_usage_and_cost() -> None:
    usage = SimpleNamespace(
        prompt_token_count=1000,
        candidates_token_count=400,
        thoughts_token_count=100,
    )
    resp = SimpleNamespace(
        text='{"tracks": [{"disc": 1, "number": 1, "title": "Song A", "length_sec": 180}], "sources": ["https://example.com"]}',
        candidates=[],
        usage_metadata=usage,
    )
    client = GeminiAgentClient(Settings(), genai_client=FakeGenaiClient([resp]))
    ans = client.research_album("", "Album", "Artist")
    assert ans.input_tokens == 1000
    assert ans.output_tokens == 500
    # (1000 / 1_000_000) * 0.75 + (500 / 1_000_000) * 3.75 = 0.00075 + 0.001875 = 0.002625
    assert ans.cost_usd == pytest.approx(0.002625)
