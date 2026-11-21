---
name: cover-reading
description: Read tracklists from images – back covers, booklets, inlays, cassette J-cards, labels, shop and eBay photos, screenshots – with tl-caa and tl-vision, including weighting and matching to the edition.
---

# Read covers

## Find images
- MusicBrainz release: `tl-caa <mbid>` → types Front/Back/Booklet/Tray/Medium. **Back** and **Booklet** first.
- Discogs: `tl-discogs release <id>` → line `images:` (primary/secondary).
- Shops/eBay: `tl-scrape <url> --links` → look for image URLs (.jpg/.png/.webp); pages without text: `tl-scrape <url> --screenshot shot.png`.

## Read
`tl-vision <url|path> --context "<Artist> – <Title>, <Format> <Year>"`
- Reads only what is printed (positions, titles, printed durations, barcode, label, cat. no.).
- Confirm entries marked `[uncertain]` with a second source.

## Classify
- Match barcode/cat. no. on the image against the edition → confirms the edition (strong!).
- Printed order beats database order when they contradict (→ `conflicts`).
- Printed durations are a primary source: if they differ by > 2 s from a database, record a `duration_conflict` and prefer the printed value consistently for all tracks.
- Back covers often have **no durations** – then take durations from a database/collector page of the same edition.
- Add the source as `{"id": "image:<url>", "url": "<url>", "kind": "image", "note": "back cover, read with tl-vision"}`.
