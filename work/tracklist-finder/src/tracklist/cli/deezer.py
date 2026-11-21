"""tl-deezer — Deezer API (no key). Digital catalogue, knows digital UPCs only!

  tl-deezer upc <barcode>
  tl-deezer search --artist A --title T [--limit 10]
  tl-deezer album <id>

Source IDs: deezer:album/<id>, URL https://www.deezer.com/album/<id>
"""
import argparse
import re

from tracklist.common import clip, get_json, mmss, run_cli

BASE = "https://api.deezer.com"


def show(d):
    if d.get("error"):
        print(f"no hit ({d['error'].get('message')})")
        return
    print(f"deezer:album/{d.get('id')} | {d.get('title')} — {(d.get('artist') or {}).get('name')} | "
          f"{d.get('release_date')} | UPC {d.get('upc')} | {d.get('nb_tracks')} Tracks | Label {d.get('label')}"
          + (" | explicit" if d.get("explicit_lyrics") else ""))
    print(f"url: {d.get('link')}")
    tracks = (d.get("tracks") or {}).get("data", [])
    total = 0
    for i, t in enumerate(tracks, 1):
        total += t.get("duration") or 0
        print(f"{t.get('disk_number', 1)}.{t.get('track_position', i)} {t.get('title')} | {mmss(t.get('duration'))}")
    print(f"Total {mmss(total)} ({total} s)")


def main():
    p = argparse.ArgumentParser(prog="tl-deezer", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    u = sp.add_parser("upc")
    u.add_argument("code")
    s = sp.add_parser("search")
    s.add_argument("--artist", default="")
    s.add_argument("--title", default="")
    s.add_argument("--limit", type=int, default=10)
    al = sp.add_parser("album")
    al.add_argument("id")
    a = p.parse_args()
    if a.cmd == "upc":
        code = re.sub(r"\D", "", a.code)
        for c in dict.fromkeys([code, code.lstrip("0"), code.zfill(13)]):
            d = get_json(f"{BASE}/album/upc:{c}")
            if not d.get("error"):
                show(d)
                return
        print("no hit (Deezer mostly knows digital UPCs only)")
    elif a.cmd == "album":
        show(get_json(f"{BASE}/album/{a.id}"))
    else:
        q = " ".join(x for x in (f'artist:"{a.artist}"' if a.artist else "", f'album:"{a.title}"' if a.title else "") if x)
        d = get_json(f"{BASE}/search/album", params={"q": q, "limit": 25})
        lines = [f"deezer:album/{r.get('id')} | {r.get('title')} — {(r.get('artist') or {}).get('name')} | "
                 f"{r.get('nb_tracks')} Tracks | {r.get('record_type')}" for r in d.get("data", [])]
        print(f"{len(lines)} Alben (q={q})")
        print("\n".join(clip(lines, a.limit)))


if __name__ == "__main__":
    run_cli(main)
