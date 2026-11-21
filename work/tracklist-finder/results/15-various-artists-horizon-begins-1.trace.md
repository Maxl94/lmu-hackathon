# Agent-Trace: 15-various-artists-horizon-begins-1

> Schnellweg geprüft: no fast path: 0 matching official MusicBrainz releases (fast path only for 1–5 identical ones)
Start 2026-11-20T15:51:22 · 25 Schritte · 24 Tool-Aufrufe · Tokens in 81369 / out 19143


> **Agent** +1s: I'll start by checking the barcode and searching both databases.

### 1. `shell` +1s – completed

```
bin/tl-gtin 4250101487415; echo "---MB---"; bin/tl-mb search --barcode 4250101487415; echo "---DC---"; bin/tl-discogs search --barcode 4250101487415
```

<details><summary>Ausgabe</summary>

```
input: '4250101487415' → digits: 4250101487415 (13 digits)
type: EAN-13  valid: yes
search variants: 4250101487415
prefix 400–440: assigned in Germany (says nothing about the country of release)
---MB---
0 Releases (Queries: barcode:(4250101487415))

---DC---
1 hits (parameters: {'barcode': '4250101487415'})
discogs:release/35282479 | Various - Horizon Begins 1 | 2025 Germany | Vinyl, 12", 45 RPM, Compilation | Label Orion Records, Olo Mastering | Kat.-Nr. ORNVS01 | Barcodes 4250101487415, ORNVS01 BP42876-01 A1, ORNVS01 BP42876-01 B1 | master -
```
</details>

### 2. `shell` +29s – completed

```
bin/tl-discogs release 35282479
```

<details><summary>Ausgabe</summary>

```
discogs:release/35282479 | Horizon Begins 1 — Various | 2025-10-24 Germany | 2× Vinyl (12", 45 RPM, Compilation) | Orion Records (10) ORNVS01 | master -
url: https://www.discogs.com/release/35282479-Various-Horizon-Begins-1
identifiers: Barcode: 4250101487415 | Matrix / Runout: ORNVS01 BP42876-01 A1 (Runout, side A, etched) | Matrix / Runout: ORNVS01 BP42876-01 B1 (Runout, side B, etched) | Matrix / Runout: ORNVS01 BP42876-02 C1 (Runout, side C, etched) | Matrix / Runout: ORNVS01 BP42876-02 D1 (Runout, side D, etched)
notes: First track is an uncredited track called "intro" by Unknown Artist. Comes with the sticker "Orion"
A1 Intro — Unknown Artist | duration missing
A2 Newlife — 200188 | duration missing
A3 Sky High — martinou | duration missing
B1 Phoenix — Ateq, Orion (42) | duration missing
B2 Past Mind — Skyra | duration missing
C1 Bubble Love — Ben Kaczor | duration missing
C2 Symbyosis — Lb Honne | duration missing
D1 Groovement — Hame (3) | duration missing
D2  Sirens — Soela | duration missing
9 tracks, total 0:00 (0 s), without duration: 9
images: secondary https://i.discogs.com/s8909w_y_lNDBGAqc5ux-912Nsa41QTM0V6ZS-QyAYc/rs:fit/g:sm/q:90/h:328/w:328/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1Mjgy/NDc5LTE3NTk1OTEw/NTEtMTIxMi5qcGVn.jpeg
community: have 246 want 124 data_quality Needs Vote
```
</details>

### 3. `shell` +38s – completed

```
bin/tl-mb search --title "Horizon Begins" --artist "Various Artists"; echo "---DC2---"; bin/tl-discogs search --title "Horizon Begins 1"; echo "---IT---"; bin/tl-itunes search "Orion Records Horizon Begins"; echo "---DZ---"; bin/tl-deezer search --artist "Various Artists" --title "Horizon Begins 1"
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Horizon Begins" AND artist:"Various Artists")

---DC2---
1 hits (parameters: {'release_title': 'Horizon Begins 1'})
discogs:release/35282479 | Various - Horizon Begins 1 | 2025 Germany | Vinyl, 12", 45 RPM, Compilation | Label Orion Records, Olo Mastering | Kat.-Nr. ORNVS01 | Barcodes 4250101487415, ORNVS01 BP42876-01 A1, ORNVS01 BP42876-01 B1 | master -
---IT---
0 Alben

---DZ---
0 Alben (q=artist:"Various Artists" album:"Horizon Begins 1")
```
</details>

### 4. `shell` +49s – completed

```
bin/tl-search "\"Horizon Begins\" Orion Records ORNVS01"; echo "==="; bin/tl-search "\"Horizon Begins 1\" Various 2025 vinyl tracklist"
```

<details><summary>Ausgabe</summary>

```
10 hits for: "Horizon Begins" Orion Records ORNVS01
1. Various - Horizon Begins 1 / ORION Records ORNVS01 - Vinyl
   https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778
   The final chapter of this story is entrusted to Hame and Soela, a perfect soundtrack to close in a special way. ... Various, Horizon Begins 1 ORNVS01, 2025-10-24 00:00:00, 4250101487415.
   + After five years of activity, Orion Records is proud to present its first various artists release. “Horizon Begins” is a | An unknown project opens the record with an intro that sets the overall mood of the release, before giving way to deep a
2. Horizon Begins 1 | Various Artists - Orion Records - Bandcamp
   https://orion01.bandcamp.com/album/horizon-begins-1
   Horizon Begins 1 by Various Artists, released 24 October 2025 After five years of activity, Orion Records is proud to present its first various artists release. “Horizon Begins” is a collection of tracks from artists con
   + Horizon Begins 1 by Various Artists, released 24 October 2025 After five years of activity, Orion Records is proud to pr | After five years of activity, Orion Records is proud to present its first various artists release. “Horizon Begins” is a
3. Orion Records Releases | Kompakt
   https://kompakt.fm/labels/orion/releases
   Horizon Begins 1 · Orion Records · 2x12" ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · Stay in the loop and subscribe to our webshop newsletter ·
   + Horizon Begins 1 · Orion Records · 2x12" ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart
4. Horizon Begins 1 - Various Artists
   https://wordandsound.net/release/162303-ORNVS01-Various-Artists-Horizon-Begins-1
   Cat-No:ORNVS01 · Release-Date... is proud to present its first various artists release. “Horizon Begins” is a collection of tracks from artists connected to the Orion universe, encountered in clubs and festivals over rec
   + Cat-No:ORNVS01 · Release-Date:24.10.2025 · Genre:Techno · Configuration:2LP · Barcode: 1 · 200188 - Newlife · 2 · Martin | Vinyl Only. After five years of activity, Orion Records is proud to present its first various artists release. “Horizon 
5. Various Artists - HORIZON BEGINS 1 / Orion Records / ORNVS01 | 2x12 Inch Vinyl kaufen | decks.de
   https://www.decks.de/track/various_artists-horizon_begins_1/cpb-wg
   Various Artists - HORIZON BEGINS 1 als 2x12 Inch Vinyl auf Orion Records / ORNVS01. Mit Tracklist und Audio-Previews. Jetz
… [7399 Zeichen gekürzt]
```
</details>

### 5. `shell` +60s – completed

```
bin/tl-scrape "https://orion01.bandcamp.com/album/horizon-begins-1" --grep -iE "track|title|duration|listen|Newlife|Sky High|Phoenix|Past Mind|Bubble Love|Symbyosis|Groovement|Sirens|Intro|[0-9]+:[0-9]{2}" 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 6. `shell` +65s – completed

```
bin/tl-scrape "https://orion01.bandcamp.com/album/horizon-begins-1" --grep "Newlife|Sky High|Phoenix|Past Mind|Bubble Love|Symbyosis|Groovement|Sirens|Intro|track_row|duration" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://orion01.bandcamp.com/album/horizon-begins-1
mode: http (http)
title: Horizon Begins 1 | Various Artists | Orion Records
source-id: web:https://orion01.bandcamp.com/album/horizon-begins-1
---
…
über
Tracklisting:
A1: 200188 - Newlife
A2: Martinou - Sky High
B1: Ateq & Orion - Phoenix
B2: Skyra - Past Mind
C1: Ben Kaczor - Bubble Love
C2: Lb Honne - Symbiosis
D1: Hame - Groovement
D2: Soela - Sirens
After five years of activity, Orion Records is proud to present its first various artists release. 
“Horizon Begins” is a collection of tracks from artists connected to the Orion universe, encountered in clubs and festivals over recent years.
```
</details>

### 7. `shell` +68s – completed

```
bin/tl-scrape "https://wordandsound.net/release/162303-ORNVS01-Various-Artists-Horizon-Begins-1" --grep "Intro|Newlife|Sky High|Phoenix|Past Mind|Bubble Love|Symb|Groovement|Sirens|min|sec" 2>&1 | head -60; echo "===DECKS==="; bin/tl-scrape "https://www.decks.de/track/various_artists-horizon_begins_1/cpb-wg" --grep "Intro|Newlife|Sky High|Phoenix|Past Mind|Bubble Love|Symb|Groovement|Sirens|[0-9]:[0-9][0-9]" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://wordandsound.net/release/162303-ORNVS01-Various-Artists-Horizon-Begins-1
mode: http (http)
title: Horizon Begins 1  - Various Artists
source-id: web:https://wordandsound.net/release/162303-ORNVS01-Various-Artists-Horizon-Begins-1
---
…
Barcode:
1
200188 - Newlife
2
Martinou - Sky High
3
Ateq & Orion - Phoenix
4
Skyra - Past Mind
5
Ben Kaczor - Bubble Love
6
Lb Honne - Symbyosis
7
Hame - Groovement
8
Soela - Sirens
 Vinyl Only.
After five years of activity, Orion Records is proud to present its first various artists release. “Horizon Begins” is a collection of tracks from artists connected to the Orion universe, encountered in clubs and festivals over recent years. The compilation aims to tell a complete story through its tracklist, moving from ambient to deeper shades of techno, with interludes of classic club sounds. An unknown project opens the record with an intro that sets the overall mood of the release, before giving way to deep and rhythmic moments by artists such as Martinou and Ateq & Orion. Skyra from Tbilisi closes side B with the unmistakable sound of Georgia. The second part of the release shifts towards a darker, more hypnotic direction with two key figures of the Swiss scene, Ben Kaczor and Lb Honne. The final chapter of this story is entrusted to Hame and Soela, a perfect soundtrack to close in a special way.
Sicherheits- und Herstellerinformationen / safety and manufacturer info (GPSR) 
WAS - Word and Sound Medien GmbH
…
Case Woo - Bozzattitude
8
Case Woo - Subliminal
9
Case Woo - Urban Souls
…
B3.Fluff Haven
C1.Bozzattitude
C2.Subliminal
C3.Urban Souls 
D1.Subspace (Radio Edit)
…
Back then, this release was hailed as the definitive and only full-length Deep House / Tech House album to emerge from the tiny island of Singapore, by one of the pioneers of the local electronic music industry.
Case himself states: „I was introduced to the Deep House genre in 1999 and it was love at first listen, pure magic! What began as a spark of inspiration soon led to a month of self-imposed studio isolation - a journey of immersion, expression, and devotion to a newfound sound. The outcome of that creative dive is „A Deeper Shade“.“
The tracks „Polyester Cookies“ and „Subliminal“ were picked up by transport recordings for TSP008 in 2000/2001 and are getting rare & expensive these days. Now you can get the whole album on wax for the first time - 65 minutes of pure deepness that stood the test of time!
goodbye.
Credits:
…
8
Another Channel - Axi
… [1650 Zeichen gekürzt]
```
</details>

### 8. `shell` +74s – completed

```
bin/tl-search "Horizon Begins 1 ORNVS01 beatport"; echo "==="; bin/tl-scrape "https://yoyaku.io/release/200188-martinou-ateq-orion-skyra-horizon-begins-1-ornvs01/" --grep "Intro|Newlife|Sky High|Phoenix|Past Mind|Bubble|Symb|Groovement|Sirens|[0-9]:[0-9][0-9]" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
10 hits for: Horizon Begins 1 ORNVS01 beatport
1. Horizon Begins 1 - Various Artists
   https://wordandsound.net/release/162303-ORNVS01-Various-Artists-Horizon-Begins-1
   Cat-No:ORNVS01 · Release-Date... first various artists release. “Horizon Begins” is a collection of tracks from artists connected to the Orion universe, encountered in clubs and festivals over recent years....
   + Cat-No:ORNVS01 · Release-Date:24.10.2025 · Genre:Techno · Configuration:2LP · Barcode: 1 · 200188 - Newlife · 2 · Martin | Vinyl Only. After five years of activity, Orion Records is proud to present its first various artists release. “Horizon 
2. Orion Records Releases | Kompakt
   https://kompakt.fm/labels/orion/releases
   Horizon Begins 1 · Orion Records · 2x12" ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · Stay in the loop and subscribe to our webshop newsletter ·
   + Horizon Begins 1 · Orion Records · 2x12" ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart
3. Horizon Begins 1 by Various Artists - Orion Records
   https://kompakt.fm/releases/horizon_begins_1
   ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · VINYL ONLY! Play All 2x12" . by · Unreleased Unveröffentlicht · View downloads · Show Full Tracklisting 8 Hide Full Tracklisting 8 · 687c7
   + After five years of activity, Orion Records is proud to present its first various artists release. “Horizon Begins” is a | ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · VINYL ONLY! Play All 2x12" . by · Unre
4. martinou - Horizon Begins 1 - ORNVS01 - Orion Records
   https://yoyaku.io/release/200188-martinou-ateq-orion-skyra-horizon-begins-1-ornvs01/
   Artist(s): martinou, Skyra, Ateq & Orion Label: ORNVS01 | Orion Records Style: Ambient, Deep Techno, Dub Techno Format: 2x12" Country: Germany · Orion Records presents its first various artists release, ‘Horizon Begins’,
   + ORNVS01 - martinou - Horizon Begins 1 on Orion Records - Yoyaku Record Store | Artist(s): martinou, Skyra, Ateq & Orion Label: ORNVS01 | Orion Records Style: Ambient, Deep Techno, Dub Techno Format: 
5. Various - Horizon Begins 1 / ORION Records ORNVS01 - Vinyl
   https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778
   Various, Horizon Begins 1 ORNVS01, 2025-10-24 00:00:00, 4250101487415. 12inch Vinyl 0.20 kg. Material information: Vinyl (PVC).
   + After five years of activity, Orion Records is proud to p
… [3289 Zeichen gekürzt]
```
</details>

### 9. `shell` +81s – completed

```
bin/tl-scrape "https://kompakt.fm/releases/horizon_begins_1" --grep "Intro|Newlife|Sky High|Phoenix|Past Mind|Bubble|Symb|Groovement|Sirens|[0-9]:[0-9][0-9]|min" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://kompakt.fm/releases/horizon_begins_1
mode: http (http)
title: Horizon Begins 1 by Various Artists | Kompakt
source-id: web:https://kompakt.fm/releases/horizon_begins_1
---
…
true
687c73b0c0688
Newlife
200188
https://kompakt.fm/artists/m-ja-wm-t-g4/releases
1
02:53
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-01-newlife.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=daa442971a96b64dafc629c17b972e1b567580e5c5522f9d7ba52af1e68d6d15
687c73b0c06a6
Sky High
Martinou
https://kompakt.fm/artists/t-w-f-ydg-lub3u-kom1/releases
2
06:21
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-02-sky_high.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=b46eb22383c9ae3a15fa88672f8b351f86d14350733e3a006df63b78855de67c
687c73b0c06b0
Phoenix
Ateq & Orion
https://kompakt.fm/artists/q-x-r-lcs-a-mi-e-9yaw-9u/releases
3
06:50
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-03-phoenix.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=a88f54bb80f8aefd5d07d726f195bf69d46dd8f412401c0891263d49a02aa711
687c73b0c06ba
Past Mind
Skyra
https://kompakt.fm/artists/u-2t5cme-kom1/releases
4
06:57
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-04-past_mind.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=8325057cccfe1edd2b3f14af2a52336a4575f5ea5466c5a3e8cf5950b837e433
687c73b0c069c
Bubble love
Ben Kaczor
https://kompakt.fm/artists/q-mv-ui-e-thy-3pvcgkom2/releases
5
06:56
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-05-bubble_love.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X
… [1318 Zeichen gekürzt]
```
</details>

### 10. `shell` +184s – completed

```
bin/tl-scrape "https://kompakt.fm/releases/horizon_begins_1" --grep "Sirens" -A 3 2>&1 | tail -20; echo "===DISC==="; bin/tl-scrape "https://www.discogs.com/de/release/35282479-Various-Horizon-Begins-1" --grep "Intro|A1|A2|A3|Newlife|Sky High|6:5|total|Unknown" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: unrecognized arguments: -A 3
===DISC===
url: https://www.discogs.com/de/release/35282479-Various-Horizon-Begins-1
mode: firecrawl (http → firecrawl)
title: Horizon Begins 1 – 2 x Vinyl (12", 45 RPM, Compilation), 2025 [r35282479] | Discogs
source-id: web:https://www.discogs.com/de/release/35282479-Various-Horizon-Begins-1
---
…
|     |     |     |
| --- | --- | --- |
| A1 | [Unknown Artist](https://www.discogs.com/artist/355-Unknown-Artist)– | Intro |
| A2 | [200188](https://www.discogs.com/artist/16809688-200188)– | Newlife |
| A3 | [martinou](https://www.discogs.com/artist/3884300-martinou)– | Sky High |
| B1 | [Ateq](https://www.discogs.com/artist/2446085-Ateq) & [Orion (42)](https://www.discogs.com/artist/3538120-Orion-42)– | Phoenix |
| B2 | [Skyra](https://www.discogs.com/artist/6588740-Skyra)– | Past Mind |
…
- Mastered By – [Isabel Schröer](https://www.discogs.com/artist/10433566-Isabel-Schr%C3%B6er)

First track is an uncredited track called "intro" by Unknown Artist.

Comes with the sticker "Orion"

- Barcode: 4250101487415
- Matrix / Runout (Runout, side A, etched): ORNVS01 BP42876-01 A1
- Matrix / Runout (Runout, side B, etched): ORNVS01 BP42876-01 B1
- Matrix / Runout (Runout, side C, etched): ORNVS01 BP42876-02 C1
```
</details>

### 11. `shell` +323s – completed

```
bin/tl-scrape "https://kompakt.fm/releases/horizon_begins_1" 2>&1 | grep -E "^[0-9]{2}:[0-9]{2}$|^[A-Za-z]" | head -80
```

<details><summary>Ausgabe</summary>

```
url: https://kompakt.fm/releases/horizon_begins_1
mode: http (http)
title: Horizon Begins 1 by Various Artists | Kompakt
source-id: web:https://kompakt.fm/releases/horizon_begins_1
Horizon Begins 1 by Various Artists | Kompakt
Downloads
Cart
Search
Log in
release
Play All
by
Horizon Begins 1
Various Artists
https://s3.amazonaws.com/media.kompakt.fm/01/assets/releases/fitted/ornvs01-horizon_begins_1.jpg
true
Newlife
https://kompakt.fm/artists/m-ja-wm-t-g4/releases
02:53
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-01-newlife.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=daa442971a96b64dafc629c17b972e1b567580e5c5522f9d7ba52af1e68d6d15
Sky High
Martinou
https://kompakt.fm/artists/t-w-f-ydg-lub3u-kom1/releases
06:21
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-02-sky_high.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=b46eb22383c9ae3a15fa88672f8b351f86d14350733e3a006df63b78855de67c
Phoenix
Ateq & Orion
https://kompakt.fm/artists/q-x-r-lcs-a-mi-e-9yaw-9u/releases
06:50
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-03-phoenix.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=a88f54bb80f8aefd5d07d726f195bf69d46dd8f412401c0891263d49a02aa711
Past Mind
Skyra
https://kompakt.fm/artists/u-2t5cme-kom1/releases
06:57
https://s3.amazonaws.com/media.kompakt.fm/01/assets/tracks/previ/ornvs01-horizon_begins_1-04-past_mind.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIQYIAJAAMTFZXDTQ%2F20261120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20261120T142257Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Signature=8325057cccfe1edd2b3f14af2a52336a4575f5ea5466c5a3e8cf5950b837e433
Bubble love
Ben Kaczor
https://kompakt.fm/artists/q-mv-ui-e-thy-3pvcgkom2/releases
06:56
https://s3.amazonaws.com/media.kompakt.fm/01/asse
… [1986 Zeichen gekürzt]
```
</details>

### 12. `shell` +327s – completed

```
bin/tl-scrape "https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778" --grep "[0-9]:[0-9][0-9]|Intro|Newlife|Sky High|Phoenix|Past Mind|Bubble|Symb|Groovement|Sirens" 2>&1 | head -50
```

<details><summary>Ausgabe</summary>

```
url: https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778
mode: firecrawl (http → firecrawl)
title: Various - Horizon Begins 1 / ORION Records ORNVS01 - Vinyl | deejay.de
source-id: web:https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778
---
…
### Product information:

Various, Horizon Begins 1 ORNVS01, 2025-10-24 00:00:00, 4250101487415.

12inch Vinyl 0.20 kg.
…
[Techno](https://www.deejay.de/m_Techno/sm_News) [Minimal](https://www.deejay.de/m_Techno/sm_News/substyles_205) [Dub](https://www.deejay.de/m_Techno/sm_News/substyles_213) [Deep](https://www.deejay.de/m_Techno/sm_News/substyles_222)

- [**A1**: 200188 - Newlife](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**A2**: Martinou - Sky High](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**B1**: Ateq & Orion - Phoenix](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**B2**: Skyra - Past Mind](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**C1**: Ben Kaczor - Bubble love](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**C2**: Lb Honne - Symbyosis](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**D1**: Hame - Groovement](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**D2**: Soela - Sirens](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")

## Description
…
### [Debut LP](https://www.deejay.de/Orion_Debut_LP_ORNLP01_Vinyl__1270741)

- [**A1**: CRYSTAL 5:21](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play") +7
- [**A2**: PAL6 4:00](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**A3**: R\_N 5:16](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**A4**: VOLUME 2:00](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**B1**: ERYEL 3:43](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**B2**: R\_J 4:27](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**B3**: ENDLESSRUN 6:31](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")
- [**B4**: NEON 3:12](https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778# "Play")

Play all
…
![Vinyl](https://www.deejay.de/pics/images/m/7/8/
… [140 Zeichen gekürzt]
```
</details>

### 13. `shell` +332s – completed

```
bin/tl-scrape "https://www.discogs.com/release/35282479" --grep "i.discogs.com" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
url: https://www.discogs.com/release/35282479
mode: firecrawl (http → firecrawl)
title: Horizon Begins 1 – 2 x Vinyl (12", 45 RPM, Compilation), 2025 [r35282479] | Discogs
source-id: web:https://www.discogs.com/release/35282479
---
…
ReplyHelpful

- [![sergiomaiajesus_'s avatar](https://i.discogs.com/lnEidkXZDlFcVat7xYAOjx83LQoc4rCHfRnNaikNfm0/rs:fill/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LXVzZXItYXZhdGFy/cy9VLTcwMzc0ODYt/MTc2MDAxNjg5MS5w/bmc.jpeg)](https://www.discogs.com/user/sergiomaiajesus_)


…
Reply1 Helpful

- [![bigfish0802's avatar](https://i.discogs.com/S6KAxN80KzQN4MPrDTch0lQphbfvZ9VRJ77u_aSEZs4/rs:fill/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LXVzZXItYXZhdGFy/cy9VLTEyNDE4NTUt/MTY1NjMzNTA4OC5q/cGVn.jpeg)](https://www.discogs.com/user/bigfish0802)
```
</details>

### 14. `shell` +340s – completed

```
bin/tl-scrape "https://www.discogs.com/release/35282479" --grep "45 RPM|16 min|intros|locked|sticker" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
url: https://www.discogs.com/release/35282479
mode: firecrawl (http → firecrawl)
title: Horizon Begins 1 – 2 x Vinyl (12", 45 RPM, Compilation), 2025 [r35282479] | Discogs
source-id: web:https://www.discogs.com/release/35282479
---
…
First track is an uncredited track called "intro" by Unknown Artist.

Comes with the sticker "Orion"

- Barcode: 4250101487415
…
Edited one year ago

16 min on 45 RPM. Why? Why rather not follow basic guidelines and recommendations for vinyl manufacturing? Record sounds obviously dead silent.

Reply12 Helpful
```
</details>

### 15. `shell` +360s – completed

```
bin/tl-scrape "https://www.juno.co.uk/products/horizon-begins-1-vinyl/1111317-01/" --grep "[0-9]:[0-9][0-9]|Newlife|Sky High|Phoenix|Past Mind|Bubble|Symb|Groovement|Sirens" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://www.juno.co.uk/products/horizon-begins-1-vinyl/1111317-01/
mode: http (http)
title: VARIOUS - Horizon Begins 1 Vinyl at Juno Records.
source-id: web:https://www.juno.co.uk/products/horizon-begins-1-vinyl/1111317-01/
---
…
PA Amplifiers | PA Amplifier Systems
PA Speakers | PA Speaker Systems
DJ Bubble Machines
DJ Lighting | DJ Lighting Equipment
DJ Laser Lighting | DJ Lasers
…
Side 1
1.
200188 - "Newlife"
3:25
2.
Martinou - "Sky High"
6:02
Side 2
1.
Ateq & Orion - "Phoenix"
6:53
2.
Skyra - "Past Mind"
7:02
Side 3
1.
Ben Kaczor - "Bubble Love"
6:51
2.
Lb Honne - "Symbyosis"
8:23
Side 4
1.
Hame - "Groovement"
5:37
2.
Soela - "Sirens"
5:42
```
</details>

### 16. `shell` +367s – completed

```
bin/tl-scrape "https://api.discogs.com/releases/35282479" --grep "images|uri|width|duration" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://api.discogs.com/releases/35282479
mode: http (http)
title: 
source-id: web:https://api.discogs.com/releases/35282479
---
…
{"id":35282479,"status":"Accepted","year":2025,"resource_url":"https://api.discogs.com/releases/35282479","uri":"https://www.discogs.com/release/35282479-Various-Horizon-Begins-1","artists":[{"name":"Various","anv":"","join":"","role":"","tracks":"","id":194,"resource_url":"https://api.discogs.com/artists/194"}],"artists_sort":"Various","labels":[{"name":"Orion Records (10)","catno":"ORNVS01","entity_type":"1","entity_type_name":"Label","id":1730519,"resource_url":"https://api.discogs.com/labels/1730519","thumbnail_url":"https://i.discogs.com/LIc1Mh7nZhbGM4Bx_2eg835Ybjv9XVb2-ufLOPX16tU/rs:fit/g:sm/q:90/h:599/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9MLTE3MzA1/MTktMTc2Mjc4MTYx/Ny03MDc1LnBuZw.jpeg"}],"series":[],"companies":[{"name":"Olo Mastering","catno":"","entity_type":"29","entity_type_name":"Mastered At","id":1805100,"resource_url":"https://api.discogs.com/labels/1805100","thumbnail_url":"https://i.discogs.com/XC_7qe5WhbZiUFBDgbp-N3q08Rt8gzp6JZhyGjupdqk/rs:fit/g:sm/q:90/h:400/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9MLTE4MDUx/MDAtMTYyODEwMzYz/My03NjcwLmpwZWc.jpeg"},{"name":"Kompakt Distribution","catno":"","entity_type":"9","entity_type_name":"Distributed By","id":276765,"resource_url":"https://api.discogs.com/labels/276765","thumbnail_url":"https://i.discogs.com/LJOyYO3ABsX9AjxBjFlk5VJq7IEa5Fc-RxEqp4NcMm8/rs:fit/g:sm/q:90/h:162/w:243/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9MLTI3Njc2/NS0xMzI1MzMwOTQ1/LmdpZg.jpeg"},{"name":"Optimal Media GmbH","catno":"BP42876","entity_type":"17","entity_type_name":"Pressed By","id":313190,"resource_url":"https://api.discogs.com/labels/313190","thumbnail_url":"https://i.discogs.com/VHruzHmKvGgDvoWX6iI_4n5eC7mKyVei1mNz573rJtk/rs:fit/g:sm/q:90/h:500/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9MLTMxMzE5/MC0xNTE2MzgxNjk2/LTIzMTgucG5n.jpeg"}],"formats":[{"name":"Vinyl","qty":"2","descriptions":["12\"","45 RPM","Compilation"]}],"data_quality":"Needs Vote","community":{"have":246,"want":124,"rating":{"count":47,"average":4.7},"submitter":{"username":"[removed]","resource_url":"https://discogs.com/users/[removed]"},"contributors":[{"username":"[removed]","resource_url":"https://discogs.com/users/[removed]"},{"username":"[removed]","resource_url":"https://discogs.com/users/[removed]"},{"username":"[removed]","resource_url":"https://discogs.com/users/[removed]
… [3686 Zeichen gekürzt]
```
</details>

### 17. `shell` +372s – completed

```
bin/tl-scrape "https://api.discogs.com/releases/35282479" --max 40000 2>&1 | grep -o "\"title\":\"[^\"]*\",\"description\":\"[^\"]\{0,80\}\|\"duration\":[0-9]*" | tail -20
```

<details><summary>Ausgabe</summary>

```
"duration":411
"title":"Skyra - Past Mind [ORNVS01]","description":"Buy: https://clone.nl/item81028.html\n\nVarious Artists - Horizon Begins 1\n\nUn
"duration":422
"title":"Ben Kaczor - Bubble Love [ORNVS01]","description":"Buy: https://clone.nl/item81028.html\n\nVarious Artists - Horizon Begins 1\n\nUn
"duration":417
"title":"Lb Honne - Symbyosis [ORNVS01]","description":"Buy: https://clone.nl/item81028.html\n\nVarious Artists - Horizon Begins 1\n\nUn
"duration":509
"title":"Hame - Groovement [ORNVS01]","description":"Buy: https://clone.nl/item81028.html\n\nVarious Artists - Horizon Begins 1\n\nUn
"duration":338
"title":"Soela - Sirens [ORNVS01]","description":"Buy: https://clone.nl/item81028.html\n\nVarious Artists - Horizon Begins 1\n\nUn
"duration":348
"duration":
"duration":
"duration":
"duration":
"duration":
"duration":
"duration":
"duration":
"duration":
```
</details>

### 18. `shell` +376s – completed

```
bin/tl-scrape "https://clone.nl/item81028.html" --grep "Intro|Newlife|Sky High|Phoenix|Past Mind|Bubble|Symb|Groovement|Sirens|[0-9]:[0-9][0-9]" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://clone.nl/item81028.html
mode: http (http)
title: Various Artists - Horizon Begins 1(2x12inch) - CLONE.NL
source-id: web:https://clone.nl/item81028.html
---
…
Various Artists - Horizon Begins 1 (2x12inch)
Orion Records presents its first various artists release. A collection of tracks from artists connected to the Orion universe, encountered in clubs and festivals over recent years. The compilation aims to tell a complete story through its tracklist, moving from ambient to deeper shades of techno, with interludes of classic club sounds.
 1 200188 - Newlife
 2 Martinou - Sky High
 3 Ateq & Orion - Phoenix
 4 Skyra - Past Mind
 5 Ben Kaczor - Bubble Love
 6 Lb Honne - Symbyosis
 7 Hame - Groovement
 8 Soela - Sirens
 Techno
 Ambient
```
</details>

### 19. `shell` +385s – completed

```
bin/tl-scrape "https://orion01.bandcamp.com/album/horizon-begins-1" --max 60000 2>&1 | grep -oE "\"(title|duration)\":[^,]{0,60}" | head -30
```

<details><summary>Ausgabe</summary>

```
(no output)
```
</details>

### 20. `shell` +389s – completed

```
bin/tl-scrape "https://orion01.bandcamp.com/album/horizon-begins-1" --max 20000 2>&1 | grep -nE "[0-9]{1,2}:[0-9]{2}|track_row|Newlife|Sky High|Sirens|Intro" | head -40
```

<details><summary>Ausgabe</summary>

```
123:A1: 200188 - Newlife
124:A2: Martinou - Sky High
130:D2: Soela - Sirens
```
</details>

### 21. `shell` +411s – completed

```
bin/tl-validate --schema
```

<details><summary>Ausgabe</summary>

```
{
 "$defs": {
  "Alternative": {
   "additionalProperties": false,
   "properties": {
    "description": {
     "title": "Description",
     "type": "string"
    },
    "source": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Source"
    },
    "why_not": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Why Not"
    }
   },
   "required": [
    "description"
   ],
   "title": "Alternative",
   "type": "object"
  },
  "ArtistCredit": {
   "additionalProperties": false,
   "properties": {
    "name": {
     "description": "one artist or group, as credited (no 'feat.' strings – each featured artist is its own entry)",
     "title": "Name",
     "type": "string"
    },
    "role": {
     "default": "main",
     "enum": [
      "main",
      "featured",
      "remixer",
      "other"
     ],
     "title": "Role",
     "type": "string"
    },
    "tracks": {
     "description": "positions the artist appears on; empty = whole release",
     "items": {
      "type": "string"
     },
     "title": "Tracks",
     "type": "array"
    },
    "sources": {
     "description": "source IDs backing the credit",
     "items": {
      "type": "string"
     },
     "title": "Sources",
     "type": "array"
    }
   },
   "required": [
    "name"
   ],
   "title": "ArtistCredit",
   "type": "object"
  },
  "Conflict": {
   "additionalProperties": false,
   "properties": {
    "field": {
     "title": "Field",
     "type": "string"
    },
    "values": {
     "additionalProperties": {
      "type": "string"
     },
     "description": "source ID → value",
     "title": "Values",
     "type": "object"
    },
    "resolution": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Resolution"
    }
   },
   "required": [
    "field",
    "values"
   ],
   "title": "Conflict",
   "type": "object"
  },
  "Credit": {
   "additionalProperties": false,
   "properties": {
    "name": {
     "title": "Name",
     "type": "string"
    },
    "role": {
     "enum": [
      "composer",
      "lyricist",
      "writer",
      "arranger",
      "producer",
      "other"
     ],
     "title": "Role",
     "type": "string"
    },
    "sources": {
     "items": {
      "type": "string"
     },
     "title": "Sources",
     "t
… [7871 Zeichen gekürzt]
```
</details>

### 22. `shell` +437s – completed

```
bin/tl-search "hardwax ORNVS01 Horizon Begins"; echo "==="; bin/tl-scrape "https://www.hardwax.com/search/?q=ORNVS01" --grep "ORNVS01|Horizon" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
10 hits for: hardwax ORNVS01 Horizon Begins
1. Horizon Begins 1 – 2 x Vinyl (12", 45 RPM, Compilation), 2025 [r35282479] | Discogs
   https://www.discogs.com/de/release/35282479-Various-Horizon-Begins-1
   Matrix / Runout (Runout, side A, etched): ORNVS01 BP42876-01 A1 · Matrix / Runout (Runout, side B, etched): ORNVS01 BP42876-01 B1 · Matrix / Runout (Runout, side C, etched): ORNVS01 BP42876-02 C1 · Matrix / Runout (Runou
   + Matrix / Runout (Runout, side A, etched): ORNVS01 BP42876-01 A1 · Matrix / Runout (Runout, side B, etched): ORNVS01 BP42 | Ateq & Orion - Phoenix [ORNVS01]6:51 · Zur Liste hinzufügen · new arrivals early-November von transitionMehr von Lists a
2. Orion Records Releases | Kompakt
   https://kompakt.fm/labels/orion/releases
   Horizon Begins 1 · Orion Records · 2x12" ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · Stay in the loop and subscribe to our webshop newsletter ·
   + Horizon Begins 1 · Orion Records · 2x12" ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart
3. Horizon Begins 1 - Various Artists
   https://wordandsound.net/release/162303-ORNVS01-Various-Artists-Horizon-Begins-1
   Cat-No:ORNVS01 · Release-Date... first various artists release. “Horizon Begins” is a collection of tracks from artists connected to the Orion universe, encountered in clubs and festivals over recent years....
   + Cat-No:ORNVS01 · Release-Date:24.10.2025 · Genre:Techno · Configuration:2LP · Barcode: 1 · 200188 - Newlife · 2 · Martin | Vinyl Only. After five years of activity, Orion Records is proud to present its first various artists release. “Horizon 
4. Horizon Begins 1 by Various Artists - Orion Records
   https://kompakt.fm/releases/horizon_begins_1
   ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · VINYL ONLY! Play All 2x12" . by · Unreleased Unveröffentlicht · View downloads · Show Full Tracklisting 8 Hide Full Tracklisting 8 · 687c7
   + After five years of activity, Orion Records is proud to present its first various artists release. “Horizon Begins” is a | ORNVS01 · 32,90 € · Incl. VAT · 687c7388d378a · release Add to Cart · View cart · VINYL ONLY! Play All 2x12" . by · Unre
5. Various - Horizon Begins 1 / ORION Records ORNVS01 - Vinyl
   https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778
   Various, Horizon Begins 1 ORNVS01, 2025-10-24 00:00:00, 4250101487415. 12inch Vinyl 0.20 kg. Material information: Vinyl (PVC).
   + Af
… [2562 Zeichen gekürzt]
```
</details>

### 23. `shell` +467s – completed

```
mkdir -p output/work && cat > /tmp/gen.py <<'EOF'
import json
DC="discogs:release/35282479"
VID="discogs:release/35282479/videos"
KO="web:https://kompakt.fm/releases/horizon_begins_1"
JU="web:https://www.juno.co.uk/products/horizon-begins-1-vinyl/1111317-01/"
BC="web:https://orion01.bandcamp.com/album/horizon-begins-1"
DJ="web:https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778"
CL="web:https://clone.nl/item81028.html"

tracks=[
 ("A1",1,"Intro",None,None,[DC],[],["duration_missing"]),
 ("A2",1,"Newlife","200188",173,[DC,KO,BC,CL],[KO,VID],["duration_conflict"]),
 ("A3",1,"Sky High","Martinou",381,[DC,KO,BC,CL,DJ],[KO],["duration_conflict"]),
 ("B1",1,"Phoenix","Ateq & Orion",410,[DC,KO,BC,CL,DJ],[KO,VID],["duration_conflict"]),
 ("B2",1,"Past Mind","Skyra",417,[DC,KO,BC,CL,DJ],[KO],["duration_conflict"]),
 ("C1",2,"Bubble Love","Ben Kaczor",416,[DC,KO,BC,CL,DJ],[KO,VID],["duration_conflict"]),
 ("C2",2,"Symbyosis","Lb Honne",509,[DC,KO,BC,CL,DJ],[KO,VID],["duration_conflict"]),
 ("D1",2,"Groovement","Hame",334,[DC,KO,BC,CL,DJ],[KO],["duration_conflict"]),
 ("D2",2,"Sirens","Soela",344,[DC,KO,BC,CL,DJ],[KO,JU],["duration_conflict"]),
]
out=[{"position":p,"disc":d,"title":t,"artist":a,"duration_s":s,"sources":src,"duration_sources":ds,"flags":fl} for p,d,t,a,s,src,ds,fl in tracks]

artists=[
 {"name":"Unknown Artist","role":"main","tracks":["A1"],"sources":[DC]},
 {"name":"200188","role":"main","tracks":["A2"],"sources":[DC,KO]},
 {"name":"Martinou","role":"main","tracks":["A3"],"sources":[DC,KO]},
 {"name":"Ateq","role":"main","tracks":["B1"],"sources":[DC,KO]},
 {"name":"Orion","role":"main","tracks":["B1"],"sources":[DC,KO]},
 {"name":"Skyra","role":"main","tracks":["B2"],"sources":[DC,BC]},
 {"name":"Ben Kaczor","role":"main","tracks":["C1"],"sources":[DC,KO]},
 {"name":"Lb Honne","role":"main","tracks":["C2"],"sources":[DC,KO]},
 {"name":"Hame","role":"main","tracks":["D1"],"sources":[DC,KO]},
 {"name":"Soela","role":"main","tracks":["D2"],"sources":[DC,KO]},
]

conflicts=[
 {"field":"positions side A (uncredited intro)","values":{DC:"A1 Intro, A2 Newlife, A3 Sky High",BC:"A1 Newlife, A2 Sky High",DJ:"A1 Newlife, A2 Sky High",KO:"1 Newlife, 2 Sky High"}, "resolution":"Followed the barcode-matched Discogs edition and the label's own description ('An unknown project opens the record with an intro') plus the label's official track videos (which list 'Unknown Artist - Intro' first): intro at A1, so Newlife = A2 and Sky High = A3. Shop listings omit the uncredited intro and start side A with Newlife."},
 {"field":"title track C2","values":{DC:"Symbyosis",KO:"Symbyosis",DJ:"Symbyosis",BC:"Symbiosis"}, "resolution":"'Symbyosis' as on the Discogs entry of this pressing, the distributor (Kompakt) listing and the deejay.de listing; Bandcamp writes 'Symbiosis'."},
 {"field":"duration track A2","values":{KO:"2:53",VID:"2:52",JU:"3:25"}, "resolution":"173 s from the distributor listing and the official track video (1 s apart); the Juno listing (3:25) deviates by 32 s and was not used."},
 {"field":"duration track A3","values":{KO:"6:21",VID:"6:25",JU:"6:02"}, "resolution":"381 s from the Kompakt listing of the 2x12\"; official video is 4 s longer (likely silence/tail), Juno 19 s shorter."},
 {"field":"duration track B1","values":{KO:"6:50",VID:"6:51",JU:"6:53"}, "resolution":"410 s from Kompakt; video 411 s and Juno 413 s are close, Kompakt taken as primary (full-length master metadata)."},
 {"field":"duration track B2","values":{KO:"6:57",VID:"7:02",JU:"7:02"}, "resolution":"417 s from Kompakt; video and Juno are 5 s longer - Kompakt taken as primary."},
 {"field":"duration track C1","values":{KO:"6:56",VID:"6:57",JU:"6:51"}, "resolution":"416 s from Kompakt; video 1 s apart, Juno 5 s shorter."},
 {"field":"duration track C2","values":{KO:"8:29",VID:"8:29",JU:"8:23"}, "resolution":"509 s, Kompakt and the official video agree exactly; Juno 6 s shorter."},
 {"field":"duration track D1","values":{KO:"5:34",VID:"5:38",JU:"5:37"}, "resolution":"334 s from Kompakt; video and Juno 3-4 s longer."},
 {"field":"duration track D2","values":{KO:"5:44",VID:"5:48",JU:"5:42"}, "resolution":"344 s from Kompakt; Juno within 2 s, video 4 s longer."},
]

sources=[
 {"id":DC,"url":"https://www.discogs.com/release/35282479","kind":"database","note":"Barcode 4250101487415 match; 2x12\" 45 RPM, DE 2025, ORNVS01; tracklist incl. uncredited intro; no durations"},
 {"id":VID,"url":"https://api.discogs.com/releases/35282479","kind":"database","note":"Official per-track videos embedded in the Discogs release (durations = video lengths)"},
 {"id":KO,"url":"https://kompakt.fm/releases/horizon_begins_1","kind":"shop","note":"Distributor (Kompakt) listing of the 2x12\" ORNVS01: 8 tracks with durations, artist credits"},
 {"id":BC,"url":"https://orion01.bandcamp.com/album/horizon-begins-1","kind":"streaming","note":"Label page: printed side positions A1-D2, title spelling 'Symbiosis'"},
 {"id":DJ,"url":"https://www.deejay.de/Various_Horizon_Begins_1_ORNVS01_Vinyl__1182778","kind":"shop","note":"Tracklist A1-D2 (8 tracks, intro not listed), barcode confirmed"},
 {"id":CL,"url":"https://clone.nl/item81028.html","kind":"shop","note":"Tracklist 1-8, no durations"},
 {"id":JU,"url":"https://www.juno.co.uk/products/horizon-begins-1-vinyl/1111317-01/","kind":"shop","note":"Deviating durations (track 1 3:25 etc.)"},
]

res={
 "input":{"id":"fall-456cefc0","title":"Horizon Begins 1","artist":"Various Artists","ean":"4250101487415","format":None},
 "status":"found",
 "release":{"title":"Horizon Begins 1","artist":"Various Artists","format":"Vinyl","country":"DE","year":2025,
   "label":"Orion Records","catno":"ORNVS01","barcode":"4250101487415",
   "edition":"2x12\" 45 RPM compilation, vinyl only (24 Oct 2025), includes uncredited intro","ids":{"discogs":"35282479"}},
 "tracks":out,
 "artists":artists,
 "total_duration_s":sum(t["duration_s"] for t in out if t["duration_s"]),
 "confidence":0.85,
 "sources":sources,
 "conflicts":conflicts,
 "missing":["duration of A1 'Intro' (uncredited track, no source gives a length)","total_duration_s excludes A1 'Intro'","MusicBrainz has no release for this barcode; no vinyl-verified durations - durations come from distributor metadata and official track videos","performer of A1 'Intro' is unknown (Discogs credits 'Unknown Artist')"],
 "alternatives":[],
 "reasoning":"EAN 4250101487415 is valid and hits exactly one release, Discogs 35282479: Orion Records ORNVS01, 2x12\" 45 RPM vinyl-only compilation, Germany, 24 Oct 2025. Tracklist, side positions and titles are confirmed by the label's Bandcamp page, deejay.de, clone.nl and the Kompakt distributor listing; the uncredited intro at the start of side A is documented in the Discogs notes, the label description and the label's official track videos. No MusicBrainz release exists; durations are taken from the Kompakt listing of this 2x12\" and cross-checked against the official track videos (0-5 s apart); the Juno listing deviates partly strongly and was only used as a cross-check."
}
json.dump(res,open("output/work/fall-456cefc0.json","w"),indent=2,ensure_ascii=False)
EOF
python3 /tmp/gen.py && bin/tl-validate output/work/fall-456cefc0.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 9 tracks (8 with duration), 7 sources, 10 conflicts, confidence=0.85
```
</details>

### 24. `shell` +470s – completed

```
cd <repo> && python3 - <<'EOF'
import json
p="output/work/fall-456cefc0.json"
d=json.load(open(p))
d["input"]={"id":"fall-456cefc0","title":"Horizon Begins 1","artist":"Various Artists","ean":"4250101487415"}
json.dump(d,open(p,"w"),indent=2,ensure_ascii=False)
EOF
bin/tl-validate output/work/fall-456cefc0.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 9 tracks (8 with duration), 7 sources, 10 conflicts, confidence=0.85
```
</details>

> **Agent** +472s: FERTIG found 9 Tracks confidence=0.85
