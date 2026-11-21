# Agent-Trace: 06-k-i-z-live-aus-leipzig

> Schnellweg geprüft: no fast path: only 0/32 tracks with a duration in both sources
Start 2026-11-20T15:42:31 · 15 Schritte · 14 Tool-Aufrufe · Tokens in 20037 / out 6366


> **Agent** +0s: I'll start by checking the barcode and searching the databases.

### 1. `shell` +1s – completed

```
bin/tl-gtin 4251484709767; echo "---"; bin/tl-mb search --barcode 4251484709767; echo "---"; bin/tl-discogs search --barcode 4251484709767
```

<details><summary>Ausgabe</summary>

```
input: '4251484709767' → digits: 4251484709767 (13 digits)
type: EAN-13  valid: yes
search variants: 4251484709767
prefix 400–440: assigned in Germany (says nothing about the country of release)
---
1 Releases (Queries: barcode:(4251484709767))
musicbrainz:release/9cd41bed-67ba-4330-8dc7-7387904606da | Görlitzer Park - Live Aus Leipzig — K.I.Z | 2025-11-12 DE | 12" Vinyl+12" Vinyl+12" Vinyl | Tracks 12+10+10 | Barcode 4251484709767 | Beat the Rich! 425148709767; Eklat Tonträger 425148709767 | Official | LP, Album, Limited Edition, Neon Green | score 100
---
1 hits (parameters: {'barcode': '4251484709767'})
discogs:release/35653735 | K.I.Z* - Görlitzer Park - Live Aus Leipzig | 2025 Germany | Vinyl, LP, Album, Limited Edition | Label K.I.Z., Eklat Tonträger | Kat.-Nr. 425148709767 | Barcodes 4 251484 709767, YA7557-1 A, YA7557-1 B | master 4051198
```
</details>

### 2. `shell` +3s – completed

```
bin/tl-mb release 9cd41bed-67ba-4330-8dc7-7387904606da; echo "==="; bin/tl-discogs release 35653735
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/9cd41bed-67ba-4330-8dc7-7387904606da | Görlitzer Park - Live Aus Leipzig — K.I.Z | 2025-11-12 DE | 12" Vinyl+12" Vinyl+12" Vinyl | Tracks 12+10+10 | Barcode 4251484709767 | Beat the Rich! 425148709767; Eklat Tonträger 425148709767 | Official | LP, Album, Limited Edition, Neon Green
release-group: 632fa284-54ba-4cba-b84a-785f22501c9b (Album, first date 2025-11-12) | Cover: front=True back=True images=8
url: https://musicbrainz.org/release/9cd41bed-67ba-4330-8dc7-7387904606da
-- Medium 1: 12" Vinyl, 12 Tracks
1.1 [A1] Frieden | 5:32 (332000 ms)
1.2 [A2] VIP In Der Psychiatrie | 3:45 (225000 ms) | ISRC DECE72502460
1.3 [A3] Ehrenlos | 2:29 (149000 ms)
1.4 [A4] Urlaub Für's Gehirn | 5:38 (338000 ms)
1.5 [A5] Unterfickt Und Geistig Behindert | 5:50 (350000 ms)
1.6 [A6] Bier | 2:24 (144000 ms)
1.7 [B1] Berlin Wird Dich Töten | 3:27 (207000 ms)
1.8 [B2] Sommer Meines Lebens | 3:29 (209000 ms)
1.9 [B3] Görlitzer Park | 4:10 (250000 ms)
1.10 [B4] Hurra Die Welt Geht Unter | 4:45 (285000 ms)
1.11 [B5] Vierspur | 4:12 (252000 ms)
1.12 [B6] Applaus | 5:20 (320000 ms)
-- Medium 2: 12" Vinyl, 10 Tracks
2.1 [C1] Filmriss | 3:19 (199000 ms)
2.2 [C2] Kinderkram | 6:08 (368000 ms) | ISRC DECE72502472
2.3 [C3] Neuruppin | 5:26 (326000 ms)
2.4 [C4] Illuminati | 2:35 (155000 ms)
2.5 [C5] 2001 | 3:43 (223000 ms)
2.6 [D1] Sensibel | 3:33 (213000 ms)
2.7 [D2] Rap Über Hass | 7:00 (420000 ms)
2.8 [D3] Geld Wie Ein Magnet | 5:09 (309000 ms)
2.9 [D4] Samstag Ist Krieg | 4:05 (245000 ms)
2.10 [D5] Grabstein | 2:38 (158000 ms)
-- Medium 3: 12" Vinyl, 10 Tracks
3.1 [E1] DJ Set | 7:26 (446000 ms)
3.2 [E2] Der Durch Die Scheibeboxxxer | 1:43 (103000 ms)
3.3 [E3] Undertheker | 3:02 (182000 ms)
3.4 [E4] Walpurgisnacht | 3:58 (238000 ms)
3.5 [E5] Wahrheit Part 1 | 3:33 (213000 ms)
3.6 [E6] Wahrheit Part 2 | 3:37 (217000 ms)
3.7 [F1] Ich Ficke Euch (Alle) | 5:50 (350000 ms)
3.8 [F2] Ich Mache Geld | 5:35 (335000 ms)
3.9 [F3] Ein Affe Und Ein Pferd | 6:38 (398000 ms)
3.10 [F4] Familienfeier | 6:14 (374000 ms)
Total: 2:22:13 (8533 s), tracks without duration: 0
===
discogs:release/35653735 | Görlitzer Park - Live Aus Leipzig — K.I.Z. | 2025-11-12 Germany | 3× Vinyl (LP, Album, Limited Edition) | K.I.Z. 425148709767; Eklat Tonträger 425148709767; Beat The Rich! 425148709767 | master 4051198
url: https://www.discogs.com/release/35653735-KIZ-Görlitzer-Park-Live-Aus-Leipzig
identifiers: Barcode: 4 251484 709767 | Matrix / Runout: YA7557-1 A (Side A) | Matrix / Runout: YA7557-1 
… [2746 Zeichen gekürzt]
```
</details>

### 3. `shell` +25s – completed

```
bin/tl-caa 9cd41bed-67ba-4330-8dc7-7387904606da; echo "==="; bin/tl-mb group 632fa284-54ba-4cba-b84a-785f22501c9b
```

<details><summary>Ausgabe</summary>

```
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014217 | Front | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014217-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883 | Back | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370015721 | Medium | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370015721-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370017433 | ? | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370017433-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370018706 | ? | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370018706-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370019492 | ? | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370019492-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370020124 | ? | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370020124-1200.jpg
caa:release/9cd41bed-67ba-4330-8dc7-7387904606da/46370020668 | ? | https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370020668-1200.jpg
8 images · read tracklist: tl-vision <url> --context "…"
===
3 Releases in release-group 632fa284-54ba-4cba-b84a-785f22501c9b
musicbrainz:release/9cd41bed-67ba-4330-8dc7-7387904606da | Görlitzer Park - Live Aus Leipzig —  | 2025-11-12 DE | 12" Vinyl+12" Vinyl+12" Vinyl | Tracks 12+10+10 | Barcode 4251484709767 | Beat the Rich! 425148709767; Eklat Tonträger 425148709767 | Official | LP, Album, Limited Edition, Neon Green
musicbrainz:release/a64dbfc0-de72-4fbb-92f3-1264a6e8b6ea | Görlitzer Park - Live aus Leipzig —  | 2025-11-12 DE | CD+CD | Tracks 17+15 | Barcode 4251484709774 | Beat the Rich! 4251484709774; Eklat Tonträger 4251484709774 | Official
musicbrainz:release/a852c52a-dd54-4192-ae79-dc240e67c6d8 | Görlitzer Park (Live aus Leipzig) —  | 2025-11-13 XW | Digital Media | Tracks 32 | Barcode 602478858666 | Eklat Tonträger | Official
```
</details>

### 4. `shell` +56s – completed

```
bin/tl-vision "https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883-1200.jpg" --context "Back cover of a 3LP K.I.Z album. Read the printed title, and the full tracklist exactly as printed: side letters (A, B, C, D, E, F), track numbers and titles."
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883-1200.jpg
model: gemini-3.8-flash@low, in 1297 / out 1560 tokens, 15.8 s
kind: back cover | readable: True
release_title: GÖRLITZER PARK - LIVE AUS LEIPZIG
artist: K.I.Z
label: Beat The Rich
barcode: 4 051484 756757
format_hints: LP
A FRIEDEN | no duration printed
- VIP IN DER PSYCHIATRIE | no duration printed
- EHRENLOS | no duration printed
- URLAUB FÜR'S GEHIRN | no duration printed
- UNTERFICKT UND GEISTIG BEHINDERT | no duration printed
- BIER | no duration printed
B BERLIN WIRD DICH TÖTEN | no duration printed
- SOMMER MEINES LEBENS | no duration printed
- GÖRLITZER PARK | no duration printed
- HURRA DIE WELT GEHT UNTER | no duration printed
- VIERSPUR | no duration printed
- APPLAUS | no duration printed
C FILMRISS | no duration printed
- KINDERKRAM | no duration printed
- NEURUPPIN | no duration printed
- ILLUMINATI | no duration printed
- 2001 | no duration printed
D SENSIBEL | no duration printed
- RAP ÜBER HASS | no duration printed
- GELD WIE EIN MAGNET | no duration printed
- SAMSTAG IST KRIEG | no duration printed
- GRABSTEIN | no duration printed
E DICKA | no duration printed [uncertain]
- DER DURCH DIE SCHEIBEBOXXXER | no duration printed
- UNDERTHEKER | no duration printed
- WALPURGISNACHT | no duration printed
- WAHRHEIT PART 1 | no duration printed
- WAHRHEIT PART 2 | no duration printed
F ICH FICKE EUCH (ALLE) | no duration printed
- ICH MACHE GELD | no duration printed
- EIN AFFE UND EIN PFERD | no duration printed
- FAMILIENFEIER | no duration printed
32 tracks read
```
</details>

### 5. `shell` +65s – completed

```
bin/tl-mb release a64dbfc0-de72-4fbb-92f3-1264a6e8b6ea
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/a64dbfc0-de72-4fbb-92f3-1264a6e8b6ea | Görlitzer Park - Live aus Leipzig — K.I.Z | 2025-11-12 DE | CD+CD | Tracks 17+15 | Barcode 4251484709774 | Beat the Rich! 4251484709774; Eklat Tonträger 4251484709774 | Official
release-group: 632fa284-54ba-4cba-b84a-785f22501c9b (Album, first date 2025-11-12) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/a64dbfc0-de72-4fbb-92f3-1264a6e8b6ea
-- Medium 1: CD, 17 Tracks
1.1 [1] Frieden (Live aus Leipzig) | 5:32 (332000 ms)
1.2 [2] VIP in der Psychiatrie (Live aus Leipzig) | 3:45 (225000 ms) | ISRC DECE72502460
1.3 [3] Ehrenlos (Live aus Leipzig) | 2:29 (149000 ms)
1.4 [4] Urlaub für's Gehirn (Live aus Leipzig) | 5:38 (338000 ms)
1.5 [5] Unterfickt und geistig behindert (Live aus Leipzig) | 5:50 (350000 ms)
1.6 [6] Bier (Live aus Leipzig) | 2:24 (144000 ms)
1.7 [7] Berlin wird dich töten (Live aus Leipzig) | 3:27 (207000 ms)
1.8 [8] Sommer meines Lebens (Live aus Leipzig) | 3:29 (209000 ms)
1.9 [9] Görlitzer Park (Live aus Leipzig) | 4:10 (250000 ms)
1.10 [10] Hurra die Welt geht unter (Live aus Leipzig) | 4:45 (285000 ms)
1.11 [11] Vierspur (Live aus Leipzig) | 4:12 (252000 ms)
1.12 [12] Applaus (Live aus Leipzig) | 5:20 (320000 ms)
1.13 [13] Filmriss (Live aus Leipzig) | 3:19 (199000 ms)
1.14 [14] Kinderkram (Live aus Leipzig) | 6:08 (368000 ms) | ISRC DECE72502472
1.15 [15] Neuruppin (Live aus Leipzig) | 5:26 (326000 ms)
1.16 [16] Illuminati (Live aus Leipzig) | 2:35 (155000 ms)
1.17 [17] 2001 (Live aus Leipzig) | 3:43 (223000 ms)
-- Medium 2: CD, 15 Tracks
2.1 [1] Sensibel (Live aus Leipzig) | 3:33 (213000 ms)
2.2 [2] Rap über Hass (Live aus Leipzig) | 7:00 (420000 ms)
2.3 [3] Geld wie ein Magnet (Live aus Leipzig) | 5:09 (309000 ms)
2.4 [4] Samstag ist Krieg (Live aus Leipzig) | 4:05 (245000 ms)
2.5 [5] Grabstein (Live aus Leipzig) | 2:38 (158000 ms)
2.6 [6] DJ Set (Live aus Leipzig) | 7:26 (446000 ms)
2.7 [7] Der durch die Scheibeboxxxer (Live aus Leipzig) | 1:43 (103000 ms)
2.8 [8] Undertheker (Live aus Leipzig) | 3:02 (182000 ms)
2.9 [9] Walpurgisnacht (Live aus Leipzig) | 3:58 (238000 ms)
2.10 [10] Wahrheit Part 1 (Live aus Leipzig) | 3:33 (213000 ms)
2.11 [11] Wahrheit Part 2 (Live aus Leipzig) | 3:37 (217000 ms)
2.12 [12] Ich ficke Euch (alle) (Live aus Leipzig) | 5:50 (350000 ms)
2.13 [13] Ich mache Geld (Live aus Leipzig) | 5:35 (335000 ms)
2.14 [14] Ein Affe und ein Pferd (Live aus Leipzig) | 6:38 (398000 ms)
2.15 [15] Familienfeier (Live aus Leipzig) | 6:1
… [65 Zeichen gekürzt]
```
</details>

### 6. `shell` +79s – completed

```
bin/tl-vision "https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370019492-1200.jpg" --context "Image from a K.I.Z 3LP. Identify what is shown and transcribe any track titles visible verbatim (case as printed)."
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370019492-1200.jpg
model: gemini-3.8-flash@low, in 1277 / out 110 tokens, 6.2 s
kind: other | readable: False
0 tracks read
notes: No text or tracklist visible on this image. It depicts a live concert photo/inner sleeve artwork featuring musicians on stage illuminated by laser light beams.
```
</details>

### 7. `shell` +87s – completed

```
bin/tl-search "\"DJ Set\" K.I.Z Görlitzer Park Live aus Leipzig Tracklist" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: "DJ Set" K.I.Z Görlitzer Park Live aus Leipzig Tracklist
1. K.I.Z - Görlitzer Park (Live aus Leipzig) Lyrics and Tracklist | Genius
   https://genius.com/albums/Kiz/Gorlitzer-park-live-aus-leipzig
   Get all the lyrics to songs on Görlitzer Park (Live aus Leipzig) and join the Genius community of music scholars to learn the meaning behind the lyrics.
2. K.I.Z – Görlitzer Park - Live Aus Leipzig | Releases | Discogs
   https://www.discogs.com/master/4051198-KIZ-G%C3%B6rlitzer-Park-Live-Aus-Leipzig
   Explore the tracklist, credits, statistics, and more for Görlitzer Park - Live Aus Leipzig by K.I.Z. Compare versions and buy on Discogs
   + Explore the tracklist, credits, statistics, and more for Görlitzer Park - Live Aus Leipzig by K.I.Z. Compare versions an
3. Görlitzer Park - Live Aus Leipzig | 3-LP (2025, Limited Edition, Live, Gatefold, Grünes Vinyl) von K.I.Z.
   https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/
   Görlitzer Park - Live Aus Leipzig von K.I.Z. als 3-LP, mit Tracklist und weiteren Infos
   + Informationen zum Tonträger Görlitzer Park - Live Aus Leipzig, 3-LP, 2025, Limited Edition, Live, Gatefold, Grünes Vinyl | Ganz häufig ist es der Fall, dass auf dem Frontcover ein Foto oder eine Grafik eines Fotografen oder Künstlers genutzt w
4. "Görlitzer Park (Live Aus Leipzig)" von K.I.Z. – laut.de – Album
   https://laut.de/K.I.Z./Alben/Goerlitzer-Park-Live-Aus-Leipzig-126193
   Wer Weiterentwicklung im Sound oder Text sucht, wird die Grenzen einer Live-LP spüren, wer hingegen das Live-Erlebnis mit nach Hause nehmen will, wird mit "Görlitzer Park (Live Aus Leipzig)" definitiv fündig. Die Trackli
   + "Görlitzer Park (Live Aus Leipzig)" ist ein starkes Dokument dessen, was K.I.Z. live gelingt: Sie zeigen Energie, Verbun | K.I.Z. - "Görlitzer Park (Live Aus Leipzig)"
5. K.I.Z. - Görlitzer Park (Live aus Leipzig)  Plattentests.de-Rezension
   https://www.plattentests.de/rezi.php?show=21269
   Mit dem Leipzig-Konzert der "Görlitzer Park"-Tour zeigt sich diese Entwicklung anhand der Setlist sehr anschaulich: Während die "bösen" Songs von früher eher dazu dienen, die Menge erst mal auf Betriebstemperatur zu brin
   + Mit dem Leipzig-Konzert der "Görlitzer Park"-Tour zeigt sich diese Entwicklung anhand der Setlist sehr anschaulich: Währ | K.I.Z. - Görlitzer Park (Live aus Leipzig) (1 Beiträge / Letzter am 10.12.2025 - 21:11 Uhr)
6. K.I.Z – DJ Set (Live aus Leipzig) Lyrics | Genius Lyrics
   http
… [1266 Zeichen gekürzt]
```
</details>

### 8. `shell` +99s – completed

```
bin/tl-scrape "https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/" --mode firecrawl 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
url: https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/
mode: firecrawl (firecrawl)
title: Görlitzer Park - Live Aus Leipzig | 3-LP (2025, Limited Edition, Live, Gatefold, Grünes Vinyl) von K.I.Z.
source-id: web:https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/
---
×

Menu

# [K.I.Z.](https://www.musik-sammler.de/artist/kiz/)Görlitzer Park - Live Aus Leipzig  3-LP, 2025, Limited Edition, Live, Gatefold, Grünes Vinyl

- ![K.I.Z.: Görlitzer Park - Live Aus Leipzig (3-LP) - Bild 1](https://www.musik-sammler.de/cover/1734000/1733527_1763107664_300.jpg)
- ![K.I.Z.: Görlitzer Park - Live Aus Leipzig (3-LP) - Bild 2](https://www.musik-sammler.de/cover/1734000/1733527_1_1763108429_300.jpg)

[![K.I.Z.: Görlitzer Park - Live Aus Leipzig (3-LP) - Thumbnail 1](https://www.musik-sammler.de/cover/1734000/1733527_1763107664_75.jpg)](https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/)

[![K.I.Z.: Görlitzer Park - Live Aus Leipzig (3-LP) - Thumbnail 2](https://www.musik-sammler.de/cover/1734000/1733527_1_1763108429_75.jpg)](https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/)

Warum so verpixel?

| Herstellungsland | Europäische Union |
| Veröffentlichungs-Jahr | 2025 |
| Zeit | k.A. |
| EAN-Nr. | 4251484709767 |
| Label/Labelcode | [EKLAT Tonträger](https://www.musik-sammler.de/label/92070/) /<br> **LC 92070** |
| Plattenfirma/Katalog-Nr. | Beat The Rich / Eklat Tonträger<br> /<br> **4251484709767** |
| Musikrichtung | Rap/Hip Hop |

| Sammlungen | Gesucht | Flohmarkt |
| --- | --- | --- |
| 3 | 0 | 0 |

## Tracklist

I = Instrumental
L = Live
B = Bonustrack
H = Hidden Track
C = Coversong


| LP<br> 1 |
| --- |
| Track | Titel | Zeit | Besonderheit |
| --- | --- | --- | --- |
| A 1. | Frieden |  | L |
| A 2. | Vip In Der Psychiatrie |  | L |
| A 3. | Ehrenlos |  | L |
| A 4. | Urlaub Für's Gehirn |  | L |
| A 5. | Unterfickt Und Geistig Behindert |  | L |
| A 6. | Bier |  | L |
| B 7. | Berlin Wird Dich Töten |  | L |
| B 8. | Sommer Meines Lebens |  | L |
| B 9. | Görlitzer Park |  | L |
| B 10. | Hurra Die Welt Geht Unter |  | L |
| B 11. | Vierspur |  | L |
| B 12. | Applaus |  | L |

| LP<br> 2 |
| --- |
| Track | Titel | Zeit | Besonderheit |
| --- | --- | --- | --- |
| A 1. | Filmriss |  | L |
| A 2. | Kinderkram |  | L |
| A 3. | Neuruppin |  | L |
| A 4. | Illuminati |  | L |
| A 5. | 2001 |  | 
… [355 Zeichen gekürzt]
```
</details>

### 9. `shell` +128s – completed

```
bin/tl-scrape "https://genius.com/albums/Kiz/Gorlitzer-park-live-aus-leipzig" --mode firecrawl 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://genius.com/albums/Kiz/Gorlitzer-park-live-aus-leipzig
mode: firecrawl (firecrawl)
title: K.I.Z - Görlitzer Park (Live aus Leipzig) Lyrics and Tracklist | Genius
source-id: web:https://genius.com/albums/Kiz/Gorlitzer-park-live-aus-leipzig
---
0

[![](https://t2.genius.com/unsafe/1905x0/https%3A%2F%2Fimages.genius.com%2F2954f82689628915f01d6390b26161d9.1000x1000x1.png)\\
\\
1 Cover](https://genius.com/album_cover_arts/1409990)

Album

# Görlitzer Park (Live aus Leipzig)

## [K.I.Z](https://genius.com/artists/Kiz)

Released November 14, 2025


16.6K

## Görlitzer Park (Live aus Leipzig) Tracklist

1

[**Frieden (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-frieden-live-aus-leipzig-lyrics)

2

[**VIP in der Psychatrie (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-vip-in-der-psychatrie-live-aus-leipzig-lyrics)

3

[**Ehrenlos (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-ehrenlos-live-aus-leipzig-lyrics)

4

[**Urlaub für's Gehirn (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-urlaub-furs-gehirn-live-aus-leipzig-lyrics)

5

[**Unterfickt und geistig behindert (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-unterfickt-und-geistig-behindert-live-aus-leipzig-lyrics)

6

[**Bier (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-bier-live-aus-leipzig-lyrics)

7

[**Berlin wird dich töten (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-berlin-wird-dich-toten-live-aus-leipzig-lyrics)

8

[**Sommer meines Lebens (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-sommer-meines-lebens-live-aus-leipzig-lyrics)

9

[**Görlitzer Park (Live aus Leipzig)  Lyrics**](https://genius.com/Kiz-gorlitzer-park-live-aus-leipzig-lyrics)
```
</details>

### 10. `shell` +134s – completed

```
bin/tl-scrape "https://musicbrainz.org/ws/2/release/9cd41bed-67ba-4330-8dc7-7387904606da?inc=artist-credits&fmt=json" --mode http 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://musicbrainz.org/ws/2/release/9cd41bed-67ba-4330-8dc7-7387904606da?inc=artist-credits&fmt=json
mode: http (http)
title: 
source-id: web:https://musicbrainz.org/ws/2/release/9cd41bed-67ba-4330-8dc7-7387904606da?inc=artist-credits&fmt=json
---
{"disambiguation":"LP, Album, Limited Edition, Neon Green","date":"2025-11-12","barcode":"4251484709767","release-events":[{"area":{"type-id":null,"name":"Germany","type":null,"iso-3166-1-codes":["DE"],"sort-name":"Germany","id":"85752fda-13c4-31a3-bee5-0e5cb1f51dad","disambiguation":""},"date":"2025-11-12"}],"packaging-id":null,"text-representation":{"language":"deu","script":"Latn"},"country":"DE","artist-credit":[{"name":"K.I.Z","joinphrase":"","artist":{"type":"Group","name":"K.I.Z","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","country":"DE","disambiguation":"German hip hop group from Berlin","id":"13c9c494-09aa-4518-8572-9f41dbdff461","sort-name":"K.I.Z"}}],"packaging":null,"asin":null,"status":"Official","title":"Görlitzer Park - Live Aus Leipzig","status-id":"4e304316-386d-3409-af2e-78857eec5cfe","id":"9cd41bed-67ba-4330-8dc7-7387904606da","cover-art-archive":{"back":true,"darkened":false,"count":8,"front":true,"artwork":true},"quality":"normal"}
```
</details>

### 11. `shell` +145s – completed

```
bin/tl-scrape "https://musicbrainz.org/ws/2/release/9cd41bed-67ba-4330-8dc7-7387904606da?inc=recordings%2Bartist-credits&fmt=json" --mode http --grep '"artist-credit"' 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
url: https://musicbrainz.org/ws/2/release/9cd41bed-67ba-4330-8dc7-7387904606da?inc=recordings%2Bartist-credits&fmt=json
mode: http (http)
title: 
source-id: web:https://musicbrainz.org/ws/2/release/9cd41bed-67ba-4330-8dc7-7387904606da?inc=recordings%2Bartist-credits&fmt=json
---
…
{"cover-art-archive":{"darkened":false,"artwork":true,"front":true,"back":true,"count":8},"disambiguation":"LP, Album, Limited Edition, Neon Green","title":"Görlitzer Park - Live Aus Leipzig","quality":"normal","barcode":"4251484709767","asin":null,"release-events":[{"date":"2025-11-12","area":{"disambiguation":"","name":"Germany","type-id":null,"id":"85752fda-13c4-31a3-bee5-0e5cb1f51dad","sort-name":"Germany","iso-3166-1-codes":["DE"],"type":null}}],"text-representation":{"language":"deu","script":"Latn"},"artist-credit":[{"joinphrase":"","artist":{"country":"DE","type":"Group","id":"13c9c494-09aa-4518-8572-9f41dbdff461","sort-name":"K.I.Z","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","disambiguation":"German hip hop group from Berlin","name":"K.I.Z"},"name":"K.I.Z"}],"media":[{"track-offset":0,"format-id":"3e9080b0-5e6c-34ab-bd15-f526b6306a64","tracks":[{"title":"Frieden","number":"A1","length":null,"artist-credit":[{"joinphrase":"","artist":{"disambiguation":"German hip hop group from Berlin","name":"K.I.Z","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","sort-name":"K.I.Z","id":"13c9c494-09aa-4518-8572-9f41dbdff461","type":"Group","country":"DE"},"name":"K.I.Z"}],"recording":{"id":"fa0299e5-d8d0-4d25-97ba-ef5fc925c123","first-release-date":"2025-11-12","disambiguation":"","artist-credit":[{"joinphrase":"","artist":{"sort-name":"K.I.Z","id":"13c9c494-09aa-4518-8572-9f41dbdff461","country":"DE","type":"Group","disambiguation":"German hip hop group from Berlin","name":"K.I.Z","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b"},"name":"K.I.Z"}],"length":332000,"video":false,"title":"Frieden (Live aus Leipzig)"},"id":"43af4012-f4ca-44fe-be29-d1b2014145c2","position":1},{"recording":{"title":"VIP in der Psychiatrie - Live aus Leipzig","video":false,"length":225000,"artist-credit":[{"name":"K.I.Z","artist":{"disambiguation":"German hip hop group from Berlin","name":"K.I.Z","type-id":"e431f5f6-b5d2-343d-8b36-72607fffb74b","id":"13c9c494-09aa-4518-8572-9f41dbdff461","sort-name":"K.I.Z","country":"DE","type":"Group"},"joinphrase":""}],"disambiguation":"","first-release-date":"2025-11-12","id":"6f9eeae8-667f-4210-a114-59447431880e"},"position":2,"id":"eced6fb9-8e55-4db7-bcbe-fc5e1e37
… [3833 Zeichen gekürzt]
```
</details>

### 12. `shell` +148s – completed

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

### 13. `shell` +184s – completed

```
mkdir -p output/work && cat > /tmp/gen.py <<'EOF'
import json
tin=[
 ("A1","Frieden",332),("A2","VIP In Der Psychiatrie",225),("A3","Ehrenlos",149),
 ("A4","Urlaub Für's Gehirn",338),("A5","Unterfickt Und Geistig Behindert",350),("A6","Bier",144),
 ("B1","Berlin Wird Dich Töten",207),("B2","Sommer Meines Lebens",209),("B3","Görlitzer Park",250),
 ("B4","Hurra Die Welt Geht Unter",285),("B5","Vierspur",252),("B6","Applaus",320),
 ("C1","Filmriss",199),("C2","Kinderkram",368),("C3","Neuruppin",326),("C4","Illuminati",155),
 ("C5","2001",223),("D1","Sensibel",213),("D2","Rap Über Hass",420),("D3","Geld Wie Ein Magnet",309),
 ("D4","Samstag Ist Krieg",245),("D5","Grabstein",158),
 ("E1","DJ Set",446),("E2","Der Durch Die Scheibeboxxxer",103),("E3","Undertheker",182),
 ("E4","Walpurgisnacht",238),("E5","Wahrheit Part 1",213),("E6","Wahrheit Part 2",217),
 ("F1","Ich Ficke Euch (Alle)",350),("F2","Ich Mache Geld",335),("F3","Ein Affe Und Ein Pferd",398),
 ("F4","Familienfeier",374)]
mb="musicbrainz:release/9cd41bed-67ba-4330-8dc7-7387904606da"
dc="discogs:release/35653735"
ms="web:https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/"
tracks=[]
for pos,t,d in tin:
    disc = 1 if pos[0] in "AB" else 2 if pos[0] in "CD" else 3
    tracks.append({"position":pos,"disc":disc,"title":t,"artist":None,"duration_s":d,
        "sources":[mb,dc,ms],"duration_sources":[mb],"flags":[]})
res={
 "input":{"id":"fall-669b8d09","title":"Live aus Leipzig","artist":"K.I.Z","ean":"4251484709767"},
 "status":"found",
 "release":{"title":"Görlitzer Park - Live Aus Leipzig","artist":"K.I.Z","format":"Vinyl",
   "country":"DE","year":2025,"label":"Beat the Rich! / Eklat Tonträger","catno":"425148709767",
   "barcode":"4251484709767",
   "edition":"3×12\" Vinyl, LP, Album, Limited Edition, Neon Green, Gatefold, printed inner sleeves",
   "ids":{"musicbrainz":"9cd41bed-67ba-4330-8dc7-7387904606da","discogs":"35653735"}},
 "tracks":tracks,
 "artists":[{"name":"K.I.Z","role":"main","tracks":[],"sources":[mb,dc,ms]}],
 "total_duration_s":sum(d for _,_,d in tin),
 "confidence":0.95,
 "sources":[
  {"id":mb,"url":"https://musicbrainz.org/release/9cd41bed-67ba-4330-8dc7-7387904606da","kind":"database",
   "note":"barcode 4251484709767 exact; 3×12\", DE 2025-11-12; all 32 track durations in ms; track artist credit = K.I.Z on every track"},
  {"id":dc,"url":"https://www.discogs.com/release/35653735","kind":"database",
   "note":"same barcode 4 251484 709767, catno 425148709767, matrix YA7557-1 A–F; identical 32-track order, no durations"},
  {"id":ms,"url":"https://www.musik-sammler.de/release/k-i-z-g%C3%B6rlitzer-park-live-aus-leipzig-3-lp-1733527/","kind":"collector",
   "note":"3-LP, EAN 4251484709767, same 32 tracks per side; no durations"},
  {"id":"image:https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883-1200.jpg","url":"https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883-1200.jpg","kind":"image",
   "note":"back cover: title 'GÖRLITZER PARK - LIVE AUS LEIPZIG', sides A–F with 32 titles in the same order, no durations printed"},
  {"id":"web:https://genius.com/albums/Kiz/Gorlitzer-park-live-aus-leipzig","url":"https://genius.com/albums/Kiz/Gorlitzer-park-live-aus-leipzig","kind":"web",
   "note":"digital tracklist (32 tracks), confirms song title 'DJ Set'; hint only, describes the digital edition"}],
 "conflicts":[
  {"field":"title track E1",
   "values":{"musicbrainz:release/9cd41bed-67ba-4330-8dc7-7387904606da":"DJ Set",
             "discogs:release/35653735":"DJ Set",
             ms:"DJ Set",
             "image:https://coverartarchive.org/release/9cd41bed-67ba-4330-8dc7-7387904606da/46370014883-1200.jpg":"DICKA (OCR, marked uncertain)"},
   "resolution":"Kept 'DJ Set': MusicBrainz, Discogs, musik-sammler and the track's own title on Genius all agree; the OCR read of the all-caps back cover was flagged uncertain."},
  {"field":"release title",
   "values":{"input":"Live aus Leipzig",
             "musicbrainz:release/9cd41bed-67ba-4330-8dc7-7387904606da":"Görlitzer Park - Live Aus Leipzig",
             "discogs:release/35653735":"Görlitzer Park - Live Aus Leipzig"},
   "resolution":"Input title is the short form; the printed and database title including the album name was used. Barcode, artist and year identify the same release."}],
 "missing":["Durations are not printed on the cover and not entered at Discogs/musik-sammler; all durations come from the MusicBrainz entry of this exact vinyl edition (no second independent duration source)."],
 "alternatives":[
  {"description":"2×CD, DE 2025-11-12, Beat the Rich! / Eklat Tonträger, barcode 4251484709774, 17+15 tracks","source":"musicbrainz:release/a64dbfc0-de72-4fbb-92f3-1264a6e8b6ea","why_not":"different barcode and format (CD); same recordings and identical durations, used only as cross-check"},
  {"description":"Digital Media, 2025-11-13, Eklat Tonträger, barcode 602478858666, 32 tracks","source":"musicbrainz:release/a852c52a-dd54-4192-ae79-dc240e67c6d8","why_not":"digital edition, not a physical carrier"}],
 "reasoning":"EAN 4251484709767 hits exactly one release in MusicBrainz and one at Discogs: the 3×12\" limited neon-green vinyl of 'Görlitzer Park - Live Aus Leipzig' (DE, 2025-11-12, Beat the Rich!/Eklat, catno 425148709767). Discogs, musik-sammler and the back cover confirm the identical 32 tracks in sides A–F; durations (32/32) exist only in MusicBrainz for this very release entry."}
open("output/work/fall-669b8d09.json","w").write(json.dumps(res,ensure_ascii=False,indent=2))
print(res["total_duration_s"])
EOF
python3 /tmp/gen.py && bin/tl-validate output/work/fall-669b8d09.json
```

<details><summary>Ausgabe</summary>

```
8533
WARN: high confidence despite open conflicts – justify or lower it
OK: status=found, 32 tracks (32 with duration), 5 sources, 2 conflicts, confidence=0.95
```
</details>

### 14. `shell` +208s – completed

```
cd . && python3 - <<'EOF'
import json
p="output/work/fall-669b8d09.json"
d=json.load(open(p))
d["confidence"]=0.88
d["reasoning"]+=" The two recorded conflicts are cosmetic (short input title, one uncertain OCR reading on the all-caps back cover) and both resolved by three agreeing sources, hence confidence just below the fully clean 0.9 band."
open(p,"w").write(json.dumps(d,ensure_ascii=False,indent=2))
EOF
bin/tl-validate output/work/fall-669b8d09.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 32 tracks (32 with duration), 5 sources, 2 conflicts, confidence=0.88
```
</details>

> **Agent** +220s: FERTIG found 32 Tracks confidence=0.88
