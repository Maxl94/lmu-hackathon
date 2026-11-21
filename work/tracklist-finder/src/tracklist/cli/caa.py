"""tl-caa <mbid> [--group] — Cover Art Archive: images of a MusicBrainz release (front, back, booklet, medium, tray).

Back/booklet often contain the printed tracklist → read with tl-vision.
--group: <mbid> is a release-group id (front cover of the group only).
Source ID: caa:release/<mbid>/<image-id>
"""
import argparse
import json

from tracklist.common import http, run_cli


def main():
    p = argparse.ArgumentParser(prog="tl-caa", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("mbid")
    p.add_argument("--group", action="store_true")
    a = p.parse_args()
    kind = "release-group" if a.group else "release"
    status, _, text, _ = http("GET", f"https://coverartarchive.org/{kind}/{a.mbid}")
    if status == 404:
        print("no images in the Cover Art Archive")
        return
    if status != 200:
        print(f"ERROR: HTTP {status}")
        return
    d = json.loads(text)
    for img in d.get("images", []):
        th = img.get("thumbnails") or {}
        url = th.get("1200") or th.get("large") or img.get("image")
        print(f"caa:{kind}/{a.mbid}/{img.get('id')} | {', '.join(img.get('types', [])) or '?'}"
              + (f" | „{img['comment']}“" if img.get("comment") else "") + f" | {url}")
    print(f"{len(d.get('images', []))} images · read tracklist: tl-vision <url> --context \"…\"")


if __name__ == "__main__":
    run_cli(main)
