# Agent-Trace: 18-matthias-petzold-slow-migration

> Schnellweg geprüft: no fast path: no EAN
Start 2026-11-20T15:57:08 · 22 Schritte · 32 Tool-Aufrufe · Tokens in 76786 / out 17933


### 1. `shell` +5s – completed

```
cd <repo> && bin/tl-discogs search --title "Slow Migration" --artist "Matthias Petzold" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 hits (parameters: {'release_title': 'Slow Migration', 'artist': 'Matthias Petzold'})
```
</details>

### 2. `shell` +5s – completed

```
cd <repo> && bin/tl-mb search --title "Slow Migration" --artist "Matthias Petzold" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Slow Migration" AND artist:"Matthias Petzold")
```
</details>

### 3. `shell` +11s – completed

```
cd <repo> && bin/tl-mb search --title "Slow Migration" 2>&1 | head -40; echo "---"; bin/tl-discogs search --title "Slow Migration" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Slow Migration")

---
2 hits (parameters: {'release_title': 'Slow Migration'})
discogs:release/6400791 | Roggiu De Mussa Pin-A - Slow Migration | 2009 Italy | CD, Album | Label UPR, Virus Studio, Siena | Kat.-Nr. UPR0019 | Barcodes - | master -
discogs:release/18324304 | Vanessa Gelvin - A Slow Migration of Heat | 2009 US | File, MP3, Album | Label Not On Label | Kat.-Nr. none | Barcodes - | master -
```
</details>

### 4. `shell` +11s – completed

```
cd <repo> && bin/tl-mb search --artist "Matthias Petzold" 2>&1 | head -40; echo "---"; bin/tl-discogs search --artist "Matthias Petzold" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
ERROR: give --barcode or --title
---
12 hits (parameters: {'artist': 'Matthias Petzold'})
discogs:release/6413759 | Matthias Petzold (2) - Psalmen Und Lobgesänge | 1994 Germany | CD, Album, Stereo | Label Indigo-Records | Kat.-Nr. 1002 CD | Barcodes - | master -
discogs:release/5633444 | Matthias Petzold (2) - Mirrors | 2012 Germany | CD, Album | Label Indigo-Records, Indigo-Records | Kat.-Nr. 1009 | Barcodes 4 260019 890092 | master -
discogs:release/6413634 | Matthias Petzold Septett - Ulysses | 1996 Germany | CD, Album, Stereo | Label Indigo-Records, P+O Pallas | Kat.-Nr. 1003 CD | Barcodes none, LC 5764, GEMA | master -
discogs:release/6413726 | Matthias Petzold (2), Esperanto-Music - Lifelines | 1992 Germany | CD, Album, Stereo | Label Indigo-Records, Indigo-Records | Kat.-Nr. 1001 CD | Barcodes GEMA | master -
discogs:release/6413496 | Matthias Petzold (2), Working Band - Elements | 2002 Germany | CD, Album, Stereo | Label Indigo-Records, Indigo-Records | Kat.-Nr. 1005 CD | Barcodes 4260019890054, LC 5764, GEMA | master -
discogs:release/6413746 | Matthias Petzold Bigband Featuring Heiner Wiberny - Pangäa | 2007 Germany | CD, Album | Label Indigo-Records | Kat.-Nr. 1007 CD | Barcodes - | master -
discogs:release/6413600 | Matthias Petzold (2), Thiemo Kirberg, Nils Imhorst - Franziskusinventionen | 2003 Germany | CD, Album, Stereo | Label Indigo-Records | Kat.-Nr. 1006 CD | Barcodes - | master -
discogs:release/12978342 | Dietrich Petzold, Ernesto Rodrigues, Guilherme Rodrigues, Matthias Bauer - Kühlspot Social Club | 2018 Germany | File, FLAC | Label Not On Label (Guilherme Rodrigues Self-released), Kühlspot Social Club, Berlin | Kat.-Nr. none | Barcodes - | master -
discogs:release/12718947 | Dietrich Petzold, Ernesto Rodrigues, Guilherme Rodrigues, Matthias Bauer - dis/con/sent | 2018 Portugal | CD, Album, Limited Edition | Label Creative Sources, Creative Sources Recordings | Kat.-Nr. CS 563 CD | Barcodes 5 609063 405637, 5609063405637, www.staff.pt 20182126 | master -
discogs:release/32104536 | dis/con/sent, Petzold* / Rodrigues* / Rodrigues* / Bauer* - Kompositionen | 2022 Portugal | File, FLAC, Album | Label Not On Label (Ernesto Rodrigues Self-released), Not On Label (Guilherme Rodrigues Self-released) | Kat.-Nr. none | Barcodes - | master -
discogs:release/12967505 | Elo Masing, Ernesto Rodrigues, Dietrich Petzold, Guilherme Rodrigues, Matthias Bauer, Klaus Kürvers - Hexagon | 2018 Portugal | File, FLAC | Label Digital Creative Sources, Kühls
… [416 Zeichen gekürzt]
```
</details>

### 5. `shell` +13s – completed

```
cd <repo> && bin/tl-search "Matthias Petzold Slow Migration" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
10 hits for: Matthias Petzold Slow Migration
1. Matthias Petzold: Slow Migration | live recording - Konzertkalender - JazzStadt Köln
   https://jazzstadt.de/de_DE/konzertkalender/matthias-petzold-slow-migration-live-recor.18005580
   Slow Migration heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds sind grooveorientiert und etwas verspielter als gewohnt. Sie erzeugen Bilder von Störchen, Schildkr
   + Slow Migration heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds | They evoke images of storks, turtles, wandering kings, intergalactic journeys, leaps into other time dimensions, and muc
2. www.loftkoeln.de
   https://www.loftkoeln.de/event/matthias-petzold-slow-migration-live-recording/
   Bela Nicolini – Trompete Matthias Petzold – Tenorsaxophon & Klarinette Ulrike Zavelberg – Cello Norman Peplow – Piano Sebastian Ascher – Bass Thomas Esch – Schlagzeug ... Slow Migration heißt das neue Bandprojekt des Sax
   + Slow Migration is the name of saxophonist and composer Matthias Petzold’s new band project. Petzold’s compositions are g | https://petzold-jazz.de/Slow-Migration/slow-migration.html · Die Frontline der Band mit Trompete, Saxophon/Klarinette un
3. Matthias Petzold | Jazz Saxophone – Biography, Albums & More | All About Jazz
   https://www.allaboutjazz.com/musicians/matthias-petzold
   Explore Matthias Petzold's biography, discography, and jazz legacy. Discover albums, articles, and interviews about Matthias Petzold – one of jazz's most celebrated saxophone players.
   + Sign in / sign up and request admin access to the Matthias Petzold musician page. | All About Jazz musician pages are maintained by musicians, publicists and trusted members like you. Interested? Tell us 
4. Sirius Quartet - Konzertkalender - JazzStadt Köln
   https://jazzstadtkoeln.de/de_DE/konzertkalender/sirius-quartet.17919840
   Das Sirius Quartet verbindet ein mitreißendes Repertoire mit unvergleichlicher Improvisationskraft. Diese am Konservatorium ausgebildeten Interpreten ...
5. Janning Trumann 6 - Konzertkalender - JazzStadt Köln
   https://jazzstadtkoeln.de/de_DE/konzertkalender/janning-trumann-6.15863261
   „(…)Zeitgenössische Improvisationsmusik auf hohem Niveau.“ Jazzthing 11/2018 Laut dem Deutschlandfunk ist Janning Trumann der profilierteste und umtriebigste ...
6. Blechlawine spielt "Slow Migration" von Matthias Petzold ...
   https://www.instagram.com/kornkam
… [1735 Zeichen gekürzt]
```
</details>

### 6. `shell` +13s – completed

```
cd <repo> && bin/tl-itunes search "Matthias Petzold Slow Migration" 2>&1 | head -20; echo "---"; bin/tl-deezer search --artist "Matthias Petzold" --title "Slow Migration" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
0 Alben

---
0 Alben (q=artist:"Matthias Petzold" album:"Slow Migration")
```
</details>

### 7. `shell` +15s – completed

```
cd <repo> && bin/tl-scrape "https://petzold-jazz.de/Slow-Migration/slow-migration.html" 2>&1 | head -120
```

<details><summary>Ausgabe</summary>

```
url: https://petzold-jazz.de/cds/slow-migration/
mode: http (http)
title: Slow Migration – Matthias Petzold
source-id: web:https://petzold-jazz.de/cds/slow-migration/
---
Slow Migration – Matthias Petzold
Zum Inhalt
Slow Migration
Label
Indigo Records 1015 CD, 2026
Kompositionen
Matthias Petzold
Aufgenommen
18. Juni 2026 (live) und 19. Juni 2026 im Loft, Köln, von Stefan Deistler
Abgemischt und gemastert
Stefan Deistler
Cover und Gestaltung
Shakur Leni Allan, Kampala (Uganda)
Fotos
Gabriele Petzold
15,– €
 inkl. MwSt., Porto und Verpackung
mehrere CDs günstiger
In den Warenkorb
Zum Warenkorb
Download bei Bandcamp
„Slow Migration“ heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds sind grooveorientiert und etwas verspielter als gewohnt. Sie erzeugen Bilder von Störchen, Schildkröten, wandernden Königen, intergalaktischen Reisen, Sprüngen in andere Zeitebenen und vielem mehr.
Die Frontline der Band mit Trompete, Saxophon/Klarinette und Cello klingt ungewöhnlich und vielschichtig. In der Band spielen Musiker aus unterschiedlichen Generationen und verbinden sich zu einer dynamischen und stilistisch vielfältigen Einheit. Jedes der Bandmitglieder bringt seinen individuellen Sound und Improvisationsstil in die Kompositionen mit ein.
Titel
Bullbush River Shuffle 
5:05
La Migration des Tortues 
5:53
Ankunft der Störche 
7:06
Playground 
6:06
Deserts 
6:36
Abrahams Reise 
5:41
Dreamtime 
7:27
Heavy Rotation 
5:26
Epilog: Three Kings 
5:31
Zum Anhören: Bullbush River Shuffle, La Migration des Tortues, Ankunft der Störche, Playground, Deserts und Dreamtime
Besetzung
Bela Nicolini
Trompete
Matthias Petzold
Tenorsaxophon/Klarinette
Ulrike Zavelberg
Cello
Norman Peplow
Klavier
Sebastian Ascher
Bass
Thomas Esch
Drums
Graphiken: Shakur Leni Allen, Kampala/Uganda
CD bestellen
Slow Migration
15,– €
 inkl. MwSt., Porto und Verpackung
mehrere CDs günstiger
In den Warenkorb
Zum Warenkorb
Download bei Bandcamp
Mehrere CDs, günstiger
Alle Preise inklusive Mehrwertsteuer, Porto und Verpackung.
1 CD
15,– €
2 CDs
25,– €
12,50 € je CD
3 CDs
33,– €
11,– € je CD
4 CDs
39,– €
9,75 € je CD
Jede weitere CD: 
5,– €
Zum Warenkorb
```
</details>

### 8. `shell` +18s – completed

```
cd <repo> && bin/tl-search "Matthias Petzold Slow Migration bandcamp" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: Matthias Petzold Slow Migration bandcamp
1. Aktuelles
   http://www.petzold-jazz.de/Aktuelles/aktuelles.html
   Do, 29. Januar, 20 Uhr (Einlass 19 Uhr) “Slow Migration” Brühl, Kornkammer, Kurfürstenstraße 48 Matthias Petzold, Saxophon Ulrike Zavelberg, Cello Bela Nicolini, Trompete Norman Peplow, Klavier Sebastian Ascher, Bass Tho
   + "Slow Migration" heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzol | Bela Nicolini - Trompete Matthias Petzold – Tenorsaxophon/Klarinette Ulrike Zavelberg – Cello Norman Peplov – Klavier Se
2. Matthias Petzold: Slow Migration | live recording - Konzertkalender - JazzStadt Köln
   https://jazzstadt.de/de_DE/konzertkalender/matthias-petzold-slow-migration-live-recor.18005580
   Jedes der Bandmitglieder bringt seinen individuellen Sound und Improvisationsstil in die Kompositionen mit ein. www.petzold-jazz.de/ Die Konzerte im LOFT beginnen in der Regel gegen 20 Uhr - das LOFT öffnet jeweils um 19
   + Slow Migration heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds | They evoke images of storks, turtles, wandering kings, intergalactic journeys, leaps into other time dimensions, and muc
3. Lebenslauf
   http://www.petzold-jazz.de/Lebenslauf/lebenslauf.html
   Lebenslauf Tallinn, Juli 2024 2026 “Slow Migration”, Bandprojekt in der Besetzung tp, sax/cl, cello, p, b, dr 2025 “11 Duets for Beginners” leichte Duos für Schüler, in Ausgaben für Saxophon, Klarinette und Flöte, erschi
   + Kompositionsaufträge der Stadt Brühl (1991 für sechs Big Band Arrangements, und 1993 für die Vertonung eines Stummfilms) | 2018 Aufnahme der Demo-CD Live im Loft mit der Band Hochhäuser Aufnahme der Klarinettenquintette mit Francois de Ribeaup
4. www.loftkoeln.de
   https://www.loftkoeln.de/event/dream-big-fish-2/
   Matthias Petzold: Slow Migration | live recording »
5. KAISER POMMES | Tranberg · Nissen · Stefansson · Steidle - Konzertkalender - JazzStadt Köln
   https://jazzstadt.de/de_DE/konzertkalender/kaiser-pommes-tranberg-nissen-stefansson-s.17754444
   Oli Steidle - Killing Popes — Ego Kills: shhpuma.bandcamp.com/album/ego... Live footage of Kaiser Pommes from 5e, CPH Jazzfest: www.instagram.com/reel/CuUPiZw... HINWEIS: Im Jahr 2024 starten die Konzerte im LOFT in der 
   + Dies war der Start-Schuss für weitere musikalische Aktivitäten in 2024 und darüber hinaus, in Form von Tourneen und Aufn | Oli Steidle - Killing Popes — 
… [1238 Zeichen gekürzt]
```
</details>

### 9. `shell` +20s – completed

```
cd <repo> && bin/tl-discogs search --catno "1015" 2>&1 | head -20; echo "---"; bin/tl-search "\"Slow Migration\" Petzold Indigo Records 1015" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
17395 hits (parameters: {'catno': '1015'})
discogs:release/34610272 | Orch. T.P. Ok Jazz* - Mabe Yo Mabe  | ? Kenya | Vinyl, 7", Single | Label Editions Populaires | Kat.-Nr. EP 1015 - F | Barcodes - | master -
discogs:release/28480555 | Frank Sinatra - My Kind Of Broadway | 1965 US | Vinyl, LP, Album, Mono | Label Reprise Records, Reprise Records | Kat.-Nr. 1015 | Barcodes P, ASCAP, ELT | master 343886
discogs:release/4678676 | Brotherhood Of Man - Save Your Kisses For Me | 1976 Spain | Vinyl, 7", 45 RPM, Single | Label Pye Records, Discos Belter, S.A. | Kat.-Nr. P.1.015 | Barcodes S.G.A.E., P-1015-A-2N1, P-1015-B-1N1 | master 61815
discogs:release/15692773 | Dennie Damaro - Snaren Der Liefde | 1994 Netherlands | CD, Album | Label Vincent Produkties, VNC | Kat.-Nr. 55 1015-2 | Barcodes 8 711255 101528 | master -
discogs:release/26516240 | The Flairs - Never No More / Hey Shoo - Blah - Dee | ? Italy | Vinyl, 7", 45 RPM | Label Broadway International | Kat.-Nr. B - 1015 | Barcodes - | master -
discogs:release/2856959 | Frank Sinatra - My Kind Of Broadway | 1965 US | Vinyl, LP, Album, Mono | Label Reprise Records, Reprise Records | Kat.-Nr. 1015 | Barcodes ASCAP, ELT, 10,491 | master 343886
discogs:release/17084763 | Joan Manuel Serrat - Dedicado A Antonio Machado, Poeta | 1976 Spain | Vinyl, LP, Album, Reissue | Label Novola, Novola | Kat.-Nr. NLX-1015 S | Barcodes NLX 1015-S-A, NLX 1015-S-B, M. 10106-1969 | master 317444
discogs:release/4427973 | NOFX / Bad Religion - Radio 93 | 1993 Germany | CD, Unofficial Release | Label Not On Label (NOFX), Not On Label (Bad Religion) | Kat.-Nr. BD 1015-2 | Barcodes - | master -
discogs:release/7371296 | Niño De Baena - Niño De Baena | 1972 Spain | Vinyl, LP, Album | Label Victoria, Victoria | Kat.-Nr. V.1015 | Barcodes SGAE, B. 4058-1972, Permiso 7.076 | master -
discogs:release/2197193 | Carroll Brothers - College Twist Party | 1962 US | Vinyl, LP, Album, Mono | Label Cameo, Cameo | Kat.-Nr. C 1015 | Barcodes C 1015-A-1 2-14-62, C 1015-B-1 2-14-62, Bell Sound   Audio Matrix | master 266083
discogs:release/8427239 | Steve Morse - Prime Cuts Volume 2 | 2009 US | CD, Compilation, Promo | Label Magna Carta, Magna Carta | Kat.-Nr. MA-1015-2 | Barcodes - | master 991027
discogs:release/15202801 | Los Elegidos (3) - Cuando Muera El Dia | 1975 Mexico | Vinyl, 7", 45 RPM, Single | Label Dimeca | Kat.-Nr. E 1015 A | Barcodes - | master -
discogs:release/34393084 | Frank Sinatra - My Kind Of Broadway | 1965 US | Vinyl, LP, Albu
… [4898 Zeichen gekürzt]
```
</details>

### 10. `shell` +23s – completed

```
cd <repo> && bin/tl-scrape "https://petzold-jazz.de/cds/slow-migration/" --links 2>&1 | grep -i -E "bandcamp|indigo|amazon|jpc|barcode|ean" | head -20
```

<details><summary>Ausgabe</summary>

```
Indigo Records 1015 CD, 2026
Download bei Bandcamp
Download bei Bandcamp
Download bei Bandcamp → https://matthiaspetzold.bandcamp.com/album/slow-migration
```
</details>

### 11. `shell` +25s – completed

```
cd <repo> && bin/tl-search "site:bandcamp.com \"Slow Migration\" Petzold" 2>&1 | head -20; echo "---"; bin/tl-search "\"Slow Migration\" \"Indigo\" 1015 CD Petzold 2026" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
10 hits for: site:bandcamp.com "Slow Migration" Petzold
1. beltalowda's collection | Bandcamp
   https://bandcamp.com/beltalowda?from=fanthanks
   A Slow Migration West (gift given) by Russian Cowboy · A Slow Migration West · by Russian Cowboy · favorite track · wishlist in wishlist » · You own this · · buy now · · hear more · appears in 3 other collections · Robbe
   + A Slow Migration West (gift given) by Russian Cowboy · A Slow Migration West · by Russian Cowboy · favorite track · wish | Rock • 55 collection items
2. A Slow Migration West, by Russian Cowboy
   https://russiancowboy.bandcamp.com/album/a-slow-migration-west
   8 track album
   + A Slow Migration West · Jan 2022 · Russian Cowboy · Jan 2021 · Demo 2020 · Jan 2020 · Contact Russian Cowboy · Streaming | 8 track album
3. Music | Russian Cowboy
   https://russiancowboy.bandcamp.com/
   A Slow Migration West · Russian Cowboy · Demo 2020 · Check out · Russian Cowboy Bloomington, Indiana · placeholder · Contact Russian Cowboy · Streaming and Download help ·
   + A Slow Migration West · Russian Cowboy · Demo 2020 · Check out · Russian Cowboy Bloomington, Indiana · placeholder · Con | Russian Cowboy. Bloomington, Indiana.
4. A Slow Migration of Heat, by Vanessa Gelvin
   https://vanessagelvin.bandcamp.com/album/a-slow-migration-of-heat
   21 track album
   + A Slow Migration of Heat · Aug 2009 · Contact Vanessa Gelvin · Streaming and Download help · Report this album or accoun | 21 track album
5. Anatomy Topography, by Vanessa Gelvin
   https://vanessagelvin.bandcamp.com/
   13 track album
---
3 hits for: "Slow Migration" "Indigo" 1015 CD Petzold 2026
1. Indigo Domotics • View topic - Need advice: Slow migration from ISY to Indigo
   https://forums.indigodomo.com/viewtopic.php?t=16480
   Users browsing this forum: No registered users and 0 guests · © Perceptive Automation, LLC. · Privacy Powered by phpBB® Forum Software © phpBB Group
2. (PDF) Patterns of animal migration
   https://www.researchgate.net/publication/299888982_Patterns_of_animal_migration
   PDF | On Aug 21, 2014, Ben B. Chapman and others published Patterns of animal migration | Find, read and cite all the research you need on ResearchGate
3. Migration of Birds Circular 16 U.S. Fish and Wildlife Service Migration of
   https://www.csu.edu/cerc/researchreports/documents/MigrationofBirdsCircular.pdf
   U.S. Fish and Wildlife Service · by Frederick C. Lincoln, 1935 revised by Steven R. Peterson, 1979 revised by John L. Zimmerman, 1998 Di
… [57 Zeichen gekürzt]
```
</details>

### 12. `shell` +27s – completed

```
cd <repo> && bin/tl-scrape "https://matthiaspetzold.bandcamp.com/album/slow-migration" 2>&1 | head -120
```

<details><summary>Ausgabe</summary>

```
url: https://matthiaspetzold.bandcamp.com/album/slow-migration
mode: http (http)
title: Slow Migration | Matthias Petzold
source-id: web:https://matthiaspetzold.bandcamp.com/album/slow-migration
---
Slow Migration | Matthias Petzold
+ hinzufügen
Album
Titel
Merchandise
Hörparty
neuer Künstler
bestehender Künstler
Statistiken
Abbrechen
Partner
Abbrechen
Künstler
PRO
Seite anzeigen
Profil bearbeiten
Werkzeuge
Abonnement
Abonnement
Sammlung anzeigen
Einkäufe
keine Ergebnisse
Einstellungen
Hilfe
Abmelden
 Registrieren
 Anmelden
Erhalte jeden Freitag neue Musikempfehlungen in deinen Posteingang.
 Musik
 Community
 Slow Migration
von 
Matthias Petzold
/
Digitales Album
 Streaming und Download
 Enthält unbegrenztes Streaming über die kostenlose Bandcamp-App und außerdem den hochwertigen Download als MP3, FLAC und mehr.
 Kann mit Geschenkkarte gekauft werden
 Download verfügbar in 16-bit/44.1kHz 
 Digitales Album kaufen
€9
EUR
 oder mehr
 Als Geschenk senden
Slow Migration
 Compact Disc (CD) + Digitales Album
 CD "Slow Migration", including a Poster with artwork of the ugandan desiger Shakur Leni Allan.
 Enthält unbegrenztes Streaming von 
Slow Migration
 über die kostenlose Bandcamp-App und außerdem den hochwertigen Download als MP3, FLAC und mehr.
 Download verfügbar in 16-bit/44.1kHz 
 wird innerhalb von 
10 Tagen
 versandt
 Kann mit Geschenkkarte gekauft werden
 Compact Disc kaufen
€15
EUR
oder mehr
 Als Geschenk senden
Teilen
 / Einbetten
1. | Bullbush River Shuffle 05:06 | Titel kaufen
2. | La Migration des Tortues 05:54 | Titel kaufen
3. | Ankunft der Störche 07:07 | Titel kaufen
4. | Playground 06:07 | Titel kaufen
5. | Deserts 06:37 | Titel kaufen
6. | Abrahams Reise 05:44 | Titel kaufen
7. | Dreamtime 07:27 | Titel kaufen
8. | Heavy Rotation 05:56 | Titel kaufen
9. | Three Kings 05:33 | Titel kaufen
über
This is the CD of Matthias Petzold's new Band, Slow Migration. It features a lineup of great musicians an an unusaul instrumentation:
Bela Nicolini - tp
Ulrike Zavelberg - cello
Matthias Petzold - ts, cl
Norman Peplow - p, el-p
Sebasitan Ascher, b
Thomas Esch, dr
Mitwirkende
 veröffentlicht am 2. November 2026
Lizenz
alle Rechte vorbehalten
Tags
Tags
jazz
composition
european
groove jazz
world music
Cologne
Warenkorb
Summe | USD
Steuern werden an der Kasse berechnet
 Ansehen
über
Matthias Petzold
Cologne, Germany
placeholder
 Matthias Petzold ist ein vielseitiger Jazzsaxophonist, Komponist und Arrangeur. Als Musiker bewegt er sich zwischen 
moderne
… [547 Zeichen gekürzt]
```
</details>

### 13. `shell` +32s – completed

```
cd <repo> && bin/tl-scrape "https://matthiaspetzold.bandcamp.com/album/slow-migration" --links 2>&1 | grep -i -E "bcbits|img|jpg|png" | head -20
```

<details><summary>Ausgabe</summary>

```
(no output)
```
</details>

### 14. `shell` +33s – completed

```
cd <repo> && bin/tl-search "\"Slow Migration\" Petzold CD jpc OR amazon OR indigo-records" 2>&1 | head -25
```

<details><summary>Ausgabe</summary>

```
0 hits for: "Slow Migration" Petzold CD jpc OR amazon OR indigo-records
```
</details>

### 15. `shell` +36s – completed

```
cd <repo> && bin/tl-scrape "https://matthiaspetzold.bandcamp.com/album/slow-migration" --mode http 2>&1 | grep -o -E "https://f4\.bcbits\.com/img/[^\"']+" | head -5; echo "---"; bin/tl-scrape "https://petzold-jazz.de/cds/slow-migration/" --links 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
---
url: https://petzold-jazz.de/cds/slow-migration/
mode: http (http)
title: Slow Migration – Matthias Petzold
source-id: web:https://petzold-jazz.de/cds/slow-migration/
---
Slow Migration – Matthias Petzold
Zum Inhalt
Slow Migration
Label
Indigo Records 1015 CD, 2026
Kompositionen
Matthias Petzold
Aufgenommen
18. Juni 2026 (live) und 19. Juni 2026 im Loft, Köln, von Stefan Deistler
Abgemischt und gemastert
Stefan Deistler
Cover und Gestaltung
Shakur Leni Allan, Kampala (Uganda)
Fotos
Gabriele Petzold
15,– €
 inkl. MwSt., Porto und Verpackung
mehrere CDs günstiger
In den Warenkorb
Zum Warenkorb
Download bei Bandcamp
„Slow Migration“ heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds sind grooveorientiert und etwas verspielter als gewohnt. Sie erzeugen Bilder von Störchen, Schildkröten, wandernden Königen, intergalaktischen Reisen, Sprüngen in andere Zeitebenen und vielem mehr.
Die Frontline der Band mit Trompete, Saxophon/Klarinette und Cello klingt ungewöhnlich und vielschichtig. In der Band spielen Musiker aus unterschiedlichen Generationen und verbinden sich zu einer dynamischen und stilistisch vielfältigen Einheit. Jedes der Bandmitglieder bringt seinen individuellen Sound und Improvisationsstil in die Kompositionen mit ein.
Titel
Bullbush River Shuffle 
5:05
La Migration des Tortues 
5:53
Ankunft der Störche 
7:06
Playground 
6:06
Deserts 
6:36
Abrahams Reise
```
</details>

### 16. `shell` +36s – completed

```
cd <repo> && bin/tl-search "Matthias Petzold Slow Migration 2026 Album Rezension" 2>&1 | head -25
```

<details><summary>Ausgabe</summary>

```
10 hits for: Matthias Petzold Slow Migration 2026 Album Rezension
1. Aktuelles
   http://www.petzold-jazz.de/Aktuelles/aktuelles.html
   "Slow Migration" heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds sind grooveorientiert und etwas verspielter als gewohnt. Sie erzeugen Bilder von Störchen, Schild
   + "Slow Migration" heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzol | Bela Nicolini - Trompete Matthias Petzold – Tenorsaxophon/Klarinette Ulrike Zavelberg – Cello Norman Peplov – Klavier Se
2. Matthias Petzold: Slow Migration | live recording - Konzertkalender - JazzStadt Köln
   https://jazzstadt.de/de_DE/konzertkalender/matthias-petzold-slow-migration-live-recor.18005580
   Die Kompositionen Petzolds sind grooveorientiert und etwas verspielter als gewohnt. Sie erzeugen Bilder von Störchen, Schildkröten, wandernden Königen, intergalaktischen Reisen, Sprüngen in andere Zeitebenen und vielem m
   + Slow Migration heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds | The band brings together musicians from different generations, who come together to form a dynamic and stylistically div
3. Matthias Petzold | Jazz Saxophone – Biography, Albums & More | All About Jazz
   https://www.allaboutjazz.com/musicians/matthias-petzold
   Explore Matthias Petzold's biography, discography, and jazz legacy. Discover albums, articles, and interviews about Matthias Petzold – one of jazz's most celebrated saxophone players.
   + Sign in / sign up and request admin access to the Matthias Petzold musician page. | All About Jazz musician pages are maintained by musicians, publicists and trusted members like you. Interested? Tell us 
4. Lebenslauf
   http://www.petzold-jazz.de/Lebenslauf/lebenslauf.html
   Lebenslauf Tallinn, Juli 2024 2026 “Slow Migration”, Bandprojekt in der Besetzung tp, sax/cl, cello, p, b, dr 2025 “11 Duets for Beginners” leichte Duos für Schüler, in Ausgaben für Saxophon, Klarinette und Flöte, erschi
   + Kompositionsaufträge der Stadt Brühl (1991 für sechs Big Band Arrangements, und 1993 für die Vertonung eines Stummfilms) | 2018 Aufnahme der Demo-CD Live im Loft mit der Band Hochhäuser Aufnahme der Klarinettenquintette mit Francois de Ribeaup
5. Matthias Petzold – Wikipedia
   https://de.wikipedia.org/wiki/Matthias_Petzold
   Matthias Petzold (* 25. April 1964 in Brühl) ist ein deutscher Jazzm
… [918 Zeichen gekürzt]
```
</details>

### 17. `shell` +42s – completed

```
cd <repo> && bin/tl-mb search --artist "Petzold" 2>&1 | head -25
```

<details><summary>Ausgabe</summary>

```
ERROR: give --barcode or --title
```
</details>

### 18. `shell` +42s – completed

```
cd <repo> && curl -sL "https://petzold-jazz.de/cds/slow-migration/" | grep -o -E "(src|href)=\"[^\"]*\.(jpg|jpeg|png|webp)\"" | head -20
```

<details><summary>Ausgabe</summary>

```
href="../../favicon-32.png"
href="../../apple-touch-icon.png"
src="../../cds/slow-migration/cover.jpg"
src="../../cds/slow-migration/slow-migration-day1.jpg"
src="../../cds/slow-migration/slow-migration-night1.jpg"
src="../../cds/slow-migration/cover.jpg"
src="../../cds/slow-migration/cover.jpg"
src="../../cds/slow-migration/cover.jpg"
src="../../cds/ankole-hills/cover.jpg"
src="../../cds/slow-migration/cover.jpg"
src="../../cds/ankole-hills/cover.jpg"
src="../../cds/giver-of-life/cover.jpg"
src="../../cds/slow-migration/cover.jpg"
src="../../cds/ankole-hills/cover.jpg"
src="../../cds/giver-of-life/cover.jpg"
src="../../cds/live-im-loft/cover.jpg"
```
</details>

### 19. `shell` +47s – completed

```
cd <repo> && for n in back rueckseite backcover cover-back; do code=$(curl -s -o /dev/null -w "%{http_code}" "https://petzold-jazz.de/cds/slow-migration/$n.jpg"); echo "$n $code"; done; echo "---"; curl -sL "https://matthiaspetzold.bandcamp.com/album/slow-migration" | grep -o -E "https://f4\.bcbits\.com/img/[a-z0-9_]+\.(jpg|png)" | sort -u | head -10
```

<details><summary>Ausgabe</summary>

```
back 404
rueckseite 404
backcover 404
cover-back 404
---
https://f4.bcbits.com/img/0048323892_10.jpg
https://f4.bcbits.com/img/0048323892_21.jpg
https://f4.bcbits.com/img/0048343113_100.png
https://f4.bcbits.com/img/0048343178_10.jpg
https://f4.bcbits.com/img/0048343178_38.jpg
https://f4.bcbits.com/img/a1557495220_10.jpg
https://f4.bcbits.com/img/a1557495220_16.jpg
https://f4.bcbits.com/img/a1557495220_2.jpg
https://f4.bcbits.com/img/a1557495220_3.jpg
https://f4.bcbits.com/img/a1557495220_5.jpg
```
</details>

### 20. `shell` +55s – completed

```
cd <repo> && bin/tl-vision "https://f4.bcbits.com/img/0048323892_10.jpg" --context "Back cover or CD of 'Slow Migration' by Matthias Petzold. Read the printed tracklist with numbers and durations, plus barcode and label/catalogue number if visible." 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://f4.bcbits.com/img/0048323892_10.jpg
model: gemini-3.8-flash@low, in 1260 / out 203 tokens, 5.2 s
kind: other | readable: False
0 tracks read
notes: Photograph of a man sitting on rocks near the ocean; no sound carrier or tracklist visible.
```
</details>

### 21. `shell` +57s – completed

```
cd <repo> && bin/tl-vision "https://f4.bcbits.com/img/0048343178_10.jpg" --context "Back cover of the CD 'Slow Migration' by Matthias Petzold. Read the printed tracklist with track numbers and durations, plus any barcode and label/catalogue number." 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://f4.bcbits.com/img/0048343178_10.jpg
model: gemini-3.8-flash@low, in 1288 / out 554 tokens, 6.6 s
kind: other | readable: True
release_title: Slow Migration
artist: Matthias Petzold
label: Indigo-Records
catalog_number: 1015CD
format_hints: CD
1. Bullbush River Shuffle | 5:05
2. La Migration Des Turtues | 5:53
3. Ankunft der Störche | 7:06
4. Playground | 6:06
5. Deserts | 6:36
6. Abrahams Reise | 5:41
7. Dreamtime | 7:27
8. Heavy Rotation | 5:26
9. Epilog: Three Kings | 5:31
9 tracks read
notes: Includes digipak/gatefold cover, CD, and a folded poster/inlay.
```
</details>

### 22. `shell` +67s – completed

```
cd <repo> && bin/tl-search "musik-sammler \"Slow Migration\" Petzold" 2>&1 | head -15
```

<details><summary>Ausgabe</summary>

```
8 hits for: musik-sammler "Slow Migration" Petzold
1. Aktuelles
   http://www.petzold-jazz.de/Aktuelles/aktuelles.html
   Do, 29. Januar, 20 Uhr (Einlass 19 Uhr) “Slow Migration” Brühl, Kornkammer, Kurfürstenstraße 48 Matthias Petzold, Saxophon Ulrike Zavelberg, Cello Bela Nicolini, Trompete Norman Peplow, Klavier Sebastian Ascher, Bass Tho
   + Do, 18. Juni, 20 Uhr Slow Migration Loft, Köln, Wissmannstraße 22 | Mi, 30. September, 20 Uhr, Slow Migration Jazzin’ Erftstadt, Erftstadt, Anneliese-Geske Haus, Gustav-Heinemann-Str.
2. www.loftkoeln.de
   https://www.loftkoeln.de/event/matthias-petzold-slow-migration-live-recording/
   Slow Migration is the name of saxophonist and composer Matthias Petzold’s new band project. Petzold’s compositions are groove-oriented and a bit more playful than usual.
   + https://petzold-jazz.de/Slow-Migration/slow-migration.html · Die Frontline der Band mit Trompete, Saxophon/Klarinette un | Bela Nicolini – Trompete Matthias Petzold – Tenorsaxophon & Klarinette Ulrike Zavelberg – Cello Norman Peplow – Piano Se
3. Matthias Petzold: Slow Migration | live recording - Konzertkalender - JazzStadt Köln
   https://jazzstadt.de/de_DE/konzertkalender/matthias-petzold-slow-migration-live-recor.18005580
   Weitere Informationen zu den Preisen, Karten-Reservierungen und den Öffnungszeiten finden sich hier: www.loftkoeln.de/de/karten/ __________________________________ Slow Migration is the name of saxophonist and composer M
   + Sie erzeugen Bilder von Störchen, Schildkröten, wandernden Königen, intergalaktischen Reisen, Sprüngen in andere Zeitebe | They evoke images of storks, turtles, wandering kings, intergalactic journeys, leaps into other time dimensions, and muc
4. Lebenslauf
   http://www.petzold-jazz.de/Lebenslauf/lebenslauf.html
```
</details>

### 23. `shell` +74s – completed

```
cd <repo> && bin/tl-vision "https://f4.bcbits.com/img/0048343178_5.jpg" --context "Back cover of CD 'Slow Migration' (Matthias Petzold, Indigo-Records 1015CD). Give the exact printed spelling of track 2's title character by character, and the exact printed text of track 9. Is there a barcode or EAN printed anywhere? Quote the digits if yes." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://f4.bcbits.com/img/0048343178_5.jpg
model: gemini-3.8-flash@low, in 1316 / out 569 tokens, 6.4 s
kind: booklet | readable: True
release_title: Slow Migration
artist: Matthias Petzold
label: Indigo-Records
format_hints: CD
1. Bullbush River Shuffle | 5:05
2. La Migration Des Turtues | 5:53
3. Ankunft der Störche | 7:06
4. Playground | 6:06
5. Deserts | 6:36
6. Abrahams Reise | 5:41
7. Dreamtime | 7:27
8. Heavy Rotation | 5:26
9. Epilog: Three Kings | 5:31
9 tracks read
notes: No barcode visible on the shown panels. On the CD label visible: 'LC-0576...'. Track 2 spelled 'La Migration Des Turtues' as printed.
```
</details>

### 24. `shell` +82s – completed

```
cd <repo> && bin/tl-validate --schema 2>&1 | head -120
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

### 25. `shell` +92s – completed

```
cd <repo> && bin/tl-validate --schema 2>&1 | sed -n '120,400p'
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

### 26. `shell` +92s – completed

```
cd <repo> && bin/tl-scrape "https://petzold-jazz.de/cds/slow-migration/" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://petzold-jazz.de/cds/slow-migration/
mode: http (http)
title: Slow Migration – Matthias Petzold
source-id: web:https://petzold-jazz.de/cds/slow-migration/
---
Slow Migration – Matthias Petzold
Zum Inhalt
Slow Migration
Label
Indigo Records 1015 CD, 2026
Kompositionen
Matthias Petzold
Aufgenommen
18. Juni 2026 (live) und 19. Juni 2026 im Loft, Köln, von Stefan Deistler
Abgemischt und gemastert
Stefan Deistler
Cover und Gestaltung
Shakur Leni Allan, Kampala (Uganda)
Fotos
Gabriele Petzold
15,– €
 inkl. MwSt., Porto und Verpackung
mehrere CDs günstiger
In den Warenkorb
Zum Warenkorb
Download bei Bandcamp
„Slow Migration“ heißt das neue Bandprojekt des Saxophonisten und Komponisten Matthias Petzold. Die Kompositionen Petzolds sind grooveorientiert und etwas verspielter als gewohnt. Sie erzeugen Bilder von Störchen, Schildkröten, wandernden Königen, intergalaktischen Reisen, Sprüngen in andere Zeitebenen und vielem mehr.
Die Frontline der Band mit Trompete, Saxophon/Klarinette und Cello klingt ungewöhnlich und vielschichtig. In der Band spielen Musiker aus unterschiedlichen Generationen und verbinden sich zu einer dynamischen und stilistisch vielfältigen Einheit. Jedes der Bandmitglieder bringt seinen individuellen Sound und Improvisationsstil in die Kompositionen mit ein.
Titel
Bullbush River Shuffle 
5:05
La Migration des Tortues 
5:53
Ankunft der Störche 
7:06
Playground 
6:06
Deserts 
6:36
Abrahams Reise 
5:41
Dreamtime 
7:27
Heavy Rotation 
5:26
Epilog: Three Kings 
5:31
Zum Anhören: Bullbush River Shuffle, La Migration des Tortues, Ankunft der Störche, Playground, Deserts und Dreamtime
Besetzung
Bela Nicolini
Trompete
Matthias Petzold
Tenorsaxophon/Klarinette
Ulrike Zavelberg
Cello
Norman Peplow
Klavier
Sebastian Ascher
Bass
Thomas Esch
```
</details>

### 27. `shell` +94s – completed

```
cd <repo> && bin/tl-scrape "https://matthiaspetzold.bandcamp.com/album/slow-migration" 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
url: https://matthiaspetzold.bandcamp.com/album/slow-migration
mode: http (http)
title: Slow Migration | Matthias Petzold
source-id: web:https://matthiaspetzold.bandcamp.com/album/slow-migration
---
Slow Migration | Matthias Petzold
+ hinzufügen
Album
Titel
Merchandise
Hörparty
neuer Künstler
bestehender Künstler
Statistiken
Abbrechen
Partner
Abbrechen
Künstler
PRO
Seite anzeigen
Profil bearbeiten
Werkzeuge
Abonnement
Abonnement
Sammlung anzeigen
Einkäufe
keine Ergebnisse
Einstellungen
Hilfe
Abmelden
 Registrieren
 Anmelden
Erhalte jeden Freitag neue Musikempfehlungen in deinen Posteingang.
 Musik
 Community
 Slow Migration
von 
Matthias Petzold
/
Digitales Album
 Streaming und Download
 Enthält unbegrenztes Streaming über die kostenlose Bandcamp-App und außerdem den hochwertigen Download als MP3, FLAC und mehr.
 Kann mit Geschenkkarte gekauft werden
 Download verfügbar in 16-bit/44.1kHz 
 Digitales Album kaufen
€9
EUR
 oder mehr
 Als Geschenk senden
Slow Migration
 Compact Disc (CD) + Digitales Album
 CD "Slow Migration", including a Poster with artwork of the ugandan desiger Shakur Leni Allan.
 Enthält unbegrenztes Streaming von 
Slow Migration
 über die kostenlose Bandcamp-App und außerdem den hochwertigen Download als MP3, FLAC und mehr.
 Download verfügbar in 16-bit/44.1kHz 
 wird innerhalb von 
10 Tagen
 versandt
 Kann mit Geschenkkarte gekauft werden
 Compact Disc kaufen
€15
EUR
oder mehr
 Als Geschenk senden
Teilen
 / Einbetten
1. | Bullbush River Shuffle 05:06 | Titel kaufen
2. | La Migration des Tortues 05:54 | Titel kaufen
3. | Ankunft der Störche 07:07 | Titel kaufen
4. | Playground 06:07 | Titel kaufen
5. | Deserts 06:37 | Titel kaufen
6. | Abrahams Reise 05:44 | Titel kaufen
7. | Dreamtime 07:27 | Titel kaufen
8. | Heavy Rotation 05:56 | Titel kaufen
9. | Three Kings 05:33 | Titel kaufen
über
This is the CD of Matthias Petzold's new Band, Slow Migration. It features a lineup of great musicians an an unusaul instrumentation:
Bela Nicolini - tp
Ulrike Zavelberg - cello
```
</details>

### 28. `shell` +99s – completed

```
cd <repo> && bin/tl-vision "https://f4.bcbits.com/img/0048343178_10.jpg" --context "Back cover of the CD 'Slow Migration' by Matthias Petzold. Transcribe the printed tracklist exactly as printed, one line per track with number, title and duration, all 9 tracks. Also quote any label, LC code and catalogue number printed." 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
ERROR: image budget for this case used up (3 images) – rely on the sources already read
```
</details>

### 29. `shell` +108s – completed

```
cd <repo> && bin/tl-validate --schema 2>&1 | sed -n '400,700p'
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

### 30. `shell` +111s – completed

```
cd <repo> && bin/tl-mb search --title "Slow Migration" --artist "Matthias Petzold" 2>&1 | head -20; echo "=== DISCOGS"; bin/tl-discogs search --title "Slow Migration" --artist "Matthias Petzold" 2>&1 | head -20; echo "=== DISCOGS 2"; bin/tl-discogs search --title "Slow Migration" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Slow Migration" AND artist:"Matthias Petzold")

=== DISCOGS
0 hits (parameters: {'release_title': 'Slow Migration', 'artist': 'Matthias Petzold'})

=== DISCOGS 2
2 hits (parameters: {'release_title': 'Slow Migration'})
discogs:release/6400791 | Roggiu De Mussa Pin-A - Slow Migration | 2009 Italy | CD, Album | Label UPR, Virus Studio, Siena | Kat.-Nr. UPR0019 | Barcodes - | master -
discogs:release/18324304 | Vanessa Gelvin - A Slow Migration of Heat | 2009 US | File, MP3, Album | Label Not On Label | Kat.-Nr. none | Barcodes - | master -
```
</details>

### 31. `write` +126s – completed

```
{"path": "<repo>/output/work/fall-3865b7e5.json", "content": "{\n  \"input\": {\"id\": \"fall-3865b7e5\", \"title\": \"Slow Migration\", \"artist\": \"Matthias Petzold\"},\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"Slow Migration\",\n    \"artist\": \"Matthias Petzold\",\n    \"format\": \"CD\",\n    \"country\": \"DE\",\n    \"year\": 2026,\n    \"label\": \"Indigo Records\",\n    \"catno\": \"1015 CD\",\n    \"barcode\": null,\n    \"edition\": \"CD incl. poster (artwork by Shakur Leni Allan)\",\n    \"ids\": {}\n  },\n  \"tracks\": [\n    {\"position\": \"1\", \"disc\": 1, \"title\": \"Bullbush River Shuffle\", \"artist\": null, \"duration_s\": 305,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"image:https://f4.bcbits.com/img/0048343178_10.jpg\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"2\", \"disc\": 1, \"title\": \"La Migration Des Turtues\", \"artist\": null, \"duration_s\": 353,\n     \"sources\": [\"image:https://f4.bcbits.com/img/0048343178_10.jpg\", \"image:https://f4.bcbits.com/img/0048343178_5.jpg\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"image:https://f4.bcbits.com/img/0048343178_10.jpg\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [\"title_conflict\"], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"3\", \"disc\": 1, \"title\": \"Ankunft der Störche\", \"artist\": null, \"duration_s\": 426,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"image:https://f4.bcbits.com/img/0048343178_10.jpg\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"image:https://f4.bcbits.com/img/0048343178_10.jpg\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"4\", \"disc\": 1, \"title\": \"Playground\", \"artist\": null, \"duration_s\": 366,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"5\", \"disc\": 1, \"title\": \"Deserts\", \"artist\": null, \"duration_s\": 396,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"6\", \"disc\": 1, \"title\": \"Abrahams Reise\", \"artist\": null, \"duration_s\": 341,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"flags\": [\"duration_conflict\"], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"7\", \"disc\": 1, \"title\": \"Dreamtime\", \"artist\": null, \"duration_s\": 447,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"8\", \"disc\": 1, \"title\": \"Heavy Rotation\", \"artist\": null, \"duration_s\": 326,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"flags\": [\"duration_conflict\"], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]},\n    {\"position\": \"9\", \"disc\": 1, \"title\": \"Epilog: Three Kings\", \"artist\": null, \"duration_s\": 331,\n     \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"],\n     \"duration_sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"],\n     \"flags\": [\"title_conflict\"], \"credits\": [{\"name\": \"Matthias Petzold\", \"role\": \"composer\", \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}]}\n  ],\n  \"artists\": [\n    {\"name\": \"Matthias Petzold\", \"role\": \"main\", \"tracks\": [], \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\"]},\n    {\"name\": \"Bela Nicolini\", \"role\": \"other\", \"tracks\": [], \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]},\n    {\"name\": \"Ulrike Zavelberg\", \"role\": \"other\", \"tracks\": [], \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]},\n    {\"name\": \"Norman Peplow\", \"role\": \"other\", \"tracks\": [], \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]},\n    {\"name\": \"Sebastian Ascher\", \"role\": \"other\", \"tracks\": [], \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]},\n    {\"name\": \"Thomas Esch\", \"role\": \"other\", \"tracks\": [], \"sources\": [\"web:https://petzold-jazz.de/cds/slow-migration/\"]}\n  ],\n  \"total_duration_s\": 3291,\n  \"confidence\": 0.75,\n  \"sources\": [\n    {\"id\": \"web:https://petzold-jazz.de/cds/slow-migration/\", \"url\": \"https://petzold-jazz.de/cds/slow-migration/\", \"kind\": \"web\", \"note\": \"Official artist site: CD on Indigo Records 1015 CD, 2026, 9 tracks with durations, personnel, composer credit\"},\n    {\"id\": \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\", \"url\": \"https://matthiaspetzold.bandcamp.com/album/slow-migration\", \"kind\": \"streaming\", \"note\": \"Artist Bandcamp: CD + digital album, same 9 tracks; digital durations differ on tracks 6 and 8\"},\n    {\"id\": \"image:https://f4.bcbits.com/img/0048343178_10.jpg\", \"url\": \"https://f4.bcbits.com/img/0048343178_10.jpg\", \"kind\": \"image\", \"note\": \"Back cover scan (Bandcamp CD art): tracks 1-3 printed with durations 5:05 / 5:53 / 7:06, track 2 printed 'La Migration Des Turtues'; no barcode visible\"},\n    {\"id\": \"image:https://f4.bcbits.com/img/0048343178_5.jpg\", \"url\": \"https://f4.bcbits.com/img/0048343178_5.jpg\", \"kind\": \"image\", \"note\": \"Second read of the same cover art: 9 tracks read, track 2 spelling 'La Migration Des Turtues' as printed, LC-0576 on CD label, no barcode\"}\n  ],\n  \"conflicts\": [\n    {\"field\": \"title track 2\", \"values\": {\"image:https://f4.bcbits.com/img/0048343178_10.jpg\": \"La Migration Des Turtues\", \"web:https://petzold-jazz.de/cds/slow-migration/\": \"La Migration des Tortues\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\": \"La Migration des Tortues\"}, \"resolution\": \"Printed cover spelling used (carrier takes precedence); the artist site and Bandcamp use the French spelling 'des Tortues' – the cover may carry a typo or the vision read may misread 'o' as 'u'\"},\n    {\"field\": \"title track 9\", \"values\": {\"web:https://petzold-jazz.de/cds/slow-migration/\": \"Epilog: Three Kings\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\": \"Three Kings\"}, \"resolution\": \"CD tracklist on the artist site used ('Epilog: Three Kings'); Bandcamp digital album lists 'Three Kings'\"},\n    {\"field\": \"duration track 6\", \"values\": {\"web:https://petzold-jazz.de/cds/slow-migration/\": \"5:41\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\": \"5:44\"}, \"resolution\": \"CD value 341 s chosen; Bandcamp gives 344 s for the digital master (3 s difference, above rounding tolerance)\"},\n    {\"field\": \"duration track 8\", \"values\": {\"web:https://petzold-jazz.de/cds/slow-migration/\": \"5:26\", \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\": \"5:56\"}, \"resolution\": \"CD value 326 s chosen; Bandcamp digital master lists 356 s (30 s difference – likely a different edit or a Bandcamp typo)\"}\n  ],\n  \"missing\": [\n    \"no barcode/EAN found on the CD panels or in any database\",\n    \"no MusicBrainz or Discogs entry for this release\",\n    \"printed title and duration of track 9 not verified on the cover image (image budget exhausted)\"\n  ],\n  \"alternatives\": [\n    {\"description\": \"Bandcamp digital album 'Slow Migration', 9 tracks, same titles except track 9 'Three Kings'\", \"source\": \"web:https://matthiaspetzold.bandcamp.com/album/slow-migration\", \"why_not\": \"digital edition; input is a physical sound carrier and the CD edition is documented on the artist site and sold on Bandcamp\"}\n  ],\n  \"reasoning\": \"No barcode given and no MusicBrainz/Discogs entry exists. The artist's own site documents the 2026 CD 'Slow Migration' on Indigo Records 1015 CD with 9 tracks, durations and personnel; the Bandcamp CD listing confirms a physical CD with the same 9 tracks, and the back-cover scan confirms the printed titles and durations of tracks 1-3. CD durations from the artist site were used; the Bandcamp digital album differs on two durations and on track 9's title.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-3865b7e5.json
```
</details>

### 32. `shell` +128s – completed

```
cd <repo> && bin/tl-validate output/work/fall-3865b7e5.json 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 9 tracks (9 with duration), 4 sources, 4 conflicts, confidence=0.75
```
</details>

> **Agent** +130s: FERTIG found 9 Tracks confidence=0.75
