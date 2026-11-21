"""tl-search "<query>" [--site domain] [--count 10] [--lang de] — web search (Brave Search API).

Targeted search for obscure sources, e.g.:
  tl-search "Bushido King of Kingz Tracklist" --site musik-sammler.de
  tl-search "4019593960000"                    (search the EAN directly: shops, collectors, eBay archives)
Then read pages with tl-scrape <url>.
"""
import argparse
import html
import re

from tracklist.common import ToolError, env, get_json, run_cli


def strip_tags(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", s or ""))


def main():
    p = argparse.ArgumentParser(prog="tl-search", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("query")
    p.add_argument("--site")
    p.add_argument("--count", type=int, default=10)
    p.add_argument("--lang", default="de")
    a = p.parse_args()
    key = env("BRAVE_SEARCH_API_KEY")
    if not key:
        raise ToolError("BRAVE_SEARCH_API_KEY missing")
    q = a.query + (f" site:{a.site}" if a.site else "")
    d = get_json("https://api.search.brave.com/res/v1/web/search",
                 params={"q": q, "count": min(a.count, 20), "search_lang": a.lang, "country": "DE"},
                 headers={"X-Subscription-Token": key, "Accept": "application/json"})
    res = (d.get("web") or {}).get("results", [])
    print(f"{len(res)} hits for: {q}")
    for i, r in enumerate(res, 1):
        print(f"{i}. {strip_tags(r.get('title'))}\n   {r.get('url')}\n   {strip_tags(r.get('description'))[:220]}")
        extra = r.get("extra_snippets") or []
        if extra:
            print("   + " + " | ".join(strip_tags(x)[:120] for x in extra[:2]))


if __name__ == "__main__":
    run_cli(main)
