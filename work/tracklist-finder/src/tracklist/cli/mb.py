"""tl-mb — MusicBrainz (free, 1 req/s, rate limit handled automatically).

  tl-mb search [--barcode EAN] [--title T] [--artist A] [--format CD|Vinyl|Cassette] [--country DE] [--limit 15]
  tl-mb release <mbid>          tracklist with durations, ISRC, media, label/cat. no., cover art status
  tl-mb group <release-group-id> [--format F]   all releases of a release group = compare editions

Source IDs for the result: musicbrainz:release/<mbid>, URL https://musicbrainz.org/release/<mbid>
"""
import argparse
import re

from tracklist.common import clip, env, get_json, mmss, run_cli

BASE = "https://musicbrainz.org/ws/2"


def ua() -> dict:
    u = env("MUSICBRAINZ_USER_AGENT")
    return {"User-Agent": u if u and "<" not in u else "gema-hackathon-tracklist/0.1 ( hackathon )", "Accept": "application/json"}


def lucene(s: str) -> str:
    return re.sub(r'([+\-!(){}\[\]^"~*?:\\/]|&&|\|\|)', r"\\\1", s)


def credit(ac) -> str:
    return "".join((c.get("name") or c.get("artist", {}).get("name", "")) + (c.get("joinphrase") or "") for c in ac or [])


def fmt_release(r: dict) -> str:
    media = r.get("media") or []
    formats = "+".join(f"{m.get('format') or '?'}" for m in media) or "?"
    counts = "+".join(str(m.get("track-count", "?")) for m in media) or "?"
    labels = "; ".join(f"{(li.get('label') or {}).get('name', '?')} {li.get('catalog-number') or ''}".strip()
                       for li in r.get("label-info") or [])
    return (f"musicbrainz:release/{r['id']} | {r.get('title')} — {credit(r.get('artist-credit'))} | "
            f"{r.get('date', '?')} {r.get('country', '??')} | {formats} | Tracks {counts} | "
            f"Barcode {r.get('barcode') or '-'} | {labels or '-'} | {r.get('status', '?')}"
            + (f" | {r['disambiguation']}" if r.get("disambiguation") else "")
            + (f" | score {r['score']}" if "score" in r else ""))


def fmt_filter(rels, fmt):
    if not fmt:
        return rels
    f = fmt.lower().replace("kassette", "cassette").replace("mc", "cassette").replace("lp", "vinyl")
    return [r for r in rels if any(f in (m.get("format") or "").lower() for m in r.get("media") or [])] or rels


def search(a):
    found: dict[str, dict] = {}
    queries = []
    if a.barcode:
        d = re.sub(r"\D", "", a.barcode)
        variants = {d, d.lstrip("0"), "0" + d if len(d) == 12 else d}
        queries.append("barcode:(" + " OR ".join(sorted(variants)) + ")")
    if a.title:
        q = f'release:"{lucene(a.title)}"'
        if a.artist:
            q += f' AND artist:"{lucene(a.artist)}"'
        if a.country:
            q += f" AND country:{a.country}"
        queries.append(q)
    if not queries:
        raise SystemExit("ERROR: give --barcode or --title")
    for q in queries:
        d = get_json(f"{BASE}/release", params={"query": q, "fmt": "json", "limit": 50}, headers=ua())
        for r in d.get("releases", []):
            found.setdefault(r["id"], r)
    rels = fmt_filter(list(found.values()), a.format)
    print(f"{len(rels)} Releases (Queries: {' | '.join(queries)})")
    print("\n".join(clip([fmt_release(r) for r in rels], a.limit)))


def release(a):
    r = get_json(f"{BASE}/release/{a.mbid}", headers=ua(),
                 params={"inc": "recordings+artist-credits+labels+isrcs+release-groups", "fmt": "json"})
    print(fmt_release(r))
    rg = r.get("release-group") or {}
    caa = r.get("cover-art-archive") or {}
    print(f"release-group: {rg.get('id')} ({rg.get('primary-type')}, first date {rg.get('first-release-date')})"
          f" | Cover: front={caa.get('front')} back={caa.get('back')} images={caa.get('count')}")
    print(f"url: https://musicbrainz.org/release/{r['id']}")
    rel_artist = credit(r.get("artist-credit"))
    total = 0
    missing = 0
    for m in r.get("media") or []:
        print(f"-- Medium {m.get('position')}: {m.get('format') or '?'}"
              + (f" „{m['title']}“" if m.get("title") else "") + f", {m.get('track-count')} Tracks")
        for t in m.get("tracks") or []:
            ms = t.get("length") or (t.get("recording") or {}).get("length")
            total += (ms or 0) / 1000
            missing += 0 if ms else 1
            ta = credit(t.get("artist-credit"))
            isrcs = (t.get("recording") or {}).get("isrcs") or []
            print(f"{m.get('position')}.{t.get('position')} [{t.get('number')}] {t.get('title')}"
                  + (f" — {ta}" if ta and ta != rel_artist else "")
                  + f" | {mmss(ms / 1000) if ms else 'duration missing'}" + (f" ({ms} ms)" if ms else "")
                  + (f" | ISRC {','.join(isrcs[:2])}" if isrcs else ""))
    print(f"Total: {mmss(total)} ({int(total)} s), tracks without duration: {missing}")


def group(a):
    d = get_json(f"{BASE}/release", headers=ua(),
                 params={"release-group": a.rgid, "inc": "media+labels", "fmt": "json", "limit": 100})
    rels = fmt_filter(d.get("releases", []), a.format)
    print(f"{len(rels)} Releases in release-group {a.rgid}")
    print("\n".join(clip([fmt_release(r) for r in rels], a.limit)))


def main():
    p = argparse.ArgumentParser(prog="tl-mb", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search")
    s.add_argument("--barcode")
    s.add_argument("--title")
    s.add_argument("--artist")
    s.add_argument("--format")
    s.add_argument("--country")
    s.add_argument("--limit", type=int, default=15)
    r = sp.add_parser("release")
    r.add_argument("mbid")
    g = sp.add_parser("group")
    g.add_argument("rgid")
    g.add_argument("--format")
    g.add_argument("--limit", type=int, default=25)
    a = p.parse_args()
    {"search": search, "release": release, "group": group}[a.cmd](a)


if __name__ == "__main__":
    run_cli(main)
