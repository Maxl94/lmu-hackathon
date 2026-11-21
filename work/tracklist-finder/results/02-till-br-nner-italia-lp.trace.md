# Agent-Trace: 02-till-br-nner-italia-lp

> Schnellweg geprüft: no fast path: 0 matching official MusicBrainz releases (fast path only for 1–5 identical ones)
Start 2026-11-20T15:42:21 · 18 Schritte · 17 Tool-Aufrufe · Tokens in 25135 / out 11908


> **Agent** +1s: I'll start by checking the barcode and searching both databases.

### 1. `shell` +2s – completed

```
bin/tl-gtin 4029759207641; echo "---"; bin/tl-mb search --barcode 4029759207641; echo "---"; bin/tl-discogs search --barcode 4029759207641
```

<details><summary>Ausgabe</summary>

```
input: '4029759207641' → digits: 4029759207641 (13 digits)
type: EAN-13  valid: yes
search variants: 4029759207641
prefix 400–440: assigned in Germany (says nothing about the country of release)
---
0 Releases (Queries: barcode:(4029759207641))

---
2 hits (parameters: {'barcode': '4029759207641'})
discogs:release/35053985 | Till Brönner - Italia | 2025 Germany | Vinyl, LP, Album | Label Ear Music | Kat.-Nr. 0220764EMU | Barcodes 4029759207641 | master 3967694
discogs:release/35061323 | Till Brönner - Italia | 2025 Germany | Vinyl, LP, Album, Limited Edition | Label Ear Music, Till Brönner | Kat.-Nr. 0220764EMU | Barcodes 4 029759 207665, 4 029759 207641, GEMA / BIEM | master 3967694
```
</details>

### 2. `shell` +3s – completed

```
bin/tl-discogs release 35053985; echo "=========="; bin/tl-discogs release 35061323
```

<details><summary>Ausgabe</summary>

```
discogs:release/35053985 | Italia — Till Brönner | 2025-09-05 Germany | 2× Vinyl (LP, Album) | Ear Music 0220764EMU | master 3967694
url: https://www.discogs.com/release/35053985-Till-Brönner-Italia
identifiers: Barcode: 4029759207641
A1 Estate | duration missing
A2 Viva La Felicità | duration missing
A3 Amarsi Un Po‘ | duration missing
A4 Via Con Me | duration missing | credits: Featuring: Mario Biondi
B1 Il Trucido E Lo Sbirro | duration missing
B2 La Donna Invisibile | duration missing
B3 Quando, Quando, Quando | duration missing | credits: Featuring: Giovanni Zarrella
B4 Parole Parole | duration missing | credits: Featuring: Chiara Civello
C1 Cosa Vuoi | duration missing
C2 Travolti Di Un Insolito Destino Nell’ Azzurro Mare D’Agosto | duration missing
C3 In Alto Mare | duration missing | credits: Featuring: Mandy Capristo
C4  L’Unica Chance | duration missing | credits: Featuring: Sera Kalo
D1 L’Appuntamento | duration missing
D1 Arrivederci | duration missing
14 tracks, total 0:00 (0 s), without duration: 14
images: primary https://i.discogs.com/CfqyWsv1fT7pmPD1WeIkRGErG2OrKXpaxhEXEaldOl8/rs:fit/g:sm/q:90/h:589/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1MDUz/OTg1LTE3NTc0MzQ0/NTMtNTg5My5qcGVn.jpeg | secondary https://i.discogs.com/BQjJtd75_FYeHnOSekEYm1VCEGdzW_gB1od5WCyRwEY/rs:fit/g:sm/q:90/h:592/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1MDUz/OTg1LTE3NTc0MzI3/NDktMTAzMC5qcGVn.jpeg | secondary https://i.discogs.com/bbz7gb7lHKBJmJ1SNeFfmk5B2fbEhknYMHF1tbiUNUg/rs:fit/g:sm/q:90/h:588/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1MDUz/OTg1LTE3NTc0MzI3/NDktNjQ0OC5qcGVn.jpeg | secondary https://i.discogs.com/NkwCRiA6kkflO7szcQ82-C6lhFCVEl1EOuwcvMX-H8Q/rs:fit/g:sm/q:90/h:590/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1MDUz/OTg1LTE3NTc0MzI3/NTAtOTQ2MS5qcGVn.jpeg | secondary https://i.discogs.com/T4cf8pthMgHSdWBlbh2w-b6oYdubyNgp8BVAN2m1KHA/rs:fit/g:sm/q:90/h:594/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1MDUz/OTg1LTE3NTc0MzI3/NDgtNDAxMS5qcGVn.jpeg | secondary https://i.discogs.com/0gSXruZizrct_bMgCBwEWufVOxwmaTTPEmh-RXNk418/rs:fit/g:sm/q:90/h:584/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM1MDUz/OTg1LTE3NTc0MzI3/NDktNzc4NS5qcGVn.jpeg
community: have 161 want 22 data_quality Needs Vote
==========
discogs:release/35061323 | Italia — Till Brönner | 2025-09-05 Germany | 2× Vinyl (LP, Album, Limited Edition) | Ear Music 0220764EMU | master 3967694
url: https://www.discogs.com/release/35061323-Till-Brönner-Italia
identi
… [2500 Zeichen gekürzt]
```
</details>

### 3. `shell` +6s – completed

```
bin/tl-mb search --title "Italia" --artist "Till Brönner"; echo "---"; bin/tl-itunes search "Till Brönner Italia"; echo "---"; bin/tl-deezer search --artist "Till Brönner" --title "Italia"; echo "---"; bin/tl-discogs versions 3967694
```

<details><summary>Ausgabe</summary>

```
2 Releases (Queries: release:"Italia" AND artist:"Till Brönner")
musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57 | ITALIA — Till Brönner | ? ?? | Digital Media | Tracks 14 | Barcode 4029759209560 | earMUSIC | Official | score 100
musicbrainz:release/ebdff475-afa0-46b3-baa9-52f75441ef14 | Italia — Till Brönner | 2025 DE | CD | Tracks 14 | Barcode - | earMUSIC 0221179EMU | Official | score 100
---
25 Alben
itunes:album/1826050972 | ITALIA — Till Brönner | 2025-09-05 | 14 Tracks
itunes:album/1442534202 | The Movie Album — Till Brönner | 2014-01-01 | 16 Tracks
itunes:album/1588069547 | Christmas — Till Brönner | 2021-10-29 | 12 Tracks
itunes:album/1530968541 | On Vacation — Till Brönner & Bob James | 2020-10-23 | 15 Tracks
itunes:album/1444167876 | Oceana — Till Brönner | 2006-01-01 | 14 Tracks
itunes:album/1443069308 | Best Of The Verve Years — Till Brönner | 2015-11-20 | 16 Tracks
itunes:album/1114160878 | The Good Life — Till Brönner | 2016-09-02 | 15 Tracks
itunes:album/1442644845 | Till Brönner (Deluxe Edition) — Till Brönner | 2012-01-01 | 16 Tracks
itunes:album/1442523342 | Rio — Till Brönner | 2008-09-17 | 14 Tracks
itunes:album/1442523503 | Midnight — Till Brönner | 1997-05-20 | 12 Tracks
... 15 weitere ausgeblendet. narrow the filter or raise --limit.
---
1 Alben (q=artist:"Till Brönner" album:"Italia")
deezer:album/785974581 | ITALIA — Till Brönner | 14 Tracks | album
---
6 versions of master 3967694
discogs:release/36331435 | Italia | 2025 Germany | Album, Stereo | Ear Music 0221179EMU | CD
discogs:release/35053985 | Italia | 2025 Germany | LP, Album | Ear Music 0220764EMU | Vinyl
discogs:release/35058344 | Italia | 2025 Germany | Album | Ear Music 0220728EMU | CD
discogs:release/35061323 | Italia | 2025 Germany | LP, Album, Limited Edition | Ear Music 0220764EMU | Vinyl
discogs:release/35284717 | Italia | 2025 Russia | Album, Unofficial Release | Ear Music (2) 0220728EMU | CD
discogs:release/36461898 | Italia = イタリア | 2025 Japan | Album, Stereo | Ear Music MOCLD-1113 | CD
```
</details>

### 4. `shell` +8s – completed

```
bin/tl-mb release 34ce3886-6ac3-4f98-9ecb-7ff973dada57
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57 | ITALIA — Till Brönner | 2025-09-05 None | Digital Media | Tracks 14 | Barcode 4029759209560 | earMUSIC | Official
release-group: 52db2a80-553c-41f6-b561-0f866415a2b2 (Album, first date 2025-09-05) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/34ce3886-6ac3-4f98-9ecb-7ff973dada57
-- Medium 1: Digital Media, 14 Tracks
1.1 [1] Estate | 5:31 (331000 ms) | ISRC DEH842503686
1.2 [2] Viva la felicità | 3:24 (204000 ms) | ISRC DEH842503678
1.3 [3] Amarsi un po’ | 5:56 (356000 ms) | ISRC DEH842503680
1.4 [4] Via con me — Till Brönner feat. Mario Biondi | 4:11 (251000 ms) | ISRC DEH842503696
1.5 [5] Il trucido e lo sbirro | 4:46 (286000 ms) | ISRC DEH842503688
1.6 [6] La donna invisibile | 3:46 (226000 ms) | ISRC DEH842503692
1.7 [7] Quando quando quando — Till Brönner feat. Giovanni Zarrella | 4:32 (272000 ms) | ISRC DEH842503695
1.8 [8] Parole parole — Till Brönner feat. Chiara Civello | 4:21 (261000 ms) | ISRC DEH842503694
1.9 [9] Cosa vuoi | 3:30 (210000 ms) | ISRC DEH842503679
1.10 [10] Travolti da un insolito destino nell’ azzurro mare d’agosto | 4:44 (284000 ms) | ISRC DEH842503693
1.11 [11] In alto mare — Till Brönner feat. Mandy Capristo | 3:03 (183000 ms) | ISRC DEH842503689
1.12 [12] L’unica chance — Till Brönner feat. Sera Kalo | 5:43 (343000 ms) | ISRC DEH842503691
1.13 [13] L’appuntamento | 5:44 (344000 ms) | ISRC DEH842503690
1.14 [14] Arrivederci | 5:32 (332000 ms) | ISRC DEH842503685
Total: 1:04:43 (3883 s), tracks without duration: 0
```
</details>

### 5. `shell` +10s – completed

```
bin/tl-itunes upc 4029759207641; echo "---"; bin/tl-itunes upc 4029759209560; echo "--- deezer"; bin/tl-deezer upc 4029759209560; echo "---"; bin/tl-deezer upc 4029759207641
```

<details><summary>Ausgabe</summary>

```
no hit (physical releases are often missing from the digital catalogue)
---
(Store de)
itunes:album/1826050972 | ITALIA — Till Brönner | 2025-09-05 | 14 Tracks | ℗ 2025 Till Brönner under exclusive license to earMUSIC, a label of Edel Music & Entertainment GmbH.
url: https://music.apple.com/de/album/italia/1826050972?uo=4
1.1 Estate | 5:31 (330526 ms)
1.2 Viva La Felicità | 3:24 (203577 ms)
1.3 Amarsi Un Po' | 5:56 (355832 ms)
1.4 Via Con Me — Till Brönner & Mario Biondi | 4:11 (251351 ms)
1.5 Il Trucido E Lo Sbirro | 4:46 (286321 ms)
1.6 La Donna Invisibile | 3:46 (226289 ms)
1.7 Quando Quando Quando | 4:32 (271966 ms)
1.8 Parole Parole (feat. Chiara Civello) | 4:21 (261424 ms)
1.9 Cosa Vuoi | 3:30 (210257 ms)
1.10 Travolti Da Un Insolito Destino Nell' Azzurro Mare d'Agosto (Soundtrack) | 4:44 (283704 ms)
1.11 In Alto Mare (feat. Mandy Capristo) | 3:03 (183286 ms)
1.12 L'unica Chance | 5:43 (342535 ms)
1.13 L'appuntamento | 5:44 (344107 ms)
1.14 Arrivederci | 5:32 (331754 ms)
Total 1:04:43 (3882 s)
--- deezer
deezer:album/785974581 | ITALIA — Till Brönner | 2025-09-05 | UPC 4029759209560 | 14 Tracks | Label earMUSIC
url: https://www.deezer.com/album/785974581
1.1 Estate | 5:30
1.2 Viva La Felicità | 3:23
1.3 Amarsi Un Po' | 5:55
1.4 Via Con Me | 4:11
1.5 Il Trucido E Lo Sbirro | 4:46
1.6 La Donna Invisibile | 3:46
1.7 Quando Quando Quando | 4:31
1.8 Parole Parole | 4:21
1.9 Cosa Vuoi | 3:30
1.10 Travolti Da Un Insolito Destino Nell' Azzurro Mare d'Agosto (Soundtrack) | 4:43
1.11 In Alto Mare | 3:03
1.12 L'unica Chance | 5:42
1.13 L'appuntamento | 5:44
1.14 Arrivederci | 5:31
Total 1:04:36 (3876 s)
---
no hit (Deezer mostly knows digital UPCs only)
```
</details>

### 6. `shell` +35s – completed

```
cd /tmp/opencode && curl -sL -o d1_2.jpg "https://i.discogs.com/bbz7gb7lHKBJmJ1SNeFfmk5B2fbEhknYMHF1tbiUNUg/rs:fit/g:sm/q:90/h:588/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM1MDUzOTg1LTE3NTc0MzI3/NDktNjQ0OC5qcGVn.jpeg" && curl -sL -o d1_5.jpg "https://i.discogs.com/0gSXruZizrct_bMgCBwEWufVOxwmaTTPEmh-RXNk418/rs:fit/g:sm/q:90/h:584/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM1MDUzOTg1LTE3NTc0MzI3/NDktNzc4NS5qcGVn.jpeg" && ls -la d1_*.jpg && file d1_*.jpg
```

<details><summary>Ausgabe</summary>

```
-rw-r--r--. 1 user user 11258 20. Nov 15:42 d1_2.jpg
-rw-r--r--. 1 user user 11258 20. Nov 15:42 d1_5.jpg
d1_2.jpg: HTML document, ASCII text, with very long lines (6440)
d1_5.jpg: HTML document, ASCII text, with very long lines (6440)
```
</details>

### 7. `shell` +50s – completed

```
cd /tmp/opencode && curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36" -o d1_2.jpg "https://i.discogs.com/bbz7gb7lHKBJmJ1SNeFfmk5B2fbEhknYMHF1tbiUNUg/rs:fit/g:sm/q:90/h:588/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM1MDUzOTg1LTE3NTc0MzI3/NDktNjQ0OC5qcGVn.jpeg"; file d1_2.jpg; head -c 300 d1_2.jpg
```

<details><summary>Ausgabe</summary>

```
d1_2.jpg: HTML document, ASCII text, with very long lines (6440)
<!DOCTYPE html>
<html lang="en-US">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>403 Forbidden | Discogs</title>
  <meta name="description"
    content="Discogs is a free online database and marketplace of music releases connecting
```
</details>

### 8. `shell` +64s – completed

```
bin/tl-mb release ebdff475-afa0-46b3-baa9-52f75441ef14; echo "---"; bin/tl-search "Till Brönner Italia 2LP 0220764EMU Tracklist" --site ear-music.net 2>/dev/null | head -20; echo "---jpc"; bin/tl-search "Till Brönner Italia Vinyl 0220764EMU" 2>/dev/null | head -20
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/ebdff475-afa0-46b3-baa9-52f75441ef14 | Italia — Till Brönner | 2025 DE | CD | Tracks 14 | Barcode - | earMUSIC 0221179EMU | Official
release-group: 52db2a80-553c-41f6-b561-0f866415a2b2 (Album, first date 2025-09-05) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/ebdff475-afa0-46b3-baa9-52f75441ef14
-- Medium 1: CD, 14 Tracks
1.1 [1] Estate | 5:31 (331000 ms) | ISRC DEH842503686
1.2 [2] Viva la felicità | 3:24 (204000 ms) | ISRC DEH842503678
1.3 [3] Amarsi un po’ | 5:56 (356000 ms) | ISRC DEH842503680
1.4 [4] Via con me — Till Brönner feat. Mario Biondi | 4:11 (251000 ms) | ISRC DEH842503696
1.5 [5] Il trucido e lo sbirro | 4:46 (286000 ms) | ISRC DEH842503688
1.6 [6] La donna invisibile | 3:46 (226000 ms) | ISRC DEH842503692
1.7 [7] Quando quando quando — Till Brönner feat. Giovanni Zarrella | 4:32 (272000 ms) | ISRC DEH842503695
1.8 [8] Parole parole — Till Brönner feat. Chiara Civello | 4:21 (261000 ms) | ISRC DEH842503694
1.9 [9] Cosa vuoi | 3:30 (210000 ms) | ISRC DEH842503679
1.10 [10] Travolti da un insolito destino nell’ azzurro mare d’agosto | 4:44 (284000 ms) | ISRC DEH842503693
1.11 [11] In alto mare — Till Brönner feat. Mandy Capristo | 3:03 (183000 ms) | ISRC DEH842503689
1.12 [12] L’unica chance — Till Brönner feat. Sera Kalo | 5:43 (343000 ms) | ISRC DEH842503691
1.13 [13] L’appuntamento | 5:44 (344000 ms) | ISRC DEH842503690
1.14 [14] Arrivederci | 5:29 (329000 ms) | ISRC DEH842503685
Total: 1:04:40 (3880 s), tracks without duration: 0
---
10 hits for: Till Brönner Italia 2LP 0220764EMU Tracklist site:ear-music.net
1. earMUSIC - news, artists & new releases Foreigner - earMUSIC
   https://www.ear-music.net/foreigner-orchestral/
   ORDER HERE VIDEO By loading the ... THEIR HITS IN A BOMBASTIC ORCHESTRAL SOUND I Want To Know What Love Is, Cold As Ice, Waiting For A Girl Like You, Hot Blooded, Juke Box Hero....
   + ORDER HERE VIDEO By loading the video, you agree to YouTube's privacy policy.Learn more Load video Always unblock YouTub
2. earMUSIC - news, artists & new releases Contact - earMUSIC
   https://ear-music.net/contact
   CUSTOMER SUPPORT / PROBLEMS · In case you have a problem with one of our products, please contact the retailer you ordered from / purchased at
3. earMUSIC - news, artists & new releases | SAGA REISSUE SERIES "STEEL UMBRELLAS" - OUT NOVEMBER 13TH 2015
   https://www.ear-music.net/news/2017/saga-reissue-series-steel-umbrellas-out-november-13th-2015
   This website uses c
… [3498 Zeichen gekürzt]
```
</details>

### 9. `shell` +68s – completed

```
bin/tl-scrape "https://www.decks.de/track/till_brnner-italia/cp2-zs/de" --grep -i "a1|a2|b1|b2|c1|d1|estate|arrivederci|tracklist|seite|side" 2>/dev/null | head -60
```

<details><summary>Ausgabe</summary>

```
(no output)
```
</details>

### 10. `shell` +73s – completed

```
bin/tl-scrape "https://www.decks.de/track/till_brnner-italia/cp2-zs/de" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://www.decks.de/track/till_brnner-italia/cp2-zs/de
mode: http (http)
title: Till Brönner - ITALIA / earMUSIC / 0220764EMU | 2LP Vinyl kaufen | decks.de
source-id: web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de
---
Till Brönner - ITALIA / earMUSIC / 0220764EMU | 2LP Vinyl kaufen | decks.de
Jazz
GTIN13:
4029759207641
Code:
cp2-zs
Release:
17.02.2026
back in Stock:
 25.02.2026
Till Brönner
ITALIA 
(LP) (2LP)
earMUSIC / 0220764EMU
2LP 
Side
BPM
Tracklist
88
Estate
80
Viva La Felicità
96
Amarsi Un Po 
145
Via Con Me
183
Il Trucido E Lo Sbirro
80
La Donna Invisibile
123
Quando Quando Quando
151
Parole Parole
100
Cosa Vuoi
82
Travolti Da Un Insolito Destino Nell Azzurro Mare D agosto
107
In Alto Mare
103
L unica Chance
164
L appuntamento
128
Arrividerci
Till Brönner
Kunden kauften auch:
Mehr Releases vom Artist: 
Sicherheits- und Herstellerinformationen
Edel Music & Entertainment GmbH
Neumühlen 17
22763 Hamburg
DE
https://www.edel.com
```
</details>

### 11. `shell` +80s – completed

```
bin/tl-vision "https://i.discogs.com/bbz7gb7lHKBJmJ1SNeFfmk5B2fbEhknYMHF1tbiUNUg/rs:fit/g:sm/q:90/h:588/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM1MDUzOTg1LTE3NTc0MzI3/NDktNjQ0OC5qcGVn.jpeg" --context "Discogs back cover image of Till Brönner ITALIA 2LP, need printed tracklist with side positions A1..D2 and durations" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/bbz7gb7lHKBJmJ1SNeFfmk5B2fbEhknYMHF1tbiUNUg/rs:fit/g:sm/q:90/h:588/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM1MDUzOTg1LTE3NTc0MzI3/NDktNjQ0OC5qcGVn.jpeg
```
</details>

### 12. `shell` +83s – completed

```
bin/tl-search "musik-sammler Till Brönner Italia 2LP 2025" 2>/dev/null | head -10
```

<details><summary>Ausgabe</summary>

```
10 hits for: musik-sammler Till Brönner Italia 2LP 2025
1. Till Brönner: Italia (180g) (2 LPs) – jpc.de
   https://www.jpc.de/jpcng/jazz/detail/-/art/till-broenner-italia/hnum/12365772
   ... Vinyl liefern wir innerhalb Deutschlands immer portofrei. ... Mit seinem 2025 erscheinenden Album »Italia« taucht Till Brönner tief in den sonnendurchfluteten Sound Italiens der 60er bis 80er Jahre ein.
   + Till Brönner (geb. 1971) ... Die gute alte Vinyl - Langspielplatte. ... Vinyl liefern wir innerhalb Deutschlands immer p | »Das Album enthält viele bekannte Hits – zumindest aus deutscher Perspektive. Aber es gibt eben auch Überraschungen«, so
2. Till Brönner: Italia (CD) – jpc.de
   https://www.jpc.de/jpcng/jazz/detail/-/art/till-broenner-italia/hnum/12365776
   Herkömmliche CD, die mit allen ... abspielbar ist. ... Mit seinem 2025 erscheinenden Album »Italia« taucht Till Brönner tief in den sonnendurchfluteten Sound Italiens der 60er bis 80er Jahre ein....
   + Till Brönner (geb. 1971) ... Herkömmliche CD, die mit allen CD-Playern und Computerlaufwerken, aber auch mit den meisten | »Das Album enthält viele bekannte Hits – zumindest aus deutscher Perspektive. Aber es gibt eben auch Überraschungen«, so
3. Till Brönner · Italia (LP) (2025)
```
</details>

### 13. `shell` +92s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/jazz/detail/-/art/till-broenner-italia/hnum/12365772" --grep -i "estate|felic|amarsi|via con|trucido|donna|quando|parole|cosa|travolti|alto mare|chance|appuntamento|arrivederci|Seite|Disc 1" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 14. `shell` +95s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/jazz/detail/-/art/till-broenner-italia/hnum/12365772" --grep="estate|felic|amarsi|trucido|donna|quando|parole|cosa|travolti|alto mare|chance|appuntamento|arrivederci|Seite" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://www.jpc.de/jpcng/jazz/detail/-/art/till-broenner-italia/hnum/12365772
mode: http (http)
title: Till Brönner: Italia (180g) (2 LPs) –
source-id: web:https://www.jpc.de/jpcng/jazz/detail/-/art/till-broenner-italia/hnum/12365772
---
…
 War hilfreich
(7)
Nächste Seite
Bitte beachten Sie
 Wir können nicht sicherstellen, dass die Angaben von Verbrauchern stammen, die das Produkt tatsächlich genutzt oder erworben haben.
```
</details>

### 15. `shell` +101s – completed

```
bin/tl-scrape "https://imusic.de/music/4029759207641/till-bronner-2025-italia-lp" --grep="Estate|Seite|A1|B1|Arrivederci|Spieldauer" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://imusic.de/music/4029759207641/till-bronner-2025-italia-lp
mode: firecrawl (http → firecrawl)
title: Till Brönner · Italia (LP) (2025)
source-id: web:https://imusic.de/music/4029759207641/till-bronner-2025-italia-lp
---
…
1. **1.**
    LP
1. Estate
2. Viva La Felicita
3. Amarsi Un Po'
…
4. L'unica Chance
5. L'appuntamento
6. Arrivederci

* * *
…
## Wir verwenden Cookies!

Diese Webseite verwendet essentielle Cookies, um sicherzustellen, dass die Webseite korrekt funktioniert und Trackingcookies, damit wir verstehen, wie Du mit unserer Seite interagierst. Letztere werden nur mit Deiner Zustimmung aktiviert. Wir verwenden Cookies auch, um auf Sie zugeschnittene Anzeigen individuell anzupassen. [Cookies einstellen](https://imusic.de/music/4029759207641/till-bronner-2025-italia-lp#)

Alle akzeptierenAlle ablehnen
```
</details>

### 16. `shell` +115s – completed

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

### 17. `shell` +145s – completed

```
mkdir -p output/work && cat > output/work/fall-c91d3538.json <<'EOF'
{
  "input": {"id": "fall-c91d3538", "title": "ITALIA (LP)", "artist": "TILL BRÖNNER", "ean": "4029759207641"},
  "status": "found",
  "release": {
    "title": "ITALIA",
    "artist": "Till Brönner",
    "format": "Vinyl",
    "country": "DE",
    "year": 2025,
    "label": "Ear Music",
    "catno": "0220764EMU",
    "barcode": "4029759207641",
    "edition": "2×12\" LP, gatefold sleeve with printed inner sleeves, 14 tracks",
    "ids": {"discogs": "35053985"}
  },
  "tracks": [
    {"position": "A1", "disc": 1, "title": "Estate", "artist": null, "duration_s": 331,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "A2", "disc": 1, "title": "Viva la felicità", "artist": null, "duration_s": 204,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "A3", "disc": 1, "title": "Amarsi un po’", "artist": null, "duration_s": 356,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "A4", "disc": 1, "title": "Via con me", "artist": "Till Brönner feat. Mario Biondi", "duration_s": 251,
     "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "B1", "disc": 1, "title": "Il trucido e lo sbirro", "artist": null, "duration_s": 286,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "B2", "disc": 1, "title": "La donna invisibile", "artist": null, "duration_s": 226,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "B3", "disc": 1, "title": "Quando quando quando", "artist": "Till Brönner feat. Giovanni Zarrella", "duration_s": 272,
     "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "B4", "disc": 1, "title": "Parole parole", "artist": "Till Brönner feat. Chiara Civello", "duration_s": 261,
     "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "C1", "disc": 1, "title": "Cosa vuoi", "artist": null, "duration_s": 210,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "C2", "disc": 1, "title": "Travolti da un insolito destino nell’ azzurro mare d’agosto", "artist": null, "duration_s": 284,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "C3", "disc": 1, "title": "In alto mare", "artist": "Till Brönner feat. Mandy Capristo", "duration_s": 183,
     "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "C4", "disc": 1, "title": "L’unica chance", "artist": "Till Brönner feat. Sera Kalo", "duration_s": 343,
     "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "D1", "disc": 1, "title": "L’appuntamento", "artist": null, "duration_s": 344,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition"]},
    {"position": "D2", "disc": 1, "title": "Arrivederci", "artist": null, "duration_s": 332,
     "sources": ["discogs:release/35053985", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de"],
     "duration_sources": ["musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "itunes:album/1826050972"],
     "flags": ["duration_other_edition", "duration_conflict"]}
  ],
  "artists": [
    {"name": "Till Brönner", "role": "main", "tracks": [], "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"]},
    {"name": "Mario Biondi", "role": "featured", "tracks": ["A4"], "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"]},
    {"name": "Giovanni Zarrella", "role": "featured", "tracks": ["B3"], "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"]},
    {"name": "Chiara Civello", "role": "featured", "tracks": ["B4"], "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"]},
    {"name": "Mandy Capristo", "role": "featured", "tracks": ["C3"], "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"]},
    {"name": "Sera Kalo", "role": "featured", "tracks": ["C4"], "sources": ["discogs:release/35053985", "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57"]}
  ],
  "total_duration_s": 3883,
  "confidence": 0.85,
  "sources": [
    {"id": "discogs:release/35053985", "url": "https://www.discogs.com/release/35053985", "kind": "database", "note": "barcode 4029759207641 exact match; 2×Vinyl LP, Ear Music 0220764EMU, 2025-09-05"},
    {"id": "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de", "url": "https://www.decks.de/track/till_brnner-italia/cp2-zs/de", "kind": "shop", "note": "shop listing with GTIN13 4029759207641, 2LP, same 14-track order"},
    {"id": "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "url": "https://musicbrainz.org/release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "kind": "streaming", "note": "Digital Media edition (barcode 4029759209560), 14 tracks with ms durations and ISRCs - used for titles/durations"},
    {"id": "itunes:album/1826050972", "url": "https://music.apple.com/de/album/italia/1826050972", "kind": "streaming", "note": "digital album, 14 tracks, durations cross-check"},
    {"id": "deezer:album/785974581", "url": "https://www.deezer.com/album/785974581", "kind": "streaming", "note": "UPC 4029759209560, 14 tracks, durations truncated to seconds - consistent"},
    {"id": "web:https://imusic.de/music/4029759207641/till-bronner-2025-italia-lp", "url": "https://imusic.de/music/4029759207641/till-bronner-2025-italia-lp", "kind": "shop", "note": "barcode 4029759207641, 2 units (2LP), same track order"}
  ],
  "conflicts": [
    {"field": "title track A2", "values": {"musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57": "Viva la felicità", "discogs:release/35053985": "Viva La Felicità", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de": "Viva La Felicità"}, "resolution": "No readable back cover; MusicBrainz spelling used per source priority (MB before Discogs), carrier print likely title-case"},
    {"field": "title track A3", "values": {"musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57": "Amarsi un po’", "discogs:release/35053985": "Amarsi Un Po‘", "itunes:album/1826050972": "Amarsi Un Po'"}, "resolution": "MusicBrainz spelling used; Discogs uses a wrong opening apostrophe"},
    {"field": "title track B3", "values": {"musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57": "Quando quando quando", "discogs:release/35053985": "Quando, Quando, Quando"}, "resolution": "MusicBrainz spelling used (MB before Discogs)"},
    {"field": "title track C2", "values": {"musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57": "Travolti da un insolito destino nell’ azzurro mare d’agosto", "discogs:release/35053985": "Travolti Di Un Insolito Destino Nell’ Azzurro Mare D’Agosto", "itunes:album/1826050972": "Travolti Da Un Insolito Destino Nell' Azzurro Mare d'Agosto (Soundtrack)"}, "resolution": "MusicBrainz spelling used; 'da un' (not 'Di Un') is the correct Italian title; iTunes adds '(Soundtrack)' which is no part of the printed title"},
    {"field": "duration track D2", "values": {"musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57": "5:32", "itunes:album/1826050972": "5:31.754", "musicbrainz:release/ebdff475-afa0-46b3-baa9-52f75441ef14": "5:29"}, "resolution": "5:32 taken (digital MB + iTunes agree within 1 s); the MB CD edition's 5:29 deviates by 3 s and is treated as an outlier"},
    {"field": "edition", "values": {"discogs:release/35053985": "2×Vinyl, LP, Album", "discogs:release/35061323": "2×Vinyl, LP, Album, Limited Edition (stickered barcode 4029759207665)"}, "resolution": "Both vinyl pressings print the same barcode 4029759207641 and have the identical tracklist; the standard pressing is chosen because the input barcode is the printed one and the limited edition carries an additional stickered barcode"},
    {"field": "positions", "values": {"discogs:release/35053985": "D1 L’Appuntamento and D1 Arrivederci (both D1)", "web:https://www.decks.de/track/till_brnner-italia/cp2-zs/de": "no side letters, 14 tracks in line"}, "resolution": "12 tracks are given as A1–C4, so the last two must be D1 and D2; D2 set for track 14"}
  ],
  "missing": [
    "No barcode hit in MusicBrainz for the physical release (only the Digital Media edition exists there)",
    "The 2LP edition carries no printed durations in any database; all durations come from the digital/CD edition of the same album (flagged duration_other_edition) - vinyl-specific times not verified",
    "No readable back cover of the vinyl (Discogs images return HTTP 403), so the printed spelling and the D-side numbering could not be verified visually"
  ],
  "alternatives": [
    {"description": "2×Vinyl LP, Limited Edition (red vinyl, gatefold), Ear Music 0220764EMU, DE 2025, 14 tracks", "source": "discogs:release/35061323", "why_not": "same printed barcode 4029759207641 but additionally stickered barcode 4029759207665; identical tracklist, input gives no indication of the limited/coloured pressing"},
    {"description": "CD, Ear Music 0221179EMU, DE 2025, 14 tracks", "source": "musicbrainz:release/ebdff475-afa0-46b3-baa9-52f75441ef14", "why_not": "CD, not the LP requested in the input"},
    {"description": "Digital Media (UPC 4029759209560), earMUSIC 2025, 14 tracks", "source": "musicbrainz:release/34ce3886-6ac3-4f98-9ecb-7ff973dada57", "why_not": "digital edition, used only for titles and durations"}
  ],
  "reasoning": "The EAN is valid and matches exactly two Discogs vinyl releases of Till Brönner's 2025 album ITALIA (catno 0220764EMU, 2×12\"); the standard pressing is chosen since the limited edition carries an extra stickered barcode. The same GTIN and the same 14-track order are confirmed by the decks.de and imusic.de listings. MusicBrainz has no physical release for this barcode, but the digital edition (same album, same 14 tracks and order) and iTunes/Deezer provide titles, ISRCs and durations, which agree within 1 s (Deezer truncates to seconds); these are flagged duration_other_edition because they are not vinyl-specific. Featured artists (Mario Biondi, Giovanni Zarrella, Chiara Civello, Mandy Capristo, Sera Kalo) agree between Discogs and MusicBrainz."
}
EOF
bin/tl-validate output/work/fall-c91d3538.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 14 tracks (14 with duration), 6 sources, 7 conflicts, confidence=0.85
```
</details>

> **Agent** +155s: FERTIG found 14 Tracks confidence=0.85
