# Agent-Trace: 04-foreigner-live-in-chicago-2lp

> Schnellweg geprüft: no fast path: 0 matching official MusicBrainz releases (fast path only for 1–5 identical ones)
Start 2026-11-20T15:42:21 · 15 Schritte · 23 Tool-Aufrufe · Tokens in 37133 / out 10428


> **Agent** +1s: I'll start by checking the barcode and finding candidates.

### 1. `shell` +1s – completed

```
bin/tl-mb search --barcode 4029759205296
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: barcode:(4029759205296))
```
</details>

### 2. `shell` +1s – completed

```
bin/tl-discogs search --barcode 4029759205296
```

<details><summary>Ausgabe</summary>

```
1 hits (parameters: {'barcode': '4029759205296'})
discogs:release/34744227 | Foreigner - Live In Chicago | 2025 Europe | Vinyl, LP, Album, Reissue, Stereo | Label Ear Music, Edel | Kat.-Nr. 0220529EMU | Barcodes 4 029759 205296, 4029759205296, LC 36979 | master 896990
```
</details>

### 3. `shell` +1s – completed

```
bin/tl-gtin 4029759205296
```

<details><summary>Ausgabe</summary>

```
input: '4029759205296' → digits: 4029759205296 (13 digits)
type: EAN-13  valid: yes
search variants: 4029759205296
prefix 400–440: assigned in Germany (says nothing about the country of release)
```
</details>

### 4. `shell` +3s – completed

```
bin/tl-discogs release 34744227
```

<details><summary>Ausgabe</summary>

```
discogs:release/34744227 | Live In Chicago — Foreigner | 2025-04-11 Europe | 2× Vinyl (LP, Album, Reissue, Stereo) | Ear Music 0220529EMU; Edel 0220529EMU | master 896990
url: https://www.discogs.com/release/34744227-Foreigner-Live-In-Chicago
identifiers: Barcode: 4 029759 205296 (Printed) | Barcode: 4029759205296 (Scanned) | Label Code: LC 36979
notes: Recorded live at the Arcada Theater, St. Charles, Illinois, USA on March 26th and 27th, 2011. First vinyl release Issued on 180 gram vinyl Double LP in single LP cover
A1 Double Vision | duration missing
A2 Head Games  | duration missing
A3 Cold As Ice | duration missing
A4 Waiting For A Girl Like You | duration missing
B1 When It Comes To Love | duration missing
B2 Blue Morning, Blue Day | duration missing
B3 Dirty White Boy | duration missing
B4 Starrider | duration missing
C1 Feels Like The First Time | duration missing
C2 Urgent | duration missing
C3 I Want To Know What Love Is | duration missing
D1 Hot Blooded | duration missing
D2 Jukebox Hero | duration missing
13 tracks, total 0:00 (0 s), without duration: 13
images: primary https://i.discogs.com/4mVjthbpHgGtRTOpKEx6NuQxJfnR-iEcDmO944T9N8Y/rs:fit/g:sm/q:90/h:596/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM0NzQ0/MjI3LTE3NTQ0MzY4/MzItMzIwMC5qcGVn.jpeg | secondary https://i.discogs.com/ZoqNU5IkUqgp-PNPpryFflHoBjZm6qf0zOz1AwemQ8U/rs:fit/g:sm/q:90/h:596/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM0NzQ0/MjI3LTE3NTQ0MzY4/MjgtNzQ1MS5qcGVn.jpeg | secondary https://i.discogs.com/ZN9Y5Yqtl9xCyu7db0Uh5S2rNR52SP2LEq6btPXQO1Y/rs:fit/g:sm/q:90/h:600/w:598/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM0NzQ0/MjI3LTE3NTQ0MzY4/NjgtNzgyNy5qcGVn.jpeg | secondary https://i.discogs.com/IFi07YyT423IbN-P4wkJBxF-VGuEjpHd8vZ5DfhUGVw/rs:fit/g:sm/q:90/h:600/w:598/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM0NzQ0/MjI3LTE3NTQ0MzY4/NjgtNTM5Mi5qcGVn.jpeg | secondary https://i.discogs.com/bHWPNtvtWJSR3tOnt6s5UfqiqwYu9-NQPKRm-rKYy0o/rs:fit/g:sm/q:90/h:589/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM0NzQ0/MjI3LTE3NTQ0MzY4/NjQtOTI3My5qcGVn.jpeg | secondary https://i.discogs.com/MNE8y9mniumYny_QVKdL7SAsvaaUo-m7lrAS9upCBbk/rs:fit/g:sm/q:90/h:600/w:596/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM0NzQ0/MjI3LTE3NTQ0MzY4/NjMtODY5OC5qcGVn.jpeg
community: have 47 want 10 data_quality Needs Vote
```
</details>

### 5. `shell` +3s – completed

```
bin/tl-mb search --title "Live in Chicago" --artist Foreigner
```

<details><summary>Ausgabe</summary>

```
2 Releases (Queries: release:"Live in Chicago" AND artist:"Foreigner")
musicbrainz:release/0db824ee-9259-4c64-be7f-25130beba083 | Live in Chicago — Foreigner | 2025-04-11 XW | Digital Media | Tracks 13 | Barcode 4029759205272 | earMUSIC | Official | score 100
musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459 | Live in Chicago — Foreigner | 2025-04-11 XE | CD | Tracks 13 | Barcode 4029759205289 | Edel Company 0220528EMU | Official | score 100
```
</details>

### 6. `shell` +6s – completed

```
bin/tl-mb release 13ed9b61-194b-4133-81a3-703edec19459
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459 | Live in Chicago — Foreigner | 2025-04-11 XE | CD | Tracks 13 | Barcode 4029759205289 | Edel Company 0220528EMU | Official
release-group: 89af84e1-6dd2-4f56-82aa-695950463e94 (Album, first date 2025-04-11) | Cover: front=True back=True images=10
url: https://musicbrainz.org/release/13ed9b61-194b-4133-81a3-703edec19459
-- Medium 1: CD, 13 Tracks
1.1 [1] Double Vision | 3:59 (238840 ms)
1.2 [2] Head Games | 5:39 (339386 ms)
1.3 [3] Cold as Ice | 5:44 (343546 ms)
1.4 [4] Waiting for a Girl Like You | 6:00 (360226 ms)
1.5 [5] When It Comes to Love | 4:00 (240466 ms)
1.6 [6] Blue Morning, Blue Day | 3:42 (221920 ms)
1.7 [7] Dirty White Boy | 4:51 (291173 ms)
1.8 [8] Starrider | 7:00 (420466 ms)
1.9 [9] Feels Like the First Time | 4:48 (287933 ms)
1.10 [10] Urgent | 7:33 (452546 ms)
1.11 [11] I Want to Know What Love Is | 7:50 (470253 ms)
1.12 [12] Hot Blooded | 5:59 (359386 ms)
1.13 [13] Juke Box Hero | 11:11 (671426 ms)
Total: 1:18:18 (4697 s), tracks without duration: 0
```
</details>

### 7. `shell` +6s – completed

```
bin/tl-mb release 0db824ee-9259-4c64-be7f-25130beba083
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/0db824ee-9259-4c64-be7f-25130beba083 | Live in Chicago — Foreigner | 2025-04-11 XW | Digital Media | Tracks 13 | Barcode 4029759205272 | earMUSIC | Official
release-group: 89af84e1-6dd2-4f56-82aa-695950463e94 (Album, first date 2025-04-11) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/0db824ee-9259-4c64-be7f-25130beba083
-- Medium 1: Digital Media, 13 Tracks
1.1 [1] Double Vision | 3:49 (229000 ms)
1.2 [2] Head Games | 5:39 (339000 ms)
1.3 [3] Cold as Ice | 5:43 (343000 ms)
1.4 [4] Waiting for a Girl Like You | 6:00 (360000 ms)
1.5 [5] When It Comes to Love | 4:00 (240000 ms)
1.6 [6] Blue Morning, Blue Day | 3:41 (221000 ms)
1.7 [7] Dirty White Boy | 4:51 (291000 ms)
1.8 [8] Starrider | 7:00 (420000 ms)
1.9 [9] Feels Like the First Time | 4:47 (287000 ms)
1.10 [10] Urgent | 7:32 (452000 ms)
1.11 [11] I Want to Know What Love Is | 7:50 (470000 ms)
1.12 [12] Hot Blooded | 5:59 (359000 ms)
1.13 [13] Juke Box Hero | 11:11 (671000 ms)
Total: 1:18:02 (4682 s), tracks without duration: 0
```
</details>

### 8. `shell` +17s – completed

```
bin/tl-discogs versions 896990 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
5 versions of master 896990
discogs:release/7014376 | Live In Chicago | 2012 Europe |  | Ear Music 0208091ERE | Blu-ray
discogs:release/7326548 | Live In Chicago | 2012 Russia | Unofficial Release | ООО "Диск Пойнт" BR 1895 | Blu-ray-R
discogs:release/14130687 | Live In Chicago | 2012 Europe | DVD-Video | Ear Music 0208090ERE | DVD
discogs:release/33766896 | Live In Chicago | 2025 Europe | Album, Reissue, Stereo | Ear Music 0220528EMU | CD
discogs:release/34744227 | Live In Chicago | 2025 Europe | LP, Album, Reissue, Stereo | Ear Music 0220529EMU | Vinyl
```
</details>

### 9. `shell` +17s – completed

```
bin/tl-caa 13ed9b61-194b-4133-81a3-703edec19459 2>&1 | head -30; echo ---; bin/tl-itunes search "Foreigner Live in Chicago" 2>&1 | head -20; echo ---; bin/tl-deezer search --artist Foreigner --title "Live in Chicago" 2>&1 | head -10
```

<details><summary>Ausgabe</summary>

```
caa:release/13ed9b61-194b-4133-81a3-703edec19459/43985736779 | Front | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/43985736779-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880048015 | Front | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880048015-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880049212 | Back, Spine | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880051987 | Front, Booklet | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880051987-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880056985 | Booklet | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880056985-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880066254 | Booklet | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880066254-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880076357 | Booklet | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880076357-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880085509 | Medium | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880085509-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880093657 | Matrix/Runout | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880093657-1200.jpg
caa:release/13ed9b61-194b-4133-81a3-703edec19459/41880094357 | Tray | https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880094357-1200.jpg
10 images · read tracklist: tl-vision <url> --context "…"
---
5 Alben
itunes:album/1797510964 | Live in Chicago — Foreigner | 2025-04-11 | 13 Tracks
itunes:album/1104084146 | Live in Chicago (feat. Foreigners Band) - Single — Ayanda Khumalo | 2016-05-01 | 3 Tracks
itunes:album/1752773729 | I DON'T WANNA LIVE IN A WORLD WITHOUT YOU - Single — Clinton Kane | 2024-06-28 | 1 Tracks
itunes:album/724937256 | Live In Los Angeles (Remastered 2003) [feat. Frankie Beverly] — Maze featuring Frankie Beverly | 1986-07-20 | 18 Tracks
itunes:album/159548677 | Live In Houston 1981: Escape Tour (Remastered) — Journey | 2005-11-15 | 19 Tracks
---
1 Alben (q=artist:"Foreigner" album:"Live in Chicago")
deezer:album/716011231 | Live in Chicago — Foreigner | 13 Tracks | album
```
</details>

### 10. `shell` +49s – completed

```
bin/tl-itunes upc 4029759205296 2>&1 | head -25; echo ---; bin/tl-itunes album 1797510964 2>&1 | head -25
```

<details><summary>Ausgabe</summary>

```
no hit (physical releases are often missing from the digital catalogue)
---
itunes:album/1797510964 | Live in Chicago — Foreigner | 2025-04-11 | 13 Tracks | ℗ 2025 Trigger Productions, Inc. under exclusive license to earMUSIC, a label of Edel Music & Entertainment GmbH
url: https://music.apple.com/de/album/live-in-chicago/1797510964?uo=4
1.1 Double Vision (Live in Chicago) | 3:49 (229155 ms)
1.2 Head Games (Live in Chicago) | 5:39 (339387 ms)
1.3 Cold as Ice (Live in Chicago) | 5:44 (343547 ms)
1.4 Waiting for a Girl Like You (Live in Chicago) | 6:00 (360227 ms)
1.5 When It Comes to Love (Live in Chicago) | 4:00 (240467 ms)
1.6 Blue Morning, Blue Day (Live in Chicago) | 3:42 (221920 ms)
1.7 Dirty White Boy (Live in Chicago) | 4:51 (291173 ms)
1.8 Starrider (Live in Chicago) | 7:00 (420467 ms)
1.9 Feels Like the First Time (Live in Chicago) | 4:48 (287933 ms)
1.10 Urgent (Live in Chicago) | 7:33 (452547 ms)
1.11 I Want to Know What Love Is (Live in Chicago) | 7:50 (470253 ms)
1.12 Hot Blooded (Live in Chicago) | 5:59 (359387 ms)
1.13 Juke Box Hero (Live in Chicago) | 11:11 (671427 ms)
Total 1:18:08 (4687 s)
```
</details>

### 11. `shell` +50s – completed

```
bin/tl-vision "https://i.discogs.com/ZoqNU5IkUqgp-PNPpryFflHoBjZm6qf0zOz1AwemQ8U/rs:fit/g:sm/q:90/h:596/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM0NzQ0MjI3LTE3NTQ0MzY4MzItMzIwMC5qcGVn.jpeg" --context "Discogs release 34744227 Foreigner Live In Chicago 2LP. Read the title as printed and any tracklist text visible (side/position labels A1..D2, titles, durations)." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/ZoqNU5IkUqgp-PNPpryFflHoBjZm6qf0zOz1AwemQ8U/rs:fit/g:sm/q:90/h:596/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM0NzQ0MjI3LTE3NTQ0MzY4MzItMzIwMC5qcGVn.jpeg
```
</details>

### 12. `shell` +62s – completed

```
bin/tl-deezer upc 4029759205272 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
deezer:album/716011231 | Live in Chicago — Foreigner | 2025-04-11 | UPC 4029759205272 | 13 Tracks | Label earMUSIC
url: https://www.deezer.com/album/716011231
1.1 Double Vision (Live in Chicago) | 3:49
1.2 Head Games (Live in Chicago) | 5:39
1.3 Cold as Ice (Live in Chicago) | 5:43
1.4 Waiting for a Girl Like You (Live in Chicago) | 6:00
1.5 When It Comes to Love (Live in Chicago) | 4:00
1.6 Blue Morning, Blue Day (Live in Chicago) | 3:41
1.7 Dirty White Boy (Live in Chicago) | 4:51
1.8 Starrider (Live in Chicago) | 7:00
1.9 Feels Like the First Time (Live in Chicago) | 4:47
1.10 Urgent (Live in Chicago) | 7:32
1.11 I Want to Know What Love Is (Live in Chicago) | 7:50
1.12 Hot Blooded (Live in Chicago) | 5:59
1.13 Juke Box Hero (Live in Chicago) | 11:11
Total 1:18:02 (4682 s)
```
</details>

### 13. `shell` +64s – completed

```
bin/tl-search "Foreigner \"Live In Chicago\" 2LP 0220529EMU vinyl tracklist" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
10 hits for: Foreigner "Live In Chicago" 2LP 0220529EMU vinyl tracklist
1. Foreigner - LIVE IN CHICAGO / earMUSIC / 0220529EMU | 2LP Vinyl kaufen | decks.de
   https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de
   Foreigner - LIVE IN CHICAGO als 2LP Vinyl auf earMUSIC / 0220529EMU. Mit Tracklist und Audio-Previews. Jetzt bei decks.de kaufen.
   + Die Geschichte von Foreigner wird seit fast 50 Jahren geschrie- ben und umfasst unzählige, unvergessliche Live-Auftritte
2. FOREIGNER - Live In Chicago (Vinyl) (2LP (180g)) - Foreigner
   https://www.nervegas.com.au/foreigner-live-in-chicago-2lp
   FOREIGNER - Live In Chicago (Vinyl) (2LP (180g)) Cat No: 0220529EMU Barcode: 4029759205296 Packaging: 2LP (180g)
   + FOREIGNER - Live In Chicago (Vinyl) (2LP (180g)) Cat No: 0220529EMU Barcode: 4029759205296 Packaging: 2LP (180g) | In 2011, iconic rock legends Foreigner delivered an electrifying 85-minute set in front of an enthusiastic crowd at the 
3. Foreigner – Live In Chicago | Releases | Discogs
   https://www.discogs.com/de/master/896990-Foreigner-Live-In-Chicago
   Durchsuchen Sie die Trackliste, Mitwirkenden, Statistiken und mehr nach Live In Chicago von Foreigner. Vergleichen Sie Versionen und kaufen Sie auf Discogs.
   + Entdecken Sie Songs, Empfehlungen und andere Albumdetails für Live In Chicago von Foreigner. Vergleichen Sie unterschied
4. FOREIGNER - Live in Chicago - 2-LP | Rock & Heavy Metal Empire
   https://napalmrecords.com/deutsch/foreigner-live-in-chicago-lp.html
   Buy from Napalm Records Onlineshop
   + Buy from Napalm Records Onlineshop
5. Live in Chicago | Foreigner LP | EMP
   https://www.emp.de/p/live-in-chicago/583437.html
   Die Geschichte von Foreigner wird seit fast 50 Jahren geschrieben und umfasst unzählige, unvergessliche Live-Auftritte. "Live in Chicago" ist vollgepackt mit Hits wie "Urgent", "I Want to Know What Love Is" und "Juke Box
```
</details>

### 14. `shell` +66s – completed

```
bin/tl-scrape "https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de" --grep -i "a1|b1|c1|d1|double|starrider|juke|tracklist" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 15. `shell` +73s – completed

```
bin/tl-scrape "https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de" --grep "(?i)(a1|b1|c1|d1|double vision|starrider|juke box|tracklist)" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de
mode: http (http)
title: Foreigner - LIVE IN CHICAGO / earMUSIC / 0220529EMU | 2LP Vinyl kaufen | decks.de
source-id: web:https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de
---
…
Side
BPM
Tracklist
A1: Double vision
A2: Head games
A3: Cold as ice
…
A6: Blue morning, blue day
A7: Dirty white boy
A8: Starrider
B1: Feels like the first time
B2: Urgent
B3: I want to know what love is
B4: Hot blooded
B5: Juke box hero
Die Geschichte von Foreigner wird seit fast 50 Jahren geschrie-
ben und umfasst unzählige, unvergessliche Live-Auftritte. "Live in
Chicago" ist vollgepackt mit Hits wie "Urgent", "I Want to Know
What Love Is" und "Juke Box Hero". Ursprünglich 2012 auf Blu-ray
und DVD veröffentlicht, wird "Live in Chicago" nun zum ersten Mal
in einem CD Jewelcase zusammen mit einer 2 LP-Vinyl-Version
```
</details>

### 16. `shell` +85s – completed

```
bin/tl-scrape "https://www.emp.de/p/live-in-chicago/583437.html" --grep "(?i)(A1|B1|C1|D1|Double Vision|Starrider|Juke Box|Tracklist|Disc 1)" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://www.emp.de/p/live-in-chicago/583437.html
mode: http (http)
title: Live in Chicago | Foreigner LP | EMP
source-id: web:https://www.emp.de/p/live-in-chicago/583437.html
---
…
Unfassbar guter Service
 Artikelbeschreibung
Die Geschichte von Foreigner wird seit fast 50 Jahren geschrieben und umfasst unzählige, unvergessliche Live-Auftritte. "Live in Chicago" ist vollgepackt mit Hits wie "Urgent", "I Want to Know What Love Is" und "Juke Box Hero". Ursprünglich 2012 auf Blu-ray und DVD veröffentlicht, wird "Live in Chicago" 2025 zum ersten Mal in einem CD Jewelcase zusammen mit einer 2 LP-Vinyl-Version erhältlich sein, wofür alle Formate gemastert wurden.
 Allgemein
Artikelnummer: | 583437
…
Germany
[email removed]
Tracklist
LP 1
1.
Double vision
2.
Head games
…
Dirty white boy
8.
Starrider
9.
Feels like the first time
…
Hot blooded
13.
Juke box hero
0 Bewertungen
```
</details>

### 17. `shell` +96s – completed

```
bin/tl-scrape "https://www.nervegas.com.au/foreigner-live-in-chicago-2lp" --grep "(?i)(A1|B1|C1|D1|Double Vision|Starrider|Juke Box|Tracklist)" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://www.nervegas.com.au/foreigner-live-in-chicago-2lp
mode: uc (http → firecrawl → uc)
title: www.nervegas.com.au
source-id: web:https://www.nervegas.com.au/foreigner-live-in-chicago-2lp
---
(keine Zeile passt auf '(?i)(A1|B1|C1|D1|Double Vision|Starrider|Juke Box|Tracklist)')
```
</details>

### 18. `shell` +105s – completed

```
bin/tl-validate --schema 2>&1 | head -80
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
```
</details>

### 19. `shell` +105s – completed

```
bin/tl-discogs release 33766896 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
discogs:release/33766896 | Live In Chicago — Foreigner | 2025-04-11 Europe | 1× CD (Album, Reissue, Stereo) | Ear Music 0220528EMU; Edel 0220528EMU | master 896990
url: https://www.discogs.com/release/33766896-Foreigner-Live-In-Chicago
identifiers: Barcode: 4029759205289 | Label Code: LC 36979 | Rights Society: GEMA/BIEM | Matrix / Runout: AP34351-01 manufactured by optimal media GmbH | Mastering SID Code: IFPI L578 | Mould SID Code: IFPI 9723
notes: This edition is issued in a standard jewel case with a transparent tray, an 8-page booklet and an inlay. The concert was actually not recorded in Chicago, but at the Arcada Theater in St. Charles, Illinois on March the 26th & 27th, 2011. This recording was originally only released on DVD and Blu-ray. It's available on CD for the first time. Made in Germany. Additional track information: "Double Vi
1 Double Vision | 3:58 (238 s)
2 Head Games | 5:39 (339 s)
3 Cold As Ice | 5:43 (343 s)
4 Waiting For A Girl Like You | 6:00 (360 s)
5 When It Comes To Love | 4:00 (240 s)
6 Blue Morning, Blue Day | 3:41 (221 s)
7 Dirty White Boy | 4:51 (291 s)
8 Starrider | 7:00 (420 s)
9 Feels Like The First Time | 4:47 (287 s)
10 Urgent | 7:32 (452 s)
11 I Want To Know What Love Is | 7:50 (470 s)
12 Hot Blooded | 5:59 (359 s)
13 Juke Box Hero | 11:11 (671 s)
13 tracks, total 78:11 (4691 s), without duration: 0
images: primary https://i.discogs.com/2nZHV7mY0VqTJ6-EE-TGiFDblskSDzQCAvOvvMqi66w/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzY2/ODk2LTE3NTQ0Mzcz/ODgtMTM4NS5qcGVn.jpeg | secondary https://i.discogs.com/iu0Nj2C9qj1EXBuMZSOAkXb7gR0s7JB17RiD4qpMIDI/rs:fit/g:sm/q:90/h:472/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzY2/ODk2LTE3NTQ0Mzcz/ODctODg0NC5qcGVn.jpeg | secondary https://i.discogs.com/c5Y0O6WQxjRPuvquZXpLeGb_NWf0ELikTeNtHFHIYCg/rs:fit/g:sm/q:90/h:587/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzY2/ODk2LTE3NTQ0Mzcz/ODYtNjExOC5qcGVn.jpeg | secondary https://i.discogs.com/qvPiMWILx38z3g4A3hX93pkcbpBuhgWFyZc1Ytkl45E/rs:fit/g:sm/q:90/h:589/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzY2/ODk2LTE3NTQ0Mzc0/MDMtNzQzMi5qcGVn.jpeg | secondary https://i.discogs.com/jziDdFwAWK2vd6Gwb8_Oy9R3PygSa1m03SZk0e5Mo98/rs:fit/g:sm/q:90/h:469/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzY2/ODk2LTE3NTQ0Mzc0/MDMtNTgyMy5qcGVn.jpeg
community: have 42 want 10 data_quality Needs Vote
```
</details>

### 20. `shell` +145s – completed

```
bin/tl-vision "https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg" --context "Back cover of Foreigner 'Live in Chicago' (earMUSIC 2025 CD, same program as the 2LP). Transcribe the title exactly as printed and every track title with its number, preserving capitalisation." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg
model: gemini-3.8-flash@low, in 1280 / out 519 tokens, 24.3 s
kind: back cover | readable: True
release_title: LIVE IN CHICAGO
artist: FOREIGNER
label: earMUSIC
catalog_number: 0220528EMU
barcode: 4029759205289
format_hints: CD
1. Double Vision | no duration printed
2. Head Games | no duration printed
3. Cold As Ice | no duration printed
4. Waiting For A Girl Like You | no duration printed
5. When It Comes To Love | no duration printed
6. Blue Morning, Blue Day | no duration printed
7. Dirty White Boy | no duration printed
8. Starrider | no duration printed
9. Feels Like The First Time | no duration printed
10. Urgent | no duration printed
11. I Want To Know What Love Is | no duration printed
12. Hot Blooded | no duration printed
13. Juke Box Hero | no duration printed
13 tracks read
notes: Recorded live at Arcada Theater, St. Charles, IL, March 26th & 27th, 2011.
Available for the first time on CD.
```
</details>

### 21. `shell` +163s – completed

```
bin/tl-validate --schema 2>&1 | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d['\$defs'].get('Conflict'),indent=1)); print(list(d['\$defs'])); print(json.dumps(d['\$defs']['Release'],indent=1)[:1500])"
```

<details><summary>Ausgabe</summary>

```
{
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
   "description": "source ID \u2192 value",
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
}
['Alternative', 'ArtistCredit', 'Conflict', 'Credit', 'InputSpec', 'Release', 'Source', 'Track']
{
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
   "default": null,
   "title": "Label"
  },
  "catno": {
   "anyOf": [
    {
     "type": "string"
    },
    {
     "type": "null"
    }
   ],
   "default": null,
   "title": "Catno"
  },
  "barcode": {
   "anyOf": [
    {
     "type": "string"
    },
    {
     "type": "null"
    }
   ],
   "default": null,
   "title": "Barcode"
  },
  "edition": {
   "anyOf": [
    {
     "type": "string"
    },
    {
     "type": "null"
    }
   ],
   "default": null,
   "description": "free text, e.g. 'Exclusive 2004 Edition', 'reissue without indexed tracks', '2\u00d7CD'",
   "title": "Edition"
  },
  "ids": {
   "additionalProperties": {
    "type": "string"
   },
   "description": "{'musicbrainz': mbid
```
</details>

### 22. `write` +216s – completed

```
{"path": "output/work/fall-6237bde7.json", "content": "{\n  \"input\": {\"id\": \"fall-6237bde7\", \"title\": \"LIVE IN CHICAGO (2LP)\", \"artist\": \"FOREIGNER\", \"ean\": \"4029759205296\"},\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"Live In Chicago\",\n    \"artist\": \"Foreigner\",\n    \"format\": \"Vinyl\",\n    \"country\": \"Europe\",\n    \"year\": 2025,\n    \"label\": \"earMUSIC / Edel\",\n    \"catno\": \"0220529EMU\",\n    \"barcode\": \"4029759205296\",\n    \"edition\": \"2×LP (180 g), first vinyl release, single LP cover\",\n    \"ids\": {\"discogs\": \"34744227\"}\n  },\n  \"tracks\": [\n    {\"position\": \"A1\", \"disc\": 1, \"title\": \"Double Vision\", \"artist\": null, \"duration_s\": 239,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"A2\", \"disc\": 1, \"title\": \"Head Games\", \"artist\": null, \"duration_s\": 339,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"A3\", \"disc\": 1, \"title\": \"Cold As Ice\", \"artist\": null, \"duration_s\": 344,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"A4\", \"disc\": 1, \"title\": \"Waiting For A Girl Like You\", \"artist\": null, \"duration_s\": 360,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"B1\", \"disc\": 1, \"title\": \"When It Comes To Love\", \"artist\": null, \"duration_s\": 240,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"B2\", \"disc\": 1, \"title\": \"Blue Morning, Blue Day\", \"artist\": null, \"duration_s\": 222,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"B3\", \"disc\": 1, \"title\": \"Dirty White Boy\", \"artist\": null, \"duration_s\": 291,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"B4\", \"disc\": 1, \"title\": \"Starrider\", \"artist\": null, \"duration_s\": 420,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"C1\", \"disc\": 2, \"title\": \"Feels Like The First Time\", \"artist\": null, \"duration_s\": 288,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"C2\", \"disc\": 2, \"title\": \"Urgent\", \"artist\": null, \"duration_s\": 453,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"C3\", \"disc\": 2, \"title\": \"I Want To Know What Love Is\", \"artist\": null, \"duration_s\": 470,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"D1\", \"disc\": 2, \"title\": \"Hot Blooded\", \"artist\": null, \"duration_s\": 359,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]},\n    {\"position\": \"D2\", \"disc\": 2, \"title\": \"Juke Box Hero\", \"artist\": null, \"duration_s\": 671,\n     \"sources\": [\"discogs:release/34744227\", \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"discogs:release/33766896\"], \"flags\": [\"duration_other_edition\"]}\n  ],\n  \"artists\": [\n    {\"name\": \"Foreigner\", \"role\": \"main\", \"tracks\": [], \"sources\": [\"discogs:release/34744227\", \"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\"]}\n  ],\n  \"total_duration_s\": 4696,\n  \"confidence\": 0.85,\n  \"sources\": [\n    {\"id\": \"discogs:release/34744227\", \"url\": \"https://www.discogs.com/release/34744227-Foreigner-Live-In-Chicago\", \"kind\": \"database\", \"note\": \"Exact barcode 4029759205296, 2×LP, Ear Music 0220529EMU, 2025-04-11; tracklist with side positions, no durations\"},\n    {\"id\": \"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"url\": \"https://musicbrainz.org/release/13ed9b61-194b-4133-81a3-703edec19459\", \"kind\": \"database\", \"note\": \"CD edition, barcode 4029759205289, earMUSIC 0220528EMU, 13 tracks with ms durations – used for durations\"},\n    {\"id\": \"discogs:release/33766896\", \"url\": \"https://www.discogs.com/release/33766896-Foreigner-Live-In-Chicago\", \"kind\": \"database\", \"note\": \"CD edition, barcode 4029759205289, durations confirm the MusicBrainz CD timings (±1 s)\"},\n    {\"id\": \"image:https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\", \"url\": \"https://coverartarchive.org/release/13ed9b61-194b-4133-81a3-703edec19459/41880049212-1200.jpg\", \"kind\": \"image\", \"note\": \"Back cover of the 2025 programme: printed title, 13 track titles in printed capitalisation, no durations printed\"},\n    {\"id\": \"web:https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de\", \"url\": \"https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de\", \"kind\": \"shop\", \"note\": \"Shop listing for earMUSIC 0220529EMU 2LP with same 13-track programme (numbering A1–A8/B1–B5, simplified)\"},\n    {\"id\": \"web:https://www.emp.de/p/live-in-chicago/583437.html\", \"url\": \"https://www.emp.de/p/live-in-chicago/583437.html\", \"kind\": \"shop\", \"note\": \"Shop listing, 2LP, same programme, sequentially numbered, 'LP 1'\"},\n    {\"id\": \"itunes:album/1797510964\", \"url\": \"https://music.apple.com/de/album/live-in-chicago/1797510964\", \"kind\": \"streaming\", \"note\": \"Digital edition durations (hint only): identical to CD except track 1 3:49\"}\n  ],\n  \"conflicts\": [\n    {\"field\": \"positions (side split)\",\n     \"values\": {\n       \"discogs:release/34744227\": \"4 sides: A1–A4, B1–B4, C1–C3, D1–D2\",\n       \"web:https://www.decks.de/track/foreigner-live_in_chicago/co6-y1/de\": \"continuous numbering A1–A8, B1–B5\",\n       \"web:https://www.emp.de/p/live-in-chicago/583437.html\": \"continuous numbering 1–13\"\n     },\n     \"resolution\": \"Followed Discogs' four-side split, which matches a 2×LP and the side timings (~17–21 min per side); shop listings number the programme continuously and are not reliable for side positions.\"},\n    {\"field\": \"duration track 1 (Double Vision, other editions)\",\n     \"values\": {\n       \"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\": \"3:59 (238.840 s, CD)\",\n       \"discogs:release/33766896\": \"3:58 (238 s, CD)\",\n       \"itunes:album/1797510964\": \"3:49 (229.155 s, digital)\"\n     },\n     \"resolution\": \"Both CD sources agree on ~238 s for the CD edition; used 239 s for the vinyl entry. Digital edition (and MusicBrainz digital release) is ~10 s shorter on track 1 – the vinyl-specific timing is unknown, so this remains unresolved.\"}\n  ],\n  \"missing\": [\n    \"No durations are published for the 2×LP edition itself (Discogs vinyl entry has none; the vinyl is not in MusicBrainz). All durations come from the 2025 CD edition (musicbrainz:release/13ed9b61, discogs:release/33766896) and are flagged duration_other_edition.\",\n    \"Vinyl-specific timing of track A1 could not be verified: CD editions list 3:58/3:59, the digital edition 3:49.\",\n    \"No MusicBrainz entry exists for the vinyl edition (only the CD and digital editions of release group 89af84e1-6dd2-4f56-82aa-695950463e94).\"\n  ],\n  \"alternatives\": [\n    {\"description\": \"CD, earMUSIC/Edel 0220528EMU, Europe 2025-04-11, 13 tracks, barcode 4029759205289\", \"source\": \"musicbrainz:release/13ed9b61-194b-4133-81a3-703edec19459\", \"why_not\": \"CD jewel case, different barcode and catalogue number\"},\n    {\"description\": \"Digital Media, earMUSIC, 2025-04-11, 13 tracks, barcode 4029759205272\", \"source\": \"musicbrainz:release/0db824ee-9259-4c64-be7f-25130beba083\", \"why_not\": \"digital edition, no physical carrier\"},\n    {\"description\": \"CD, Ear Music 0220528EMU, Europe 2025, 13 tracks, barcode 4029759205289\", \"source\": \"discogs:release/33766896\", \"why_not\": \"CD edition, different barcode\"},\n    {\"description\": \"Blu-ray (Ear Music 0208091ERE, Europe 2012) and DVD (0208090ERE) of the same 2011 concert\", \"source\": \"discogs:release/7014376\", \"why_not\": \"other formats (video), different barcode and year\"}\n  ],\n  \"reasoning\": \"The barcode 4029759205296 resolves uniquely to the 2025 European 2×LP reissue on earMUSIC/Edel (Discogs release 34744227, catno 0220529EMU), which is the only physical carrier with this EAN; the title's '(2LP)' and the catalogue number confirm it against shop listings for 0220529EMU. The 13 titles and their order agree between the Discogs vinyl entry, the printed back cover of the same 2025 programme (CD back cover read as image) and the CD/digital editions. Because no durations exist for the vinyl, the CD edition's millisecond timings were adopted (two CD sources agree within 1 s) and each track is flagged duration_other_edition. Track 1 differs by ~10 s between CD and digital editions, which is documented as a conflict and in missing. Single-artist release: Foreigner is the only credited artist.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-6237bde7.json
```
</details>

### 23. `shell` +225s – completed

```
bin/tl-validate output/work/fall-6237bde7.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 13 tracks (13 with duration), 7 sources, 2 conflicts, confidence=0.85
```
</details>

> **Agent** +244s: FERTIG found 13 Tracks confidence=0.85
