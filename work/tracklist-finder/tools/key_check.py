#!/usr/bin/env python3
"""Prüft alle Keys aus .env mit je einer minimalen Anfrage. Gibt nie Key-Werte aus. Nur Standardbibliothek.

Aufruf:  uv run python tools/key_check.py            # alle Dienste
         uv run python tools/key_check.py discogs tidal
Status:  OK · FEHLT (kein Key in .env) · FEHLER (Key gesetzt, Anfrage scheitert)
"""
from __future__ import annotations

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EAN_KOK = "4019593960000"        # Bushido – King of Kingz (Exclusive 2004 Edition), physische CD
UPC_RAM_DIGITAL = "886443927087"  # Daft Punk – Random Access Memories, digitale Ausgabe


def load_env(path: Path) -> dict[str, str]:
    vals: dict[str, str] = {}
    if not path.exists():
        return vals
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        k, v = k.strip(), v.strip()
        if v[:1] in ("'", '"'):
            end = v.find(v[0], 1)
            v = v[1:end] if end > 0 else v[1:]
        else:
            v = re.split(r"\s+#", v, maxsplit=1)[0].strip()
        vals[k] = v
    return vals


ENV = load_env(ROOT / ".env")


def get(k: str) -> str:
    return ENV.get(k) or os.environ.get(k, "")


_SECRET_HINTS = ("KEY", "TOKEN", "SECRET", "PASSWORD", "QUERY_ID", "PROXY")
SECRETS = sorted(
    {v for k, v in {**os.environ, **ENV}.items() if v and len(v) >= 8 and any(h in k for h in _SECRET_HINTS)},
    key=len, reverse=True,
)


def scrub(text: object) -> str:
    t = str(text)
    for s in SECRETS:
        t = t.replace(s, "***")
    return t[:220]


class Missing(Exception):
    pass


class Fail(Exception):
    pass


def need(*keys: str) -> list[str]:
    missing = [k for k in keys if not get(k)]
    if missing:
        raise Missing(", ".join(missing))
    return [get(k) for k in keys]


def basic(user: str, pw: str) -> str:
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def req(method, url, *, headers=None, data=None, form=None, timeout=25):
    h = {"User-Agent": "gema-hackathon-keycheck/0.1", "Accept": "application/json"}
    h.update(headers or {})
    body = None
    if form is not None:
        body = urllib.parse.urlencode(form).encode()
        h.setdefault("Content-Type", "application/x-www-form-urlencoded")
    elif data is not None:
        body = json.dumps(data).encode()
        h.setdefault("Content-Type", "application/json")
    r = urllib.request.Request(url, data=body, method=method, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            code, hdrs, raw = resp.status, resp.headers, resp.read()
    except urllib.error.HTTPError as e:
        code, hdrs, raw = e.code, e.headers, e.read()
    except Exception as e:  # noqa: BLE001
        raise Fail(f"nicht erreichbar: {type(e).__name__}: {e}") from None
    hdrs = {k.lower(): v for k, v in hdrs.items()}
    js: dict = {}
    try:
        parsed = json.loads(raw) if raw else {}
        js = parsed if isinstance(parsed, dict) else {"_list": parsed}
    except ValueError:
        pass
    return code, hdrs, js, raw


def errmsg(js, raw=b"") -> str:
    if isinstance(js, dict):
        e = js.get("error") or js.get("message") or js.get("errors") or js.get("detail") or js.get("error_description")
        if isinstance(e, dict):
            e = e.get("message") or e.get("type") or e
        if isinstance(e, list) and e:
            e = e[0].get("detail") or e[0].get("message") or e[0] if isinstance(e[0], dict) else e[0]
        if e:
            return str(e)
    return raw[:120].decode("utf-8", "replace") if raw else ""


def expect(code, js, raw, what):
    if code != 200:
        raise Fail(f"{what}: HTTP {code} {errmsg(js, raw)}")


# --------------------------------------------------------------------------- LLM

def c_saia():
    (k,) = need("SAIA_API_KEY")
    base = (get("SAIA_BASE_URL") or "https://chat-ai.academiccloud.de/v1").rstrip("/")
    auth = {"Authorization": f"Bearer {k}"}
    code, _, js, raw = req("GET", f"{base}/models", headers=auth)
    expect(code, js, raw, "/models")
    n = len(js.get("data", []))
    model = get("SAIA_MODEL") or "glm-5.3-flash"
    code, h, js, raw = req("POST", f"{base}/chat/completions", headers=auth,
                           data={"model": model, "messages": [{"role": "user", "content": "Sag ok."}], "max_tokens": 16})
    expect(code, js, raw, f"chat {model}")
    # SAIA-Header: x-ratelimit-{limit,remaining}-requests-{10s,hour,day} (ältere Doku: -minute/-hour/-day/-month)
    windows = [m.group(1) for k in h if (m := re.fullmatch(r"x-ratelimit-limit-(?:requests-)?(\w+)", k))]
    def hv(kind, w):
        return h.get(f"x-ratelimit-{kind}-requests-{w}") or h.get(f"x-ratelimit-{kind}-{w}") or "?"
    lim = " ".join(f"{w}={hv('remaining', w)}/{hv('limit', w)}" for w in windows)
    return f"{n} Modelle, Chat mit {model} ok. Limits (frei/gesamt): {lim or 'keine Header'}"


def c_anthropic():
    (k,) = need("ANTHROPIC_API_KEY")
    code, _, js, raw = req("GET", "https://api.anthropic.com/v1/models?limit=100",
                           headers={"x-api-key": k, "anthropic-version": "2023-06-01"})
    expect(code, js, raw, "/v1/models")
    ids = [m["id"] for m in js.get("data", [])]
    want = get("ANTHROPIC_MODEL") or "claude-opus-5-5"
    return f"{len(ids)} Modelle, {want} {'verfügbar' if want in ids else 'NICHT in der Liste'}"


def c_openai():
    (k,) = need("OPENAI_API_KEY")
    base = (get("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
    code, _, js, raw = req("GET", f"{base}/models", headers={"Authorization": f"Bearer {k}"})
    expect(code, js, raw, "/models")
    return f"{len(js.get('data', []))} Modelle"


def c_azure():
    need("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_ENDPOINT")
    return "gesetzt (nicht automatisch getestet)"


def c_openrouter():
    (k,) = need("OPENROUTER_API_KEY")
    code, _, js, raw = req("GET", "https://openrouter.ai/api/v1/key", headers={"Authorization": f"Bearer {k}"})
    expect(code, js, raw, "/key")
    d = js.get("data", {})
    return f"Key ok, Limit {d.get('limit')}, verbraucht {d.get('usage')}"


# --------------------------------------------------------------------------- Suche & Scraping

def c_brave():
    (k,) = need("BRAVE_SEARCH_API_KEY")
    q = urllib.parse.quote("Bushido King of Kingz Tracklist")
    code, h, js, raw = req("GET", f"https://api.search.brave.com/res/v1/web/search?q={q}&count=3",
                           headers={"X-Subscription-Token": k})
    expect(code, js, raw, "web/search")
    n = len((js.get("web") or {}).get("results", []))
    return f"{n} Treffer, Rate-Limit frei: {h.get('x-ratelimit-remaining', '?')}"


def c_tavily():
    (k,) = need("TAVILY_API_KEY")
    code, _, js, raw = req("POST", "https://api.tavily.com/search", headers={"Authorization": f"Bearer {k}"},
                           data={"query": "Bushido King of Kingz tracklist", "max_results": 2})
    expect(code, js, raw, "search")
    return f"{len(js.get('results', []))} Treffer"


def c_exa():
    (k,) = need("EXA_API_KEY")
    code, _, js, raw = req("POST", "https://api.exa.ai/search", headers={"x-api-key": k},
                           data={"query": "Bushido King of Kingz tracklist", "numResults": 2})
    expect(code, js, raw, "search")
    return f"{len(js.get('results', []))} Treffer"


def c_serpapi():
    (k,) = need("SERPAPI_API_KEY")
    code, _, js, raw = req("GET", f"https://serpapi.com/account.json?api_key={urllib.parse.quote(k)}")
    expect(code, js, raw, "account")
    return f"Plan {js.get('plan_name')}, Suchen übrig: {js.get('total_searches_left')}"


def c_firecrawl():
    (k,) = need("FIRECRAWL_API_KEY")
    base = (get("FIRECRAWL_API_URL") or "https://api.firecrawl.dev").rstrip("/")
    code, _, js, raw = req("POST", f"{base}/v1/scrape", headers={"Authorization": f"Bearer {k}"},
                           data={"url": "https://example.com", "formats": ["markdown"]}, timeout=60)
    expect(code, js, raw, "scrape")
    md = ((js or {}).get("data") or {}).get("markdown", "")
    return f"scrape ok ({len(md)} Zeichen Markdown)"


def c_jina():
    (k,) = need("JINA_API_KEY")
    code, _, js, raw = req("GET", "https://r.jina.ai/https://example.com",
                           headers={"Authorization": f"Bearer {k}", "Accept": "text/plain"}, timeout=40)
    expect(code, js, raw, "reader")
    return f"reader ok ({len(raw)} Bytes)"


# --------------------------------------------------------------------------- Musik

def c_musicbrainz():
    ua = get("MUSICBRAINZ_USER_AGENT")
    if not ua or "<" in ua:
        raise Missing("MUSICBRAINZ_USER_AGENT (Kontakt-Platzhalter ersetzen)")
    code, _, js, raw = req("GET", f"https://musicbrainz.org/ws/2/release?query=barcode:{EAN_KOK}&fmt=json",
                           headers={"User-Agent": ua})
    expect(code, js, raw, "release search")
    return f"Barcode-Suche ok ({js.get('count')} Treffer)"


def c_discogs():
    (k,) = need("DISCOGS_USER_TOKEN")
    code, h, js, raw = req("GET", "https://api.discogs.com/oauth/identity",
                           headers={"Authorization": f"Discogs token={k}"})
    expect(code, js, raw, "identity")
    code, h, js, raw = req("GET", f"https://api.discogs.com/database/search?barcode={EAN_KOK}",
                           headers={"Authorization": f"Discogs token={k}"})
    expect(code, js, raw, "search")
    return f"Token ok, Barcode-Suche {len(js.get('results', []))} Treffer, Limit {h.get('x-discogs-ratelimit')}/min"


def c_tidal():
    cid, sec = need("TIDAL_CLIENT_ID", "TIDAL_CLIENT_SECRET")
    code, _, js, raw = req("POST", "https://auth.tidal.com/v1/oauth2/token",
                           headers={"Authorization": basic(cid, sec)}, form={"grant_type": "client_credentials"})
    expect(code, js, raw, "token")
    tok = js["access_token"]
    out = []
    for upc in (UPC_RAM_DIGITAL, EAN_KOK):
        code, _, js, raw = req("GET", f"https://openapi.tidal.com/v2/albums?countryCode=DE&filter%5BbarcodeId%5D={upc}",
                               headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.api+json"})
        expect(code, js, raw, f"albums {upc}")
        items = js.get("data") or []
        title = (items[0].get("attributes") or {}).get("title") if items else None
        out.append(f"{upc}: {title or 'kein Treffer'}")
    return "Token ok · " + " · ".join(out)


def c_lastfm():
    (k,) = need("LASTFM_API_KEY")
    q = urllib.parse.urlencode({"method": "album.getinfo", "artist": "Bushido", "album": "King of Kingz",
                                "api_key": k, "format": "json"})
    code, _, js, raw = req("GET", f"https://ws.audioscrobbler.com/2.0/?{q}")
    if code != 200 or (js or {}).get("error"):
        raise Fail(f"album.getinfo: HTTP {code} {errmsg(js, raw)}")
    tracks = ((js.get("album") or {}).get("tracks") or {}).get("track") or []
    tracks = tracks if isinstance(tracks, list) else [tracks]
    with_dur = sum(1 for t in tracks if t.get("duration"))
    return f"album.getinfo ok: {len(tracks)} Tracks, {with_dur} mit Dauer"


def c_genius():
    (k,) = need("GENIUS_ACCESS_TOKEN")
    code, _, js, raw = req("GET", "https://api.genius.com/search?q=" + urllib.parse.quote("Bushido King of Kingz"),
                           headers={"Authorization": f"Bearer {k}"})
    expect(code, js, raw, "search")
    return f"{len(((js or {}).get('response') or {}).get('hits', []))} Treffer"


def c_spotify():
    cid, sec = need("SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET")
    code, _, js, raw = req("POST", "https://accounts.spotify.com/api/token",
                           headers={"Authorization": basic(cid, sec)}, form={"grant_type": "client_credentials"})
    expect(code, js, raw, "token")
    code, _, js, raw = req("GET", f"https://api.spotify.com/v1/search?q=upc:{UPC_RAM_DIGITAL}&type=album&limit=1",
                           headers={"Authorization": f"Bearer {js['access_token']}"})
    expect(code, js, raw, "search upc")
    items = ((js.get("albums") or {}).get("items")) or []
    return f"UPC-Suche: {items[0]['name'] if items else 'kein Treffer'}"


def c_youtube():
    (k,) = need("YOUTUBE_API_KEY")
    q = urllib.parse.urlencode({"part": "snippet", "type": "video", "maxResults": 2,
                                "q": "Bushido King of Kingz full album", "key": k})
    code, _, js, raw = req("GET", f"https://www.googleapis.com/youtube/v3/search?{q}")
    expect(code, js, raw, "search")
    return f"{len(js.get('items', []))} Videos"


# --------------------------------------------------------------------------- Marktplätze / Bibliotheken / EAN

def c_ebay():
    cid, sec = need("EBAY_CLIENT_ID", "EBAY_CLIENT_SECRET")
    code, _, js, raw = req("POST", "https://api.ebay.com/identity/v1/oauth2/token",
                           headers={"Authorization": basic(cid, sec)},
                           form={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"})
    expect(code, js, raw, "token")
    code, _, js, raw = req("GET", f"https://api.ebay.com/buy/browse/v1/item_summary/search?gtin={EAN_KOK}&limit=3",
                           headers={"Authorization": f"Bearer {js['access_token']}",
                                    "X-EBAY-C-MARKETPLACE-ID": get("EBAY_MARKETPLACE_ID") or "EBAY_DE"})
    expect(code, js, raw, "browse search gtin")
    return f"GTIN-Suche: {js.get('total', 0)} Angebote"


def c_dnb():
    (k,) = need("DNB_SRU_ACCESS_TOKEN")
    q = urllib.parse.urlencode({"version": "1.1", "operation": "searchRetrieve", "query": f"num={EAN_KOK}",
                                "recordSchema": "MARC21-xml", "maximumRecords": 1, "accessToken": k})
    code, _, _, raw = req("GET", f"https://services.dnb.de/sru/dnb.dma?{q}", headers={"Accept": "application/xml"})
    if code != 200:
        raise Fail(f"SRU HTTP {code}")
    m = re.search(rb"numberOfRecords>(\d+)<", raw)
    return f"SRU ok, {m.group(1).decode() if m else '?'} Treffer"


def c_opengtindb():
    (k,) = need("OPENGTINDB_QUERY_ID")
    q = urllib.parse.urlencode({"ean": EAN_KOK, "cmd": "query", "queryid": k})
    code, _, _, raw = req("GET", f"https://opengtindb.org/?{q}", headers={"Accept": "text/plain"})
    if code != 200:
        raise Fail(f"HTTP {code}")
    first = raw.decode("utf-8", "replace").strip().splitlines()[:2]
    return " | ".join(first)


def c_upcitemdb():
    (k,) = need("UPCITEMDB_API_KEY")
    code, _, js, raw = req("GET", f"https://api.upcitemdb.com/prod/v1/lookup?upc={EAN_KOK}",
                           headers={"user_key": k, "key_type": "3scale"})
    expect(code, js, raw, "lookup")
    return f"{js.get('total')} Treffer"


CHECKS = {
    "saia": c_saia, "anthropic": c_anthropic, "openai": c_openai, "azure": c_azure, "openrouter": c_openrouter,
    "brave": c_brave, "tavily": c_tavily, "exa": c_exa, "serpapi": c_serpapi, "firecrawl": c_firecrawl, "jina": c_jina,
    "musicbrainz": c_musicbrainz, "discogs": c_discogs, "tidal": c_tidal, "lastfm": c_lastfm, "genius": c_genius,
    "spotify": c_spotify, "youtube": c_youtube,
    "ebay": c_ebay, "dnb": c_dnb, "opengtindb": c_opengtindb, "upcitemdb": c_upcitemdb,
}


def run(name):
    try:
        return name, "OK", CHECKS[name]()
    except Missing as e:
        return name, "FEHLT", str(e)
    except Fail as e:
        return name, "FEHLER", scrub(e)
    except Exception as e:  # noqa: BLE001
        return name, "FEHLER", scrub(f"{type(e).__name__}: {e}")


def main(argv):
    names = [n for n in (argv or CHECKS) if n in CHECKS]
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(run, names))
    w = max(len(n) for n in names)
    for name, status, detail in results:
        print(f"{name:<{w}}  {status:<6}  {scrub(detail)}")
    ok = sum(1 for _, s, _ in results if s == "OK")
    print(f"\n{ok}/{len(results)} OK · fehlend: {sum(1 for _, s, _ in results if s == 'FEHLT')}"
          f" · Fehler: {sum(1 for _, s, _ in results if s == 'FEHLER')}")


if __name__ == "__main__":
    main(sys.argv[1:])
