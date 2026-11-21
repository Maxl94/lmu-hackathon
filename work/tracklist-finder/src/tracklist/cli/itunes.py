"""tl-itunes — Apple iTunes Search/Lookup (no key, ~20 req/min). Digital catalogue!

  tl-itunes upc <barcode> [--country de]        album + tracklist by UPC/EAN
  tl-itunes search "<artist> <title>" [--country de] [--limit 10]
  tl-itunes album <collectionId> [--country de]

Source IDs: itunes:album/<collectionId>, URL from collectionViewUrl
"""
import argparse
import re

from tracklist.common import clip, get_json, mmss, run_cli

BASE = "https://itunes.apple.com"


def show_album(results):
    coll = next((r for r in results if r.get("wrapperType") == "collection"), None)
    tracks = [r for r in results if r.get("wrapperType") == "track"]
    if not coll and not tracks:
        print("no hit")
        return
    c = coll or tracks[0]
    print(f"itunes:album/{c.get('collectionId')} | {c.get('collectionName')} — {c.get('artistName')} | "
          f"{(c.get('releaseDate') or '')[:10]} | {c.get('trackCount')} Tracks | {c.get('copyright', '')}")
    print(f"url: {c.get('collectionViewUrl', '')}")
    total = 0
    for t in sorted(tracks, key=lambda x: (x.get("discNumber", 1), x.get("trackNumber", 0))):
        s = (t.get("trackTimeMillis") or 0) / 1000
        total += s
        print(f"{t.get('discNumber', 1)}.{t.get('trackNumber')} {t.get('trackName')}"
              + (f" — {t['artistName']}" if t.get("artistName") != c.get("artistName") else "")
              + f" | {mmss(s)} ({t.get('trackTimeMillis')} ms)")
    print(f"Total {mmss(total)} ({int(total)} s)")


def main():
    p = argparse.ArgumentParser(prog="tl-itunes", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    u = sp.add_parser("upc")
    u.add_argument("code")
    u.add_argument("--country", default="de")
    s = sp.add_parser("search")
    s.add_argument("term")
    s.add_argument("--country", default="de")
    s.add_argument("--limit", type=int, default=10)
    al = sp.add_parser("album")
    al.add_argument("id")
    al.add_argument("--country", default="de")
    a = p.parse_args()
    if a.cmd == "upc":
        code = re.sub(r"\D", "", a.code)
        for cc in dict.fromkeys([a.country, "us"]):
            d = get_json(f"{BASE}/lookup", params={"upc": code, "entity": "song", "country": cc})
            if d.get("resultCount"):
                print(f"(Store {cc})")
                show_album(d["results"])
                return
        print("no hit (physical releases are often missing from the digital catalogue)")
    elif a.cmd == "album":
        d = get_json(f"{BASE}/lookup", params={"id": a.id, "entity": "song", "country": a.country})
        show_album(d.get("results", []))
    else:
        d = get_json(f"{BASE}/search", params={"term": a.term, "entity": "album", "country": a.country, "limit": 25})
        lines = [f"itunes:album/{r.get('collectionId')} | {r.get('collectionName')} — {r.get('artistName')} | "
                 f"{(r.get('releaseDate') or '')[:10]} | {r.get('trackCount')} Tracks" for r in d.get("results", [])]
        print(f"{len(lines)} Alben")
        print("\n".join(clip(lines, a.limit)))


if __name__ == "__main__":
    run_cli(main)
