"""tl-discogs — Discogs API (token from .env, 60 req/min; 25 without token).

  tl-discogs search [--barcode EAN] [--title T] [--artist A] [--format CD|Vinyl|Cassette] [--catno X] [--country Germany] [--q "free text"] [--limit 20]
  tl-discogs release <id>       tracklist (positions like A1/B2 on vinyl), durations, formats, barcodes/identifiers, notes
  tl-discogs versions <master-id> [--format CD] [--country Germany]   all releases of a master = compare editions

Caution: many releases (including unofficial ones!) share one barcode. Durations are often empty on Discogs.
Source IDs: discogs:release/<id>, URL https://www.discogs.com/release/<id>
"""
import argparse

from tracklist.common import clip, env, get_json, parse_duration, run_cli

BASE = "https://api.discogs.com"


def hdr() -> dict:
    h = {"Accept": "application/json"}
    if env("DISCOGS_USER_TOKEN"):
        h["Authorization"] = f"Discogs token={env('DISCOGS_USER_TOKEN')}"
    return h


def search(a):
    params = {"type": "release", "per_page": 50}
    for k, v in (("barcode", a.barcode), ("release_title", a.title), ("artist", a.artist), ("format", a.format),
                 ("catno", a.catno), ("country", a.country), ("q", a.q)):
        if v:
            params[k] = v
    if a.barcode:
        params["barcode"] = "".join(ch for ch in a.barcode if ch.isdigit())
    d = get_json(f"{BASE}/database/search", params=params, headers=hdr())
    res = d.get("results", [])
    # barcode search without hits: retry with/without leading 0
    if not res and a.barcode:
        b = params["barcode"]
        alt = b[1:] if b.startswith("0") else "0" + b
        params["barcode"] = alt
        res = get_json(f"{BASE}/database/search", params=params, headers=hdr()).get("results", [])
    lines = []
    for r in res:
        lines.append(f"discogs:release/{r['id']} | {r.get('title')} | {r.get('year', '?')} {r.get('country', '?')} | "
                     f"{', '.join(r.get('format') or [])} | Label {', '.join((r.get('label') or [])[:2])} | "
                     f"Kat.-Nr. {r.get('catno', '-')} | Barcodes {', '.join((r.get('barcode') or [])[:3]) or '-'} | "
                     f"master {r.get('master_id') or '-'}")
    total = d.get("pagination", {}).get("items", len(res))
    print(f"{total} hits (parameters: { {k: v for k, v in params.items() if k not in ('type', 'per_page')} })")
    print("\n".join(clip(lines, a.limit)))


def release(a):
    r = get_json(f"{BASE}/releases/{a.id}", headers=hdr())
    fmts = "; ".join(f"{f.get('qty') or '1'}× {f.get('name')} ({', '.join(f.get('descriptions') or [])})" for f in r.get("formats") or [])
    labels = "; ".join(f"{lab.get('name')} {lab.get('catno')}" for lab in r.get("labels") or [])
    print(f"discogs:release/{r['id']} | {r.get('title')} — {', '.join(x.get('name') or '' for x in r.get('artists') or [])} | "
          f"{r.get('released') or r.get('year')} {r.get('country')} | {fmts} | {labels} | master {r.get('master_id') or '-'}")
    print(f"url: {r.get('uri')}")
    ids = [f"{i.get('type')}: {i.get('value')}" + (f" ({i['description']})" if i.get("description") else "")
           for i in r.get("identifiers") or []]
    if ids:
        print("identifiers: " + " | ".join(ids[:10]))
    if r.get("notes"):
        print("notes: " + " ".join(r["notes"].split())[:400])
    total, missing, n = 0, 0, 0
    for t in r.get("tracklist") or []:
        typ = t.get("type_")
        if typ == "heading":
            print(f"-- {t.get('title')}")
            continue
        sub = t.get("sub_tracks") or []
        dur = parse_duration(t.get("duration"))
        n += 1
        total += dur or 0
        missing += 0 if dur else 1
        artists = ", ".join(x.get("name") or "" for x in t.get("artists") or [])
        extra = [f"{x.get('role')}: {x.get('name')}" for x in t.get("extraartists") or []
                 if any(r in (x.get("role") or "") for r in ("Featuring", "Remix", "Vocals"))]
        print(f"{t.get('position') or '-'} {t.get('title')}" + (f" — {artists}" if artists else "")
              + f" | {t.get('duration') or 'duration missing'}" + (f" ({dur} s)" if dur else "")
              + (" [index]" if typ == "index" else "") + (f" | credits: {'; '.join(extra[:4])}" if extra else ""))
        for s in sub:
            print(f"   {s.get('position')} {s.get('title')} | {s.get('duration') or '-'}")
    print(f"{n} tracks, total {total // 60}:{total % 60:02d} ({total} s), without duration: {missing}")
    imgs = r.get("images") or []
    if imgs:
        print("images: " + " | ".join(f"{i.get('type')} {i.get('uri')}" for i in imgs[:6]))
    comm = r.get("community") or {}
    if comm:
        print(f"community: have {comm.get('have')} want {comm.get('want')} data_quality {r.get('data_quality')}")


def versions(a):
    params = {"per_page": 100}
    if a.format:
        params["format"] = a.format
    if a.country:
        params["country"] = a.country
    d = get_json(f"{BASE}/masters/{a.master}/versions", params=params, headers=hdr())
    lines = [f"discogs:release/{v['id']} | {v.get('title')} | {v.get('released', '?')} {v.get('country', '?')} | "
             f"{v.get('format', '')} | {v.get('label', '')} {v.get('catno', '')} | {', '.join(v.get('major_formats') or [])}"
             for v in d.get("versions", [])]
    print(f"{d.get('pagination', {}).get('items', len(lines))} versions of master {a.master}")
    print("\n".join(clip(lines, a.limit)))


def main():
    p = argparse.ArgumentParser(prog="tl-discogs", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search")
    for o in ("--barcode", "--title", "--artist", "--format", "--catno", "--country", "--q"):
        s.add_argument(o)
    s.add_argument("--limit", type=int, default=20)
    r = sp.add_parser("release")
    r.add_argument("id")
    v = sp.add_parser("versions")
    v.add_argument("master")
    v.add_argument("--format")
    v.add_argument("--country")
    v.add_argument("--limit", type=int, default=40)
    a = p.parse_args()
    {"search": search, "release": release, "versions": versions}[a.cmd](a)


if __name__ == "__main__":
    run_cli(main)
