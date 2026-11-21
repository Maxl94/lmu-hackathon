---
name: deep-sources
description: Dig deeper than MusicBrainz/Discogs – obscure and German sources (musik-sammler.de, hitparade.ch, shops, eBay, archives, YouTube), escalation levels and scraper modes when databases return nothing or too little.
---

# Dig deeper

## When
- No hits in MusicBrainz/Discogs, or only other editions.
- Durations missing (common on Discogs, vinyl, cassettes).
- Sources contradict each other and a third source should decide.

## Sources by usefulness (German market)
| Source | Strength | Access |
|---|---|---|
| **musik-sammler.de** | German collector DB, Schlager/folk/cassettes, often **with durations + EAN** | `tl-search "<title> <artist>" --site musik-sammler.de` → `tl-scrape <url> --grep "\d+:\d{2}"` |
| **hitparade.ch** (+ austriancharts.at, germancharts.de) | Tracklists **with durations** per CD edition | `tl-search … --site hitparade.ch` → `tl-scrape` |
| **Genius** | Rap/hip-hop tracklists (no durations) | `tl-search … --site genius.com` |
| **Shops with EAN** (jpc.de, medimops, rebuy, booklooker, Amazon) | Tracklists, **back cover photos** | `tl-search "<ean>"` |
| **eBay / Kleinanzeigen** | Photos of the back cover for obscure releases | `tl-search "<title> <artist> MC"` → `tl-scrape --mode uc` → image URL → `tl-vision` |
| **Wikipedia (de/en)** | Tracklists, edition history, indexing/bans | `tl-scrape https://de.wikipedia.org/wiki/<Title>` |
| **YouTube** full-album uploads | Description with timestamps (hint only!) | `tl-search "<artist> <title> full album"` |
| **Internet Archive / Wayback** | Old label/shop pages, cassette digitisations | `tl-scrape https://web.archive.org/web/2005/<url>` |
| **45worlds.com / 45cat** | Vinyl singles, cassettes | Cloudflare → `tl-scrape --mode firecrawl` |

## Search tricks
- Search the EAN directly: `tl-search "4019593960000"` finds shops and collector entries.
- Search the catalogue number (with and without spaces).
- Try German and English terms: "Tracklist", "Titelliste", "Trackliste", "Songs".
- For cassettes/vinyl: "MC", "Musikkassette", "LP", "Seite A".

## Scraper modes (`tl-scrape --mode`)
1. `http` (default, fast) → 2. `firecrawl` (JS pages) → 3. `browser` (Selenium) → 4. `uc` (SeleniumBase, Cloudflare).
`--mode auto` (default) escalates by itself. `--screenshot f.png` + `tl-vision f.png` for pages whose content exists only as an image.

## Weighting
- Collector/chart pages with matching EAN = strong source (`kind: collector` / `charts`).
- Shops = medium (`kind: shop`), YouTube/forums = weak (`kind: web`), confirmation only.
- Always check that the source describes **the same edition** (EAN, format, year, track count).
