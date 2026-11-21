r"""tl-scrape <url> — read a web page as text. Levels: http → firecrawl → browser (Selenium) → uc (SeleniumBase).

  tl-scrape <url> [--mode auto|http|firecrawl|browser|uc] [--max 12000] [--grep REGEX] [--links] [--screenshot out.png]

--mode auto   (default) http; on 403/429/503, Cloudflare page or almost empty text → firecrawl → uc
--grep REGEX  only matching lines (±2 lines context), e.g. --grep "(?i)king of kingz|\d+:\d{2}"
--links       also print links (text → URL) for further navigation
--screenshot  render the page in a browser and save as PNG (for tl-vision), forces browser mode
Proxy: SCRAPER_PROXY (httpx) or SELENIUM_PROXY (browser) from .env.
Source ID: web:<url>
"""
import argparse
import json
import re
import time

from bs4 import BeautifulSoup

from tracklist.common import ROOT, ToolError, clip_text, env, http, run_cli

BLOCK_TITLES = ("Just a moment", "Attention Required", "Access denied", "Un instant", "Checking your browser")


def html_to_text(raw: str, base_url: str, want_links: bool):
    soup = BeautifulSoup(raw, "html.parser")
    title = (soup.title.string or "").strip() if soup.title else ""
    for tag in soup(["script", "style", "noscript", "svg", "iframe", "header", "footer", "nav", "form"]):
        tag.decompose()
    for br in soup.find_all(["br"]):
        br.replace_with("\n")
    for tr in soup.find_all("tr"):
        cells = [c.get_text(" ", strip=True) for c in tr.find_all(["td", "th"])]
        tr.replace_with("\n" + " | ".join(c for c in cells if c) + "\n")
    text = soup.get_text("\n")
    text = re.sub(r"[ \t\xa0]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text).strip()
    links = []
    if want_links:
        from urllib.parse import urljoin
        seen = set()
        for a in soup.find_all("a", href=True):
            href = urljoin(base_url, a["href"])
            label = a.get_text(" ", strip=True)[:80]
            if label and href.startswith("http") and href not in seen:
                seen.add(href)
                links.append(f"{label} → {href}")
    return title, text, links


def blocked(status: int, title: str, text: str) -> bool:
    return status in (401, 403, 429, 503) or any(t in title for t in BLOCK_TITLES) or len(text) < 200


def via_http(url):
    ua = env("SCRAPER_USER_AGENT") or "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"
    status, _, text, final = http("GET", url, headers={"User-Agent": ua, "Accept-Language": "de,en;q=0.8"},
                                  scraper=True, retries=1, timeout=float(env("SCRAPER_TIMEOUT_SECONDS", "20")))
    return status, final, text


def via_firecrawl(url):
    key = env("FIRECRAWL_API_KEY")
    if not key:
        raise ToolError("FIRECRAWL_API_KEY missing")
    base = env("FIRECRAWL_API_URL", "https://api.firecrawl.dev").rstrip("/")
    status, _, text, _ = http("POST", f"{base}/v1/scrape", headers={"Authorization": f"Bearer {key}"},
                              json_body={"url": url, "formats": ["markdown"], "onlyMainContent": True}, timeout=90)
    if status != 200:
        raise ToolError(f"firecrawl HTTP {status}: {text[:200]}")
    d = json.loads(text).get("data") or {}
    return (d.get("metadata") or {}).get("title", ""), d.get("markdown", "")


def via_browser(url, uc=False, screenshot=None):
    binary = env("SELENIUM_BINARY", "/usr/bin/chromium-browser")
    proxy = env("SELENIUM_PROXY")
    if uc:
        from seleniumbase import SB
        kw = dict(uc=True, headless2=True, binary_location=binary)
        if proxy:
            kw["proxy"] = proxy
        with SB(**kw) as sb:
            sb.uc_open_with_reconnect(url, 5)
            time.sleep(2)
            if screenshot:
                sb.save_screenshot(screenshot)
            return sb.get_title(), sb.get_page_source(), sb.get_current_url()
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    o = Options()
    o.binary_location = binary
    if env("SELENIUM_HEADLESS", "true") != "false":
        o.add_argument("--headless=new")
    o.add_argument("--window-size=1366,2400")
    if proxy:
        o.add_argument(f"--proxy-server={proxy}")
    remote = env("SELENIUM_REMOTE_URL")
    d = webdriver.Remote(command_executor=remote, options=o) if remote else webdriver.Chrome(options=o)
    try:
        d.set_page_load_timeout(int(env("SELENIUM_PAGE_LOAD_TIMEOUT", "30")))
        d.get(url)
        time.sleep(3)
        if screenshot:
            d.save_screenshot(screenshot)
        return d.title, d.page_source, d.current_url
    finally:
        d.quit()


def grep(text: str, pattern: str) -> str:
    rx = re.compile(pattern)
    lines = text.splitlines()
    keep = set()
    for i, line in enumerate(lines):
        if rx.search(line):
            keep.update(range(max(0, i - 2), min(len(lines), i + 3)))
    if not keep:
        return f"(keine Zeile passt auf {pattern!r})"
    out, last = [], -2
    for i in sorted(keep):
        if i != last + 1:
            out.append("…")
        out.append(lines[i])
        last = i
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(prog="tl-scrape", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url")
    p.add_argument("--mode", default="auto", choices=["auto", "http", "firecrawl", "browser", "uc"])
    p.add_argument("--max", type=int, default=6000)
    p.add_argument("--grep")
    p.add_argument("--links", action="store_true")
    p.add_argument("--screenshot")
    a = p.parse_args()
    mode = "browser" if a.screenshot and a.mode in ("auto", "http", "firecrawl") else a.mode
    tried = []
    title = text = ""
    links: list[str] = []
    final = a.url

    def attempt(m):
        nonlocal title, text, links, final
        tried.append(m)
        if m == "http":
            status, final, raw = via_http(a.url)
            title, text, links = html_to_text(raw, final, a.links)
            return not blocked(status, title, text), f"HTTP {status}"
        if m == "firecrawl":
            title, text = via_firecrawl(a.url)
            links = re.findall(r"\[([^\]]{1,80})\]\((https?://[^)\s]+)\)", text) if a.links else []
            links = [f"{t} → {u}" for t, u in links]
            return len(text) > 200 and not any(t in title for t in BLOCK_TITLES), "ok"
        shot = str(ROOT / a.screenshot) if a.screenshot and not a.screenshot.startswith("/") else a.screenshot
        title, raw, final = via_browser(a.url, uc=(m == "uc"), screenshot=shot)
        _, text, links = html_to_text(raw, final, a.links)
        return not any(t in title for t in BLOCK_TITLES), "ok"

    order = {"auto": ["http", "firecrawl", "uc"]}.get(mode, [mode])
    note = ""
    for m in order:
        try:
            ok, note = attempt(m)
        except ToolError as e:
            ok, note = False, str(e)
        except Exception as e:  # noqa: BLE001
            ok, note = False, f"{type(e).__name__}: {str(e)[:150]}"
        if ok:
            break
    else:
        print(f"WARN: alle Modi blockiert/leer ({' → '.join(tried)}; zuletzt: {note})")
    print(f"url: {final}\nmode: {tried[-1]} ({' → '.join(tried)})\ntitle: {title}\nsource-id: web:{final}")
    if a.screenshot:
        print(f"screenshot: {a.screenshot}")
    body = grep(text, a.grep) if a.grep else text
    print("---")
    print(clip_text(body, a.max))
    if a.links and links:
        print("--- links")
        print("\n".join(links[:80]) + (f"\n... {len(links) - 80} weitere" if len(links) > 80 else ""))


if __name__ == "__main__":
    run_cli(main)
