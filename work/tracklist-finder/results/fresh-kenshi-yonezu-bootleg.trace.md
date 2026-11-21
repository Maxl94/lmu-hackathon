# Agent-Trace: fresh-kenshi-yonezu-bootleg

> Schnellweg geprüft: no fast path: no EAN
Start 2026-11-20T16:51:07 · 11 Schritte · 14 Tool-Aufrufe · Tokens in 58670 / out 9076


> **Agent** +1s: I'll start by researching this release.

### 1. `shell` +2s – completed

```
bin/tl-mb search --title "BOOTLEG" --artist "Yonezu"
```

<details><summary>Ausgabe</summary>

```
1 Releases (Queries: release:"BOOTLEG" AND artist:"Yonezu")
musicbrainz:release/2f923832-09d2-4ae9-b1f3-2680ef5a01de | BOOTLEG — Kenshi Yonezu | 2017-11-03 XW | Digital Media | Tracks 14 | Barcode 886446811420 | Sony Music Labels Inc. | Official | score 100
```
</details>

### 2. `shell` +25s – completed

```
bin/tl-mb search --title "BOOTLEG" --artist "Kenshi Yonezu" --format CD; echo "---DISCOGS---"; bin/tl-discogs search --title "BOOTLEG" --artist "Kenshi Yonezu" --format CD
```

<details><summary>Ausgabe</summary>

```
1 Releases (Queries: release:"BOOTLEG" AND artist:"Kenshi Yonezu")
musicbrainz:release/2f923832-09d2-4ae9-b1f3-2680ef5a01de | BOOTLEG — Kenshi Yonezu | 2017-11-03 XW | Digital Media | Tracks 14 | Barcode 886446811420 | Sony Music Labels Inc. | Official | score 100
---DISCOGS---
5 hits (parameters: {'release_title': 'BOOTLEG', 'artist': 'Kenshi Yonezu', 'format': 'CD'})
discogs:release/12531413 | Kenshi Yonezu = 米津玄師* - Bootleg | 2017 Japan | CD, Album | Label Reissue Records, ABS Recording | Kat.-Nr. SRCL 9571 | Barcodes 4547366329698, JASRAC | master 1419381
discogs:release/11114145 | Kenshi Yonezu = 米津玄師* - Bootleg | 2017 Japan | CD, Album, Stereo, DVD, DVD-Video, NTSC, Stereo, All Media, Limited Edition | Label Reissue Records, ABS Recording | Kat.-Nr. SRCL 9569~70 | Barcodes 4547366329681, JASRAC | master 1419381
discogs:release/27971019 | Kenshi Yonezu = 米津玄師* - Bootleg | 2017 Japan | CD, Album, Limited Edition | Label Reissue Records, ABS Recording | Kat.-Nr. SRCL 9567~8 | Barcodes 4547366329674, JASRAC | master 1419381
discogs:release/12491102 | Kenshi Yonezu = 米津玄師* - Bootleg | 2017 Taiwan | CD, Album, DVD, DVD-Video | Label Sony Music Labels, Sony Music | Kat.-Nr. 19075802642 | Barcodes 190758026428 | master 1419381
discogs:release/36987714 | Kenshi Yonezu = 米津玄师* - Bootleg = 私藏 | 2019 China | CD, Album, Stereo | Label Starsing Records, Sony Music | Kat.-Nr. 19075893942 | Barcodes 9787798420036, 9 787798 420036 > | master 1419381
```
</details>

### 3. `shell` +27s – completed

```
bin/tl-mb release 2f923832-09d2-4ae9-b1f3-2680ef5a01de
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/2f923832-09d2-4ae9-b1f3-2680ef5a01de | BOOTLEG — Kenshi Yonezu | 2017-11-03 XW | Digital Media | Tracks 14 | Barcode 886446811420 | Sony Music Labels Inc. | Official
release-group: c7ff52d0-1aad-435b-95cd-18988f705e87 (Album, first date 2017-11-01) | Cover: front=True back=False images=2
url: https://musicbrainz.org/release/2f923832-09d2-4ae9-b1f3-2680ef5a01de
-- Medium 1: Digital Media, 14 Tracks
1.1 [1] Hien | 4:03 (243000 ms) | ISRC JPU901702915
1.2 [2] LOSER | 4:03 (243000 ms) | ISRC JPU901602597
1.3 [3] Peace Sign | 3:58 (238000 ms) | ISRC JPU901701672
1.4 [4] Sunanowakusei (+ Hatsune Miku) — Kenshi Yonezu + Miku Hatsune | 4:00 (240000 ms) | ISRC JPU901702916
1.5 [5] Orion | 4:41 (281000 ms) | ISRC JPU901700003
1.6 [6] Kaijyuunomarch | 4:55 (295000 ms) | ISRC JPU901702917
1.7 [7] Moonlight | 3:44 (224000 ms) | ISRC JPU901702918
1.8 [8] Shunrai | 4:48 (288000 ms) | ISRC JPU901702919
1.9 [9] fogbound (+ Elaiza Ikeda) — Kenshi Yonezu + Elaiza Ikeda | 4:15 (255200 ms) | ISRC JPU901702920
1.10 [10] Number Nine | 4:21 (261000 ms) | ISRC JPU901602598
1.11 [11] Alice | 3:09 (189000 ms) | ISRC JPU901702921
1.12 [12] Nighthawks | 4:20 (260413 ms) | ISRC JPU901702922
1.13 [13] Uchiagehanabi | 4:19 (259000 ms) | ISRC JPU901702923
1.14 [14] Haiirotoao ( + Masaki Suda ) — Kenshi Yonezu + Masaki Suda | 5:32 (332000 ms) | ISRC JPU901702924
Total: 1:00:09 (3608 s), tracks without duration: 0
```
</details>

### 4. `shell` +27s – completed

```
bin/tl-discogs release 12531413
```

<details><summary>Ausgabe</summary>

```
discogs:release/12531413 | Bootleg — Kenshi Yonezu, Kenshi Yonezu | 2017-11-01 Japan | 1× CD (Album) | Reissue Records SRCL 9571 | master 1419381
url: https://www.discogs.com/release/12531413-Kenshi-Yonezu-米津玄師-Bootleg
identifiers: Barcode: 4547366329698 | Rights Society: JASRAC
1 飛燕 | 4:03 (243 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
2 Loser | 4:03 (243 s) | credits: Vocals, Guitar: Kenshi Yonezu
3 ピースサイン | 3:58 (238 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
4 砂の惑星 (+ 初音ミク) | 4:00 (240 s) | credits: Vocals: Kenshi Yonezu; Vocals: Miku Hatsune
5 Orion | 4:41 (281 s) | credits: Vocals, Guitar: Kenshi Yonezu
6 かいじゅうのマーチ | 4:55 (295 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
7 Moonlight | 3:44 (224 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
8 春雷 | 4:48 (288 s) | credits: Producer, Arranged By, Vocals, Guitar: Kenshi Yonezu
9 Fogbound (+ 池田エライザ) | 4:15 (255 s) | credits: Vocals: Elaiza Ikeda; Vocals: Kenshi Yonezu
10 ナンバーナイン | 4:22 (262 s) | credits: Vocals: Kenshi Yonezu
11 爱丽丝 | 3:09 (189 s) | credits: Vocals: Kenshi Yonezu
12 Nighthawks | 4:20 (260 s) | credits: Producer, Arranged By, Vocals, Guitar: Kenshi Yonezu
13 打上花火 | 4:19 (259 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
14 灰色と青 (+ 菅田将暉) | 5:32 (332 s) | credits: Vocals: Kenshi Yonezu; Vocals: Masaki Suda
14 tracks, total 60:09 (3609 s), without duration: 0
images: primary https://i.discogs.com/CE8A9IdXLgOcoVXLTPo3npG3kN-wsiXXnz6mY8sKkwc/rs:fit/g:sm/q:90/h:525/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTEyNTMx/NDEzLTE3MzkyMDMz/NzEtNTg2MS5qcGVn.jpeg | secondary https://i.discogs.com/gquy7dqPNbO2Y7Qza9qfpPctleOrlbnCAfLx92XUAO8/rs:fit/g:sm/q:90/h:523/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTEyNTMx/NDEzLTE3MzkyMDMz/NzAtNzk2Ny5qcGVn.jpeg | secondary https://i.discogs.com/VjVFQ9Uw5_e6VJGiTGlJWcwY0Z_0stSZUMr41tP8GFU/rs:fit/g:sm/q:90/h:595/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTEyNTMx/NDEzLTE3MjkwOTcw/ODYtOTYzOC5qcGVn.jpeg | secondary https://i.discogs.com/IDY__yKFEYL-PpJCqY-qXgHRkrWhnupOgyxkptfMRQo/rs:fit/g:sm/q:90/h:468/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTEyNTMx/NDEzLTE3MjkwOTcw/ODUtODk0Ny5qcGVn.jpeg | secondary https://i.discogs.com/ijFbCvOew6Pt6RPpSpEzQ1ztZXTF7Ge0IwRfObloKPg/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTEyNTMx/NDEzLTE3MjkwOTcw/ODUtNzcxOS5qcGVn.jpeg | secondary https://i.discogs.com/eCH8ieFs1w0S9zN66eq-8CCM2c6kz-1OC7muA2hzmv0/rs:fit/g:sm/q:90
… [154 Zeichen gekürzt]
```
</details>

### 5. `shell` +34s – completed

```
bin/tl-mb group c7ff52d0-1aad-435b-95cd-18988f705e87 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
4 Releases in release-group c7ff52d0-1aad-435b-95cd-18988f705e87
musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1 | BOOTLEG —  | 2017-11-01 JP | CD | Tracks 14 | Barcode 4547366329698 | Sony Music Records SRCL-9571 | Official | 通常盤
musicbrainz:release/2f923832-09d2-4ae9-b1f3-2680ef5a01de | BOOTLEG —  | 2017-11-03 XW | Digital Media | Tracks 14 | Barcode 886446811420 | Sony Music Labels Inc. | Official
musicbrainz:release/3e907a33-bd52-40f7-b09a-ab6e4405ab05 | BOOTLEG —  | 2017-11-01 JP | Digital Media | Tracks 14 | Barcode 4547366335286 | Sony Music Records SRCL09571B00Z | Official
musicbrainz:release/8a2bb5cf-fd97-470a-abad-0e10666aeeec | BOOTLEG —  | 2020-08-05 XW | Digital Media | Tracks 14 | Barcode 4547366467222 | Sony Music Records SEXX02044B00Z | Official | 24bit/96kHz
```
</details>

### 6. `shell` +35s – completed

```
bin/tl-discogs release 27971019 | head -30; echo "===="; bin/tl-discogs release 11114145 | head -20
```

<details><summary>Ausgabe</summary>

```
discogs:release/27971019 | Bootleg — Kenshi Yonezu, Kenshi Yonezu | 2017-11-01 Japan | 1× CD (Album, Limited Edition) | Reissue Records SRCL 9567~8 | master 1419381
url: https://www.discogs.com/release/27971019-Kenshi-Yonezu-米津玄師-Bootleg
identifiers: Barcode: 4547366329674 | Rights Society: JASRAC
notes: CD+12" sleeve, poster, dummy record, PlayPASS, and 6 different cover art prints.
1 飛燕 | 4:03 (243 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
2 Loser | 4:03 (243 s) | credits: Vocals, Guitar: Kenshi Yonezu
3 ピースサイン | 3:58 (238 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
4 砂の惑星 (+ 初音ミク) | 4:00 (240 s) | credits: Vocals: Kenshi Yonezu; Vocals: Miku Hatsune
5 Orion | 4:41 (281 s) | credits: Vocals, Guitar: Kenshi Yonezu
6 かいじゅうのマーチ | 4:55 (295 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
7 Moonlight | 3:44 (224 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
8 春雷 | 4:48 (288 s) | credits: Producer, Arranged By, Vocals, Guitar: Kenshi Yonezu
9 Fogbound (+ 池田エライザ) | 4:15 (255 s) | credits: Vocals: Elaiza Ikeda; Vocals: Kenshi Yonezu
10 ナンバーナイン | 4:22 (262 s) | credits: Vocals: Kenshi Yonezu
11 爱丽丝 | 3:09 (189 s) | credits: Vocals: Kenshi Yonezu
12 Nighthawks | 4:20 (260 s) | credits: Producer, Arranged By, Vocals, Guitar: Kenshi Yonezu
13 打上花火 | 4:19 (259 s) | credits: Producer, Arranged By, Vocals: Kenshi Yonezu
14 灰色と青 (+ 菅田将暉) | 5:32 (332 s) | credits: Vocals: Kenshi Yonezu; Vocals: Masaki Suda
14 tracks, total 60:09 (3609 s), without duration: 0
images: primary https://i.discogs.com/Zq88z5pSEoIR8At49VGTLQjCpFnA3AH6OSBP4nGV8e4/rs:fit/g:sm/q:90/h:584/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI3OTcx/MDE5LTE3MTI1Nzc4/MDUtNjI5OS5qcGVn.jpeg | secondary https://i.discogs.com/0-TdjAf4aQcS2d4N4hYS4__-yh4iU8LVAq_fTFYwOes/rs:fit/g:sm/q:90/h:593/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI3OTcx/MDE5LTE3MTI1Nzgw/MzgtNTY0NS5qcGVn.jpeg | secondary https://i.discogs.com/zT2kObrCloDlerazJn2gPcsA8zL1XG7RaKcR8dTYdOI/rs:fit/g:sm/q:90/h:600/w:272/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI3OTcx/MDE5LTE3MTI1Nzc4/ODEtMjUwOC5qcGVn.jpeg | secondary https://i.discogs.com/LLUgdYXy_BLDe_GmYTFqPmls_Mv33UXIFujT3FwcHKA/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI3OTcx/MDE5LTE3MTI1ODA5/NTEtMTk3Mi5qcGVn.jpeg | secondary https://i.discogs.com/XU8VxsZC26VzjbkC2TAZBMMvJBaqC0d5Ae_OuYkO0BY/rs:fit/g:sm/q:90/h:600/w:450/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI3OTcx/MDE5LTE3MTI1ODA2/MTAtOTMzN
… [2246 Zeichen gekürzt]
```
</details>

### 7. `shell` +47s – completed

```
bin/tl-mb release 02ce8500-8e14-48dc-a216-2e2d807a7ee1
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1 | BOOTLEG — 米津玄師 | 2017-11-01 JP | CD | Tracks 14 | Barcode 4547366329698 | Sony Music Records SRCL-9571 | Official | 通常盤
release-group: c7ff52d0-1aad-435b-95cd-18988f705e87 (Album, first date 2017-11-01) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/02ce8500-8e14-48dc-a216-2e2d807a7ee1
-- Medium 1: CD, 14 Tracks
1.1 [1] 飛燕 | 4:03 (243333 ms) | ISRC JPU901702915
1.2 [2] LOSER | 4:04 (243813 ms) | ISRC JPU901602597
1.3 [3] ピースサイン | 3:59 (238533 ms) | ISRC JPU901701672
1.4 [4] 砂の惑星 — 米津玄師 + 初音ミク | 4:00 (240026 ms) | ISRC JPU901702916
1.5 [5] orion | 4:42 (281906 ms) | ISRC JPU901700003
1.6 [6] かいじゅうのマーチ | 4:56 (295720 ms) | ISRC JPU901702917
1.7 [7] Moonlight | 3:45 (224706 ms) | ISRC JPU901702918
1.8 [8] 春雷 | 4:49 (288893 ms) | ISRC JPU901702919
1.9 [9] fogbound — 米津玄師 + 池田エライザ | 4:15 (255200 ms) | ISRC JPU901702920
1.10 [10] ナンバーナイン | 4:22 (261986 ms) | ISRC JPU901602598
1.11 [11] 爱丽丝 | 3:10 (189760 ms) | ISRC JPU901702921
1.12 [12] Nighthawks | 4:20 (260413 ms) | ISRC JPU901702922
1.13 [13] 打上花火 | 4:19 (259386 ms) | ISRC JPU901702923
1.14 [14] 灰色と青 — 米津玄師 + 菅田将暉 | 5:32 (332186 ms) | ISRC JPU901702924
Total: 1:00:16 (3615 s), tracks without duration: 0
```
</details>

### 8. `shell` +65s – completed

```
bin/tl-vision "https://i.discogs.com/ijFbCvOew6Pt6RPpSpEzQ1ztZXTF7Ge0IwRfObloKPg/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTEyNTMxNDEzLTE3MjkwOTcwODUtNzcxOS5qcGVn.jpeg" --context "Back cover of Kenshi Yonezu CD BOOTLEG (SRCL-9571)? List every printed track title exactly, with track numbers, and any printed durations. Also note catalogue number and barcode." 2>&1 | tail -30
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/ijFbCvOew6Pt6RPpSpEzQ1ztZXTF7Ge0IwRfObloKPg/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTEyNTMxNDEzLTE3MjkwOTcwODUtNzcxOS5qcGVn.jpeg
```
</details>

### 9. `shell` +65s – completed

```
bin/tl-vision "https://i.discogs.com/VjVFQ9Uw5_e6VJGiTGlJWcwY0Z_0stSZUMr41tP8GFU/rs:fit/g:sm/q:90/h:595/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTEyNTMxNDEzLTE3MjkwOTcwODYtOTYzOC5qcGVn.jpeg" --context "Back cover of Kenshi Yonezu CD BOOTLEG (SRCL-9571). List every printed track title exactly, with track numbers, and any printed durations." 2>&1 | tail -30
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/VjVFQ9Uw5_e6VJGiTGlJWcwY0Z_0stSZUMr41tP8GFU/rs:fit/g:sm/q:90/h:595/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTEyNTMxNDEzLTE3MjkwOTcwODYtOTYzOC5qcGVn.jpeg
```
</details>

### 10. `shell` +75s – completed

```
bin/tl-caa --help 2>&1 | head -20; echo ====; bin/tl-caa 02ce8500-8e14-48dc-a216-2e2d807a7ee1 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
usage: tl-caa [-h] [--group] mbid

tl-caa <mbid> [--group] — Cover Art Archive: images of a MusicBrainz release (front, back, booklet, medium, tray).

Back/booklet often contain the printed tracklist → read with tl-vision.
--group: <mbid> is a release-group id (front cover of the group only).
Source ID: caa:release/<mbid>/<image-id>

positional arguments:
  mbid

options:
  -h, --help  show this help message and exit
  --group
====
caa:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1/19258630514 | Front | http://coverartarchive.org/release/02ce8500-8e14-48dc-a216-2e2d807a7ee1/19258630514-1200.jpg
1 images · read tracklist: tl-vision <url> --context "…"
```
</details>

### 11. `shell` +79s – completed

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

### 12. `shell` +81s – completed

```
bin/tl-validate --schema 2>&1 | python3 -c "
import json,sys
s=json.load(sys.stdin)
print(json.dumps(s['\$defs'].get('Conflict'),ensure_ascii=False,indent=1))
print(list(s['properties'].keys()))
"
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
}
['input', 'status', 'release', 'tracks', 'artists', 'total_duration_s', 'confidence', 'sources', 'conflicts', 'missing', 'alternatives', 'reasoning']
```
</details>

### 13. `write` +103s – completed

```
{"path": "output/work/fall-cdd5b62e.json", "content": "{\n  \"input\": {\"id\": \"fall-cdd5b62e\", \"title\": \"BOOTLEG\", \"artist\": \"Kenshi Yonezu\", \"format\": \"CD\"},\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"BOOTLEG\",\n    \"artist\": \"米津玄師\",\n    \"format\": \"CD\",\n    \"country\": \"JP\",\n    \"year\": 2017,\n    \"label\": \"Sony Music Records\",\n    \"catno\": \"SRCL-9571\",\n    \"barcode\": \"4547366329698\",\n    \"edition\": \"通常盤 (Standard Edition), 1×CD\",\n    \"ids\": {\n      \"musicbrainz\": \"02ce8500-8e14-48dc-a216-2e2d807a7ee1\",\n      \"discogs\": \"12531413\"\n    }\n  },\n  \"tracks\": [\n    {\"position\": \"1\", \"disc\": 1, \"title\": \"飛燕\", \"artist\": null, \"duration_s\": 243,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"2\", \"disc\": 1, \"title\": \"LOSER\", \"artist\": null, \"duration_s\": 244,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"3\", \"disc\": 1, \"title\": \"ピースサイン\", \"artist\": null, \"duration_s\": 239,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"4\", \"disc\": 1, \"title\": \"砂の惑星\", \"artist\": \"米津玄師 + 初音ミク\", \"duration_s\": 240,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"5\", \"disc\": 1, \"title\": \"orion\", \"artist\": null, \"duration_s\": 282,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"6\", \"disc\": 1, \"title\": \"かいじゅうのマーチ\", \"artist\": null, \"duration_s\": 296,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"7\", \"disc\": 1, \"title\": \"Moonlight\", \"artist\": null, \"duration_s\": 225,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"8\", \"disc\": 1, \"title\": \"春雷\", \"artist\": null, \"duration_s\": 289,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"9\", \"disc\": 1, \"title\": \"fogbound\", \"artist\": \"米津玄師 + 池田エライザ\", \"duration_s\": 255,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"10\", \"disc\": 1, \"title\": \"ナンバーナイン\", \"artist\": null, \"duration_s\": 262,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"11\", \"disc\": 1, \"title\": \"爱丽丝\", \"artist\": null, \"duration_s\": 190,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"12\", \"disc\": 1, \"title\": \"Nighthawks\", \"artist\": null, \"duration_s\": 260,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"13\", \"disc\": 1, \"title\": \"打上花火\", \"artist\": null, \"duration_s\": 259,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []},\n    {\"position\": \"14\", \"disc\": 1, \"title\": \"灰色と青\", \"artist\": \"米津玄師 + 菅田将暉\", \"duration_s\": 332,\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"],\n     \"duration_sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"], \"flags\": []}\n  ],\n  \"artists\": [\n    {\"name\": \"米津玄師\", \"role\": \"main\", \"tracks\": [],\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"]},\n    {\"name\": \"初音ミク\", \"role\": \"featured\", \"tracks\": [\"4\"],\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"]},\n    {\"name\": \"池田エライザ\", \"role\": \"featured\", \"tracks\": [\"9\"],\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"]},\n    {\"name\": \"菅田将暉\", \"role\": \"featured\", \"tracks\": [\"14\"],\n     \"sources\": [\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"discogs:release/12531413\"]}\n  ],\n  \"total_duration_s\": 3616,\n  \"confidence\": 0.8,\n  \"sources\": [\n    {\"id\": \"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"url\": \"https://musicbrainz.org/release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\", \"kind\": \"database\", \"note\": \"Matched Japanese CD edition SRCL-9571 / barcode 4547366329698, durations in ms\"},\n    {\"id\": \"discogs:release/12531413\", \"url\": \"https://www.discogs.com/release/12531413\", \"kind\": \"database\", \"note\": \"Same edition: SRCL 9571, barcode 4547366329698, 14 tracks, durations agree within 1 s\"}\n  ],\n  \"conflicts\": [\n    {\"field\": \"title track 2\", \"values\": {\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\": \"LOSER\", \"discogs:release/12531413\": \"Loser\"},\n     \"resolution\": \"MusicBrainz CD entry used (uppercase is the official single spelling); Discogs normalises capitalisation\"},\n    {\"field\": \"title track 5\", \"values\": {\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\": \"orion\", \"discogs:release/12531413\": \"Orion\"},\n     \"resolution\": \"MusicBrainz CD entry used (lowercase is the official single spelling); Discogs normalises capitalisation\"},\n    {\"field\": \"title track 9\", \"values\": {\"musicbrainz:release/02ce8500-8e14-48dc-a216-2e2d807a7ee1\": \"fogbound\", \"discogs:release/12531413\": \"Fogbound\"},\n     \"resolution\": \"MusicBrainz CD entry used (lowercase is the official spelling); Discogs normalises capitalisation\"}\n  ],\n  \"missing\": [\n    \"No barcode in the input, so the edition was chosen by format: several Japanese physical editions with identical 14-track CD exist (standard 通常盤 SRCL-9571, limited SRCL 9567~8, CD+DVD SRCL 9569~70). The plain CD without extras was taken.\",\n    \"Back cover could not be read (Discogs images return HTTP 403, Cover Art Archive has only the front for this release); printed titles/credits were therefore taken from the MusicBrainz CD entry, which Discogs corroborates.\"\n  ],\n  \"alternatives\": [\n    {\"description\": \"CD + DVD, Limited Edition, SRCL 9569~70, Japan 2017, barcode 4547366329681, 14 tracks + 4 music videos\",\n     \"source\": \"discogs:release/11114145\", \"why_not\": \"includes a DVD; input specifies only CD and gives no barcode or limited-edition hint\"},\n    {\"description\": \"Limited Edition CD + 12\\\" sleeve, poster, dummy record, 6 cover prints, SRCL 9567~8, Japan 2017, barcode 4547366329674\",\n     \"source\": \"discogs:release/27971019\", \"why_not\": \"deluxe box with extra items; input gives no barcode or edition hint\"},\n    {\"description\": \"Taiwan CD+DVD edition, catno 19075802642, barcode 190758026428\",\n     \"source\": \"discogs:release/12491102\", \"why_not\": \"different country/barcode, includes DVD\"},\n    {\"description\": \"China 2019 CD edition (Bootleg = 私藏), catno 19075893942, barcode 9787798420036\",\n     \"source\": \"discogs:release/36987714\", \"why_not\": \"different country and barcode\"},\n    {\"description\": \"Digital Media edition, barcode 886446811420, 14 tracks (MusicBrainz)\",\n     \"source\": \"musicbrainz:release/2f923832-09d2-4ae9-b1f3-2680ef5a01de\", \"why_not\": \"digital only; physical edition preferred\"}\n  ],\n  \"reasoning\": \"The input gives only title, artist and format CD. MusicBrainz release group 'BOOTLEG' contains exactly one physical CD: the Japanese standard edition 通常盤 SRCL-9571 (barcode 4547366329698). Discogs lists the same edition as release 12531413 with identical catalogue number, barcode and 14 tracks; all durations agree within 1 s (MB ms values used). Track titles are Japanese as printed on the Japanese CD, romanised titles in the digital edition (Hien, Peace Sign, etc.) were not used. Featured artists on tracks 4, 9 and 14 are credited separately in both databases. The CD+DVD and deluxe editions and the Taiwan/China pressings share the same 14 audio tracks but differ in barcode and extras, so they are recorded as alternatives.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-cdd5b62e.json
```
</details>

### 14. `shell` +104s – completed

```
bin/tl-validate output/work/fall-cdd5b62e.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 14 tracks (14 with duration), 2 sources, 3 conflicts, confidence=0.8
```
</details>

> **Agent** +106s: FERTIG found 14 Tracks confidence=0.8
