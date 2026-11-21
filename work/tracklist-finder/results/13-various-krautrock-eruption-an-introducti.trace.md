# Agent-Trace: 13-various-krautrock-eruption-an-introducti

> Schnellweg geprüft: no fast path: 6 duration differences > 2 s between MusicBrainz and Discogs – agent should resolve
Start 2026-11-20T15:48:16 · 13 Schritte · 19 Tool-Aufrufe · Tokens in 65027 / out 15690


> **Agent** +4s: I'll start by checking the barcode and searching both databases.

### 1. `shell` +5s – completed

```
cd <repo> && bin/tl-discogs search --barcode 4015698189711 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
1 hits (parameters: {'barcode': '4015698189711'})
discogs:release/33751572 | Various - Krautrock Eruption (An Introduction To German Electronic Music 1970-1980) | 2025 Germany | CD, Compilation | Label Bureau B, Bureau B | Kat.-Nr. BB478 | Barcodes 4 015698 189711, 4015698189711, LC 13875 | master 3814443
```
</details>

### 2. `shell` +5s – completed

```
cd <repo> && bin/tl-gtin 4015698189711 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
input: '4015698189711' → digits: 4015698189711 (13 digits)
type: EAN-13  valid: yes
search variants: 4015698189711
prefix 400–440: assigned in Germany (says nothing about the country of release)
```
</details>

### 3. `shell` +5s – completed

```
cd <repo> && bin/tl-mb search --barcode 4015698189711 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
1 Releases (Queries: barcode:(4015698189711))
musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15 | Krautrock Eruption: An Introduction To German Electronic Music 1970–1980 — Various Artists | 2025-03-21 XW | CD | Tracks 12 | Barcode 4015698189711 | Bureau B 267192 | Official | score 100
```
</details>

> **Agent** +10s: Barcode hits both databases. Fetching details.

### 4. `shell` +10s – completed

```
cd <repo> && bin/tl-discogs release 33751572 2>&1
```

<details><summary>Ausgabe</summary>

```
discogs:release/33751572 | Krautrock Eruption (An Introduction To German Electronic Music 1970-1980) — Various | 2025 Germany | 1× CD (Compilation) | Bureau B BB478 | master 3814443
url: https://www.discogs.com/release/33751572-Various-Krautrock-Eruption-An-Introduction-To-German-Electronic-Music-1970-1980
identifiers: Barcode: 4 015698 189711 (Text [EAN-13]) | Barcode: 4015698189711 (Scanned [EAN]) | Label Code: LC 13875 | Matrix / Runout: BB478. VA - Krautrock Eruption LC13875 AP30607-01 manufactured by optimal media GmbH | Mastering SID Code: IFPI L578 | Mould SID Code: IFPI 9706 | Rights Society: Gema | Other: 978-3-95575-233-0 (ISBN)
notes: ℗ & © 2025 Bureau B, Stahltwiete 10, 22761 Hamburg, Germany, [email removed] • • Made in the EU www.bureau-b.com (from the back sleeve)
1 Ballet Statique — Conrad Schnitzler | 5:03 (303 s)
2 I've Heard That One Before / Watch Your Step — Faust | 2:50 (170 s)
3 Foreign Affairs — Brian Eno, Dieter Moebius, Hans-Joachim Roedelius | 3:30 (210 s)
4 Emphasis — Harald Grosskopf | 4:59 (299 s)
5 21:32 (Bureau B Edit) — Cluster | 4:36 (276 s)
6 Rastakraut Pasta — Dieter Moebius, Conny Plank | 6:18 (378 s)
7 Glaubersalz — Hans-Joachim Roedelius | 3:29 (209 s)
8 Minimal Tape 3/7.2 — Pyrolator | 4:22 (262 s)
9 Himmelblau (Bureau B Edit) — Wolfgang Riechmann | 6:08 (368 s)
10 Kluster 2 (Electric Music) (Bureau B Edit) — Kluster (3) | 2:46 (166 s)
11 Apricot Brandy II (Bureau B Edit) — Günter Schickert | 5:24 (324 s)
12 Falter-Lamento — Asmus Tietchens | 6:18 (378 s)
12 tracks, total 55:43 (3343 s), without duration: 0
images: primary https://i.discogs.com/GWXaBJhis4rLQONY1PwidgsjofmBI_kn_2FkcMmCGvY/rs:fit/g:sm/q:90/h:534/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzUx/NTcyLTE3NDUwODc5/OTAtODgxMi5qcGVn.jpeg | secondary https://i.discogs.com/p_l_DmxnTDaCKz8WKcpx_rnurx-t0AxMz8Xwlt3CTqo/rs:fit/g:sm/q:90/h:535/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNzUx/NTcyLTE3NDUwODc5/OTAtOTIxMi5qcGVn.jpeg
community: have 46 want 10 data_quality Needs Vote
```
</details>

### 5. `shell` +10s – completed

```
cd <repo> && bin/tl-mb release 30f95ef1-7c0e-430f-9e08-c672ad37da15 2>&1
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15 | Krautrock Eruption: An Introduction To German Electronic Music 1970–1980 — Various Artists | 2025-03-21 XW | CD | Tracks 12 | Barcode 4015698189711 | Bureau B 267192 | Official
release-group: 47e01589-9682-4301-aacc-175d6cb64842 (Album, first date 2025-03-21) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/30f95ef1-7c0e-430f-9e08-c672ad37da15
-- Medium 1: CD, 12 Tracks
1.1 [1] Ballet Statique — Conrad Schnitzler | 4:57 (296720 ms)
1.2 [2] I’ve Heard That One Before / Watch Your Step — Faust | 2:49 (169173 ms)
1.3 [3] Foreign Affairs — Brian Eno | 3:27 (207133 ms)
1.4 [4] Emphasis — Harald Grosskopf | 4:56 (295840 ms)
1.5 [5] 21:32 (bureau b edit) — Cluster | 4:37 (276720 ms)
1.6 [6] Rastakraut Pasta — Moebius | 6:17 (376854 ms)
1.7 [7] Glaubersalz — Roedelius | 3:24 (203944 ms)
1.8 [8] Minimal Tape 3/7.2 — Pyrolator | 4:20 (259640 ms)
1.9 [9] Himmelblau (bureau b edit) — Riechmann | 6:04 (363810 ms)
1.10 [10] Kluster 2 (Electric Music) (bureau b edit) — Kluster | 2:46 (165608 ms)
1.11 [11] Apricot Brandy II (bureau b edit) — Günter Schickert | 5:22 (321944 ms)
1.12 [12] Falter-Lamento — Asmus Tietchens | 6:12 (371896 ms)
Total: 55:09 (3309 s), tracks without duration: 0
```
</details>

> **Agent** +77s: Both sources match with 12 tracks, but durations differ on many tracks. Let me check the release group/other editions and the cover image.

### 6. `shell` +77s – completed

```
cd <repo> && bin/tl-discogs versions 3814443 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
3 versions of master 3814443
discogs:release/33751572 | Krautrock Eruption (An Introduction To German Electronic Music 1970-1980) | 2025 Germany | Compilation | Bureau B BB478 | CD
discogs:release/33677340 | Krautrock Eruption (An Introduction To German Electronic Music 1970-1980) | 2025 Germany | LP, Compilation | Bureau B BB478 | Vinyl
discogs:release/33707157 | Krautrock Eruption (An Introduction To German Electronic Music 1970-1980) | 2025 Germany | LP, Compilation | Bureau B BB478LPRT | Vinyl
```
</details>

### 7. `shell` +77s – completed

```
cd <repo> && bin/tl-caa 30f95ef1-7c0e-430f-9e08-c672ad37da15 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
caa:release/30f95ef1-7c0e-430f-9e08-c672ad37da15/41827729052 | Front | https://coverartarchive.org/release/30f95ef1-7c0e-430f-9e08-c672ad37da15/41827729052-1200.jpg
1 images · read tracklist: tl-vision <url> --context "…"
```
</details>

### 8. `shell` +95s – completed

```
cd <repo> && bin/tl-vision "https://i.discogs.com/p_l_DmxnTDaCKz8WKcpx_rnurx-t0AxMz8Xwlt3CTqo/rs:fit/g:sm/q:90/h:535/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMzNzUx/NTcyLTE3NDUwODc5OTAtOTIxMi5qcGVn.jpeg" --context "Back sleeve of CD 'Krautrock Eruption' Bureau B BB478. Read the printed tracklist: track numbers, titles, artist credits and any durations." 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/p_l_DmxnTDaCKz8WKcpx_rnurx-t0AxMz8Xwlt3CTqo/rs:fit/g:sm/q:90/h:535/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMzNzUx/NTcyLTE3NDUwODc5OTAtOTIxMi5qcGVn.jpeg
```
</details>

### 9. `shell` +102s – completed

```
cd <repo> && bin/tl-discogs release 33677340 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
discogs:release/33677340 | Krautrock Eruption (An Introduction To German Electronic Music 1970-1980) — Various | 2025-03-21 Germany | 1× Vinyl (LP, Compilation) | Bureau B BB478; Ventil Verlag BB478 | master 3814443
url: https://www.discogs.com/release/33677340-Various-Krautrock-Eruption-An-Introduction-To-German-Electronic-Music-1970-1980
identifiers: Barcode: 4 015698 041187 (Text) | Barcode: 4015698041187 (Scanned) | Label Code: LC 13875 | Matrix / Runout: I1 INDIGO LP 26719 - 1 A (Side A) | Matrix / Runout: I1 INDIGO LP 26719 - 1 B (Side B) | Rights Society: Gema
notes: Issued with a printed inner sleeve. A1 • Published by Tapete Songs • Originally released in 1978 on "[m22107]" (EGG 90 184) • A2 • Published by Tapete Songs • Originally released in 1973 on "[m28083]" (Virgin VC 501) • A3 • Published by Universal Music Publishing, Copyright Control, Rueckbank Musikverlag • Originally released in 1978 on "[m12000]" (SKY 021) • A4 • Published by Copyright Control • 
A1 Ballet Statique — Conrad Schnitzler | 5:03 (303 s)
A2 I've Heard That One Before / Watch Your Step — Faust | 2:50 (170 s)
A3 Foreign Affairs — Brian Eno, Dieter Moebius, Hans-Joachim Roedelius | 3:30 (210 s)
A4 Emphasis — Harald Grosskopf | 4:59 (299 s)
A5 21:32 (Bureau B Edit) — Cluster | 4:36 (276 s)
A6 Rastakraut Pasta — Dieter Moebius, Conny Plank | 6:18 (378 s)
B1 Glaubersalz — Hans-Joachim Roedelius | 3:29 (209 s)
B2 Minimal Tape 3/7.2 — Pyrolator | 4:22 (262 s)
B3 Himmelblau (Bureau B Edit) — Wolfgang Riechmann | 6:08 (368 s)
B4 Kluster 2 (Electric Music) (Bureau B Edit) — Kluster (3) | 2:46 (166 s)
B5 Apricot Brandy II (Bureau B Edit) — Günter Schickert | 5:24 (324 s)
B6 Falter-Lamento — Asmus Tietchens | 6:18 (378 s)
12 tracks, total 55:43 (3343 s), without duration: 0
images: primary https://i.discogs.com/rm6WMH3te6Fuu2_YD2cD2_kJtKMitWdFnJ9szQkrWkg/rs:fit/g:sm/q:90/h:568/w:599/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTMzNjc3/MzQwLTE3NDQ4ODk1/MDEtMzMxMi5qcGVn.jpeg
community: have 149 want 44 data_quality Correct
```
</details>

### 10. `shell` +102s – completed

```
cd <repo> && bin/tl-mb group 47e01589-9682-4301-aacc-175d6cb64842 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
1 Releases in release-group 47e01589-9682-4301-aacc-175d6cb64842
musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15 | Krautrock Eruption: An Introduction To German Electronic Music 1970–1980 —  | 2025-03-21 XW | CD | Tracks 12 | Barcode 4015698189711 | Bureau B 267192 | Official
```
</details>

### 11. `shell` +109s – completed

```
cd <repo> && bin/tl-deezer search --artist "Various Artists" --title "Krautrock Eruption" 2>&1 | head -15
```

<details><summary>Ausgabe</summary>

```
1 Alben (q=artist:"Various Artists" album:"Krautrock Eruption")
deezer:album/704460101 | Krautrock Eruption – An Introduction To German Electronic Music 1970-1980 — Verschiedene Interpreten | 12 Tracks | album
```
</details>

### 12. `shell` +114s – completed

```
cd <repo> && bin/tl-itunes search "Various Krautrock Eruption" 2>&1 | head -15
```

<details><summary>Ausgabe</summary>

```
1 Alben
itunes:album/1793124678 | Krautrock Eruption – An Introduction To German Electronic Music 1970-1980 — Verschiedene Interpret:innen | 2020-01-01 | 12 Tracks
```
</details>

### 13. `shell` +135s – completed

```
cd <repo> && bin/tl-itunes --help 2>&1 | head -30; echo ---; bin/tl-deezer --help 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
usage: tl-itunes [-h] {upc,search,album} ...

tl-itunes — Apple iTunes Search/Lookup (no key, ~20 req/min). Digital catalogue!

  tl-itunes upc <barcode> [--country de]        album + tracklist by UPC/EAN
  tl-itunes search "<artist> <title>" [--country de] [--limit 10]
  tl-itunes album <collectionId> [--country de]

Source IDs: itunes:album/<collectionId>, URL from collectionViewUrl

positional arguments:
  {upc,search,album}

options:
  -h, --help          show this help message and exit
---
usage: tl-deezer [-h] {upc,search,album} ...

tl-deezer — Deezer API (no key). Digital catalogue, knows digital UPCs only!

  tl-deezer upc <barcode>
  tl-deezer search --artist A --title T [--limit 10]
  tl-deezer album <id>

Source IDs: deezer:album/<id>, URL https://www.deezer.com/album/<id>

positional arguments:
  {upc,search,album}

options:
  -h, --help          show this help message and exit
```
</details>

### 14. `shell` +143s – completed

```
cd <repo> && bin/tl-itunes album 1793124678 --country de 2>&1 | head -25
```

<details><summary>Ausgabe</summary>

```
itunes:album/1793124678 | Krautrock Eruption – An Introduction To German Electronic Music 1970-1980 — Verschiedene Interpret:innen | 2020-01-01 | 12 Tracks | ℗ 2020 Bureau B
url: https://music.apple.com/de/album/krautrock-eruption-an-introduction-to-german/1793124678?uo=4
1.1 Ballet Statique — Conrad Schnitzler | 4:57 (296720 ms)
1.2 I’ve Heard That One Before/Watch Your Step — Faust | 2:49 (169173 ms)
1.3 Foreign Affairs — Brian Eno, Moebius & Roedelius | 3:31 (211107 ms)
1.4 Emphasis — Harald Grosskopf | 4:59 (299267 ms)
1.5 21:32 (bureau b edit) — Cluster | 4:37 (276720 ms)
1.6 Rastakraut Pasta — Moebius & Plank | 6:17 (377453 ms)
1.7 Glaubersalz — Roedelius | 3:27 (207307 ms)
1.8 Minimal Tape 3/7.2 — Pyrolator | 4:22 (261707 ms)
1.9 Himmelblau (bureau b edit) — Riechmann | 6:04 (363810 ms)
1.10 Kluster 2 (Electric Music) [bureau b edit] — Kluster | 2:46 (165608 ms)
1.11 Apricot Brandy II (bureau b edit) — Günter Schickert | 5:22 (321944 ms)
1.12 Falter-Lamento — Asmus Tietchens | 6:18 (378400 ms)
Total 55:29 (3329 s)
```
</details>

### 15. `shell` +144s – completed

```
cd <repo> && bin/tl-deezer album 704460101 2>&1 | head -25
```

<details><summary>Ausgabe</summary>

```
deezer:album/704460101 | Krautrock Eruption – An Introduction To German Electronic Music 1970-1980 — Verschiedene Interpreten | 2025-03-21 | UPC 4015698189711 | 12 Tracks | Label Bureau B
url: https://www.deezer.com/album/704460101
1.1 Ballet Statique | 4:56
1.2 I’ve Heard That One Before/Watch Your Step | 2:49
1.3 Foreign Affairs | 3:31
1.4 Emphasis | 4:59
1.5 21:32 (bureau b edit) | 4:36
1.6 Rastakraut Pasta | 6:17
1.7 Glaubersalz | 3:27
1.8 Minimal Tape 3/7.2 | 4:21
1.9 Himmelblau (bureau b edit) | 6:03
1.10 Kluster 2 (Electric Music) (bureau b edit) | 2:45
1.11 Apricot Brandy II (bureau b edit) | 5:21
1.12 Falter-Lamento | 6:18
Total 55:23 (3323 s)
```
</details>

### 16. `shell` +164s – completed

```
cd <repo> && bin/tl-validate --schema 2>&1 | head -80
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

### 17. `shell` +175s – completed

```
cd <repo> && bin/tl-validate --schema 2>&1 | sed -n '80,400p'
```

<details><summary>Ausgabe</summary>

```
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
   
… [2560 Zeichen gekürzt]
```
</details>

> **Agent** +243s: Both databases agree on the 12-track list. Now building the result with a per-track duration majority decision.

### 18. `write` +243s – completed

```
{"path": "<repo>/output/work/fall-d8f463c9.json", "content": "{\n  \"input\": {\n    \"id\": \"fall-d8f463c9\",\n    \"title\": \"Krautrock Eruption (An Introduction To German Electronic Music 1970-1980)\",\n    \"artist\": \"Various\",\n    \"ean\": \"4015698189711\"\n  },\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"Krautrock Eruption: An Introduction To German Electronic Music 1970–1980\",\n    \"artist\": \"Various Artists\",\n    \"format\": \"CD\",\n    \"country\": \"DE\",\n    \"year\": 2025,\n    \"label\": \"Bureau B\",\n    \"catno\": \"BB478\",\n    \"barcode\": \"4015698189711\",\n    \"edition\": \"CD compilation, Bureau B BB478 (Indigo 267192), LC 13875, made in EU, ISBN 978-3-95575-233-0\",\n    \"ids\": {\n      \"musicbrainz\": \"30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n      \"discogs\": \"33751572\"\n    }\n  },\n  \"tracks\": [\n    {\n      \"position\": \"1\",\n      \"disc\": 1,\n      \"title\": \"Ballet Statique\",\n      \"artist\": \"Conrad Schnitzler\",\n      \"duration_s\": 297,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"2\",\n      \"disc\": 1,\n      \"title\": \"I’ve Heard That One Before / Watch Your Step\",\n      \"artist\": \"Faust\",\n      \"duration_s\": 169,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": []\n    },\n    {\n      \"position\": \"3\",\n      \"disc\": 1,\n      \"title\": \"Foreign Affairs\",\n      \"artist\": \"Brian Eno, Dieter Moebius, Hans-Joachim Roedelius\",\n      \"duration_s\": 210,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"4\",\n      \"disc\": 1,\n      \"title\": \"Emphasis\",\n      \"artist\": \"Harald Grosskopf\",\n      \"duration_s\": 299,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"5\",\n      \"disc\": 1,\n      \"title\": \"21:32 (bureau b edit)\",\n      \"artist\": \"Cluster\",\n      \"duration_s\": 277,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": []\n    },\n    {\n      \"position\": \"6\",\n      \"disc\": 1,\n      \"title\": \"Rastakraut Pasta\",\n      \"artist\": \"Dieter Moebius, Conny Plank\",\n      \"duration_s\": 377,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": []\n    },\n    {\n      \"position\": \"7\",\n      \"disc\": 1,\n      \"title\": \"Glaubersalz\",\n      \"artist\": \"Hans-Joachim Roedelius\",\n      \"duration_s\": 209,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"8\",\n      \"disc\": 1,\n      \"title\": \"Minimal Tape 3/7.2\",\n      \"artist\": \"Pyrolator\",\n      \"duration_s\": 262,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"9\",\n      \"disc\": 1,\n      \"title\": \"Himmelblau (bureau b edit)\",\n      \"artist\": \"Wolfgang Riechmann\",\n      \"duration_s\": 364,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"10\",\n      \"disc\": 1,\n      \"title\": \"Kluster 2 (Electric Music) (bureau b edit)\",\n      \"artist\": \"Kluster\",\n      \"duration_s\": 166,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": []\n    },\n    {\n      \"position\": \"11\",\n      \"disc\": 1,\n      \"title\": \"Apricot Brandy II (bureau b edit)\",\n      \"artist\": \"Günter Schickert\",\n      \"duration_s\": 322,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    },\n    {\n      \"position\": \"12\",\n      \"disc\": 1,\n      \"title\": \"Falter-Lamento\",\n      \"artist\": \"Asmus Tietchens\",\n      \"duration_s\": 378,\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"duration_sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ],\n      \"flags\": [\n        \"duration_conflict\"\n      ]\n    }\n  ],\n  \"artists\": [\n    {\n      \"name\": \"Conrad Schnitzler\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"1\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Faust\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"2\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Brian Eno\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"3\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ]\n    },\n    {\n      \"name\": \"Dieter Moebius\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"3\",\n        \"6\"\n      ],\n      \"sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ]\n    },\n    {\n      \"name\": \"Hans-Joachim Roedelius\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"3\",\n        \"7\"\n      ],\n      \"sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ]\n    },\n    {\n      \"name\": \"Harald Grosskopf\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"4\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Cluster\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"5\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Conny Plank\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"6\"\n      ],\n      \"sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ]\n    },\n    {\n      \"name\": \"Pyrolator\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"8\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Wolfgang Riechmann\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"9\"\n      ],\n      \"sources\": [\n        \"discogs:release/33751572\",\n        \"itunes:album/1793124678\"\n      ]\n    },\n    {\n      \"name\": \"Kluster\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"10\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Günter Schickert\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"11\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    },\n    {\n      \"name\": \"Asmus Tietchens\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"12\"\n      ],\n      \"sources\": [\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n        \"discogs:release/33751572\"\n      ]\n    }\n  ],\n  \"total_duration_s\": 3330,\n  \"confidence\": 0.85,\n  \"sources\": [\n    {\n      \"id\": \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n      \"url\": \"https://musicbrainz.org/release/30f95ef1-7c0e-430f-9e08-c672ad37da15\",\n      \"kind\": \"database\",\n      \"note\": \"barcode 4015698189711 exact match, CD, 12 tracks, durations in ms\"\n    },\n    {\n      \"id\": \"discogs:release/33751572\",\n      \"url\": \"https://www.discogs.com/release/33751572\",\n      \"kind\": \"database\",\n      \"note\": \"barcode 4015698189711 exact match, CD, Bureau B BB478, matrix BB478/optimal media, GEMA, joint artist credits per track\"\n    },\n    {\n      \"id\": \"itunes:album/1793124678\",\n      \"url\": \"https://music.apple.com/de/album/krautrock-eruption-an-introduction-to-german/1793124678\",\n      \"kind\": \"streaming\",\n      \"note\": \"digital edition, same 12 tracks; used only as duration cross-check (ms)\"\n    },\n    {\n      \"id\": \"deezer:album/704460101\",\n      \"url\": \"https://www.deezer.com/album/704460101\",\n      \"kind\": \"streaming\",\n      \"note\": \"digital edition, UPC 4015698189711, durations to the second, used as rough cross-check only\"\n    },\n    {\n      \"id\": \"discogs:release/33677340\",\n      \"url\": \"https://www.discogs.com/release/33677340\",\n      \"kind\": \"database\",\n      \"note\": \"same master, 1xLP (barcode 4015698041187) - confirms track order and joint credits (Eno/Moebius/Roedelius, Moebius/Plank)\"\n    }\n  ],\n  \"conflicts\": [\n    {\n      \"field\": \"duration track 1\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"296.72\",\n        \"itunes:album/1793124678\": \"296.72\",\n        \"discogs:release/33751572\": \"303\"\n      },\n      \"resolution\": \"Took 297 s: MusicBrainz (ms precision) and iTunes agree exactly, Discogs is the outlier (+6 s)\"\n    },\n    {\n      \"field\": \"duration track 3\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"207.133\",\n        \"discogs:release/33751572\": \"210\",\n        \"itunes:album/1793124678\": \"211.107\"\n      },\n      \"resolution\": \"Took 210 s (Discogs, physical CD); iTunes within 1.1 s, MusicBrainz is the outlier (-3 s)\"\n    },\n    {\n      \"field\": \"duration track 4\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"295.84\",\n        \"discogs:release/33751572\": \"299\",\n        \"itunes:album/1793124678\": \"299.267\"\n      },\n      \"resolution\": \"Took 299 s (Discogs + iTunes agree); MusicBrainz is the outlier (-3.2 s)\"\n    },\n    {\n      \"field\": \"duration track 7\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"203.944\",\n        \"discogs:release/33751572\": \"209\",\n        \"itunes:album/1793124678\": \"207.307\"\n      },\n      \"resolution\": \"Took 209 s (Discogs, physical CD); iTunes within 1.7 s, MusicBrainz is the outlier (-5.1 s)\"\n    },\n    {\n      \"field\": \"duration track 8\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"259.64\",\n        \"discogs:release/33751572\": \"262\",\n        \"itunes:album/1793124678\": \"261.707\"\n      },\n      \"resolution\": \"Took 262 s (Discogs, physical CD); iTunes within 0.3 s, MusicBrainz is the outlier (-2.4 s)\"\n    },\n    {\n      \"field\": \"duration track 9\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"363.81\",\n        \"itunes:album/1793124678\": \"363.81\",\n        \"discogs:release/33751572\": \"368\"\n      },\n      \"resolution\": \"Took 364 s: MusicBrainz and iTunes agree exactly, Discogs is the outlier (+4 s)\"\n    },\n    {\n      \"field\": \"duration track 11\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"321.944\",\n        \"itunes:album/1793124678\": \"321.944\",\n        \"discogs:release/33751572\": \"324\"\n      },\n      \"resolution\": \"Took 322 s: MusicBrainz and iTunes agree exactly, Discogs is the outlier (+2.1 s)\"\n    },\n    {\n      \"field\": \"duration track 12\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"371.896\",\n        \"discogs:release/33751572\": \"378\",\n        \"itunes:album/1793124678\": \"378.4\"\n      },\n      \"resolution\": \"Took 378 s (Discogs + iTunes agree); MusicBrainz is the outlier (-6.5 s)\"\n    },\n    {\n      \"field\": \"artist track 3\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"Brian Eno\",\n        \"discogs:release/33751572\": \"Brian Eno, Dieter Moebius, Hans-Joachim Roedelius\",\n        \"itunes:album/1793124678\": \"Brian Eno, Moebius & Roedelius\"\n      },\n      \"resolution\": \"Used the joint credit (Discogs and iTunes both list all three performers; taken from the album 'After the Heat'); MusicBrainz only stores one\"\n    },\n    {\n      \"field\": \"artist track 6\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"Moebius\",\n        \"discogs:release/33751572\": \"Dieter Moebius, Conny Plank\",\n        \"itunes:album/1793124678\": \"Moebius & Plank\"\n      },\n      \"resolution\": \"Used the duo credit Dieter Moebius, Conny Plank (Discogs/iTunes); MusicBrainz only stores one artist\"\n    },\n    {\n      \"field\": \"artist track 7\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"Roedelius\",\n        \"discogs:release/33751572\": \"Hans-Joachim Roedelius\"\n      },\n      \"resolution\": \"Used the full name Hans-Joachim Roedelius (Discogs); MusicBrainz short form refers to the same artist\"\n    },\n    {\n      \"field\": \"artist track 9\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"Riechmann\",\n        \"discogs:release/33751572\": \"Wolfgang Riechmann\"\n      },\n      \"resolution\": \"Used the full name Wolfgang Riechmann (Discogs); MusicBrainz short form refers to the same artist\"\n    },\n    {\n      \"field\": \"country\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"XW\",\n        \"discogs:release/33751572\": \"Germany\"\n      },\n      \"resolution\": \"DE (German label Bureau B, GEMA rights society, LC 13875); MusicBrainz uses the vague 'worldwide'\"\n    },\n    {\n      \"field\": \"year\",\n      \"values\": {\n        \"musicbrainz:release/30f95ef1-7c0e-430f-9e08-c672ad37da15\": \"2025-03-21\",\n        \"discogs:release/33751572\": \"2025\",\n        \"itunes:album/1793124678\": \"2020-01-01\"\n      },\n      \"resolution\": \"2025 (both physical editions agree; iTunes date is a placeholder)\"\n    }\n  ],\n  \"missing\": [\n    \"Printed back cover could not be read (Discogs image returned HTTP 403, MusicBrainz has front cover only) - title capitalisation, especially '(bureau b edit)' vs '(Bureau B Edit)', is taken from MusicBrainz\",\n    \"Duration discrepancies between MusicBrainz and Discogs of up to 6.5 s on 8 of 12 tracks could not be settled by a physical source; per-track majority of sources used\"\n  ],\n  \"alternatives\": [\n    {\n      \"description\": \"1×LP, Bureau B BB478 / Ventil Verlag, 2025 Germany, barcode 4015698041187, 12 tracks (A1-A6, B1-B6)\",\n      \"source\": \"discogs:release/33677340\",\n      \"why_not\": \"vinyl edition, different barcode; the input barcode belongs to the CD\"\n    },\n    {\n      \"description\": \"1×LP, Bureau B BB478LPRT, 2025 Germany, 12 tracks (variant vinyl pressing)\",\n      \"source\": \"discogs:release/33707157\",\n      \"why_not\": \"vinyl edition, different catalogue number and barcode\"\n    }\n  ],\n  \"reasoning\": \"EAN 4015698189711 is a valid EAN-13 and hits exactly one release in MusicBrainz and one in Discogs, both the 2025 Bureau B CD (BB478, GEMA, LC 13875) with the same 12 tracks in the same order - so the edition is unambiguous (physical CD preferred over the LP and the digital versions). Titles follow MusicBrainz (printed cover not readable); artist credits for tracks 3, 6, 7, 9 were completed from the Discogs per-track credits, which are corroborated by the LP entry and iTunes. Durations: MusicBrainz (ms) and the digital edition agree exactly on tracks 1, 2, 5, 6, 9, 10, 11; on tracks 3, 4, 7, 8, 12 MusicBrainz deviates from both Discogs and iTunes by 2-6.5 s, so the majority value (Discogs/iTunes) was taken. Total 55:30.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-d8f463c9.json
```
</details>

### 19. `shell` +246s – completed

```
cd <repo> && bin/tl-validate output/work/fall-d8f463c9.json 2>&1
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 12 tracks (12 with duration), 5 sources, 14 conflicts, confidence=0.85
```
</details>

> **Agent** +251s: FERTIG found 12 Tracks confidence=0.85
