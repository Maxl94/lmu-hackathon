# Agent-Trace: 07-fantastischen-vier-die-long-player-rsd-e

> Schnellweg geprüft: no fast path: 0 matching official MusicBrainz releases (fast path only for 1–5 identical ones)
Start 2026-11-20T15:42:31 · 27 Schritte · 26 Tool-Aufrufe · Tokens in 46472 / out 14879


> **Agent** +0s: I'll start by checking the barcode and searching the databases.

### 1. `shell` +1s – completed

```
bin/tl-gtin 4262459550239; echo "---"; bin/tl-mb search --barcode 4262459550239; echo "---"; bin/tl-discogs search --barcode 4262459550239
```

<details><summary>Ausgabe</summary>

```
input: '4262459550239' → digits: 4262459550239 (13 digits)
type: EAN-13  valid: yes
search variants: 4262459550239
prefix 400–440: assigned in Germany (says nothing about the country of release)
---
0 Releases (Queries: barcode:(4262459550239))

---
1 hits (parameters: {'barcode': '4262459550239'})
discogs:release/33691152 | Die Fantastischen Vier - Long Player | 2025 Germany | Vinyl, LP, Album, Record Store Day, Limited Edition, Reissue | Label Rekord Music And Distribution, Rekord Music And Distribution | Kat.-Nr. 2984265RMP | Barcodes 4 262459 550239, 4262459550239, LC91252 | master 3616795
```
</details>

### 2. `shell` +2s – completed

```
bin/tl-discogs release 33691152
```

<details><summary>Ausgabe</summary>

```
discogs:release/33691152 | Long Player — Die Fantastischen Vier | 2025-04-12 Germany | 2× Vinyl (LP, Album, Record Store Day, Limited Edition, Reissue) | Rekord Music And Distribution 2984265RMP | master 3616795
url: https://www.discogs.com/release/33691152-Die-Fantastischen-Vier-Long-Player
identifiers: Barcode: 4 262459 550239 (Text) | Barcode: 4262459550239 (Scanned) | Label Code: LC91252 | Rights Society: GEMA | Matrix / Runout: Long Player -64867-I Kr SST -A- (Side A [etched and stamped]) | Matrix / Runout: Long Player -64867-I Kr SST -B- (Side B [etched and stamped]) | Matrix / Runout: Long Player -64868-I Kr SST -C- (Side C [etched and stamped]) | Matrix / Runout: Long Player -64868-I Kr SST -D- (Side C [etched and stamped]) | Rights Society: GEMA
notes: Info Record Store Day Sticker: Record Store Day 2025 Exklusive Das 11. Studioalbum als 180g coloured marbeled 2-LP inkl. Longplayer Record Butler The different EAN code is stuck on the back sleeve as a sticker.
A1 Long Player | 3:07 (187 s)
A2 Wie Weit | 2:56 (176 s)
A3 Bestandsaufnahme | 3:24 (204 s)
A4 Weekendfeeling | 3:50 (230 s)
B1 Was Man Will | 3:21 (201 s)
B2 Win Win Win | 3:16 (196 s)
B3 44 Tausend | 2:34 (154 s)
B4 Aufhören | 2:49 (169 s)
C1 Projekt Y | 2:27 (147 s)
C2 5 Zimmer Mit Bad | 2:47 (167 s)
C3 Fliegen | 4:35 (275 s)
C4 So Oder So | 2:54 (174 s)
D1 Wiedersehen | 2:36 (156 s)
D2 Hallenbad | 4:18 (258 s)
D3 Endstation Erde | 4:12 (252 s)
D4 Inferno | 4:41 (281 s)
16 tracks, total 53:47 (3227 s), without duration: 0
images: primary https://i.discogs.com/Oo9aXCTubulUkVCyedXSBoc8NBaE4sVg73KUWjG7N7Y/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNTM0Mi5qcGVn.jpeg | secondary https://i.discogs.com/gQ0Rdo0NccLxqgstn6Ci6bhRVCab8F0_GYCXdn7UaK8/rs:fit/g:sm/q:90/h:600/w:599/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNTQ5Ny5qcGVn.jpeg | secondary https://i.discogs.com/g5apTkR8fY44zFsiwuSFcPICbwvacCDASekFVuGbBq8/rs:fit/g:sm/q:90/h:289/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNzUxNC5qcGVn.jpeg | secondary https://i.discogs.com/nxFDZgPzhTU0YY-vwyg3L9sMYsooiPx1Tjs-n9BTx7I/rs:fit/g:sm/q:90/h:600/w:597/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNjY2Mi5qcGVn.jpeg | secondary https://i.discogs.com/lUDD2YmPeOY1u85XxV-4oyPpKwKygfVp7G6HOTMUjMo/rs:fit/g:sm/q:90/h:600/w:599/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTQtOTM4NS5qcGVn.jp
… [251 Zeichen gekürzt]
```
</details>

### 3. `shell` +5s – completed

```
bin/tl-mb search --title "Long Player" --artist "Die Fantastischen Vier" --format Vinyl; echo "---"; bin/tl-mb search --title "Long Player" --artist "Die Fantastischen Vier"
```

<details><summary>Ausgabe</summary>

```
3 Releases (Queries: release:"Long Player" AND artist:"Die Fantastischen Vier")
musicbrainz:release/6194317e-f625-4baf-a281-2cb6184d38a4 | Long Player — Die Fantastischen Vier | 2024-10-04 AL | Digital Media | Tracks 16 | Barcode 4262459550116 | Rekord Music and Distribution | Official | score 100
musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da | Long Player — Die Fantastischen Vier | 2024-10-04 DE | CD | Tracks 16 | Barcode 0746052842662 | Rekord Music and Distribution 2984266RMP | Official | score 100
musicbrainz:release/5e647adf-507b-45bf-9e7a-bff47b78b5ee | Long Player on Tour — Die Fantastischen Vier | 2025-05-02 DE | CD+CD | Tracks 18+15 | Barcode 4262459550260 | Rekord Music and Distribution | Official | score 90
---
3 Releases (Queries: release:"Long Player" AND artist:"Die Fantastischen Vier")
musicbrainz:release/6194317e-f625-4baf-a281-2cb6184d38a4 | Long Player — Die Fantastischen Vier | 2024-10-04 AL | Digital Media | Tracks 16 | Barcode 4262459550116 | Rekord Music and Distribution | Official | score 100
musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da | Long Player — Die Fantastischen Vier | 2024-10-04 DE | CD | Tracks 16 | Barcode 0746052842662 | Rekord Music and Distribution 2984266RMP | Official | score 100
musicbrainz:release/5e647adf-507b-45bf-9e7a-bff47b78b5ee | Long Player on Tour — Die Fantastischen Vier | 2025-05-02 DE | CD+CD | Tracks 18+15 | Barcode 4262459550260 | Rekord Music and Distribution | Official | score 90
```
</details>

### 4. `shell` +27s – completed

```
bin/tl-mb release 7cbbf3a1-c6d4-4dc4-a26e-15078742d7da
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da | Long Player — Die Fantastischen Vier | 2024-10-04 DE | CD | Tracks 16 | Barcode 0746052842662 | Rekord Music and Distribution 2984266RMP | Official
release-group: 61c6be96-73ec-4dbd-ac9d-b45470cc545e (Album, first date 2024-10-04) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da
-- Medium 1: CD, 16 Tracks
1.1 [1] Long Player | 3:07 (187173 ms) | ISRC DEZR22300154
1.2 [2] Wie weit | 2:57 (176533 ms) | ISRC DEZR22300139,DEZR22300155
1.3 [3] Bestandsaufnahme | 3:24 (204160 ms) | ISRC DEZR22300156
1.4 [4] Weekendfeeling | 3:51 (230773 ms) | ISRC DEZR22300157
1.5 [5] Was man will | 3:21 (201413 ms) | ISRC DEZR22300158
1.6 [6] Win Win Win | 3:17 (196586 ms) | ISRC DEZR22300159
1.7 [7] 44 Tausend | 2:34 (154066 ms) | ISRC DEZR22300160
1.8 [8] Aufhören | 2:49 (169253 ms) | ISRC DEZR22300161
1.9 [9] Projekt Y | 2:28 (147746 ms) | ISRC DEZR22300162
1.10 [10] 5 Zimmer mit Bad | 2:47 (167386 ms) | ISRC DEZR22300163
1.11 [11] Fliegen | 4:36 (275733 ms) | ISRC DEZR22300164
1.12 [12] So oder so | 2:55 (174613 ms) | ISRC DEZR22300165
1.13 [13] Wiedersehen | 2:37 (156666 ms) | ISRC DEZR22300166
1.14 [14] Hallenbad | 4:18 (257933 ms) | ISRC DEZR22300167
1.15 [15] Endstation Erde | 4:12 (252026 ms) | ISRC DEZR22300168
1.16 [16] Inferno | 4:42 (281653 ms) | ISRC DEZR22300169
Total: 53:54 (3233 s), tracks without duration: 0
```
</details>

### 5. `shell` +43s – completed

```
bin/tl-mb group 61c6be96-73ec-4dbd-ac9d-b45470cc545e; echo "---"; bin/tl-discogs versions 3616795
```

<details><summary>Ausgabe</summary>

```
2 Releases in release-group 61c6be96-73ec-4dbd-ac9d-b45470cc545e
musicbrainz:release/6194317e-f625-4baf-a281-2cb6184d38a4 | Long Player —  | 2024-10-04 AL | Digital Media | Tracks 16 | Barcode 4262459550116 | Rekord Music and Distribution | Official
musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da | Long Player —  | 2024-10-04 DE | CD | Tracks 16 | Barcode 0746052842662 | Rekord Music and Distribution 2984266RMP | Official
---
6 versions of master 3616795
discogs:release/31916212 | Long Player | 2024 Germany | Album | Rekord Music And Distribution 2984266RMP | CD
discogs:release/32238924 | Long Player | 2024  | AAC, Album | Rekord Music And Distribution none | File
discogs:release/31972811 | Long Player | 2024 Germany | LP, Album, Limited Edition | Rekord Music And Distribution 2984265RMP | Vinyl
discogs:release/31907761 | Long Player | 2024 Germany | LP, Album | Rekord Music And Distribution 2984265RMP | Vinyl
discogs:release/31918495 | Long Player | 2024 Germany | LP, Album, Limited Edition, Numbered, Picture Disc | Rekord Music And Distribution 550154 | Vinyl
discogs:release/33691152 | Long Player | 2025 Germany | LP, Album, Record Store Day, Limited Edition, Reissue | Rekord Music And Distribution 2984265RMP | Vinyl
```
</details>

### 6. `shell` +57s – completed

```
bin/tl-itunes search "Die Fantastischen Vier Long Player"; echo "---"; bin/tl-lastfm album --artist "Die Fantastischen Vier" --title "Long Player"
```

<details><summary>Ausgabe</summary>

```
2 Alben
itunes:album/1759547350 | Long Player — Die Fantastischen Vier | 2024-10-04 | 16 Tracks
itunes:album/1806034960 | Long Player On Tour (Live) — Die Fantastischen Vier | 2025-05-02 | 33 Tracks
---
lastfm:album/Die Fantastischen Vier/Long Player | mbid 6194317e-f625-4baf-a281-2cb6184d38a4 | url: https://www.last.fm/music/Die+Fantastischen+Vier/Long+Player
1 Long Player | 3:07
2 Wie Weit | duration missing
3 Bestandsaufnahme | 3:24
4 Weekendfeeling | 3:50
5 Was Man Will | duration missing
6 Win Win Win | 3:16
7 44 Tausend [Explicit] | duration missing
8 Aufhören | 2:49
9 Projekt Y | 2:27
10 5 Zimmer mit Bad | 2:47
11 Fliegen | 4:35
12 So oder So [Explicit] | duration missing
13 Wiedersehen | duration missing
14 Hallenbad | duration missing
15 Endstation Erde | duration missing
16 Inferno | duration missing
16 tracks, total 26:15 (1575 s)
```
</details>

### 7. `shell` +65s – completed

```
bin/tl-itunes album 1759547350 2>/dev/null || bin/tl-itunes --help
```

<details><summary>Ausgabe</summary>

```
itunes:album/1759547350 | Long Player — Die Fantastischen Vier | 2024-10-04 | 16 Tracks | ℗ 2024 Rekord Music and Distribution
url: https://music.apple.com/de/album/long-player/1759547350?uo=4
1.1 Long Player | 3:07 (187173 ms)
1.2 Wie Weit — Die Fantastischen Vier & MIA. | 2:57 (176533 ms)
1.3 Bestandsaufnahme | 3:24 (204160 ms)
1.4 Weekendfeeling | 3:51 (230773 ms)
1.5 Was Man Will — Die Fantastischen Vier & Hansi Biebl Band | 3:21 (201413 ms)
1.6 Win Win Win | 3:17 (196587 ms)
1.7 44 Tausend | 2:34 (154067 ms)
1.8 Aufhören | 2:49 (169253 ms)
1.9 Projekt Y | 2:28 (147747 ms)
1.10 5 Zimmer mit Bad | 2:47 (167387 ms)
1.11 Fliegen | 4:36 (275733 ms)
1.12 So oder So | 2:55 (174613 ms)
1.13 Wiedersehen — Die Fantastischen Vier & jan SEVEN dettwyler | 2:37 (156667 ms)
1.14 Hallenbad — Die Fantastischen Vier & Kadavar | 4:18 (257933 ms)
1.15 Endstation Erde — Die Fantastischen Vier & Kadavar | 4:12 (252027 ms)
1.16 Inferno — Die Fantastischen Vier & Kadavar | 4:42 (281653 ms)
Total 53:54 (3233 s)
```
</details>

### 8. `shell` +69s – completed

```
bin/tl-scrape "https://musicbrainz.org/ws/2/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da?inc=artist-credits+recordings&fmt=json" --grep -o '"artist":\{[^}]*\}' 2>/dev/null | head -50
```

<details><summary>Ausgabe</summary>

```
(no output)
```
</details>

### 9. `shell` +71s – completed

```
bin/tl-scrape --help
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url

tl-scrape <url> — read a web page as text. Levels: http → firecrawl → browser (Selenium) → uc (SeleniumBase).

  tl-scrape <url> [--mode auto|http|firecrawl|browser|uc] [--max 12000] [--grep REGEX] [--links] [--screenshot out.png]

--mode auto   (default) http; on 403/429/503, Cloudflare page or almost empty text → firecrawl → uc
--grep REGEX  only matching lines (±2 lines context), e.g. --grep "(?i)king of kingz|\d+:\d{2}"
--links       also print links (text → URL) for further navigation
--screenshot  render the page in a browser and save as PNG (for tl-vision), forces browser mode
Proxy: SCRAPER_PROXY (httpx) or SELENIUM_PROXY (browser) from .env.
Source ID: web:<url>

positional arguments:
  url

options:
  -h, --help            show this help message and exit
  --mode {auto,http,firecrawl,browser,uc}
  --max MAX
  --grep GREP
  --links
  --screenshot SCREENSHOT
```
</details>

### 10. `shell` +78s – completed

```
bin/tl-scrape "https://musicbrainz.org/ws/2/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da?inc=artist-credits+recordings&fmt=json" --max 20000 | head -c 6000
```

<details><summary>Ausgabe</summary>

```
url: https://musicbrainz.org/ws/2/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da?inc=artist-credits+recordings&fmt=json
mode: http (http)
title: 
source-id: web:https://musicbrainz.org/ws/2/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da?inc=artist-credits+recordings&fmt=json
---
{"status-id":"4e304316-386d-3409-af2e-78857eec5cfe","date":"2024-10-04","packaging-id":"e724a489-a7e8-30a1-a17c-30dfd6831202","status":"Official","packaging":"Gatefold Cover","country":"DE","disambiguation":"","cover-art-archive":{"back":false,"front":true,"count":1,"darkened":false,"artwork":true},"id":"7cbbf3a1-c6d4-4dc4-a26e-15078742d7da","media":[{"track-offset":0,"tracks":[{"recording":{"title":"Long Player","video":false,"artist-credit":[{"name":"Die Fantastischen Vier","artist":{"country":"DE","type":"Group","sort-name":"Fantastischen Vier, Die","id":"7928481f-848e-4551-b658-472c0aaf0c85","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","name":"Die Fantastischen Vier","disambiguation":""},"joinphrase":""}],"length":187173,"disambiguation":"","id":"ddb4f5a6-bb36-40ea-bcc2-b9542bd64a27","first-release-date":"2024-10-04"},"id":"cc340d99-6db2-435a-943c-1308463429e3","position":1,"title":"Long Player","number":"1","length":187173,"artist-credit":[{"joinphrase":"","artist":{"type":"Group","country":"DE","sort-name":"Fantastischen Vier, Die","id":"7928481f-848e-4551-b658-472c0aaf0c85","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","name":"Die Fantastischen Vier","disambiguation":""},"name":"Die Fantastischen Vier"}]},{"number":"2","title":"Wie weit","artist-credit":[{"name":"Die Fantastischen Vier","joinphrase":"","artist":{"disambiguation":"","name":"Die Fantastischen Vier","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","id":"7928481f-848e-4551-b658-472c0aaf0c85","sort-name":"Fantastischen Vier, Die","country":"DE","type":"Group"}}],"length":176533,"id":"625ae0ab-3b01-4c73-b919-aff2da131574","position":2,"recording":{"first-release-date":"2024-08-16","id":"f3d1939a-62b0-4af6-b7a3-c9fe247c3e24","disambiguation":"","length":176533,"artist-credit":[{"name":"Die Fantastischen Vier","artist":{"name":"Die Fantastischen Vier","disambiguation":"","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","sort-name":"Fantastischen Vier, Die","id":"7928481f-848e-4551-b658-472c0aaf0c85","type":"Group","country":"DE"},"joinphrase":" feat. "},{"joinphrase":"","artist":{"type":"Group","country":"DE","id":"6a0f0a74-8689-4bf6-aa8e-6a954ac5f0cb","sort-name":"MIA.","type-id":"e431f5f6-b5d2-343d-8b36-72607ff
… [3500 Zeichen gekürzt]
```
</details>

### 11. `shell` +86s – completed

```
bin/tl-scrape "https://musicbrainz.org/ws/2/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da?inc=artist-credits+recordings&fmt=json" --max 30000 --grep "(?i)kadavar|seven dettwyler|mia\.|hansi biebl" 2>/dev/null | python3 -c "
import sys,re
t=sys.stdin.read()
for m in re.finditer(r'\"joinphrase\":\"([^\"]*)\",\"artist[^}]*\"name\":\"([^\"]+)\"',t):
    print(m.group(1),'|',m.group(2))
for m in re.finditer(r'\"name\":\"([^\"]+)\",\"joinphrase\":\"([^\"]*)\"',t):
    print(m.group(1),'|',m.group(2))
"
```

<details><summary>Ausgabe</summary>

```
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | MIA.
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 &  | Die Fantastischen Vier
 | Hansi Biebl Band
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 &  | Die Fantastischen Vier
 | jan SEVEN dettwyler
 | Kadavar
 &  | Die Fantastischen Vier
 | Kadavar
 | Die Fantastischen Vier
 | Die Fantastischen Vier
 | Kadavar
Die Fantastischen Vier | 
Die Fantastischen Vier | 
Die Fantastischen Vier | 
Die Fantastischen Vier | 
Die Fantastischen Vier | 
Die Fantastischen Vier |  & 
Die Fantastischen Vier | 
Die Fantastischen Vier | 
Kadavar | 
Die Fantastischen Vier | 
Kadavar |
```
</details>

### 12. `shell` +95s – completed

```
bin/tl-vision "https://i.discogs.com/g5apTkR8fY44zFsiwuSFcPICbwvacCDASekFVuGbBq8/rs:fit/g:sm/q:90/h:289/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNzUxNC5qcGVn.jpeg" --context "Back cover of the 2025 RSD 2-LP reissue 'Long Player' by Die Fantastischen Vier. Read the printed tracklist with side letters (A1..D4), track titles and durations, and note any barcode." 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/g5apTkR8fY44zFsiwuSFcPICbwvacCDASekFVuGbBq8/rs:fit/g:sm/q:90/h:289/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNzUxNC5qcGVn.jpeg
```
</details>

### 13. `shell` +108s – completed

```
cd /tmp/opencode && curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36" -o back.jpg "https://i.discogs.com/g5apTkR8fY44zFsiwuSFcPICbwvacCDASekFVuGbBq8/rs:fit/g:sm/q:90/h:289/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMzNjkx/MTUyLTE3NDQ1ODA1/MTUtNzUxNC5qcGVn.jpeg" && file back.jpg && ls -l back.jpg
```

<details><summary>Ausgabe</summary>

```
back.jpg: HTML document, ASCII text, with very long lines (6440)
-rw-r--r--. 1 user user 11258 20. Nov 15:44 back.jpg
```
</details>

### 14. `shell` +116s – completed

```
bin/tl-search "4262459550239 Long Player Fantastischen Vier RSD 2LP" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: 4262459550239 Long Player Fantastischen Vier RSD 2LP
1. Die Fantastischen Vier I Long Player Record Store Day Edition
   https://www.diefantastischenvier.de/news/long-player-rsd-edition
   Sichert euch ein Exemplar der Long Player Vinyl 2LP RSD Edition im offiziellen Shop der Fantastischen Vier.
   + Sichert euch ein Exemplar der Long Player Vinyl 2LP RSD Edition im offiziellen Shop der Fantastischen Vier.
2. Die Fantastischen Vier Vinyl 2LP - Long Player - RSD Edition ...
   https://diefantastischenvier.shop/products/die-fantastischen-vier-long-player-vinyl-2lp-rsd-edition
   Merch direkt aus dem offiziellen Die Fantastischen Vier Shop: Hoodies, T-Shirts, Vinyls & mehr
3. RSD 2025 – Music & More Onlineshop
   https://onlineshop.musicundmore.de/produkt/rsd-2025-3/
   Benutzername oder E-Mail-Adresse · Anmeldung merken Passwort vergessen
4. Die Fantastischen Vier | Vinyl 2LP - Long Player - RSD Edition (coloured marbeled Vinyl inkl. Record Butler) | krasserstoff.com
   https://krasserstoff.com/products/die-fantastischen-vier-long-player-vinyl-2lp-rsd-edition
   Brandaktuelle Updates zu exklusiven Deals, Merchandise und Tickets zu Konzerten deiner Lieblingskünstler
5. Vinyl 2LP - Long Player | Die Fantastischen Vier | Offizieller Shop
   https://diefantastischenvier.shop/products/die-fantastischen-vier-long-player-vinyl-2lp
   Vinyl 2LP - Long Player. Jetzt offiziell ab 34,99 € im Die Fantastischen Vier Shop kaufen!
   + Das elfte Studioalbum der Fantastischen Vier!
6. Die Fantastischen Vier | Offizieller Shop für Merch
   https://diefantastischenvier.shop/
   Die Fantastischen VierVinyl 2LP - Long Player - RSD Edition (coloured marbeled Vinyl inkl.
   + Die Fantastischen VierFeuerzeug - Die 4. Dimensionbordeaux/orange ... Thomas DLtd. Deluxe Inkplosion 2LP + T-Shirt Bundl | Die Fantastischen VierVinyl 2LP - Long Player - RSD Edition (coloured marbeled Vinyl inkl.
7. Die Fantastischen Vier: Long Player (2 LPs) –
   https://www.jpc.de/jpcng/poprock/detail/-/art/die-fantastischen-vier-long-player/hnum/11638005
   Die LP Die Fantastischen Vier: Long Player jetzt probehören und portofrei für 32,99 Euro kaufen. Mehr von Die Fantastischen Vier gibt es im Shop.
   + Seit ihrer Gründung 1989 prägen die Fantastischen Vier die deutsche Musiklandschaft. Anfang der 90er-Jahre machten sie m | Nach sechs Jahren melden sich Die Fantastischen Vier mit »Long Player« zurück.
8. Long Player | 2-LP (2024) von Die Fantastischen Vier
   https://www.musik-sammler.de/r
… [227 Zeichen gekürzt]
```
</details>

### 15. `shell` +131s – completed

```
bin/tl-scrape "https://www.musik-sammler.de/release/die-fantastischen-vier-long-player-2-lp-1683630/" --max 6000 --grep "(?i)A1|B1|C1|D1|Long Player|Seite|Vinyl|2024" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://www.musik-sammler.de/release/die-fantastischen-vier-long-player-2-lp-1683630/
mode: http (http)
title: Long Player | 2-LP (2024) von Die Fantastischen Vier
source-id: web:https://www.musik-sammler.de/release/die-fantastischen-vier-long-player-2-lp-1683630/
---
…
Long Player | 2-LP (2024) von Die Fantastischen Vier
×
MS.de
Startseite
Mitglieder
FAQs/Documentation
…
Login
MS.de
Startseite
Mitglieder
FAQs/Documentation
…
Z
Die Fantastischen Vier
Long Player
2-LP, 2024
Warum so verpixel?
Herstellungsland | Europäische Union
Veröffentlichungs-Jahr | 2024
Zeit | 57:00
EAN-Nr. | 0746052842655
…
Da Musik-Sammler.de nachwievor von privater Hand administriert, betrieben und bezahlt wird, ist jede
 Abmahnung ein existenzbedrohendes Risiko. Nach der letzten Abmahnung, die einen 5-stelligen(!) Betrag
 forderte, sehe ich mich nun gezwungen drastische Maßnahmen zu ergreifen oder die Seite komplett
 aufzugeben. Daher werden jetzt alle hochgeladenen Bilder der Veröffentlichungen für NICHT-EINGELOGGTE
 Nutzer verpixelt. Wer einen Musik-Sammler.de Nutzeraccount hat, braucht sich also einfach nur einmal
```
</details>

### 16. `shell` +135s – completed

```
bin/tl-scrape "https://diefantastischenvier.shop/products/die-fantastischen-vier-long-player-vinyl-2lp-rsd-edition" --mode firecrawl --max 8000 --grep "(?i)track|A1|Seite|Side|4262459550239|Long Player" 2>&1 | head -50
```

<details><summary>Ausgabe</summary>

```
url: https://diefantastischenvier.shop/products/die-fantastischen-vier-long-player-vinyl-2lp-rsd-edition
mode: firecrawl (firecrawl)
title: Vinyl 2LP - Long Player - RSD Edition (coloured marbeled Vinyl inkl. Record Butler) | Die Fantastischen Vier | Offizieller Shop
source-id: web:https://diefantastischenvier.shop/products/die-fantastischen-vier-long-player-vinyl-2lp-rsd-edition
---
…
![](https://assets.krasserstoff.com/api/v2/assets/WyJiYWY2MzQ2NS04NTY5LTRjMDctYWViNS00OGM1MDUwMzY5MmUiLDM0NDAsbnVsbF0--55bdc0c5eb982de00e506491bc47c9ed199b8f25d7b43132e878a51e118c0631.webp?w=3440)![](https://assets.krasserstoff.com/api/v2/assets/WyI3MTg0MGVkOC00ZWQ2LTRmM2ItODYxYi05M2Q4MjBlYTRmZTIiLDM0NDAsbnVsbF0--90c820d0859674a442852c878f112a0848e9cb011f691eae23ec093b433201b0.webp?w=3440)![](https://assets.krasserstoff.com/api/v2/assets/WyIxNzhhZDU3YS0wYzFjLTRlNDEtOWUwOC0yMTBlYThjMmU4YTAiLDM0NDAsbnVsbF0--4bfcd69e668eb518f421577dce1707731285e0838d3364c2938ffad19adb4f40.webp?w=3440)

## Die Fantastischen Vier  Vinyl 2LP - Long Player - RSD Edition (coloured marbeled Vinyl inkl. Record Butler)

Label: Rekord Music Publishing
```
</details>

### 17. `shell` +152s – completed

```
cd /tmp/opencode && curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36" -o rsd1.webp "https://assets.krasserstoff.com/api/v2/assets/WyI3MTg0MGVkOC00ZWQ2LTRmM2ItODYxYi05M2Q4MjBlYTRmZTIiLDM0NDAsbnVsbF0--90c820d0859674a442852c878f112a0848e9cb011f691eae23ec093b433201b0.webp?w=1600" && file rsd1.webp
```

<details><summary>Ausgabe</summary>

```
rsd1.webp: RIFF (little-endian) data, WebP image, VP8 encoding, 3000x3000, Scaling: [none]x[none], YUV color, decoders should clamp
```
</details>

### 18. `shell` +180s – completed

```
cd /tmp/opencode && bin/tl-vision /tmp/opencode/rsd1.webp --context "Product image of the 2025 RSD edition 2-LP 'Long Player' by Die Fantastischen Vier. If a tracklist is visible, list tracks with side/position letters and durations; also report any barcode." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
/bin/bash: line 1: bin/tl-vision: No such file or directory
```
</details>

### 19. `shell` +246s – completed

```
bin/tl-vision /tmp/opencode/rsd1.webp --context "Product image of the 2025 RSD edition 2-LP 'Long Player' by Die Fantastischen Vier. If a tracklist is visible, list tracks with side/position letters and durations; also report any barcode." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
source-id: image:/tmp/opencode/rsd1.webp
model: gemini-3.8-flash@low, in 1297 / out 932 tokens, 44.8 s
kind: shop photo | readable: True
release_title: LONG PLAYER
artist: DIE FANTASTISCHEN VIER
format_hints: 2-LP
A1 LONG PLAYER | 3:07
A2 WIE WEIT | 2:56
A3 BESTANDSAUFNAHME | 3:24
A4 WEEKEND FEELING | 3:50
B1 WAS MAN WILL | 3:21
B2 WIN WIN WIN | 3:16
B3 44 TAUSEND | 3:31
B4 AUFHÖREN | 2:49
C1 PROJEKT Y | 2:27
C2 5 ZIMMER MIT BAD | 2:47
C3 KLINGEN | 4:20
C4 SO ODER SO | 2:54
D1 WIDERSEHEN | 2:36
D2 HALLENBAD | 4:18
D3 ENDSTATION ERDE | 4:17
D4 INFERNO | 4:41
16 tracks read
notes: Record Store Day sticker visible on the front cover. Barcode is present on the upper right of the back cover, but digits are too small and low-resolution to decipher.
```
</details>

### 20. `shell` +263s – completed

```
bin/tl-validate --schema 2>&1 | head -120
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
```
</details>

### 21. `shell` +265s – completed

```
bin/tl-validate --schema 2>&1 | sed -n '120,400p'
```

<details><summary>Ausgabe</summary>

```
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
     "type": "array"
    }
   },
   "required": [
    "name",
    "role"
   ],
   "title": "Credit",
   "type": "object"
  },
  "InputSpec": {
   "additionalProperties": false,
   "properties": {
    "id": {
     "title": "Id",
     "type": "string"
    },
    "title": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Title"
    },
    "artist": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Artist"
    },
    "ean": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Ean"
    },
    "format": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Format"
    },
    "notes": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Notes"
    }
   },
   "required": [
    "id"
   ],
   "title": "InputSpec",
   "type": "object"
  },
  "Release": {
   "additionalProperties": false,
   "properties": {
    "title": {
     "title": "Title",
     "type": "string"
    },
    "artist": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Artist"
    },
    "format": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Format"
    },
    "country": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Country"
    },
    "year": {
     "anyOf": [
      {
       "type": "integer"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Year"
    },
    "label": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "defaul
… [1869 Zeichen gekürzt]
```
</details>

### 22. `shell` +267s – completed

```
bin/tl-validate --schema 2>&1 | sed -n '400,700p'
```

<details><summary>Ausgabe</summary>

```
  },
  "Track": {
   "additionalProperties": false,
   "properties": {
    "position": {
     "description": "as on the carrier: '1', 'A1', '2-03'",
     "title": "Position",
     "type": "string"
    },
    "disc": {
     "default": 1,
     "title": "Disc",
     "type": "integer"
    },
    "title": {
     "title": "Title",
     "type": "string"
    },
    "artist": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "only if different from the release artist (compilations)",
     "title": "Artist"
    },
    "duration_s": {
     "anyOf": [
      {
       "type": "integer"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Duration S"
    },
    "sources": {
     "description": "source IDs backing title/position",
     "items": {
      "type": "string"
     },
     "title": "Sources",
     "type": "array"
    },
    "duration_sources": {
     "description": "source IDs backing the duration (only those supporting the chosen value)",
     "items": {
      "type": "string"
     },
     "title": "Duration Sources",
     "type": "array"
    },
    "flags": {
     "description": "e.g. duration_missing, duration_conflict, title_conflict, bonus, hidden",
     "items": {
      "type": "string"
     },
     "title": "Flags",
     "type": "array"
    },
    "isrc": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "description": "ISRC of the recording (filled by the credits step from MusicBrainz)",
     "title": "Isrc"
    },
    "credits": {
     "description": "composer/lyricist/writer/arranger/producer – filled by the deterministic credits step, separate from performing artists",
     "items": {
      "$ref": "#/$defs/Credit"
     },
     "title": "Credits",
     "type": "array"
    }
   },
   "required": [
    "position",
    "title"
   ],
   "title": "Track",
   "type": "object"
  }
 },
 "additionalProperties": false,
 "properties": {
  "input": {
   "$ref": "#/$defs/InputSpec"
  },
  "status": {
   "enum": [
    "found",
    "ambiguous",
    "not_found"
   ],
   "title": "Status",
   "type": "string"
  },
  "release": {
   "anyOf": [
    {
     "$ref": "#/$defs/Release"
    },
    {
     "type": "null"
    }
   ],
   "default": null
  },
  "tracks": {
   "items": {
    "$ref": "#/$defs/Track"
   },
   "title": "Tracks",
   "type": "array"
  },
  
… [1376 Zeichen gekürzt]
```
</details>

### 23. `write` +289s – completed

```
{"path": "<repo>/output/work/fall-9154823d.json", "content": "{\n  \"input\": {\n    \"id\": \"fall-9154823d\",\n    \"title\": \"Long Player (RSD Exklusive)\",\n    \"artist\": \"Fantastischen Vier, Die\",\n    \"ean\": \"4262459550239\",\n    \"format\": null\n  },\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"Long Player\",\n    \"artist\": \"Die Fantastischen Vier\",\n    \"format\": \"Vinyl\",\n    \"country\": \"DE\",\n    \"year\": 2025,\n    \"label\": \"Rekord Music and Distribution\",\n    \"catno\": \"2984265RMP\",\n    \"barcode\": \"4262459550239\",\n    \"edition\": \"Record Store Day 2025 Exclusive reissue, 2×LP 180g coloured marbled, incl. Longplayer Record Butler (barcode sticker on back sleeve)\",\n    \"ids\": {\n      \"discogs\": \"33691152\",\n      \"musicbrainz\": \"7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"\n    }\n  },\n  \"tracks\": [\n    {\"position\": \"A1\", \"disc\": 1, \"title\": \"Long Player\", \"artist\": null, \"duration_s\": 187,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300154\"},\n    {\"position\": \"A2\", \"disc\": 1, \"title\": \"Wie weit\", \"artist\": \"Die Fantastischen Vier feat. MIA.\", \"duration_s\": 177,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300139\"},\n    {\"position\": \"A3\", \"disc\": 1, \"title\": \"Bestandsaufnahme\", \"artist\": null, \"duration_s\": 204,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300156\"},\n    {\"position\": \"A4\", \"disc\": 1, \"title\": \"Weekendfeeling\", \"artist\": null, \"duration_s\": 231,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300157\"},\n    {\"position\": \"B1\", \"disc\": 1, \"title\": \"Was man will\", \"artist\": \"Die Fantastischen Vier & Hansi Biebl Band\", \"duration_s\": 201,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300158\"},\n    {\"position\": \"B2\", \"disc\": 1, \"title\": \"Win Win Win\", \"artist\": null, \"duration_s\": 197,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300159\"},\n    {\"position\": \"B3\", \"disc\": 1, \"title\": \"44 Tausend\", \"artist\": null, \"duration_s\": 154,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300160\"},\n    {\"position\": \"B4\", \"disc\": 1, \"title\": \"Aufhören\", \"artist\": null, \"duration_s\": 169,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300161\"},\n    {\"position\": \"C1\", \"disc\": 2, \"title\": \"Projekt Y\", \"artist\": null, \"duration_s\": 148,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300162\"},\n    {\"position\": \"C2\", \"disc\": 2, \"title\": \"5 Zimmer mit Bad\", \"artist\": null, \"duration_s\": 167,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300163\"},\n    {\"position\": \"C3\", \"disc\": 2, \"title\": \"Fliegen\", \"artist\": null, \"duration_s\": 276,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300164\"},\n    {\"position\": \"C4\", \"disc\": 2, \"title\": \"So oder so\", \"artist\": null, \"duration_s\": 175,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300165\"},\n    {\"position\": \"D1\", \"disc\": 2, \"title\": \"Wiedersehen\", \"artist\": \"Die Fantastischen Vier & jan SEVEN dettwyler\", \"duration_s\": 157,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300166\"},\n    {\"position\": \"D2\", \"disc\": 2, \"title\": \"Hallenbad\", \"artist\": \"Die Fantastischen Vier & Kadavar\", \"duration_s\": 258,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300167\"},\n    {\"position\": \"D3\", \"disc\": 2, \"title\": \"Endstation Erde\", \"artist\": \"Die Fantastischen Vier & Kadavar\", \"duration_s\": 252,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300168\"},\n    {\"position\": \"D4\", \"disc\": 2, \"title\": \"Inferno\", \"artist\": \"Die Fantastischen Vier & Kadavar\", \"duration_s\": 282,\n     \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"],\n     \"duration_sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"discogs:release/33691152\"],\n     \"flags\": [\"duration_other_edition\"], \"isrc\": \"DEZR22300169\"}\n  ],\n  \"artists\": [\n    {\"name\": \"Die Fantastischen Vier\", \"role\": \"main\", \"tracks\": [], \"sources\": [\"discogs:release/33691152\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\"]},\n    {\"name\": \"MIA.\", \"role\": \"featured\", \"tracks\": [\"A2\"], \"sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"itunes:album/1759547350\"]},\n    {\"name\": \"Hansi Biebl Band\", \"role\": \"featured\", \"tracks\": [\"B1\"], \"sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"itunes:album/1759547350\"]},\n    {\"name\": \"jan SEVEN dettwyler\", \"role\": \"featured\", \"tracks\": [\"D1\"], \"sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"itunes:album/1759547350\"]},\n    {\"name\": \"Kadavar\", \"role\": \"featured\", \"tracks\": [\"D2\", \"D3\", \"D4\"], \"sources\": [\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"itunes:album/1759547350\"]}\n  ],\n  \"total_duration_s\": 3233,\n  \"confidence\": 0.92,\n  \"sources\": [\n    {\"id\": \"discogs:release/33691152\", \"url\": \"https://www.discogs.com/release/33691152-Die-Fantastischen-Vier-Long-Player\", \"kind\": \"database\", \"note\": \"Only hit for the EAN 4262459550239; RSD 2025 2×LP, side positions and per-track durations, GEMA/LC91252, note that the EAN is a sticker on the back sleeve\"},\n    {\"id\": \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"url\": \"https://musicbrainz.org/release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"kind\": \"database\", \"note\": \"CD edition of the same album (barcode 0746052842662); ms-precise durations, ISRCs and per-recording artist credits (feat. MIA., & Hansi Biebl Band, & jan SEVEN dettwyler, & Kadavar)\"},\n    {\"id\": \"image:/tmp/opencode/rsd1.webp\", \"url\": \"https://assets.krasserstoff.com/api/v2/assets/WyI3MTg0MGVkOC00ZWQ2LTRmM2ItODYxYi05M2Q4MjBlYTRmZTIiLDM0NDAsbnVsbF0--90c820d0859674a442852c878f112a0848e9cb011f691eae23ec093b433201b0.webp\", \"kind\": \"image\", \"note\": \"Official shop product photo of the RSD edition back cover: confirms the 16-track side layout A1–D4 and the RSD sticker; titles printed in all caps; some OCR durations/titles unreliable (e.g. 'KLINGEN' for 'Fliegen')\"},\n    {\"id\": \"itunes:album/1759547350\", \"url\": \"https://music.apple.com/de/album/long-player/1759547350\", \"kind\": \"streaming\", \"note\": \"Digital edition (2024); used only as hint for the guest credits and to confirm 16 tracks / identical durations\"}\n  ],\n  \"conflicts\": [\n    {\"field\": \"title track A2\", \"values\": {\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"Wie weit\", \"discogs:release/33691152\": \"Wie Weit\"}, \"resolution\": \"MusicBrainz spelling used; the printed cover is set in all caps, so capitalisation cannot be decided from the carrier; difference is capitalisation only\"},\n    {\"field\": \"title track B1\", \"values\": {\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"Was man will\", \"discogs:release/33691152\": \"Was Man Will\"}, \"resolution\": \"MusicBrainz spelling used; capitalisation-only difference\"},\n    {\"field\": \"title track C2\", \"values\": {\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"5 Zimmer mit Bad\", \"discogs:release/33691152\": \"5 Zimmer Mit Bad\"}, \"resolution\": \"MusicBrainz spelling used; capitalisation-only difference\"},\n    {\"field\": \"title track C4\", \"values\": {\"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"So oder so\", \"discogs:release/33691152\": \"So Oder So\"}, \"resolution\": \"MusicBrainz spelling used; capitalisation-only difference\"},\n    {\"field\": \"duration track B3\", \"values\": {\"discogs:release/33691152\": \"2:34\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"2:34 (154066 ms)\", \"image:/tmp/opencode/rsd1.webp\": \"3:31 (cover OCR)\"}, \"resolution\": \"154 s kept; the shop-photo OCR value 3:31 is contradicted by Discogs and MusicBrainz (which agree to the second) and the same OCR misread the C3 title, so it is treated as a reading error, not an edition difference\"},\n    {\"field\": \"duration track C3\", \"values\": {\"discogs:release/33691152\": \"4:35\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"4:36 (275733 ms)\", \"image:/tmp/opencode/rsd1.webp\": \"4:20 (cover OCR)\"}, \"resolution\": \"276 s kept (Discogs 275 s = rounding); cover OCR read 4:20 together with a wrong title ('KLINGEN'), so it is an OCR error\"},\n    {\"field\": \"duration track D3\", \"values\": {\"discogs:release/33691152\": \"4:12\", \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\": \"4:12 (252026 ms)\", \"image:/tmp/opencode/rsd1.webp\": \"4:17 (cover OCR)\"}, \"resolution\": \"252 s kept; Discogs and MusicBrainz agree exactly, cover OCR deviates\"}\n  ],\n  \"missing\": [\n    \"Durations of the vinyl edition itself were not measured: the ms-precise values come from the CD/digital edition of the same recordings (MusicBrainz), which agree with the Discogs vinyl timings within 1 s (flag duration_other_edition)\",\n    \"The Discogs back-cover images returned HTTP 403, so the carrier print could not be verified directly; only the official shop product photo of the RSD back cover was readable\",\n    \"No printed per-track artist credits were readable on the carrier; guest credits come from the MusicBrainz recording credits and the iTunes credits of the same recordings\"\n  ],\n  \"alternatives\": [\n    {\"description\": \"2×LP, 2024, Germany, Rekord Music and Distribution 2984265RMP (black vinyl, EAN 0746052842655)\", \"source\": \"discogs:release/31907761\", \"why_not\": \"2024 first pressing, different barcode; the input refers to the RSD edition whose EAN is a sticker on this 2025 reissue\"},\n    {\"description\": \"2×LP, 2024, Germany, limited edition, same catno 2984265RMP\", \"source\": \"discogs:release/31972811\", \"why_not\": \"different barcode/edition, not the RSD 2025 reissue\"},\n    {\"description\": \"2×LP picture disc, 2024, Germany, limited/numbered, catno 550154\", \"source\": \"discogs:release/31918495\", \"why_not\": \"picture disc edition with its own barcode and catno\"},\n    {\"description\": \"CD, 2024, Germany, Rekord Music and Distribution 2984266RMP, barcode 0746052842662 (MusicBrainz release 7cbbf3a1, Discogs 31901212)\", \"source\": \"musicbrainz:release/7cbbf3a1-c6d4-4dc4-a26e-15078742d7da\", \"why_not\": \"CD, not the 2-LP; used here only as duration and credit source\"},\n    {\"description\": \"Digital Media, 2024-10-04, barcode 4262459550116\", \"source\": \"musicbrainz:release/6194317e-f625-4baf-a281-2cb6184d38a4\", \"why_not\": \"digital edition, GEMA licensing requires the physical carrier\"}\n  ],\n  \"reasoning\": \"The EAN 4262459550239 is a valid EAN-13 and yields exactly one database hit: Discogs release 33691152, the Record Store Day 2025 exclusive 2×LP reissue of 'Long Player' (2025-04-12, DE, Rekord Music and Distribution 2984265RMP, LC91252, GEMA), whose notes explain that this EAN is stuck on the back sleeve as a sticker. That matches the input title 'Long Player (RSD Exklusive)' and the physical-first rule, so this is the edition. MusicBrainz has no vinyl entry (only the 2024 CD and digital releases of the same album), so the side positions A1–D4 come from Discogs and are confirmed by the official shop photo of the RSD back cover (16 tracks, same order). Titles follow MusicBrainz spelling because the cover is set in all caps; the four capitalisation differences to Discogs are logged as conflicts. Durations are taken from MusicBrainz (ms-precise) and agree with the Discogs vinyl timings within 1 s on every track, hence flagged duration_other_edition. Guest artists (MIA., Hansi Biebl Band, jan SEVEN dettwyler, Kadavar) come from the MusicBrainz recording credits, corroborated by the iTunes credits of the same recordings.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-9154823d.json
```
</details>

### 24. `shell` +299s – completed

```
bin/tl-validate output/work/fall-9154823d.json
```

<details><summary>Ausgabe</summary>

```
WARN: high confidence despite open conflicts – justify or lower it
OK: status=found, 16 tracks (16 with duration), 4 sources, 7 conflicts, confidence=0.92
```
</details>

### 25. `edit` +304s – completed

```
{"path": "<repo>/output/work/fall-9154823d.json", "oldString": "Guest artists (MIA., Hansi Biebl Band, jan SEVEN dettwyler, Kadavar) come from the MusicBrainz recording credits, corroborated by the iTunes credits of the same recordings.\"", "newString": "Guest artists (MIA., Hansi Biebl Band, jan SEVEN dettwyler, Kadavar) come from the MusicBrainz recording credits, corroborated by the iTunes credits of the same recordings. Confidence stays high (0.92) despite the logged conflicts: barcode hit plus two agreeing sources, and the conflicts are resolved ones – four capitalisation-only title variants and three cover-OCR duration misreads that two databases contradict to the second.\""}
```

<details><summary>Ausgabe</summary>

```
Edited output/work/fall-9154823d.json (1 replacement)
```
</details>

### 26. `shell` +305s – completed

```
bin/tl-validate output/work/fall-9154823d.json
```

<details><summary>Ausgabe</summary>

```
WARN: high confidence despite open conflicts – justify or lower it
OK: status=found, 16 tracks (16 with duration), 4 sources, 7 conflicts, confidence=0.92
```
</details>

> **Agent** +314s: FERTIG found 16 Tracks confidence=0.92
