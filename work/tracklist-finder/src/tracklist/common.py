"""Gemeinsame Hilfen für alle tl-* Tools.

- .env laden (Repo-Root), Keys nie ausgeben
- HTTP mit Datei-Cache (.cache/http), prozessübergreifendem Rate-Limit pro Host und Proxy pro Dienst
- knappe Ausgaben: Was ein Tool druckt, landet im Kontext des Modells → nur das Nötige, begrenzt, mit Hinweis
"""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import httpx
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

CACHE_DIR = ROOT / (os.environ.get("HTTP_CACHE_DIR") or ".cache/http")
RL_DIR = ROOT / ".cache/ratelimit"
CACHE_TTL = float(os.environ.get("HTTP_CACHE_TTL_HOURS") or 168) * 3600

# Mindestabstand zwischen Requests pro Host (Sekunden), gilt über alle parallelen Agent-Sessions hinweg
HOST_INTERVAL = {
    "musicbrainz.org": 1.1,
    "api.genius.com": 0.2,
    "api.discogs.com": 1.05,
    "itunes.apple.com": 3.0,
    "coverartarchive.org": 0.2,
    "api.deezer.com": 0.12,
    "ws.audioscrobbler.com": 0.25,
    "api.search.brave.com": 0.05,
}

# Proxy-Zuordnung: Host-Muster → Env-Variable
PROXY_ENV = [
    ("musicbrainz.org", "MUSICBRAINZ_PROXY"),
    ("discogs.com", "DISCOGS_PROXY"),
    ("search.brave.com", "WEBSEARCH_PROXY"),
]

UA_DEFAULT = "gema-hackathon-tracklist/0.1"


class ToolError(Exception):
    """Fehler, die dem Agenten als knappe Meldung gezeigt werden."""


def env(name: str, default: str = "") -> str:
    return (os.environ.get(name) or default).strip()


def die(msg: str, code: int = 2) -> None:
    print(f"ERROR: {msg}")
    sys.exit(code)


def proxy_for(url: str, scraper: bool = False) -> str | None:
    host = urlparse(url).hostname or ""
    for pat, var in PROXY_ENV:
        if pat in host and env(var):
            return env(var)
    if scraper and env("SCRAPER_PROXY"):
        return env("SCRAPER_PROXY")
    return None


def _rate_limit(host: str) -> None:
    interval = next((v for k, v in HOST_INTERVAL.items() if host.endswith(k)), 0)
    if not interval:
        return
    RL_DIR.mkdir(parents=True, exist_ok=True)
    path = RL_DIR / host
    with open(path, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            last = float(f.read().strip() or 0)
        except ValueError:
            last = 0.0
        wait = last + interval - time.time()
        if wait > 0:
            time.sleep(wait)
        f.seek(0)
        f.truncate()
        f.write(str(time.time()))
        fcntl.flock(f, fcntl.LOCK_UN)


def _cache_key(method: str, url: str, params, body) -> Path:
    raw = json.dumps([method, url, params, body], sort_keys=True, default=str)
    return CACHE_DIR / (hashlib.sha1(raw.encode()).hexdigest() + ".json")


def http(method: str, url: str, *, params=None, headers=None, json_body=None, data=None, timeout: float = 30,
         cache: bool = True, ttl: float | None = None, retries: int = 3, scraper: bool = False,
         follow: bool = True) -> tuple[int, dict, str, str]:
    """→ (status, headers, text, final_url). Cacht nur 200er."""
    key = _cache_key(method, url, params, json_body or data) if cache else None
    if key and key.exists() and time.time() - key.stat().st_mtime < (ttl or CACHE_TTL):
        c = json.loads(key.read_text())
        return c["status"], c["headers"], c["text"], c.get("url", url)
    h = {"User-Agent": UA_DEFAULT}
    h.update(headers or {})
    host = urlparse(url).hostname or ""
    if host.endswith("musicbrainz.org"):
        retries = max(retries, 5)  # MB antwortet unter Last oft 502/503 → länger warten
    last_err = None
    for attempt in range(retries + 1):
        _rate_limit(host)
        try:
            with httpx.Client(proxy=proxy_for(url, scraper), timeout=timeout, follow_redirects=follow) as c:
                r = c.request(method, url, params=params, headers=h, json=json_body, data=data)
        except httpx.HTTPError as e:
            last_err = f"{type(e).__name__}: {e}"
            time.sleep(1.5 * (attempt + 1))
            continue
        if r.status_code in (429, 502, 503, 504) and attempt < retries:
            ra = r.headers.get("retry-after")
            time.sleep(max(float(ra) if ra and ra.replace(".", "").isdigit() else 0, 2.0 * (attempt + 1)))
            continue
        hdrs = {k.lower(): v for k, v in r.headers.items()}
        if key and r.status_code == 200:
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            key.write_text(json.dumps({"status": r.status_code, "headers": hdrs, "text": r.text, "url": str(r.url)}))
        return r.status_code, hdrs, r.text, str(r.url)
    raise ToolError(f"{host} not reachable ({last_err})")


def get_json(url: str, **kw) -> dict:
    status, _, text, _ = http("GET", url, **kw)
    if status != 200:
        snippet = re.sub(r"\s+", " ", text[:200])
        raise ToolError(f"HTTP {status} von {urlparse(url).hostname}: {snippet}")
    try:
        return json.loads(text)
    except ValueError:
        raise ToolError(f"keine JSON-Antwort von {urlparse(url).hostname}") from None


def fetch_bytes(url: str, timeout: float = 60) -> tuple[bytes, str]:
    """Binärdaten (Bilder) mit eigenem Cache. → (bytes, content_type)"""
    d = ROOT / ".cache/blobs"
    d.mkdir(parents=True, exist_ok=True)
    k = hashlib.sha1(url.encode()).hexdigest()
    p, meta = d / k, d / (k + ".type")
    if p.exists() and meta.exists():
        return p.read_bytes(), meta.read_text()
    _rate_limit(urlparse(url).hostname or "")
    with httpx.Client(proxy=proxy_for(url, scraper=True), timeout=timeout, follow_redirects=True,
                      headers={"User-Agent": env("SCRAPER_USER_AGENT") or UA_DEFAULT}) as c:
        r = c.get(url)
    if r.status_code != 200:
        raise ToolError(f"HTTP {r.status_code} beim Laden von {url}")
    ctype = r.headers.get("content-type", "application/octet-stream").split(";")[0]
    p.write_bytes(r.content)
    meta.write_text(ctype)
    return r.content, ctype


# ---------------------------------------------------------------- Ausgabe

def mmss(seconds: float | int | None) -> str:
    if seconds is None:
        return "?:??"
    s = int(round(seconds))
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def parse_duration(text: str | None) -> int | None:
    """'4:35' / '1:02:03' / '275' → Sekunden."""
    if not text:
        return None
    t = str(text).strip()
    if re.fullmatch(r"\d+", t):
        return int(t)
    m = re.fullmatch(r"(?:(\d+):)?(\d{1,3}):(\d{2})", t)
    if not m:
        return None
    h, mi, s = int(m.group(1) or 0), int(m.group(2)), int(m.group(3))
    return h * 3600 + mi * 60 + s


def clip(lines: list[str], limit: int, hint: str = "narrow the filter or raise --limit.") -> list[str]:
    if limit <= 0 or len(lines) <= limit:
        return lines
    return lines[:limit] + [f"... {len(lines) - limit} weitere ausgeblendet. {hint}"]


def clip_text(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n... [{len(text) - max_chars} chars cut off, raise --max or use --grep]"


def live(event: str, **kw) -> None:
    """Live-Ereignis für die Oberfläche (output/<id>.events.jsonl, Pfad aus $TL_LIVE_LOG). Fehler hier nie durchreichen."""
    path = os.environ.get("TL_LIVE_LOG")
    if not path:
        return
    try:
        import json as _json
        import time as _time
        with open(path, "a") as f:
            f.write(_json.dumps({"ts": round(_time.time(), 2), "event": event, **kw}, ensure_ascii=False) + "\n")
    except OSError:
        pass


def run_cli(main) -> None:
    """Einheitliche Fehlerbehandlung für alle Tools (+ Live-Ereignisse tool_start/tool_end)."""
    import sys as _sys
    import time as _time
    tool = os.path.basename(_sys.argv[0]) if _sys.argv else "?"
    if not tool.startswith("tl-"):
        tool = "tl-" + (os.environ.get("TL_TOOL_NAME") or tool.rsplit(".", 1)[0])
    args = " ".join(_sys.argv[1:])[:300]
    t0 = _time.time()
    live("tool_start", tool=tool, args=args)
    ok = False
    try:
        main()
        ok = True
    except ToolError as e:
        die(str(e))
    except KeyboardInterrupt:
        die("aborted", 130)
    except SystemExit as e:
        ok = not e.code
        raise
    except Exception as e:  # noqa: BLE001 – Agent soll eine Zeile sehen, keinen Traceback
        die(f"internal tool error: {type(e).__name__}: {str(e)[:200]} (try another tool/source)")
    finally:
        live("tool_end", tool=tool, args=args, seconds=round(_time.time() - t0, 1), ok=ok)
