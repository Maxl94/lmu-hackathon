"""tl-lastfm album --artist A --title T — Last.fm album.getInfo (key from .env).

Community data: not tied to a specific edition, durations partly rounded/missing. Good as a cross-check.
Source ID: lastfm:album/<artist>/<title>, URL from the response
"""
import argparse

from tracklist.common import ToolError, env, get_json, mmss, run_cli


def main():
    p = argparse.ArgumentParser(prog="tl-lastfm", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    al = sp.add_parser("album")
    al.add_argument("--artist", required=True)
    al.add_argument("--title", required=True)
    a = p.parse_args()
    if not env("LASTFM_API_KEY"):
        raise ToolError("LASTFM_API_KEY missing in .env")
    d = get_json("https://ws.audioscrobbler.com/2.0/", params={
        "method": "album.getinfo", "artist": a.artist, "album": a.title, "api_key": env("LASTFM_API_KEY"),
        "format": "json", "autocorrect": 1})
    if d.get("error"):
        print(f"no hit ({d.get('message')})")
        return
    alb = d.get("album") or {}
    print(f"lastfm:album/{alb.get('artist')}/{alb.get('name')} | mbid {alb.get('mbid') or '-'} | url: {alb.get('url')}")
    tracks = (alb.get("tracks") or {}).get("track") or []
    tracks = tracks if isinstance(tracks, list) else [tracks]
    total = 0
    for t in tracks:
        dur = t.get("duration")
        total += dur or 0
        print(f"{(t.get('@attr') or {}).get('rank', '?')} {t.get('name')} | {mmss(dur) if dur else 'duration missing'}")
    print(f"{len(tracks)} tracks, total {mmss(total)} ({total} s)")


if __name__ == "__main__":
    run_cli(main)
