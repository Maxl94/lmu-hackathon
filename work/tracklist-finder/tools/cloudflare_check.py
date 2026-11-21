"""Testet, ob Cloudflare-geschützte Seiten per Selenium erreichbar sind.

1. normales Selenium headless
2. SeleniumBase UC-Mode (headless2), mit Klick auf die Cloudflare-Checkbox falls nötig
Optional per --proxy socks5://127.0.0.1:1081 über SSH-Tunnel.
"""
import argparse
import time

BLOCK_TITLES = ("Just a moment", "Attention Required", "Access denied", "Un instant")


def verdict(src: str, title: str = "") -> str:
    # Cloudflare bettet challenge-platform-Skripte auch in normale Seiten ein → Titel ist das verlässlichere Signal
    if any(t in title for t in BLOCK_TITLES):
        return "BLOCKED"
    return "OK"


def plain(url: str, proxy: str | None) -> None:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    o = Options()
    o.binary_location = "/usr/bin/chromium-browser"
    o.add_argument("--headless=new")
    if proxy:
        o.add_argument(f"--proxy-server={proxy}")
    d = webdriver.Chrome(options=o)
    try:
        d.set_page_load_timeout(40)
        d.get(url)
        time.sleep(8)
        src = d.page_source
        print(f"  plain selenium : {verdict(src, d.title):9} title={d.title[:60]!r} len={len(src)}")
    finally:
        d.quit()


def uc(url: str, proxy: str | None) -> None:
    from seleniumbase import SB

    kw = dict(uc=True, headless2=True, binary_location="/usr/bin/chromium-browser")
    if proxy:
        kw["proxy"] = proxy
    with SB(**kw) as sb:
        sb.uc_open_with_reconnect(url, 6)
        src = sb.get_page_source()
        first = verdict(src, sb.get_title())
        if first == "BLOCKED":
            try:
                sb.uc_gui_click_captcha()
                time.sleep(4)
            except Exception as e:  # noqa: BLE001
                print(f"  (captcha click: {type(e).__name__}: {str(e)[:80]})")
            src = sb.get_page_source()
        print(f"  seleniumbase UC: {verdict(src, sb.get_title()):9} (erst: {first}) title={sb.get_title()[:60]!r} len={len(src)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--proxy")
    a = ap.parse_args()
    for u in a.urls:
        print(u)
        for fn in (plain, uc):
            try:
                fn(u, a.proxy)
            except Exception as e:  # noqa: BLE001
                print(f"  {fn.__name__}: FEHLER {type(e).__name__}: {str(e)[:120]}")
