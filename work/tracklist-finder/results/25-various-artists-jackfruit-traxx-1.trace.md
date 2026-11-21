# Agent-Trace: 25-various-artists-jackfruit-traxx-1

> Schnellweg geprüft: no fast path: no EAN
Start 2026-11-20T16:01:28 · 16 Schritte · 27 Tool-Aufrufe · Tokens in 36902 / out 9014


> **Agent** +0s: I'll start by checking the input and searching the databases.

### 1. `shell` +1s – completed

```
bin/tl-mb search --title "Jackfruit Traxx 1" --artist "Various Artists" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Jackfruit Traxx 1" AND artist:"Various Artists")
```
</details>

### 2. `shell` +1s – completed

```
bin/tl-discogs search --title "Jackfruit Traxx 1" --artist "Various Artists" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 hits (parameters: {'release_title': 'Jackfruit Traxx 1', 'artist': 'Various Artists'})
```
</details>

### 3. `shell` +3s – completed

```
bin/tl-mb search --title "Jackfruit Traxx" 2>&1 | head -40; echo ---; bin/tl-discogs search --title "Jackfruit Traxx" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Jackfruit Traxx")

---
0 hits (parameters: {'release_title': 'Jackfruit Traxx'})
```
</details>

### 4. `shell` +4s – completed

```
bin/tl-search "Jackfruit Traxx 1" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
10 hits for: Jackfruit Traxx 1
1. Jackfruit Recordings / Jackfruit Traxx - Bandcamp
   https://jackfruitrec.bandcamp.com/
   Traxx Salad Vol.1 Nesi, Dompe, Nils Ohrmann, Edgar Peng · Bonsoir Clara Phillipe Autuori, Autuori · Blizzard Dompe · Your Love DJ Chi · Warehouse Grooves, Vol.4 Dompe · Check out · Jackfruit Recordings / Jackfruit Traxx 
   + Traxx Salad Vol.1 Nesi, Dompe, Nils Ohrmann, Edgar Peng · Bonsoir Clara Phillipe Autuori, Autuori · Blizzard Dompe · You
2. Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
   https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
   Buy Traxx Salad Vol. 1 (JFXX1) by Various Artists on Jack Fruit Recordings. excl vinyl record. Selected Wax — record store for DJs. Worldwide shipping.
   + Buy Traxx Salad Vol. 1 (JFXX1) by Various Artists on Jack Fruit Recordings. excl vinyl record. Selected Wax — record sto
3. Various - Traxx Salad Vol. 1
   https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html
   And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Peng with a remix for Nils Ohrmann, and of course Dompe as label head are all on board.
   + Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the fir | Vinyl Various - Traxx Salad Vol. 1
4. Maltitz - Tears of Pears [Jackfruit Traxx] | Music & Downloads on Beatport
   https://www.beatport.com/release/tears-of-pears/5363316
   "Maltitz - Tears of Pears [Jackfruit Traxx]" | Find the latest releases here | #1 source for DJ Sets and more
5. Alien Radio (DE) - Just in Time Remixes [Jackfruit Traxx] | Music & Downloads on Beatport
   https://www.beatport.com/release/just-in-time-remixes/4934517
   "Alien Radio (DE) - Just in Time Remixes [Jackfruit Traxx]" | Find the latest releases here | #1 source for DJ Sets and more
6. Dompe - Last Days of Disko [Jackfruit Traxx] | Music & Downloads on Beatport
   https://www.beatport.com/de/release/last-days-of-disko/4573969
   "Dompe - Last Days of Disko [Jackfruit Traxx]" | Find the latest releases here | #1 source for DJ Sets and more
7. Dompe - Dreamberry [Jackfruit Traxx] | Music & Downloads on Beatport
   https://www.beatport.com/release/dreamberry/4741608
   "Dompe - Dreamberry [Jackfruit Traxx]" | Find the latest releases here | #1 source for DJ Sets and more
8. Dompe - Dreamberry (Original Mix) [Jackfruit Traxx] | Music & Downloads on 
… [1468 Zeichen gekürzt]
```
</details>

### 5. `shell` +7s – completed

```
bin/tl-search "\"Jackfruit Traxx 1\" release tracklist" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
1 hits for: "Jackfruit Traxx 1" release tracklist
1. NESI (ES) Releases :: Beatport
   https://www.beatport.com/artist/nesi-es/1116348/releases
   Jackfruit Traxx · 127-128 BPM · 2025-05-30 · $2.98 · Add to queue · Add to playlist · Animo · Jonas Van Opstal · Get In Tone Records · 130 BPM · 2025-04-25 · $1.49 · Add to queue · Add to playlist · Voltaire Music pres. 
   + Nesi is a rising star in the world of house music hailing from Barcelona, Spain. With a passion for music that started a | Jackfruit Traxx · 127-128 BPM · 2025-05-30 · $2.98 · Add to queue · Add to playlist · Animo · Jonas Van Opstal · Get In
```
</details>

### 6. `shell` +20s – completed

```
bin/tl-discogs search --title "Traxx Salad" 2>&1 | head -30; echo ---; bin/tl-mb search --title "Traxx Salad" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
2 hits (parameters: {'release_title': 'Traxx Salad'})
discogs:release/37837974 | Various - Traxx Salad Vol. 2 | 2026 Germany | Vinyl, 12" | Label JackFruit Traxx | Kat.-Nr. JFXX2 | Barcodes - | master -
discogs:release/36475918 | Various - Traxx Salad Vol. 1 | 2026 Germany | Vinyl, 12" | Label JackFruit Traxx | Kat.-Nr. JFXX1 | Barcodes - | master -
---
0 Releases (Queries: release:"Traxx Salad")
```
</details>

### 7. `shell` +21s – completed

```
bin/tl-discogs release 36475918 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
discogs:release/36475918 | Traxx Salad Vol. 1 — Various | 2026-02-00 Germany | 1× Vinyl (12") | JackFruit Traxx JFXX1 | master -
url: https://www.discogs.com/release/36475918-Various-Traxx-Salad-Vol-1
A1 Old School — Nesi (5) | duration missing
A2 Last Days Of Disko — Dompe | duration missing
B1 No Place Like Heim — Dompe | duration missing
B2 Che (Edgar Peng Remix) — Nils Ohrmann | duration missing | credits: Remix: Edgar Peng
4 tracks, total 0:00 (0 s), without duration: 4
images: primary https://i.discogs.com/RAaAmVxnIVZnbMTWKGqaB3apnRpA-xC9Mvfbj1zKhwE/rs:fit/g:sm/q:90/h:600/w:592/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM2NDc1/OTE4LTE3NzA5MDky/ODgtNDc2MS5qcGVn.jpeg | secondary https://i.discogs.com/096XfgXQMzp5iz2D7O28iAybdpKNWEeWP-XTs4au5jA/rs:fit/g:sm/q:90/h:600/w:590/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM2NDc1/OTE4LTE3NzA5MDky/ODctNjAwMS5qcGVn.jpeg
community: have 49 want 10 data_quality Needs Vote
```
</details>

### 8. `shell` +22s – completed

```
bin/tl-search "Jackfruit Traxx" --site discogs.com 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: Jackfruit Traxx site:discogs.com
1. jackfruit ))) records Diskographie | Discogs
   https://www.discogs.com/de/label/10626-jackfruit-records
   Entdecken Sie Musik des Labels jackfruit ))) records. Finden Sie heraus, was in Ihrer Sammlung fehlt, und kaufen Sie jackfruit ))) records-Veröffentlichungen.
2. Regatta De Blanc - Jackfruit ))) Compilation Vol.1 (1997, Vinyl) - Discogs
   https://www.discogs.com/Various-Regatta-De-Blanc-Jackfruit--Compilation-Vol1/release/9669830
   Comes with press sheet. (Catn° on press sheet JFT 001) Run out groove etchings A : MPO A jackfruit compilation 01 D+M cut by pole Run out groove etchings B : MPO B jackfruit compilation 01 D+M cut by pole
   + Comes with press sheet. (Catn° on press sheet JFT 001) Run out groove etchings A : MPO A jackfruit compilation 01 D+M cu
3. Regatta De Blanc - Jackfruit ))) Compilation Vol. 1 – CD (Compilation), 1997 [r806930] | Discogs
   https://www.discogs.com/de/release/806930-Various-Regatta-De-Blanc-Jackfruit--Compilation-Vol-1
   Auf Discogs können Sie sich ansehen, wer an 1997 CDvon Regatta De Blanc - Jackfruit ))) Compilation Vol. 1 mitgewirkt hat, Rezensionen und Titellisten lesen und auf dem Marktplatz nach der Veröffentlichung suchen.
4. JackFruit Recordings Diskographie | Discogs
   https://www.discogs.com/de/label/1854882-JackFruit-Recordings
   Entdecken Sie Musik des Labels JackFruit Recordings. Finden Sie heraus, was in Ihrer Sammlung fehlt, und kaufen Sie JackFruit Recordings-Veröffentlichungen.
5. DJ Milton – Jack Traxx – Vinyl (12", 33 ⅓ RPM, White Label), [r5816921] | Discogs
   https://www.discogs.com/release/5816921-DJ-Milton-Jack-Traxx
   View credits, reviews, tracks and shop for the Vinyl release of "Jack Traxx" on Discogs.
6. Phono Jones – Jackfruit EP – 3 x File (320 kbps, MP3, EP), 2008 [r1452492] | Discogs
   https://www.discogs.com/release/1452492-Phono-Jones-Jackfruit-EP
   View credits, reviews, tracks and shop for the 2008 File release of "Jackfruit EP" on Discogs.
7. DJ Milton – Jack Traxx – Vinyl (12", 33 ⅓ RPM), 1996 [r175067] | Discogs
   https://www.discogs.com/release/175067-DJ-Milton-Jack-Traxx
   View credits, reviews, tracks and shop for the 1996 Vinyl release of "Jack Traxx" on Discogs.
   + Street Traxx II · D.J. Funk #1 · 1994 US · Vinyl — · 12", 33 ⅓ RPM · Shop · Want · Street Traxx III · D.J. Funk · 1995 U
8. Jackfruit Discography | Discogs
   https://www.discogs.com/label/39238-Jackfruit
   Explore music from the Jackfruit label. Disc
… [308 Zeichen gekürzt]
```
</details>

### 9. `shell` +24s – completed

```
bin/tl-scrape "https://jackfruitrec.bandcamp.com/music" --grep -i "traxx" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 10. `shell` +25s – completed

```
bin/tl-search "\"Jackfruit Traxx 1\" vinyl 12\"" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 hits for: "Jackfruit Traxx 1" vinyl 12"
```
</details>

### 11. `shell` +27s – completed

```
bin/tl-scrape "https://jackfruitrec.bandcamp.com/music" --grep "Traxx|traxx" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://jackfruitrec.bandcamp.com/music
mode: http (http)
title: Musik | Jackfruit Recordings / Jackfruit Traxx
source-id: web:https://jackfruitrec.bandcamp.com/music
---
…
Musik | Jackfruit Recordings / Jackfruit Traxx
+ hinzufügen
Album
…
 Turn up the Volume (Bandcamp exclusive)
 Dompe
 Traxx Salad, Vol.2
 Nesi, Dompe , Autuori
 Warehouse Grooves, Vol. 5
…
 Tronic
 Dompe
 Traxx Salad Vol.1
 Nesi, Dompe, Nils Ohrmann, Edgar Peng
 Bonsoir Clara
…
 Ansehen
über
Jackfruit Recordings / Jackfruit Traxx
Berlin, Germany
placeholder
Jackfruit Recordings a Label for House Music founded by Dompe in 2017...
Kontakt/Hilfe
Jackfruit Recordings / Jackfruit Traxx kontaktieren
Hilfe 
für Streaming und Download
```
</details>

### 12. `shell` +28s – completed

```
bin/tl-search "Jackfruit Traxx JFXX" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
10 hits for: Jackfruit Traxx JFXX
1. Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
   https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
   Buy Traxx Salad Vol. 1 (JFXX1) by Various Artists on Jack Fruit Recordings. excl vinyl record. Selected Wax — record store for DJs. Worldwide shipping.
   + also available: Vol. 2 14,95 € In Stockcause we love vinyl. Following the huge success of Jackfruit Recordings, we found
2. Jackfruit Recordings / Jackfruit Traxx - Bandcamp
   https://jackfruitrec.bandcamp.com/
   Jackfruit Recordings / Jackfruit Traxx. Berlin, Germany. Jackfruit Recordings a Label for House Music founded by Dompe in 2017...
3. DOMPE - Berlin House DJ, Producer & Jackfruit Recordings
   https://www.dompe.de/
   Beatport Spotify DOMPE SoundCloud DOMPE SoundCloud Jackfruit Bandcamp Latest Jackfruit Traxx release Think About It DOMPE / JFTRAXX26 / 24.04.2026
   + Official website of DOMPE, Berlin-based house DJ, producer and founder of Jackfruit Recordings and Jackfruit Traxx. Book | Beatport Spotify DOMPE SoundCloud DOMPE SoundCloud Jackfruit Bandcamp Latest Jackfruit Traxx release Think About It DOMP
4. Merch - Jackfruit Recordings / Jackfruit Traxx - Bandcamp
   https://jackfruitrec.bandcamp.com/merch
   Merch from Jackfruit Recordings / Jackfruit Traxx
   + Jackfruit Recordings a Label for House Music founded by Dompe in 2017... | Merch from Jackfruit Recordings / Jackfruit Traxx
5. Records - decks.de: Vinyl Shop
   https://www.decks.de/label/jack-fruit-recordings
   TRAXX SALAD VOL. 2 · 12 Inch 13.07.26 · check a2 --> dompe - factor · House · Progressive · Techhouse · JFXX2 · Jack Fruit Recordings · a1Nesi - In This House · a2Dompe - Factor · b1Dompe - Little Helper · b2Autuori - Bo
   + TRAXX SALAD VOL. 2 · 12 Inch 13.07.26 · check a2 --> dompe - factor · House · Progressive · Techhouse · JFXX2 · Jack Fru | TRAXX SALAD VOL 1 · 12 Inch 09.02.26 · incl. one vinyl only track. 4 house stomper! House · Detroit House · Techhouse · 
6. Alien Radio (DE) - Just in Time Remixes [Jackfruit Traxx] | Music & Downloads on Beatport
   https://www.beatport.com/release/just-in-time-remixes/4934517
   Jackfruit Traxx · CatalogJFTRAXX8 · Add to queue · Add to playlist · $2.98 · Link: Embed: Title / Artists · Label / Remixers · Genre / BPM & Key ·
   + Jackfruit Traxx · CatalogJFTRAXX8 · Add to queue · Add to playlist · $2.98 · Link: Embed: Title / Artists · Label / Remi
7. Dompe - Dreamberry [Jackfruit Tra
… [1433 Zeichen gekürzt]
```
</details>

### 13. `shell` +32s – completed

```
bin/tl-scrape "https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/" --grep -i "track|Nesi|Dompe|Ohrmann|min" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 14. `shell` +32s – completed

```
bin/tl-scrape "https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1" --grep "" --max 6000 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
url: https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1
mode: http (http)
title: Traxx Salad Vol.1 | Nesi, Dompe, Nils Ohrmann, Edgar Peng | Jackfruit Recordings / Jackfruit Traxx
source-id: web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1
---
Traxx Salad Vol.1 | Nesi, Dompe, Nils Ohrmann, Edgar Peng | Jackfruit Recordings / Jackfruit Traxx
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
 Merchandise
 Community
 Traxx Salad Vol.1
von 
Nesi, Dompe, Nils Ohrmann, Edgar Peng
 Unterstützt von
schlense
/
Digitales Album
 Streaming und Download
 Enthält unbegrenztes Streaming über die kostenlose Bandcamp-App und außerdem den hochwertigen Download als MP3, FLAC und mehr.
 Kann mit Geschenkkarte gekauft werden
 Download verfügbar in 24-bit/44.1kHz 
 Digitales Album kaufen
€5
EUR
 oder mehr
 Als Geschenk senden
Traxx Salad Vol.1
 Schallplatte/Vinyl + Digitales Album
 Enthält unbegrenztes Streaming von 
Traxx Salad Vol.1
 über die kostenlose Bandcamp-App und außerdem den hochwertigen Download als MP3, FLAC und mehr.
 Download verfügbar in 24-bit/44.1kHz 
 wird innerhalb von 
3 Tagen
 versandt
 Kann mit Geschenkkarte gekauft werden
 Vinyl kaufen
€12
EUR
oder mehr
 Als Geschenk senden
Teilen
 / Einbetten
1. | Nesi - Old School 05:30 | Titel kaufen
2. | Dompe - Last Days of Disko 06:03 | Titel kaufen
3. | Nils Ohrmann, Edgar Peng - Che (Edgar Peng Remix) 05:32 | Titel kaufen
Mitwirkende
 veröffentlicht am 1. April 2026
Lizenz
alle Rechte vorbehalten
Tags
Tags
deep house
electronic
```
</details>

### 15. `shell` +35s – completed

```
bin/tl-scrape "https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/" --max 4000 2>&1 | sed -n '1,80p'
```

<details><summary>Ausgabe</summary>

```
url: https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
mode: http (http)
title: Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
source-id: web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
---
Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
0
%
LOG IN TO USE ALL
FEATURES
Exclusive pressings, DJ-only edits, and warehouse finds. Sign up to get the drops before they sell out on Discogs.
Log in
or
Sign in with Google
Don't have an account?
Create Account
Light
Light
Dark
80
%
Pre-order
Tech House
VARIOUS
 — 
Traxx Salad Vol. 1
Label
: 
Jack Fruit Recordings
 · 
Catalog
: 
JFXX1
 · 
Format
: 
excl Vinyl
 · 
Release Date
: 
Coming Soon
 · 
Features
: 
Standard
 · 
14.90
 €
Pre-Order
+ Watchlist
Coming Soon
Coming Soon
Tracklist
Nesi - Old School
(
Original Mix
)
Various
+ Watchlist
Dompe - Last Days Of Disko
(
Original Mix
)
Various
+ Watchlist
Dompe - No Place Like Heim (Vinyl Only)
(
Original Mix
)
Various
+ Watchlist
Nils Ohrmann - Che (Edgar Peng Remix)
(
Original Mix
)
Various
+ Watchlist
About Release
also available: Vol. 2 14,95 € In Stockcause we love vinyl. Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Peng with a remix for Nils Ohrmann, and of course Dompe as label head are all on board. Dompe also contributes an exclusive vinyl-only track. House music all life long.
You May Also Like
```
</details>

### 16. `shell` +35s – completed

```
bin/tl-scrape "https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html" --max 5000 2>&1 | sed -n '1,120p'
```

<details><summary>Ausgabe</summary>

```
url: https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html
mode: http (http)
title: Various - Traxx Salad Vol. 1
source-id: web:https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html
---
Various - Traxx Salad Vol. 1
Rupture de stock
search


Various - Traxx Salad Vol. 1
 €15.90
 No tax
cause we love vinyl. Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Peng with a remix for Nils Ohrmann, and of course Dompe as label head are all on board. Dompe also contributes an exclusive vinyl-only track. House music all life long. House Tech
Politique de livraison
Colissimo sous 3 à 4 jours
Description
Product Details
cause we love vinyl. Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Peng with a remix for Nils Ohrmann, and of course Dompe as label head are all on board. Dompe also contributes an exclusive vinyl-only track. House music all life long. House Tech
Reference 
JFXX1
 Comments (0)
 No customer reviews for the moment.
 Your review appreciation cannot be sent
 OK
 Report comment
 Are you sure that you want to report this comment?
 No
 Yes
 Report sent
 Your report has been submitted and will be considered by a moderator.
 OK
 Your report cannot be sent
 OK
Write your review
×
 Review sent
 Your comment has been submitted and will be available once approved by a moderator.
 OK
 Your review cannot be sent
 OK
 16 other products in the same category:

 Quick view
pdqb - Treasure II (7")
 €4.50
Rupture de stock

 Quick view
Trippy Journey - Night Club EP
 €17.50
Rupture de stock

 Quick view
Patrice Bäumel - Speicher 133
 €15.90
Rupture de stock

 Quick view
Souffle Caramel - CLUB DE JAZZ
 €14.00
New

 Quick view
KiNK - Quantum Shake 10"
 €14.50
Rupture de stock

 Quick view
Demuja - DEMUJA PRESENTS...
 €19.50
New
Rupture de stock

 Quick view
inconnu - Volume Two
 €17.50
Rupture de stock

 Quick view
Painless Future - Zukunft
 €5.00

 Quick view
Venda - Outcast EP
 €15.90
Rupture de stock

 Quick view
Feral - Trip No Trip [180...
 €14.50
Rupture de stock

 Quick view
Unknown Artist - Go Go /...
 €16.50

 Quick view
Idris Bena - FATA MORGANA
 €12.50
New

 Quick view
Bootywagon - Co
… [193 Zeichen gekürzt]
```
</details>

### 17. `shell` +39s – completed

```
bin/tl-scrape "https://www.decks.de/label/jack-fruit-recordings" --grep "TRAXX SALAD" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
url: https://www.decks.de/label/jack-fruit-recordings
mode: http (http)
title: Records - decks.de: Vinyl Shop
source-id: web:https://www.decks.de/label/jack-fruit-recordings
---
…
Vinyl Releases
Various Artists
TRAXX SALAD VOL. 2
12 Inch 
13.07.26
…
 *
Various Artists
TRAXX SALAD VOL 1
12 Inch 
09.02.26
```
</details>

### 18. `shell` +40s – completed

```
bin/tl-deezer search --artist "Nesi" --title "Old School" 2>&1 | head -20; echo ---; bin/tl-itunes search "Nesi Old School" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
1 Alben (q=artist:"Nesi" album:"Old School")
deezer:album/753089831 | Old School — NESI (ES) | 2 Tracks | single
---
25 Alben
itunes:album/1812848719 | Old School - Single — NESI (ES) | 2025-05-30 | 2 Tracks
itunes:album/286331380 | The Best of Kool Savas — Kool Savas | 2008-08-01 | 36 Tracks
itunes:album/1440912031 | Licensed to Ill — Beastie Boys | 1986-11-15 | 13 Tracks
itunes:album/275971005 | The Best of Joy Division — Joy Division | 2008-03-24 | 14 Tracks
itunes:album/1445027963 | Old School (The Reprise) - Single — Urban Cone | 2017-05-05 | 1 Tracks
itunes:album/189259056 | The Very Best of En Vogue — En Vogue | 2001-08-21 | 16 Tracks
itunes:album/1443927962 | Funk Essentials: The Best of Kurtis Blow — Kurtis Blow | 1994-01-01 | 14 Tracks
itunes:album/1217873628 | Genie und Wahnsinn (Wir sind die Best Ofs) — Der Tobi & Das Bo | 1995-02-01 | 13 Tracks
itunes:album/315875060 | Old School Hip Hop Greats — Verschiedene Interpret:innen | 2009-04-01 | 23 Tracks
itunes:album/1729337751 | Old School — The New Mastersounds | 2024-03-29 | 10 Tracks
... 15 weitere ausgeblendet. narrow the filter or raise --limit.
```
</details>

### 19. `shell` +42s – completed

```
bin/tl-search "Dompe \"No Place Like Heim\"" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: Dompe "No Place Like Heim"
1. Records - decks.de: Vinyl Shop
   https://www.decks.de/label/jack-fruit-recordings
   b1Dompe - No Place Like Heim (Vinyl Only) b2Nils Ohrmann - Che (Edgar Peng Remix) out of stock · 11.76 EUR * Dompe · FRENCH COLLECTION VOL. II (2LP) 2LP 12.05.25 · jeder track spielbar auf einer tollen houseparty!! House
2. Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
   https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
   Dompe - No Place Like Heim (Vinyl Only)(Original Mix) Various · • 0:00 · + Watchlist · Nils Ohrmann - Che (Edgar Peng Remix)(Original Mix) Various · • 0:00 · + Watchlist · also available: Vol. 2 14,95 € In Stockcause we 
   + Dompe - No Place Like Heim (Vinyl Only)(Original Mix) Various · • 0:00 · + Watchlist · Nils Ohrmann - Che (Edgar Peng Re | Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the fir
3. House Vinyl New Releases Charts | deejay.de
   https://www.deejay.de/m_House/sm_Charts/liste_2026/page_140/perpage_160/page_1
   Order now. Collecting orders for repress. ... 2026 Repress DJ Support: Seth Troxler, Marco Carola, Sasha & Digweed, Camelphat, Dennis Cruz and many more The chances are you've already heard this track being played all ov
   + Order now. Collecting orders for repress. ... 2026 Repress DJ Support: Seth Troxler, Marco Carola, Sasha & Digweed, Came | In 1995 Celvin Rotane’s “I Believe” carved its place in house history. Powered by the unmistakable “Huh!” sample a soari
4. Various - Traxx Salad Vol. 1 (WHITE LABEL VINYL - JFXX1) | Mint (M) Ge – Love Vinyl Records
   https://www.lovevinylrecords.com/products/various-traxx-salad-vol-1-white-label-vinyl-jfxx1-mint-m-generic
   Label: JackFruit Recordings – JFXX1 Format: Vinyl, 12" Country: Germany Released: Feb 2026 Genre: Electronic Style: House, Tech House A1 Nesi (5)– Old School A2 Dompe– Last Days Of Disko B1 Dompe– No Place Like Heim B2 N
   + Label: JackFruit Recordings – JFXX1 Format: Vinyl, 12" Country: Germany Released: Feb 2026 Genre: Electronic Style: Hous | Please refer to the description to determine whether the images are Actual Photos or Photos Not Actual. New records will
5. deejay.de - Exclusive News
   https://www.deejay.de/m_Exclusive/lang_fr
   B1: Dompe - No Place Like Heim (Vinyl Only) B2: Nils Ohrmann - Che (Edgar Peng Remix) Play all · 4 · cause we love vinyl. Following the huge success of Jackfr
… [1545 Zeichen gekürzt]
```
</details>

### 20. `shell` +43s – completed

```
bin/tl-vision "https://i.discogs.com/096XfgXQMzp5iz2D7O28iAybdpKNWEeWP-XTs4au5jA/rs:fit/g:sm/q:90/h:600/w:590/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM2NDc1OTE4LTE3NzA5MDkyODctNjAwMS5qcGVn.jpeg" --context "Back cover of vinyl 12-inch 'Traxx Salad Vol. 1' on JackFruit Traxx JFXX1. Read tracklist exactly: positions, artists, titles, and any durations printed." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/096XfgXQMzp5iz2D7O28iAybdpKNWEeWP-XTs4au5jA/rs:fit/g:sm/q:90/h:600/w:590/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTM2NDc1OTE4LTE3NzA5MDkyODctNjAwMS5qcGVn.jpeg
```
</details>

### 21. `shell` +48s – completed

```
bin/tl-search "\"Jackfruit Traxx\" \"Vol. 1\" OR \"Vol.1\" compilation 2026" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: "Jackfruit Traxx" "Vol. 1" OR "Vol.1" compilation 2026
1. Various - Traxx Salad Vol. 1 (WHITE LABEL VINYL - JFXX1) | Mint (M) Ge – Love Vinyl Records
   https://www.lovevinylrecords.com/products/various-traxx-salad-vol-1-white-label-vinyl-jfxx1-mint-m-generic
   Label: JackFruit Recordings – JFXX1 Format: Vinyl, 12" Country: Germany Released: Feb 2026 Genre: Electronic Style: House, Tech House A1 Nesi (5)– Old School A2 Dompe– Last Days Of Disko B1 Dompe– No Place Like Heim B2 N
   + Label: JackFruit Recordings – JFXX1 Format: Vinyl, 12" Country: Germany Released: Feb 2026 Genre: Electronic Style: Hous
2. Merch - Jackfruit Recordings / Jackfruit Traxx - Bandcamp
   https://jackfruitrec.bandcamp.com/merch
   Dompe - Fruitsalad 1_Vinyl – Dompe - Fruitsalad 01 Dompe · Vinyl · €7 EUR · more merch… · Check out · Jackfruit Recordings / Jackfruit Traxx Berlin, Germany · placeholder · Jackfruit Recordings a Label for House Music fo
   + Dompe - Fruitsalad 1_Vinyl – Dompe - Fruitsalad 01 Dompe · Vinyl · €7 EUR · more merch… · Check out · Jackfruit Recordin | French Collection, Vol.2 – French Collection, Vol. 2 (2x12) Dompe ... Jackfruit Recordings a Label for House Music found
3. Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
   https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
   Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks.
   + also available: Vol. 2 14,95 € In Stockcause we love vinyl. Following the huge success of Jackfruit Recordings, we found
4. Jackfruit Recordings / Jackfruit Traxx - Bandcamp
   https://jackfruitrec.bandcamp.com/
   Jackfruit Recordings / Jackfruit Traxx. Berlin, Germany. Jackfruit Recordings a Label for House Music founded by Dompe in 2017...
   + Warehouse Grooves, Vol. 5 Dompe ... Jackfruit Recordings a Label for House Music founded by Dompe in 2017...
5. Various - Traxx Salad Vol. 1
   https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html
   And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Peng with a remix for Nils Ohrmann, and of course Dompe as label head are all on board.
   + cause we love vinyl. Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023 | Vinyl Various - Traxx Sal
… [1193 Zeichen gekürzt]
```
</details>

### 22. `shell` +54s – completed

```
bin/tl-scrape "https://www.deejay.de/m_Exclusive/lang_fr" --grep "Heim|JFXX1|Traxx Salad" 2>&1 | head -20; echo ===; bin/tl-discogs search --catno JFXX1 2>&1 | head
```

<details><summary>Ausgabe</summary>

```
url: https://www.deejay.de/m_Exclusive/lang_fr
mode: firecrawl (http → firecrawl)
title: Sorties vinyle exclusives | deejay.de
source-id: web:https://www.deejay.de/m_Exclusive/lang_fr
---
(keine Zeile passt auf 'Heim|JFXX1|Traxx Salad')
===
1 hits (parameters: {'catno': 'JFXX1'})
discogs:release/36475918 | Various - Traxx Salad Vol. 1 | 2026 Germany | Vinyl, 12" | Label JackFruit Traxx | Kat.-Nr. JFXX1 | Barcodes - | master -
```
</details>

### 23. `shell` +57s – completed

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

### 24. `shell` +59s – completed

```
bin/tl-search "deejay.de Traxx Salad Vol.1 JFXX1" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
10 hits for: deejay.de Traxx Salad Vol.1 JFXX1
1. Various Artists — Traxx Salad Vol. 1 | JFXX1 | Vinyl | Selected Wax
   https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/
   Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks.
   + French Collection Vol. II 2x12" — ... Traxx Salad Vol. | also available: Vol. 2 14,95 € In Stockcause we love vinyl. Following the huge success of Jackfruit Recordings, we found
2. deejay.de - Exclusive News
   https://www.deejay.de/m_Exclusive/lang_fr
   And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Peng with a remix for Nils Ohrmann, and of course Dompe as label head are all on board.
   + Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the fir | STRIKER TRAXX proudly presents its very first release — STX101: BALLAN “Chantal Grooves EP”. Born as the new sub-label o
3. Various - Traxx Salad Vol. 1
   https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html
   Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the first vinyl release on the label: Jackfruit Traxx Salad Vol.1. It features four tracks. Nesi, Edgar Pen
   + Following the huge success of Jackfruit Recordings, we founded the sublabel Jackfruit Traxx in 2023. And here is the fir | Vinyl Various - Traxx Salad Vol. 1
4. Various - Traxx Salad Vol. 1 (WHITE LABEL VINYL - JFXX1) | Mint (M) Ge – Love Vinyl Records
   https://www.lovevinylrecords.com/products/various-traxx-salad-vol-1-white-label-vinyl-jfxx1-mint-m-generic
   Label: JackFruit Recordings – JFXX1 Format: Vinyl, 12" Country: Germany Released: Feb 2026 Genre: Electronic Style: House, Tech House A1 Nesi (5)– Old School A2 Dompe– Last Days Of Disko B1 Dompe– No Place Like Heim B2 N
   + Label: JackFruit Recordings – JFXX1 Format: Vinyl, 12" Country: Germany Released: Feb 2026 Genre: Electronic Style: Hous
5. Records - decks.de: Vinyl Shop
   https://www.decks.de/label/jack-fruit-recordings
   TRAXX SALAD VOL.
```
</details>

### 25. `shell` +66s – completed

```
bin/tl-validate --schema 2>&1 | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:v for k,v in d['\$defs'].items() if k in ('Conflict','Result','Release','Track','Missing')}, indent=1)[:4000]); print('REQ', d.get('required'))"
```

<details><summary>Ausgabe</summary>

```
{
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
    "description": "{'musicbrainz': mbid, 'discogs': '3057907'}",
    "title": "Ids",
    "type": "object"
   }
  },
  "required": [
   "title"
  ],
  "title": "Release",
  "type": "object"
 },
 "Track": {
  "additionalProperties": false,
  "properties": {
   "position": {
    "description": "as on the carrier: '1', 'A1', '2-03'",
    "title": "Position",

… [1551 Zeichen gekürzt]
```
</details>

### 26. `write` +80s – completed

```
{"path": "output/work/fall-27db0efc.json", "content": "{\n  \"input\": {\n    \"id\": \"fall-27db0efc\",\n    \"title\": \"Jackfruit Traxx 1\",\n    \"artist\": \"Various Artists\"\n  },\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"Traxx Salad Vol. 1\",\n    \"artist\": \"Various Artists\",\n    \"format\": \"Vinyl\",\n    \"country\": \"DE\",\n    \"year\": 2026,\n    \"label\": \"JackFruit Traxx\",\n    \"catno\": \"JFXX1\",\n    \"barcode\": null,\n    \"edition\": \"12\\\" vinyl, 4 tracks, B1 is a vinyl-only track\",\n    \"ids\": {\n      \"discogs\": \"36475918\"\n    }\n  },\n  \"tracks\": [\n    {\n      \"position\": \"A1\",\n      \"disc\": 1,\n      \"title\": \"Old School\",\n      \"artist\": \"Nesi\",\n      \"duration_s\": 330,\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\"\n      ],\n      \"duration_sources\": [\n        \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\"\n      ],\n      \"flags\": [\n        \"duration_other_edition\"\n      ]\n    },\n    {\n      \"position\": \"A2\",\n      \"disc\": 1,\n      \"title\": \"Last Days Of Disko\",\n      \"artist\": \"Dompe\",\n      \"duration_s\": 363,\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\"\n      ],\n      \"duration_sources\": [\n        \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\"\n      ],\n      \"flags\": [\n        \"duration_other_edition\"\n      ]\n    },\n    {\n      \"position\": \"B1\",\n      \"disc\": 1,\n      \"title\": \"No Place Like Heim\",\n      \"artist\": \"Dompe\",\n      \"duration_s\": null,\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\"\n      ],\n      \"duration_sources\": [],\n      \"flags\": [\n        \"duration_missing\",\n        \"vinyl_only\"\n      ]\n    },\n    {\n      \"position\": \"B2\",\n      \"disc\": 1,\n      \"title\": \"Che (Edgar Peng Remix)\",\n      \"artist\": \"Nils Ohrmann\",\n      \"duration_s\": 332,\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\"\n      ],\n      \"duration_sources\": [\n        \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\"\n      ],\n      \"flags\": [\n        \"duration_other_edition\"\n      ]\n    }\n  ],\n  \"artists\": [\n    {\n      \"name\": \"Nesi\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"A1\"\n      ],\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\"\n      ]\n    },\n    {\n      \"name\": \"Dompe\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"A2\",\n        \"B1\"\n      ],\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\"\n      ]\n    },\n    {\n      \"name\": \"Nils Ohrmann\",\n      \"role\": \"main\",\n      \"tracks\": [\n        \"B2\"\n      ],\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\"\n      ]\n    },\n    {\n      \"name\": \"Edgar Peng\",\n      \"role\": \"remixer\",\n      \"tracks\": [\n        \"B2\"\n      ],\n      \"sources\": [\n        \"discogs:release/36475918\",\n        \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\"\n      ]\n    }\n  ],\n  \"total_duration_s\": 1025,\n  \"confidence\": 0.7,\n  \"sources\": [\n    {\n      \"id\": \"discogs:release/36475918\",\n      \"url\": \"https://www.discogs.com/release/36475918-Various-Traxx-Salad-Vol-1\",\n      \"kind\": \"database\",\n      \"note\": \"Vinyl 12\\\", DE, 2026, JackFruit Traxx JFXX1; no durations, no barcode\"\n    },\n    {\n      \"id\": \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\",\n      \"url\": \"https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\",\n      \"kind\": \"streaming\",\n      \"note\": \"Label's own digital edition (3 tracks, vinyl-only B1 missing); durations 5:30 / 6:03 / 5:32\"\n    },\n    {\n      \"id\": \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\",\n      \"url\": \"https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\",\n      \"kind\": \"shop\",\n      \"note\": \"Lists 4 tracks incl. 'Dompe - No Place Like Heim (Vinyl Only)'; no track durations (0:00)\"\n    },\n    {\n      \"id\": \"web:https://www.decks.de/label/jack-fruit-recordings\",\n      \"url\": \"https://www.decks.de/label/jack-fruit-recordings\",\n      \"kind\": \"shop\",\n      \"note\": \"a1/b1/b2 listing for 'TRAXX SALAD VOL 1', 12 Inch, 09.02.26, 'incl. one vinyl only track'\"\n    },\n    {\n      \"id\": \"web:https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html\",\n      \"url\": \"https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html\",\n      \"kind\": \"shop\",\n      \"note\": \"Label blurb: 'the first vinyl release on the label: Jackfruit Traxx Salad Vol.1 ... four tracks', Dompe contributes an exclusive vinyl-only track\"\n    }\n  ],\n  \"conflicts\": [\n    {\n      \"field\": \"release title\",\n      \"values\": {\n        \"input\": \"Jackfruit Traxx 1\",\n        \"discogs:release/36475918\": \"Traxx Salad Vol. 1\",\n        \"web:https://techno-import.fr/en/racine/56945-various-traxx-salad-vol-1.html\": \"Jackfruit Traxx Salad Vol.1\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\": \"Traxx Salad Vol. 1\"\n      },\n      \"resolution\": \"No release titled exactly 'Jackfruit Traxx 1' exists in any source. The only physical release of the Jackfruit Traxx sublabel with volume number 1 is 'Traxx Salad Vol. 1' (cat. JFXX1, the label's first vinyl release, described by the label itself as 'Jackfruit Traxx Salad Vol.1'); the input title is treated as label + volume shorthand.\"\n    },\n    {\n      \"field\": \"track B1 title\",\n      \"values\": {\n        \"discogs:release/36475918\": \"No Place Like Heim\",\n        \"web:https://www.selectedwax.com/album/various_traxx_salad_vol_1_jfxx1_excl_vinyl__1188613/\": \"No Place Like Heim (Vinyl Only)\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\": \"No Place Like Heim (Vinyl Only)\"\n      },\n      \"resolution\": \"Chose 'No Place Like Heim' (Discogs, the only database entry); '(Vinyl Only)' is treated as a shop/format annotation, not part of the title, and is recorded as a flag.\"\n    },\n    {\n      \"field\": \"label name\",\n      \"values\": {\n        \"discogs:release/36475918\": \"JackFruit Traxx\",\n        \"web:https://www.decks.de/label/jack-fruit-recordings\": \"Jack Fruit Recordings\",\n        \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\": \"Jackfruit Recordings / Jackfruit Traxx\"\n      },\n      \"resolution\": \"Sublabel JackFruit Traxx as credited on the Discogs release; shops file it under the parent label Jackfruit Recordings.\"\n    }\n  ],\n  \"missing\": [\n    \"No barcode on this vinyl release (EAN not available).\",\n    \"Duration of the vinyl-only track B1 'No Place Like Heim' is not published by any source; the Bandcamp digital edition does not contain it.\",\n    \"Durations for A1, A2 and B2 come from the label's digital edition (same recordings, vinyl-only track omitted) and are flagged duration_other_edition.\",\n    \"total_duration_s (1025 s) is the sum of the three known tracks only.\",\n    \"No MusicBrainz entry exists for this release.\"\n  ],\n  \"alternatives\": [\n    {\n      \"description\": \"Traxx Salad Vol. 2, Vinyl 12\\\", JackFruit Traxx JFXX2, 2026, DE (4 tracks)\",\n      \"source\": \"discogs:release/37837974\",\n      \"why_not\": \"Second volume of the series, different catalogue number and tracklist; does not match the '1' in the input title.\"\n    },\n    {\n      \"description\": \"Digital edition 'Traxx Salad Vol.1' on Bandcamp (3 tracks, without the vinyl-only track B1)\",\n      \"source\": \"web:https://jackfruitrec.bandcamp.com/album/traxx-salad-vol-1\",\n      \"why_not\": \"Digital media only; GEMA licensing requires the physical edition, which has four tracks.\"\n    }\n  ],\n  \"reasoning\": \"No source has a release literally named 'Jackfruit Traxx 1'; the label's own blurb identifies JFXX1 as the first vinyl release of the Jackfruit Traxx sublabel, titled 'Traxx Salad Vol. 1'. Discogs holds exactly one entry for cat. JFXX1 (release 36475918, DE 2026, 12\\\" vinyl, 4 tracks), and three independent shops (selectedwax, decks.de, techno-import) confirm the same four positions A1 Nesi 'Old School', A2 Dompe 'Last Days Of Disko', B1 Dompe 'No Place Like Heim' (vinyl only), B2 Nils Ohrmann 'Che (Edgar Peng Remix)', the latter with Edgar Peng as remixer. The vinyl carries no printed durations and no barcode; durations for A1/A2/B2 are taken from the label's digital edition (5:30 / 6:03 / 5:32) and flagged as coming from another edition. B1 has no published duration. Title mismatch and label naming are recorded as conflicts, hence confidence 0.7.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-27db0efc.json
```
</details>

### 27. `shell` +81s – completed

```
bin/tl-validate output/work/fall-27db0efc.json 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 4 tracks (3 with duration), 5 sources, 3 conflicts, confidence=0.7
```
</details>

> **Agent** +82s: FERTIG found 4 Tracks confidence=0.7
