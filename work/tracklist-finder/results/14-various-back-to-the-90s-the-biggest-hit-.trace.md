# Agent-Trace: 14-various-back-to-the-90s-the-biggest-hit-

> Schnellweg geprüft: no fast path: 0 matching official MusicBrainz releases (fast path only for 1–5 identical ones)
Start 2026-11-20T15:48:21 · 17 Schritte · 26 Tool-Aufrufe · Tokens in 34794 / out 18975


> **Agent** +1s: I'll start by checking the barcode and searching the databases.

### 1. `shell` +1s – completed

```
bin/tl-gtin 4005902510288
```

<details><summary>Ausgabe</summary>

```
input: '4005902510288' → digits: 4005902510288 (13 digits)
type: EAN-13  valid: yes
search variants: 4005902510288
prefix 400–440: assigned in Germany (says nothing about the country of release)
```
</details>

### 2. `shell` +1s – completed

```
bin/tl-discogs search --barcode 4005902510288
```

<details><summary>Ausgabe</summary>

```
1 hits (parameters: {'barcode': '4005902510288'})
discogs:release/30190112 | Various - Back To The 90s – The Biggest Hit Collection | ? Unknown | CD, Compilation | Label Pink Revolver | Kat.-Nr. 264.2475.2 | Barcodes 4005902510288 | master -
```
</details>

### 3. `shell` +1s – completed

```
bin/tl-mb search --barcode 4005902510288
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: barcode:(4005902510288))
```
</details>

### 4. `shell` +5s – completed

```
bin/tl-discogs release 30190112
```

<details><summary>Ausgabe</summary>

```
discogs:release/30190112 | Back To The 90s – The Biggest Hit Collection — Various | 0 None | 2× CD (Compilation) | Pink Revolver 264.2475.2 | master -
url: https://www.discogs.com/release/30190112-Various-Back-To-The-90s-The-Biggest-Hit-Collection
identifiers: Barcode: 4005902510288
1-1 Rhythm Is A Dancer (7" Edit) — Snap! | duration missing
1-2 Freed From Desire — Gala | duration missing
1-3 Saturday Night — Whigfield | duration missing
1-4 Samba De Janeiro — Bellini | duration missing
1-5 I Like To Move It (Erick "More" Club Mix) — Reel 2 Real, The Mad Stuntman | duration missing | credits: Remix: Erick Morillo
1-6 Satisfaction — Benny Benassi, The Biz (5) | duration missing
1-7 Coco Jamboo (Radio Edit) — Mr. President | duration missing
1-8 Hardcore Vibes (Video Mix) — Dune (3) | duration missing
1-9 It's My Life (Radio Edit) — Dr. Alban | duration missing
1-10 Toca Me (Radio Cut) — Fragma | duration missing
1-11 Komodo (Radio Mix) — Mauro Picotto | duration missing
1-12 Show Me Love (Stonebridge Radio Edit) — Robin S. | duration missing | credits: Remix: StoneBridge
1-13 The Theme (Of Progressive Attack) (Trip Mix Radio Edit) — Brooklyn Bounce | duration missing
1-14 Where Are You (Radio Edit) — Paffendorf | duration missing
1-15 Hard To Say I'm Sorry (Original Radio Edit) — Aquagen | duration missing
1-16 I Believe (Radio Edit) — Celvin Rotane | duration missing
1-17 Why Don't You Dance With Me? (Radio Edit) — Future Breeze | duration missing
1-18 Pizza (Radio Cut) — Shaun Baker | duration missing
1-19 Another Day In Paradise (Edit) — Jam Tronik | duration missing
1-20 Got The Groove (Sm Radio Edit) — SM-Trax | duration missing
2-1 L'amour Toujours — Gigi D'Agostino | duration missing
2-2 I Wanna Be A Hippy — Technohead | duration missing
2-3 Ecuador (Original Radio Edit) — Sash! | duration missing
2-4 King Of My Castle (Roy Malone Kings Mix Edit) — Wamdue Project | duration missing | credits: Remix: Roy Malone
2-5 Free (Mood II Swing Radio Edit) — Ultra Naté | duration missing
2-6 Sonic Empire (Short Mix) — Members Of Mayday | duration missing
2-7 Children (Dream Version Special Radio Edit) — Robert Miles | duration missing
2-8 The Bomb (These Sounds Fall Into My Mind) (Radio Edit) — The Bucketheads | duration missing
2-9 Beachball (Vocal Radio Edit) — Nalin & Kane | duration missing
2-10 The Nighttrain (Radio Edit) — Kadoc | duration missing
2-11 Baker Street (Edit) — Undercover | duration missing
2-12 Gipsy Woman (Piano Version) — Glass Waters | du
… [1090 Zeichen gekürzt]
```
</details>

### 5. `shell` +44s – completed

```
bin/tl-mb search --title "Back To The 90s - The Biggest Hit Collection" --artist "Various"
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Back To The 90s \- The Biggest Hit Collection" AND artist:"Various")
```
</details>

### 6. `shell` +69s – completed

```
bin/tl-itunes upc 4005902510288; echo ---; bin/tl-deezer upc 4005902510288; echo ---; bin/tl-mb search --title "Back To The 90s" --artist "Various"
```

<details><summary>Ausgabe</summary>

```
no hit (physical releases are often missing from the digital catalogue)
---
no hit (Deezer mostly knows digital UPCs only)
---
14 Releases (Queries: release:"Back To The 90s" AND artist:"Various")
musicbrainz:release/cb30382b-fd5d-44c3-8284-b06ef0f950dd | Back to the 90’s — Various Artists | 1999 NL | CD | Tracks 19 | Barcode 5099749545922 | Sony Music Media 495459-2 | Official | score 100
musicbrainz:release/779603c4-663e-4fdf-86f1-8b9af8130f1d | Back to the 90’s — Various Artists | 2009 BE | CD+CD+CD+CD+CD | Tracks 18+19+18+18+20 | Barcode 5099930762725 | EMI 5099930762725 | Official | score 100
musicbrainz:release/f4f665bb-a8a7-45ce-97b3-6d5e2fd0799b | Big Tunes: Back to the 90s 2 — Various Artists | 2010-07-26 GB | CD+CD+CD | Tracks 20+20+20 | Barcode 5051275032529 | Universal Music TV 5051275032529; Dance Nation DANCENCD02 | Official | score 78
musicbrainz:release/03b48299-b915-4bbd-a28f-a11331827d6c | MNM Back to the 90s & Nillies — Various Artists | 2019-02-22 BE | Digital Media | Tracks 61 | Barcode - | CNR Music Group | ? | score 78
musicbrainz:release/544f574b-f349-4e77-915a-b2e14fe7c54f | MNM Back to the 90’s & Nillies — Various Artists | 2019-02-22 BE | CD+CD+CD | Tracks 20+20+21 | Barcode 5411530818594 | CNR Records Belgium AL-30927-2 | Official | score 78
musicbrainz:release/761bba40-9a5d-447b-a7b5-bee791d0eedc | Back to the 90’s: 100% Original Hits! — Various Artists | 2008 NL | CD+CD | Tracks 19+20 | Barcode 887254932420 | Sony Music 88725493242 | Official | score 78
musicbrainz:release/c5f96dbf-b7a8-4419-897d-80bc0908f02f | …Baby One More Time: Back to the 90s — Various Artists | 2015-02-23 GB | CD+CD+CD | Tracks 20+19+19 | Barcode 888750642127 | Sony Music 88875064212 | Official | score 73
musicbrainz:release/a778d579-6061-4d38-a27a-4e0aa161a95f | …Baby One More Time: Back to the 90s — Various Artists | 2015-02-23 IE | Digital Media+Digital Media+Digital Media | Tracks 20+19+19 | Barcode 886445019506 | Sony Music CG | Official | score 73
musicbrainz:release/6651a0b3-9e96-4dd2-8bd8-c85cf7c35596 | Mnm Back to the 90's & Nillies -100 Hits — Various Artists | 2020-02-28 BE | CD+CD+CD+CD+CD | Tracks 20+20+20+20+20 | Barcode 5411530823796 | CNR Music Group AL313982 | Official | score 68
musicbrainz:release/75548534-abef-499e-8398-c4470b8408d0 | Trance Dance - Back to the 90s the 2021 Edition — Various Artists | 2020-12-10 US | CD+CD | Tracks 20+20 | Barcode 4032989948727 | MORE Music and Media GmbH & Co. KG 4032989948727 | Official | score 65
m
… [940 Zeichen gekürzt]
```
</details>

### 7. `shell` +82s – completed

```
bin/tl-discogs versions 30190112 2>/dev/null | head -50; echo ---; bin/tl-lastfm album --artist "Various" --title "Back To The 90s - The Biggest Hit Collection"
```

<details><summary>Ausgabe</summary>

```
8168519 versions of master 30190112
discogs:release/8532114 | Mary Had A Little Lamb | 1878 US |  | Not On Label (Thomas Alva Edison Self-released) none | Cylinder
discogs:release/5695167 | Experimental Talking Clock | 1878 US |  | Not On Label (Frank Lambert (2) Self-released) none | Cylinder
discogs:release/15739753 | Mary Had A Little Lamb | 1888 Germany | 5", Single Sided | E. Berliner's Gramophone 30 | Shellac
discogs:release/27170094 | Whistling | 1888  |  | Edison Records none | Cylinder
discogs:release/2583289 | Electric Light Quadrille | 1889 US | 2 Minute | Edison Records none | Cylinder
discogs:release/26680979 | Old King Coal | 1889 Germany | 5", Single Sided | E. Berliner's Gramophone 20 | Shellac
discogs:release/33358139 | Thompson's Old Gray Mule | 1891 US | 2 Minute | North American Phonograph Company none | Cylinder
discogs:release/32733165 | Frankie Galop | 1892 US | 2 Minute | New Jersey Phonograph Company 633 | Cylinder
discogs:release/19899979 | Isle Of Champagne | 1893 US | 2 Minute | United States Phonograph Company none | Cylinder
discogs:release/30014467 | Why Should I Keep From Whistling? | 1893 US | 3 Minute, Single, Mono | Columbia Phonograph Co. none | Cylinder
discogs:release/29918884 | Vocal Solo | 1894 US | 2 Minute | United States Phonograph Company none | Cylinder
discogs:release/15485990 | The Volunteer Organist | 1894 US | 2 Minute | North American Phonograph Company 1292 | Cylinder
discogs:release/15485981 | Sweet Marie | 1894 US | 2 Minute | North American Phonograph Company 1289 | Cylinder
discogs:release/8816419 | Ousqu'est St Nazaire | 1895 France |  | Lioret 1015 | Cylinder
discogs:release/8815358 | Le Chat Noir | 1895 France |  | Lioret 1005 | Cylinder
discogs:release/8815983 | Les Matelots | 1895 France |  | Lioret 1008 | Cylinder
discogs:release/8816500 | Etoile D'Angleterre - Piston | 1895 France |  | Lioret 4215 | Cylinder
discogs:release/4273683 | Rabbit Hash | 1895 US | 7", Single Sided | E. Berliner's Gramophone 635 | Shellac
discogs:release/9346100 | La Paloma | 1895 US | 7", 78 RPM, Single Sided | E. Berliner's Gramophone 243 | Shellac
discogs:release/8817330 | Fanfares - Trompette | 1895 France |  | Lioret 3901 | Cylinder
discogs:release/3647954 | When Summer Comes Again | 1895 US | 7", Single Sided | E. Berliner's Gramophone 163 | Shellac
discogs:release/15484038 | When You Know The Girl You Love Loves You | 1895 US | 7", Single Sided | E. Berliner's Gramophone 156 | Shellac
discogs:release/8816195 | Ta
… [2271 Zeichen gekürzt]
```
</details>

### 8. `shell` +92s – completed

```
bin/tl-discogs search --catno 264.2475.2; echo ===; bin/tl-discogs search --title "Back To The 90s - The Biggest Hit Collection" --format CD
```

<details><summary>Ausgabe</summary>

```
1 hits (parameters: {'catno': '264.2475.2'})
discogs:release/30190112 | Various - Back To The 90s – The Biggest Hit Collection | ? Unknown | CD, Compilation | Label Pink Revolver | Kat.-Nr. 264.2475.2 | Barcodes 4005902510288 | master -
===
1 hits (parameters: {'release_title': 'Back To The 90s - The Biggest Hit Collection', 'format': 'CD'})
discogs:release/30190112 | Various - Back To The 90s – The Biggest Hit Collection | ? Unknown | CD, Compilation | Label Pink Revolver | Kat.-Nr. 264.2475.2 | Barcodes 4005902510288 | master -
```
</details>

### 9. `shell` +97s – completed

```
bin/tl-search "\"264.2475.2\"" ; echo ===; bin/tl-search "\"Back To The 90s\" \"Biggest Hit Collection\" Pink Revolver"
```

<details><summary>Ausgabe</summary>

```
2 hits for: "264.2475.2"
1. Back To The 90s – The Biggest Hit Collection – 2 x CD (Compilation), [r30190112] | Discogs
   https://www.discogs.com/de/release/30190112-Various-BACK-TO-THE-90s-THE-BIGGEST-HIT-COLLECTION
   Auf Discogs können Sie sich ansehen, wer an CDvon Back To The 90s – The Biggest Hit Collection mitgewirkt hat, Rezensionen und Titellisten lesen und auf dem Marktplatz nach der Veröffentlichung suchen.
2. Searching for a [phone removed]… Caller? They are from Washington
   [url removed]
   [phone removed] | [phone removed] ~ Ebyyon Lakoke · [phone removed] | [phone removed] ~ Ymbairm Efkerpumm · [phone removed] | [phone removed] ~ Rytn Awhent · [phone removed] | [phone removed] ~ Ujtekge Vetke · [phone removed] | [phone removed] ~ Efid
   + [phone removed] | [phone removed] ~ Ebyyon Lakoke · [phone removed] | [phone removed] ~ Ymbairm Efkerpumm · [phone removed]
===
10 hits for: "Back To The 90s" "Biggest Hit Collection" Pink Revolver
1. Back To The 90s: The Biggest Hit Collection (2 CDs) – jpc.de
   https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759
   Pink Revolver · Artikelnummer: 11714759 · UPC/EAN: 4005902510288 · Erscheinungstermin: 9.2.2024 · Weiterlesen · Tracklisting Mitwirkende · 1 Snap!: Rhythm Is A Dancer (7" Edit) Hörprobe Track 1: Rhythm Is A Dancer (7" Ed
   + Pink Revolver · Artikelnummer: 11714759 · UPC/EAN: 4005902510288 · Erscheinungstermin: 9.2.2024 · Weiterlesen · Tracklis
2. Back to the 90s - the Biggest Hit Collection Vol.2: Amazon.de: CDs & Vinyl
   https://www.amazon.de/Back-90s-Biggest-Collection-Vol-2/dp/B0DKB3T8BB
   Entdecken, shoppen und einkaufen bei Amazon.de: Günstige Preise für Elektronik & Foto, Filme, Musik, Bücher, Games, Spielzeug, Sportartikel, Drogerie & mehr
   + Manufacturer ‏ : ‎ Pink Revolver · Label ‏ : ‎ Pink Revolver · ASIN ‏ : ‎ B0DKB3T8BB · Country of origin ‏ : ‎ Germany ·
3. Back to the 90s - the Biggest Hit Collection: Amazon.de: CDs & Vinyl
   https://www.amazon.de/-/en/Back-90s-Biggest-Hit-Collection/dp/B0CQKRDGY4
   Entdecken, shoppen und einkaufen bei Amazon.de: Günstige Preise für Elektronik & Foto, Filme, Musik, Bücher, Games, Spielzeug, Sportartikel, Drogerie & mehr
   + Back to the 90s - the Biggest Hit Collection · A service that provides customers with MP3 versions of qualified physical
4. Various - BACK TO THE 90S - THE BIGGEST HIT COLLECTION - decks.de: Vinyl Shop
   https://www.decks.de/track/various-back_to_the_90s_-_the_bi
… [3581 Zeichen gekürzt]
```
</details>

### 10. `shell` +101s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759" --grep -i -E "min|Sek|[0-9]:[0-9]{2}" 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 11. `shell` +101s – completed

```
bin/tl-scrape "https://www.decks.de/track/various-back_to_the_90s_-_the_biggest_hit_collection/cm5-ip" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://www.decks.de/track/various-back_to_the_90s_-_the_biggest_hit_collection/cm5-ip
mode: http (http)
title: Various - BACK TO THE 90S - THE BIGGEST HIT COLLECTION / Pink Revolver / 26424752 | 2CD CD kaufen | decks.de
source-id: web:https://www.decks.de/track/various-back_to_the_90s_-_the_biggest_hit_collection/cm5-ip
---
Various - BACK TO THE 90S - THE BIGGEST HIT COLLECTION / Pink Revolver / 26424752 | 2CD CD kaufen | decks.de
Pop
Dance
Pop
GTIN13:
4005902510288
Code:
cm5-ip
Release:
09.02.2024
Various
BACK TO THE 90S - THE BIGGEST HIT COLLECTION 
(2CD)
Pink Revolver / 26424752
2CD 
Side
BPM
Tracklist
124
Snap! - Rhythm Is A Dancer (7- Edit)
129
Gala - Freed From Desire
130
Whigfield - Saturday Night
133
Bellini - Samba De Janeiro (Radio Edit)
123
Reel 2 Real - I Like To Move It (Erick -More- Club Mix)
130
Benny Benassi - Satisfaction
100
Mr. President - Coco Jamboo (Radio Version)
82
Dune - Hardcore Vibes
129
Dr. Alban - It s My Life (Radio Edit)
135
Fragma - Toca Me
89
Mauro Picotto - Komodo (Radio Mix)
121
Robin S. - Show Me Love (Radio Mix)
134
Brooklyn Bounce - The Theme (Of Progressive Attack)(Trip Mix Radio Edit)
138
Paffendorf - Where Are You
70
Aquagen - Hard To Say I m Sorry (Radio Edit)
130
Celvin Rotane - I Believe (Radio Edit)
135
Future Breeze - Why Dont You Dance With Me (Radio Edit)
70
Shaun Baker - Pizza
108
```
</details>

### 12. `shell` +103s – completed

```
bin/tl-scrape "https://www.decks.de/track/various-back_to_the_90s_-_the_biggest_hit_collection/cm5-ip" 2>&1 | tail -40
```

<details><summary>Ausgabe</summary>

```
Robert Miles - Children (Radio Edit)
126
The Bucketheads - The Bomb (These Sounds Fall Into My Mind)(Radio Edit)
134
Nalin & Kane - Beachball (Vocal Radio Edit)
70
Kadoc - The Nighttrain (Radio Edit)
123
Undercover - Baker Street
119
Glass Waters - Gipsy Woman (Piano Version)
136
Perpetual Motion - Keep On Dancin (Lets Go)
128
Tom Wilson - Techno Cat
137
Red 5 - Da Beat Goes
79
Bass Bumpers - Keep On Pushing
83
Mark Oh - Tears Don t Lie (Original Short Mix)
123
East Side Beat - Ride Like The Wind
140
CRW - I Feel Love
80
Interactive - Forever Young (Radio Edit)
e-mail Erinnerung
Wenn der Artikel lieferbar ist, wird eine Benachrichtigung an Deine eingetragene e-mail-Adresse versendet.
2 CDs full of 90s classics
pink revolver
Kunden kauften auch:
Mehr Releases vom Label: 
Sicherheits- und Herstellerinformationen
Believe Digital GmbH
Van-der-Smissen-Str. 322767 HamburgDE
[email protected]
* Preise inklusive 19% MwSt. zzgl. 
Versandkosten
.
```
</details>

### 13. `shell` +103s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759" --grep "^[0-9]{1,2}[.:]" 2>&1 | head -100
```

<details><summary>Ausgabe</summary>

```
url: https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759
mode: http (http)
title: Back To The 90s: The Biggest Hit Collection (2 CDs) –
source-id: web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759
---
…
4005902510288
Erscheinungstermin:
9.2.2024
Ähnliche Artikel
Back To The 90s: The Biggest Hit Collection Vol.2
```
</details>

### 14. `shell` +131s – completed

```
bin/tl-scrape "https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html" 2>&1 | head -120
```

<details><summary>Ausgabe</summary>

```
url: https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html
mode: http (http)
title: Back To The 90s - The Biggest Hit Collection (2024) » Music Box - music collection of popular genres...
source-id: web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html
---
Back To The 90s - The Biggest Hit Collection (2024) » Music Box - music collection of popular genres...
Music Box collection
 » 
Dance
 » Back To The 90s - The Biggest Hit Collection (2024)
Back To The 90s - The Biggest Hit Collection (2024)
21/02/2024 18:04
Dance
, 
Hard Dance
, 
Eurobeat
, 
Hard Trance
, 
Hands Up
, 
Electronica
, 
Hardcore
, 
Happy Hardcore
, 
Progressive House
, 
Techno
Artist:
 Various Performers
Title:
 Back To The 90s - The Biggest Hit Collection
Label:
 Pink Revolver (Rough Trade)
Style:
 Rave Sound, Hard Trance, Hands Up, Bouncy, Euroreggae, Dancecore, Happy Hardcore, Techno, Ambient House
Release Date:
 22-02-2024
Format:
 2 × CD, Compilation
Quality:
 320 Kbps/Joint Stereo/44100Hz
Codec:
 MPEG-1 Audio Layer 3
Tracks:
 40 Tracks
Time:
 02:31:21 Min
Size:
 352 MB
Tracklist:
01. Snap! - Rhythm Is A Dancer (7_ Edit) 3:46
02. Gala - Freed From Desire 3:33
03. Whigfield - Saturday Night 3:44
04. Bellini - Samba De Janeiro (Radio Edit) 2:49
05. Reel 2 Real - I Like To Move It (Erick More Club Mix) 5:54
06. Benny Benassi - Satisfaction 3:08
07. Mr. President - Coco Jamboo (Radio Version) 3:40
08. Dune - Hardcore Vibes 3:32
09. Dr. Alban - It's My Life (Radio Edit) 4:01
10. Fragma - Toca Me 3:34
11. Mauro Picotto - Komodo (Radio Mix) 3:23
12. Robin S. - Show Me Love (Radio Mix) 3:20
13. Brooklyn Bounce - The Theme (Of Progressive Attack) (Trip Mix Radio Edit) 3:39
14. Paffendorf - Where Are You 3:28
15. Aquagen - Hard To Say I'm Sorry (Radio Edit) 3:23
16. Celvin Rotane - I Believe (Radio Edit) 3:30
17. Future Breeze - Why Dont You Dance With Me (Radio Edit) 3:25
18. Shaun Baker - Pizza (Radio Cut) 3:47
19. Jam Tronik - Another Day In Paradise (Edit) 3:44
20. Sm-Trax - Got The Groove (Sm Radio Edit) 3:57
21. Gigi D'agostino - L'amour Toujours 3:58
22. Technohead - I Wanna Be A Hippy 3:16
23. Sash! - Ecuador (Original Radio Edit) 3:32
24. Wamdue Project - King Of My Castle (Roy Malone's Radio Edit) 3:27
25. Ultra Nate - Free (Mood Ii Swing Radio Edit) 3:52
26. Members Of Mayday - Sonic Empire (Short Mix) 3:58
27. Robert Miles - Children (Dream Version Special Radio Edit) 3:36
28. The Bucketheads - The Bomb! (These S
… [814 Zeichen gekürzt]
```
</details>

### 15. `shell` +136s – completed

```
bin/tl-itunes search "Various Back To The 90s The Biggest Hit Collection" 2>&1 | head -20; echo ===; bin/tl-deezer search --artist "Various Artists" --title "Back To The 90s The Biggest Hit Collection" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
25 Alben
itunes:album/256556109 | Karaoke - Singing to the Hits: 60's Female (Re-Recorded Versions) — Various Artists | 2007-05-28 | 16 Tracks
itunes:album/255694261 | Pinoy Biggie Hits (The Biggest Of The Year) — Verschiedene Interpret:innen | 2007-03-31 | 16 Tracks
itunes:album/139061326 | Synthesizer Classics - A Homage to the Biggest Synthesizer Hits of the 70's & 80's — Verschiedene Interpret:innen | 1999-01-01 | 11 Tracks
itunes:album/6771284839 | SAX HOUSE 2026 - The Biggest Saxophone House Lounge Hits — Verschiedene Interpret:innen | 2026-05-20 | 14 Tracks
itunes:album/301758072 | The Biggest Desi Hits, Vol.1 — Verschiedene Interpret:innen | 2009-02-09 | 28 Tracks
itunes:album/402748530 | The Biggest UK Bhangra Hits, Vol. 3 — Verschiedene Interpret:innen | 2010-11-26 | 51 Tracks
itunes:album/301655247 | The Biggest UK Bhangra Hits, Vol. 1 — Verschiedene Interpret:innen | 2009-02-02 | 30 Tracks
itunes:album/285665021 | 80s Hits - the Best — Verschiedene Interpret:innen | 2007-01-17 | 11 Tracks
itunes:album/347563271 | The Biggest Desi Bhangra Hits Vol:2 — Various Artists | 2009-11-27 | 46 Tracks
itunes:album/347255098 | The Biggest UK Bhangra Hits Vol:2 — Various Artists | 2009-11-27 | 48 Tracks
... 15 weitere ausgeblendet. narrow the filter or raise --limit.
===
0 Alben (q=artist:"Various Artists" album:"Back To The 90s The Biggest Hit Collection")
```
</details>

### 16. `shell` +150s – completed

```
bin/tl-caa c9c1e9c0 2>/dev/null | head; bin/tl-caa --help 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 400
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
```
</details>

### 17. `shell` +151s – completed

```
bin/tl-itunes search "Back To The 90s Biggest Hit Collection" 2>&1 | head -10; echo ===; bin/tl-itunes search "Back to the 90s Pink Revolver" 2>&1 | head -10
```

<details><summary>Ausgabe</summary>

```
5 Alben
itunes:album/725784933 | Greatest Hits (Remastered) — Huey Lewis and the News | 2006-05-23 | 21 Tracks
itunes:album/1469579555 | Greatest Hits — Tom Petty & The Heartbreakers | 1993-11-16 | 18 Tracks
itunes:album/6833023042 | Techno Top 100 Classics - The Biggest Hit Collection — Verschiedene Interpret:innen | 2026-09-18 | 100 Tracks
itunes:album/1435854353 | Greatest Hits — Bruce Springsteen | 1995-02-27 | 18 Tracks
itunes:album/1725169451 | Moment of Truth — The Red Clay Strays | 2022-04-29 | 12 Tracks
===
2 Alben
itunes:album/1065973975 | Wish You Were Here — Pink Floyd | 1975-09-12 | 6 Tracks
itunes:album/1441164604 | Sgt. Pepper's Lonely Hearts Club Band — The Beatles | 1967-06-01 | 15 Tracks
```
</details>

### 18. `shell` +159s – completed

```
bin/tl-vision "https://i.discogs.com/zdOO0fTFWsZWY3Rt5LReTszOxUIfxy5znFDrcfAZXi8/rs:fit/g:sm/q:90/h:600/w:598/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMwMTkwMTEyLTE3MTEyODAwMDMtNjE4Mi5qcGVn.jpeg" --context "Discogs image of 2CD 'Back To The 90s - The Biggest Hit Collection': describe what is shown, read all printed text" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/zdOO0fTFWsZWY3Rt5LReTszOxUIfxy5znFDrcfAZXi8/rs:fit/g:sm/q:90/h:600/w:598/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMwMTkwMTEyLTE3MTEyODAwMDMtNjE4Mi5qcGVn.jpeg
```
</details>

### 19. `shell` +159s – completed

```
bin/tl-vision "https://i.discogs.com/JjMiNdrcynZF5QzcXgnUEDWnmYUEkl9_TwhOkty2bcQ/rs:fit/g:sm/q:90/h:510/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMwMTkwMTEyLTE3MTEyODAwMDYtODc5Ny5qcGVn.jpeg" --context "Discogs image of 2CD 'Back To The 90s - The Biggest Hit Collection' (Pink Revolver 264.2475.2): read all printed text, especially tracklist, durations, track numbers and any catalogue/barcode text" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/JjMiNdrcynZF5QzcXgnUEDWnmYUEkl9_TwhOkty2bcQ/rs:fit/g:sm/q:90/h:510/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTMwMTkwMTEyLTE3MTEyODAwMDYtODc5Ny5qcGVn.jpeg
```
</details>

### 20. `shell` +167s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759" 2>&1 | sed -n '1,200p'
```

<details><summary>Ausgabe</summary>

```
url: https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759
mode: http (http)
title: Back To The 90s: The Biggest Hit Collection (2 CDs) –
source-id: web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759
---
Back To The 90s: The Biggest Hit Collection (2 CDs) – 
Inhalt
Einstellungen Privatsphäre
 Anmelden 
 Konto anlegen 
 Back To The 90s: The Biggest Hit Collection auf 2 CDs
Back To The 90s: The Biggest Hit Collection
 2
 CDs
CD (Compact Disc)
Herkömmliche CD, die mit allen CD-Playern und Computerlaufwerken, aber auch mit den meisten SACD- oder Multiplayern abspielbar ist.
Derzeit nicht erhältlich.
 Lassen Sie sich über unseren eCourier benachrichtigen, falls das Produkt bestellt werden kann. 
 Benachrichtigung anfordern 
Informieren Sie mich ...
 wenn der Artikel im Preis gesenkt wird 
Label:
Pink Revolver
UPC/EAN:
4005902510288
Erscheinungstermin:
9.2.2024
Ähnliche Artikel
Back To The 90s: The Biggest Hit Collection Vol.2
 2 CDs
EUR 14,99*
 Aktueller Preis: EUR 14,99 
Bravo Hits Vol. 135
 2 CDs
EUR 24,99*
 Aktueller Preis: EUR 24,99 
Bravo Hits Vol. 134
 2 CDs
EUR 22,99*
 Aktueller Preis: EUR 22,99 
 Weiterlesen 
 Tracklisting 
 Mitwirkende 
 Disk 1 von 2
 (CD)
1
Snap!
:
 Rhythm Is A Dancer (7" Edit)
Hörprobe Track 1: Rhythm Is A Dancer (7" Edit)
2
Gala
:
 Freed From Desire
Hörprobe Track 2: Freed From Desire
3
Whigfield
:
 Saturday Night
Hörprobe Track 3: Saturday Night
4
Vincenzo Bellini
:
 Samba De Janeiro
Hörprobe Track 4: Samba De Janeiro
5
 I Like To Move It (Erick "More" Club Mix)
Hörprobe Track 5: I Like To Move It (Erick "More" Club Mix)
6
 Satisfaction
Hörprobe Track 6: Satisfaction
7
Mr. President
:
 Coco Jamboo (Radio Edit)
Hörprobe Track 7: Coco Jamboo (Radio Edit)
8
Dune
:
 Hardcore Vibes (Video Mix)
Hörprobe Track 8: Hardcore Vibes (Video Mix)
9
Dr. Alban
:
 It's My Life (Radio Edit)
Hörprobe Track 9: It's My Life (Radio Edit)
10
Keine Künstlerinformation
:
 Toca Me (Radio Cut)
Hörprobe Track 10: Toca Me (Radio Cut)
11
Mauro Picotto
:
 Komodo (Radio Mix)
Hörprobe Track 11: Komodo (Radio Mix)
12
Robin S.
:
 Show Me Love (Stonebridge Radio Edit)
Hörprobe Track 12: Show Me Love (Stonebridge Radio Edit)
13
Brooklyn Bounce
:
 The Theme (Of Progressive Attack) (Trip Mix Radio Edit)
Hörprobe Track 13: The Theme (Of Progressive Attack) (Trip Mix Radio Edit)
14
Paffendorf
:
 Where Are You (Radio Edit)
Hörprobe Track 
… [1744 Zeichen gekürzt]
```
</details>

### 21. `shell` +245s – completed

```
bin/tl-mb search --title "Biggest Hit Collection" 2>&1 | head -8; echo ===; bin/tl-deezer search --artist "Various" --title "Back To The 90s" 2>&1 | head -6
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Biggest Hit Collection")

===
25 Alben (q=artist:"Various" album:"Back To The 90s")
deezer:album/103152752 | Back to the 90s: Best New Arrangement of Popular Songs — Verschiedene Interpreten | 15 Tracks | album
deezer:album/111128762 | Back To The 90's, vol. 2 — Verschiedene Interpreten | 21 Tracks | album
deezer:album/112855442 | Back To The 90's Special RnB — Verschiedene Interpreten | 14 Tracks | album
deezer:album/1136718711 | Back to the 90S — Verschiedene Interpreten | 20 Tracks | album
deezer:album/1146464991 | Back to the 90s - Hip-Hop — Verschiedene Interpreten | 9 Tracks | album
```
</details>

### 22. `write` +277s – completed

```
{"path": "<repo>/output/work/fall-b79d8bd8.json", "content": "{\n  \"input\": {\"id\": \"fall-b79d8bd8\", \"title\": \"BACK TO THE 90S - THE BIGGEST HIT COLLECTION\", \"artist\": \"VARIOUS\", \"ean\": \"4005902510288\"},\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"Back To The 90s – The Biggest Hit Collection\",\n    \"artist\": \"Various Artists\",\n    \"format\": \"CD\",\n    \"country\": \"DE\",\n    \"year\": 2024,\n    \"label\": \"Pink Revolver\",\n    \"catno\": \"264.2475.2\",\n    \"barcode\": \"4005902510288\",\n    \"edition\": \"2×CD compilation, 40 tracks (20 per disc), released 2024-02-09\",\n    \"ids\": {\"musicbrainz\": null, \"discogs\": \"30190112\"}\n  },\n  \"tracks\": [\n    {\"position\": \"1\", \"disc\": 1, \"title\": \"Rhythm Is A Dancer (7\\\" Edit)\", \"artist\": \"Snap!\", \"duration_s\": 226, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"2\", \"disc\": 1, \"title\": \"Freed From Desire\", \"artist\": \"Gala\", \"duration_s\": 213, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"3\", \"disc\": 1, \"title\": \"Saturday Night\", \"artist\": \"Whigfield\", \"duration_s\": 224, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"4\", \"disc\": 1, \"title\": \"Samba De Janeiro\", \"artist\": \"Bellini\", \"duration_s\": 169, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"5\", \"disc\": 1, \"title\": \"I Like To Move It (Erick \\\"More\\\" Club Mix)\", \"artist\": \"Reel 2 Real, The Mad Stuntman\", \"duration_s\": 354, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"6\", \"disc\": 1, \"title\": \"Satisfaction\", \"artist\": \"Benny Benassi, The Biz\", \"duration_s\": 188, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"7\", \"disc\": 1, \"title\": \"Coco Jamboo (Radio Edit)\", \"artist\": \"Mr. President\", \"duration_s\": 220, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"8\", \"disc\": 1, \"title\": \"Hardcore Vibes (Video Mix)\", \"artist\": \"Dune\", \"duration_s\": 212, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"9\", \"disc\": 1, \"title\": \"It's My Life (Radio Edit)\", \"artist\": \"Dr. Alban\", \"duration_s\": 241, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"10\", \"disc\": 1, \"title\": \"Toca Me (Radio Cut)\", \"artist\": \"Fragma\", \"duration_s\": 214, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"11\", \"disc\": 1, \"title\": \"Komodo (Radio Mix)\", \"artist\": \"Mauro Picotto\", \"duration_s\": 203, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"12\", \"disc\": 1, \"title\": \"Show Me Love (Stonebridge Radio Edit)\", \"artist\": \"Robin S.\", \"duration_s\": 200, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"13\", \"disc\": 1, \"title\": \"The Theme (Of Progressive Attack) (Trip Mix Radio Edit)\", \"artist\": \"Brooklyn Bounce\", \"duration_s\": 219, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"14\", \"disc\": 1, \"title\": \"Where Are You (Radio Edit)\", \"artist\": \"Paffendorf\", \"duration_s\": 208, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"15\", \"disc\": 1, \"title\": \"Hard To Say I'm Sorry (Original Radio Edit)\", \"artist\": \"Aquagen\", \"duration_s\": 203, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"16\", \"disc\": 1, \"title\": \"I Believe (Radio Edit)\", \"artist\": \"Celvin Rotane\", \"duration_s\": 210, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"17\", \"disc\": 1, \"title\": \"Why Don't You Dance With Me? (Radio Edit)\", \"artist\": \"Future Breeze\", \"duration_s\": 205, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"18\", \"disc\": 1, \"title\": \"Pizza (Radio Cut)\", \"artist\": \"Shaun Baker\", \"duration_s\": 227, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"19\", \"disc\": 1, \"title\": \"Another Day In Paradise (Edit)\", \"artist\": \"Jam Tronik\", \"duration_s\": 224, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"20\", \"disc\": 1, \"title\": \"Got The Groove (SM Radio Edit)\", \"artist\": \"SM-Trax\", \"duration_s\": 237, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"1\", \"disc\": 2, \"title\": \"L'amour Toujours\", \"artist\": \"Gigi D'Agostino\", \"duration_s\": 238, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"2\", \"disc\": 2, \"title\": \"I Wanna Be A Hippy\", \"artist\": \"Technohead\", \"duration_s\": 196, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"3\", \"disc\": 2, \"title\": \"Ecuador (Original Radio Edit)\", \"artist\": \"Sash!\", \"duration_s\": 212, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"4\", \"disc\": 2, \"title\": \"King Of My Castle (Roy Malone Kings Mix Edit)\", \"artist\": \"Wamdue Project\", \"duration_s\": 207, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"5\", \"disc\": 2, \"title\": \"Free (Mood II Swing Radio Edit)\", \"artist\": \"Ultra Naté\", \"duration_s\": 232, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"6\", \"disc\": 2, \"title\": \"Sonic Empire (Short Mix)\", \"artist\": \"Members Of Mayday\", \"duration_s\": 238, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"7\", \"disc\": 2, \"title\": \"Children (Dream Version Special Radio Edit)\", \"artist\": \"Robert Miles\", \"duration_s\": 216, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"8\", \"disc\": 2, \"title\": \"The Bomb (These Sounds Fall Into My Mind) (Radio Edit)\", \"artist\": \"The Bucketheads\", \"duration_s\": 203, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"9\", \"disc\": 2, \"title\": \"Beachball (Vocal Radio Edit)\", \"artist\": \"Nalin & Kane\", \"duration_s\": 231, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"10\", \"disc\": 2, \"title\": \"The Nighttrain (Radio Edit)\", \"artist\": \"Kadoc\", \"duration_s\": 199, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"11\", \"disc\": 2, \"title\": \"Baker Street (Edit)\", \"artist\": \"Undercover\", \"duration_s\": 250, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"12\", \"disc\": 2, \"title\": \"Gipsy Woman (Piano Version)\", \"artist\": \"Glass Waters\", \"duration_s\": 249, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"13\", \"disc\": 2, \"title\": \"Keep On Dancin' (Let's Go) (Radio Edit)\", \"artist\": \"Perpetual Motion\", \"duration_s\": 204, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"14\", \"disc\": 2, \"title\": \"Techno Cat (Dance Like Your Dad Radio Mix)\", \"artist\": \"Tom Wilson\", \"duration_s\": 239, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"15\", \"disc\": 2, \"title\": \"Da Beat Goes (Radio Version)\", \"artist\": \"Red 5\", \"duration_s\": 227, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"16\", \"disc\": 2, \"title\": \"Keep On Pushing (Radio Edit)\", \"artist\": \"Bass Bumpers\", \"duration_s\": 236, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"17\", \"disc\": 2, \"title\": \"Tears Don't Lie (Original Short Mix)\", \"artist\": \"Mark 'Oh\", \"duration_s\": 218, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"18\", \"disc\": 2, \"title\": \"Ride Like The Wind\", \"artist\": \"East Side Beat\", \"duration_s\": 238, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"19\", \"disc\": 2, \"title\": \"I Feel Love (DJ JamX & De Leon Remix)\", \"artist\": \"CRW\", \"duration_s\": 431, \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []},\n    {\"position\": \"20\", \"disc\": 2, \"title\": \"Forever Young\", \"artist\": \"Interactive\", \"duration_s\": 221, \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"duration_sources\": [\"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"flags\": []}\n  ],\n  \"artists\": [\n    {\"name\": \"Snap!\", \"role\": \"main\", \"tracks\": [\"1-1\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Gala\", \"role\": \"main\", \"tracks\": [\"1-2\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Whigfield\", \"role\": \"main\", \"tracks\": [\"1-3\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Bellini\", \"role\": \"main\", \"tracks\": [\"1-4\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Reel 2 Real\", \"role\": \"main\", \"tracks\": [\"1-5\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"The Mad Stuntman\", \"role\": \"featured\", \"tracks\": [\"1-5\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Erick Morillo\", \"role\": \"remixer\", \"tracks\": [\"1-5\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Benny Benassi\", \"role\": \"main\", \"tracks\": [\"1-6\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"The Biz\", \"role\": \"featured\", \"tracks\": [\"1-6\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Mr. President\", \"role\": \"main\", \"tracks\": [\"1-7\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Dune\", \"role\": \"main\", \"tracks\": [\"1-8\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Dr. Alban\", \"role\": \"main\", \"tracks\": [\"1-9\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Fragma\", \"role\": \"main\", \"tracks\": [\"1-10\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Mauro Picotto\", \"role\": \"main\", \"tracks\": [\"1-11\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Robin S.\", \"role\": \"main\", \"tracks\": [\"1-12\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"StoneBridge\", \"role\": \"remixer\", \"tracks\": [\"1-12\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Brooklyn Bounce\", \"role\": \"main\", \"tracks\": [\"1-13\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Paffendorf\", \"role\": \"main\", \"tracks\": [\"1-14\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Aquagen\", \"role\": \"main\", \"tracks\": [\"1-15\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Celvin Rotane\", \"role\": \"main\", \"tracks\": [\"1-16\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Future Breeze\", \"role\": \"main\", \"tracks\": [\"1-17\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Shaun Baker\", \"role\": \"main\", \"tracks\": [\"1-18\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Jam Tronik\", \"role\": \"main\", \"tracks\": [\"1-19\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"SM-Trax\", \"role\": \"main\", \"tracks\": [\"1-20\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Gigi D'Agostino\", \"role\": \"main\", \"tracks\": [\"2-1\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Technohead\", \"role\": \"main\", \"tracks\": [\"2-2\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Sash!\", \"role\": \"main\", \"tracks\": [\"2-3\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Wamdue Project\", \"role\": \"main\", \"tracks\": [\"2-4\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Roy Malone\", \"role\": \"remixer\", \"tracks\": [\"2-4\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Ultra Naté\", \"role\": \"main\", \"tracks\": [\"2-5\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Members Of Mayday\", \"role\": \"main\", \"tracks\": [\"2-6\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Robert Miles\", \"role\": \"main\", \"tracks\": [\"2-7\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"The Bucketheads\", \"role\": \"main\", \"tracks\": [\"2-8\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Nalin & Kane\", \"role\": \"main\", \"tracks\": [\"2-9\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Kadoc\", \"role\": \"main\", \"tracks\": [\"2-10\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Undercover\", \"role\": \"main\", \"tracks\": [\"2-11\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Glass Waters\", \"role\": \"main\", \"tracks\": [\"2-12\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Perpetual Motion\", \"role\": \"main\", \"tracks\": [\"2-13\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Tom Wilson\", \"role\": \"main\", \"tracks\": [\"2-14\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Red 5\", \"role\": \"main\", \"tracks\": [\"2-15\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Bass Bumpers\", \"role\": \"main\", \"tracks\": [\"2-16\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Mark 'Oh\", \"role\": \"main\", \"tracks\": [\"2-17\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"East Side Beat\", \"role\": \"main\", \"tracks\": [\"2-18\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"CRW\", \"role\": \"main\", \"tracks\": [\"2-19\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"JamX & De Leon\", \"role\": \"remixer\", \"tracks\": [\"2-19\"], \"sources\": [\"discogs:release/30190112\"]},\n    {\"name\": \"Interactive\", \"role\": \"main\", \"tracks\": [\"2-20\"], \"sources\": [\"discogs:release/30190112\"]}\n  ],\n  \"total_duration_s\": 9082,\n  \"confidence\": 0.9,\n  \"sources\": [\n    {\"id\": \"discogs:release/30190112\", \"url\": \"https://www.discogs.com/release/30190112\", \"kind\": \"database\", \"note\": \"Barcode 4005902510288, 2×CD, Pink Revolver 264.2475.2, full 40-track list with per-track artists; no durations, country/year not stated\"},\n    {\"id\": \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"url\": \"https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"kind\": \"shop\", \"note\": \"EAN 4005902510288, 2 CDs, Pink Revolver, release 9.2.2024; tracklist per disc matches Discogs\"},\n    {\"id\": \"web:https://www.decks.de/track/various-back_to_the_90s_-_the_biggest_hit_collection/cm5-ip\", \"url\": \"https://www.decks.de/track/various-back_to_the_90s_-_the_biggest_hit_collection/cm5-ip\", \"kind\": \"shop\", \"note\": \"GTIN 4005902510288, Pink Revolver 26424752, 2CD, release 09.02.2024, BPM per track\"},\n    {\"id\": \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\", \"url\": \"https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\", \"kind\": \"web\", \"note\": \"2×CD rip listing of the same 40 tracks in the same order with track durations, total 02:31:21 (= sum of listed durations); mix-title tags partly abbreviated/renamed\"}\n  ],\n  \"conflicts\": [\n    {\"field\": \"title track 1-8\", \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"resolution\": \"Use Discogs/jpc spelling 'Hardcore Vibes (Video Mix)'; the duration source lists only 'Hardcore Vibes'.\"},\n    {\"field\": \"title track 1-12\", \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"resolution\": \"Use 'Show Me Love (Stonebridge Radio Edit)' (Discogs + jpc); the duration source lists 'Show Me Love (Radio Mix)'.\"},\n    {\"field\": \"title track 2-4\", \"sources\": [\"discogs:release/30190112\", \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"resolution\": \"Use 'King Of My Castle (Roy Malone Kings Mix Edit)' (Discogs + jpc); the duration source lists 'Roy Malone's Radio Edit'.\"},\n    {\"field\": \"title track 2-14\", \"sources\": [\"discogs:release/30190112\", \"web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html\"], \"resolution\": \"Use 'Techno Cat (Dance Like Your Dad Radio Mix)' (Discogs); the duration source lists 'Techno Cat'.\"}\n  ],\n  \"missing\": [\n    \"No MusicBrainz release exists for this barcode/title; no physical-edition duration data in Discogs, jpc or decks.de - all 40 durations come from one web listing of the same 2×CD (music-box.life), so they are single-sourced\",\n    \"Discogs gives neither release country nor year; year 2024 taken from jpc.de and decks.de (both 2024-02-09), country DE inferred from German EAN prefix/label/distributor\",\n    \"Back/cover images on Discogs could not be read (HTTP 403), so printed title spelling is unverified\"\n  ],\n  \"alternatives\": [\n    {\"description\": \"Back To The 90s: The Biggest Hit Collection Vol. 2, 2×CD, Pink Revolver, 2025, EAN 4018939546533\", \"source\": \"web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection-vol-2/hnum/12022287\", \"why_not\": \"different release (Vol. 2) and different barcode\"}\n  ],\n  \"reasoning\": \"The barcode 4005902510288 is a valid EAN-13 and hits exactly one Discogs release (r30190112): 2×CD, Pink Revolver 264.2475.2, 40 tracks in 2×20 order. German retailers jpc.de and decks.de list the same EAN, label and catalogue number as a 2CD released 2024-02-09 and print a tracklist that matches Discogs track by track, so the edition (2CD, 2024) is secured. MusicBrainz has no release with this barcode or title, and there is no digital/streaming counterpart (iTunes, Deezer: no hit), which is consistent with a physical-only compilation. Discogs, jpc and decks give no track durations, so durations are taken from a web listing of the same 2×CD whose 40 titles are in identical order and whose stated total (2:31:21) equals the sum of its track times (9082 s); a few mix-name tags there are abbreviated, so the printed/Discogs titles were kept. All 46 performing artists (40 track acts plus featured The Mad Stuntman, The Biz and remixers Erick Morillo, StoneBridge, Roy Malone, JamX & De Leon) are listed with their tracks.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-b79d8bd8.json
```
</details>

### 23. `shell` +366s – completed

```
bin/tl-validate output/work/fall-b79d8bd8.json
```

<details><summary>Ausgabe</summary>

```
INVALID:
- release.ids.musicbrainz: Input should be a valid string
- conflicts.0.values: Field required
- conflicts.0.sources: Extra inputs are not permitted
- conflicts.1.values: Field required
- conflicts.1.sources: Extra inputs are not permitted
- conflicts.2.values: Field required
- conflicts.2.sources: Extra inputs are not permitted
- conflicts.3.values: Field required
- conflicts.3.sources: Extra inputs are not permitted
```
</details>

### 24. `shell` +502s – completed

```
bin/tl-validate --schema 2>&1 | grep -A30 -i "conflict"
```

<details><summary>Ausgabe</summary>

```
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
--
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
--
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
--
  "conflicts": {
   "items": {
    "$ref": "#/$defs/Conflict"
   },
   "title": "Conflicts",
   "type": "array"
  },
  "missing": {
   "description": "what is missing, e.g. 'duration track 20'",
   "items": {
    "type": "string"
   },
   "title": "Missing",
   "type": "array"
  },
  "alternatives": {
   "description": "other fitting editions and why they were not chosen",
   "items": {
    "$ref": "#/$defs/Alternative"
   },
   "title": "Alternatives",
   "type": "array"
  },
  "reasoning": {
   "description": "short: why exactly this edition",
   "title": "Reasoning",
   "type": "string"
  }
 },
 "required": [
  "input",
  "status",
  "confidence",
  "reasoning"
 ],
```
</details>

### 25. `shell` +505s – completed

```
cd <repo> && python3 - <<'EOF'
import json
p='output/work/fall-b79d8bd8.json'
d=json.load(open(p))
d['release']['ids']['musicbrainz']=None
D="discogs:release/30190112"
J="web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-back-to-the-90s-the-biggest-hit-collection/hnum/11714759"
M="web:https://music-box.life/dance/39727-back-to-the-90s-the-biggest-hit-collection-2024.html"
d['conflicts']=[
 {"field":"title track 1-8","values":{D:"Hardcore Vibes (Video Mix)",J:"Hardcore Vibes (Video Mix)",M:"Hardcore Vibes"},"resolution":"Use Discogs/jpc spelling 'Hardcore Vibes (Video Mix)'; the duration source lists only 'Hardcore Vibes'."},
 {"field":"title track 1-12","values":{D:"Show Me Love (Stonebridge Radio Edit)",J:"Show Me Love (Stonebridge Radio Edit)",M:"Show Me Love (Radio Mix)"},"resolution":"Use 'Show Me Love (Stonebridge Radio Edit)' (Discogs + jpc)."},
 {"field":"title track 2-4","values":{D:"King Of My Castle (Roy Malone Kings Mix Edit)",J:"King Of My Castle (Roy Malone Kings Mix Edit)",M:"King Of My Castle (Roy Malone's Radio Edit)"},"resolution":"Use 'King Of My Castle (Roy Malone Kings Mix Edit)' (Discogs + jpc)."},
 {"field":"title track 2-14","values":{D:"Techno Cat (Dance Like Your Dad Radio Mix)",M:"Techno Cat"},"resolution":"Use Discogs spelling with mix suffix."},
]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
EOF
bin/tl-validate output/work/fall-b79d8bd8.json
```

<details><summary>Ausgabe</summary>

```
INVALID:
- release.ids.musicbrainz: Input should be a valid string
```
</details>

### 26. `shell` +506s – completed

```
cd <repo> && python3 - <<'EOF'
import json
p='output/work/fall-b79d8bd8.json'
d=json.load(open(p))
d['release']['ids'].pop('musicbrainz',None)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
EOF
bin/tl-validate output/work/fall-b79d8bd8.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 40 tracks (40 with duration), 4 sources, 4 conflicts, confidence=0.9
```
</details>

> **Agent** +507s: FERTIG found 40 Tracks confidence=0.9
