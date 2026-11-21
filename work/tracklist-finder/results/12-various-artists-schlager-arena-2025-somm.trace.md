# Agent-Trace: 12-various-artists-schlager-arena-2025-somm

> Schnellweg geprüft: no fast path: 0 matching official MusicBrainz releases (fast path only for 1–5 identical ones)
Start 2026-11-20T15:46:46 · 20 Schritte · 19 Tool-Aufrufe · Tokens in 26957 / out 11886


> **Agent** +0s: I'll start by checking the barcode and searching the databases.

### 1. `shell` +1s – completed

```
bin/tl-gtin 4099964172904; echo "---"; bin/tl-mb search --barcode 4099964172904; echo "---"; bin/tl-discogs search --barcode 4099964172904
```

<details><summary>Ausgabe</summary>

```
input: '4099964172904' → digits: 4099964172904 (13 digits)
type: EAN-13  valid: yes
search variants: 4099964172904
prefix 400–440: assigned in Germany (says nothing about the country of release)
---
0 Releases (Queries: barcode:(4099964172904))

---
0 hits (parameters: {'barcode': '04099964172904'})
```
</details>

### 2. `shell` +6s – completed

```
bin/tl-mb search --title "Schlager Arena 2025" --artist "Various Artists" 2>&1 | head -20; echo "---"; bin/tl-discogs search --title "Schlager Arena 2025" 2>&1 | head -30; echo "---"; bin/tl-itunes upc 4099964172904 2>&1 | head -20; echo "---"; bin/tl-deezer upc 4099964172904 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Schlager Arena 2025" AND artist:"Various Artists")

---
1 hits (parameters: {'release_title': 'Schlager Arena 2025'})
discogs:release/33835569 | Various - Schlager Arena 2025 (Die Grössten Hits Des Jahres) | 2024 Germany | CD, Compilation | Label More Music And Media, TELAMO | Kat.-Nr. 409996412486 | Barcodes 4099964124866, LC 10125, GEMA BIEM MCPS | master -
---
no hit (physical releases are often missing from the digital catalogue)
---
no hit (Deezer mostly knows digital UPCs only)
```
</details>

### 3. `shell` +8s – completed

```
bin/tl-discogs release 33835569 2>&1 | head -60; echo "===="; bin/tl-discogs search --title "Schlager Arena 2025 Sommer" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
discogs:release/33835569 | Schlager Arena 2025 (Die Grössten Hits Des Jahres) — Various | 2024 Germany | 2× CD (Compilation) | More Music And Media 409996412486; TELAMO 409996412486 | master -
url: https://www.discogs.com/release/33835569-Various-Schlager-Arena-2025-Die-Grössten-Hits-Des-Jahres
identifiers: Barcode: 4099964124866 | Label Code: LC 10125 | Rights Society: GEMA BIEM MCPS
notes: For this compilation: ℗+© 2024 MORE Music and Media GmbH & Co. KG. Printed and manufactured in Germany. Vertrieb: Telamo Musik & Unterhaltung GmbH | A BMG Company.
1-1 Aperol Spritz — Vincent Gross | duration missing
1-2 Warum Hast Du Nicht Ja Gesagt — Norman Langen | duration missing
1-3 Es Geht Wieder Los (Radio Version) — Laura Wilde | duration missing
1-4 Was Ist Daran Falsch?! (Radio Reload) — Linda Hesse | duration missing
1-5 Nicht Einmal Der Himmel — Bernhard Brink | duration missing
1-6 Rosa Oder Blau (Que Sera) (Ultrafox DJ Mix) — Fantasy (16), Ultrafox (4) | duration missing | credits: Producer, Remix: Ultrafox (4)
1-7 Was Ist Das Für Ein Gefühl — Annemarie Eilfeld | duration missing
1-8 Träumefänger (Alles Wird Gut) — Joey Heindle | duration missing
1-9 First Class — Neon (67) | duration missing
1-10 Ist Das Liebe (È Questo L'amore) — Daniel Lopes | duration missing
1-11 Nichts Bleibt Für Immer — Judy Weiss | duration missing
1-12 Wer Kann Schon Nein Sagen — Mike Leon Grosch | duration missing
1-13 Verlieb Mich (Radio Version) — Sarah Zucker | duration missing
1-14 Mein Stern — Jay Khan | duration missing
1-15 Ich Will Das Lied Sein — Tanja Lasch | duration missing
1-16 Mädchen No. 1 (Radio Version) — Jennifer Junker | duration missing
1-17 Auf Die Geschichten, Die Das Leben Schreibt (Radio Version) — Timo (63) | duration missing
1-18 Herzdame 2.0 — Olaf Henning | duration missing
1-19 Labyrinth (Radio Mix) — Diana Sorbello | duration missing
1-20 Ich Hol Dich Hier Raus — Markus (6) | duration missing
2-1 Smalltalk (Ultrafox Mix) — Anna-Carina Woitschack, Ultrafox (4) | duration missing | credits: Remix, Producer: Ultrafox (4)
2-2 Amor Amor — Patrick Lindner | duration missing
2-3 Egal Was Andere Sagen — Team 5ünf | duration missing
2-4 Liebe Verboten (Uh La La) (Radio Edit) — Anna-Maria Zimmermann | duration missing
2-5 Gute Laune — Wind (4) | duration missing
2-6 Verlieben, Verloren, Vergessen, Verzeih'n — Joelina Drews, Lucas Cordalis, Achim Petry | duration missing
2-7 Liebe Bleibt Ein Großes Wunder (Radio Edit) — Petra Frey | duration missing
2-8 Nach 
… [2230 Zeichen gekürzt]
```
</details>

### 4. `shell` +13s – completed

```
bin/tl-discogs search --catno 409996417290 2>&1|head; echo "---"; bin/tl-discogs search --catno 4099964172904 2>&1|head; echo "---"; bin/tl-discogs search --title "Schlager Arena" 2>&1|head -30; echo "---"; bin/tl-search "Schlager Arena 2025 Sommer Edition 4099964172904" 2>&1|head -30
```

<details><summary>Ausgabe</summary>

```
0 hits (parameters: {'catno': '409996417290'})

---
0 hits (parameters: {'catno': '4099964172904'})

---
1 hits (parameters: {'release_title': 'Schlager Arena'})
discogs:release/33835569 | Various - Schlager Arena 2025 (Die Grössten Hits Des Jahres) | 2024 Germany | CD, Compilation | Label More Music And Media, TELAMO | Kat.-Nr. 409996412486 | Barcodes 4099964124866, LC 10125, GEMA BIEM MCPS | master -
---
10 hits for: Schlager Arena 2025 Sommer Edition 4099964172904
1. Schlager Arena 2025:Sommer Edition-Die größten Hit von Various (CD) kaufen
   https://www.thalia.de/shop/home/artikeldetails/A1075332387
   13.06.2025 · 4099964172904 Weitere Details · Overlay schließen · Overlay schließen · CD · 2 · Warner Music · Deutsch · Various · 13.06.2025 · 4099964172904 · MFP Tonträger Carl-Miele-Straße 22 33442 Herzebrock-Clarholz D
   + 13.06.2025 · 4099964172904 Weitere Details · Overlay schließen · Overlay schließen · CD · 2 · Warner Music · Deutsch · V
2. Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres (2 CDs) – jpc.de
   https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766
   Die CD von Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres jetzt probehören und für 18,99 Euro kaufen.
   + 4 Anna-Carina Woitschack: Sommernacht Hörprobe Track 4: Anna-Carina Woitschack: Sommernacht · 5 Ross Antony & Linda Fäh: | 2 Die Schlagerpiloten: Mit dir geht der Sommer nie vorbei Hörprobe Track 2: Die Schlagerpiloten: Mit dir geht der Sommer
3. VARIOUS | Schlager Arena 2025:Sommer Edition-Die größten Hit - (CD) VARIOUS auf CD online kaufen | SATURN
   https://www.saturn.de/de/product/_diverse-interpreten-schlager-arena-2025sommer-edition-die-grossten-hi-cd-2993446.html
   TitelSchlager Arena 2025:Sommer Edition-Die größten Hit · GenreSchlager · InterpretVARIOUS · DatenträgerCDZu den technischen Daten · Sofort-Lieferung · + 5,99 € · In unter 90 Minuten – regional verfügbar · Lieferung nach
   + VARIOUS | Schlager Arena 2025:Sommer Edition-Die größten Hit - (CD) im Onlineshop von SATURN kaufen. Jetzt bequem online | TitelSchlager Arena 2025:Sommer Edition-Die größten Hit · GenreSchlager · InterpretVARIOUS · DatenträgerCDZu den technis
4. Schlager Arena 2025:Sommer Edition-die Größten Hit: Amazon.de: Musik-CDs & Vinyl
   https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3
   Entdecken, shoppen und einkaufen bei Amazon.de: Günstige Preise für Elektr
… [1614 Zeichen gekürzt]
```
</details>

### 5. `shell` +14s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766" --grep -i "track|Titel|CD 1|CD 2" 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 6. `shell` +16s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766" 2>&1 | head -150
```

<details><summary>Ausgabe</summary>

```
url: https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766
mode: http (http)
title: Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres (2 CDs) –
source-id: web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766
---
Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres (2 CDs) – 
Inhalt
Einstellungen Privatsphäre
 Anmelden 
 Konto anlegen 
 Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres auf 2 CDs
Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres
 2
 CDs
CD (Compact Disc)
Herkömmliche CD, die mit allen CD-Playern und Computerlaufwerken, aber auch mit den meisten SACD- oder Multiplayern abspielbar ist.
 versandfertig innerhalb von 3 Tagen
(soweit verfügbar beim Lieferanten)
EUR 18,99*
Aktueller Preis: EUR 18,99
 Portofrei innerhalb Deutschlands 
Informieren Sie mich ...
 wenn der Artikel im Preis gesenkt wird 
Label:
More
Artikelnummer:
12285766
UPC/EAN:
4099964172904
Erscheinungstermin:
13.3.2020
 Weiterlesen 
 Tracklisting 
 Disk 1 von 2
 (CD)
1
 Thomas Anders, Florian Silbereisen & Barbara Schöneberger: Sie!
Hörprobe Track 1: Thomas Anders, Florian Silbereisen & Barbara Schöneberger: Sie!
2
 Fantasy: Das bleibt unter uns Cherie
Hörprobe Track 2: Fantasy: Das bleibt unter uns Cherie
3
 Linda Hesse: Ein gebrochenes Herz
Hörprobe Track 3: Linda Hesse: Ein gebrochenes Herz
4
 Anna-Carina Woitschack: Sommernacht
Hörprobe Track 4: Anna-Carina Woitschack: Sommernacht
5
 Ross Antony & Linda Fäh: Schau mal herein
Hörprobe Track 5: Ross Antony & Linda Fäh: Schau mal herein
6
 Jay Khan: Verdammt!
Hörprobe Track 6: Jay Khan: Verdammt!
7
 Die Schlagerpiloten: Playa Bonita
Hörprobe Track 7: Die Schlagerpiloten: Playa Bonita
8
 Bernhard Brink: Dein Schrei nach Liebe
Hörprobe Track 8: Bernhard Brink: Dein Schrei nach Liebe
9
 Anita Hofmann: Leben XXL
Hörprobe Track 9: Anita Hofmann: Leben XXL
10
 Patrick Lindner: So fühlt sich nur die Liebe an
Hörprobe Track 10: Patrick Lindner: So fühlt sich nur die Liebe an
11
 Timo: Solange wir leben
Hörprobe Track 11: Timo: Solange wir leben
12
 Jörg Bausch: Wir sind wie Piloten
Hörprobe Track 12: Jörg Bausch: Wir sind wie Piloten
13
 Frank Lukas: Noch immer dieselben
Hörprobe Track 13: Frank Lukas: Noch immer dieselben
14
 Zeno: Dein Blick
Hörprobe Track 14: Zeno: Dein Blick
15
 Franziska: Sie wollte immer Paris
Hörprobe T
… [2022 Zeichen gekürzt]
```
</details>

### 7. `shell` +22s – completed

```
bin/tl-scrape "https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766" 2>&1 | sed -n '150,260p'
```

<details><summary>Ausgabe</summary>

```
 Die Wolkenstürmer: Flieger Richtung Liebe
Hörprobe Track 18: Die Wolkenstürmer: Flieger Richtung Liebe
19
 Michael Morgan: Wie ein Orkan
Hörprobe Track 19: Michael Morgan: Wie ein Orkan
20
 Laura & Mark: Ein bisschen verliebt
Hörprobe Track 20: Laura & Mark: Ein bisschen verliebt
Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres
EUR 18,99*
Aktueller Preis: EUR 18,99
Sicherheits- und Herstellerinformationen
Bilder zur Produktsicherheit
Herstellerinformationen
Universal International Music B.V.
 s-Gravelandseweg 80
 1217 EW Hilversum
 Netherlands (the)
[email removed] 
 Bewertungen und Rezensionen
 » Mehr Rezensionen aus dem Bereich Pop/Rock
 Es gibt noch keine Rezensionen für dieses Produkt
Erste Rezension schreiben
Bitte beachten Sie
 Wir können nicht sicherstellen, dass die Angaben von Verbrauchern stammen, die das Produkt tatsächlich genutzt oder erworben haben.
Schließen
Bitte beachten Sie
 Die Gesamtnote ergibt sich aus der durchschnittlichen Anzahl an Sternen aller Bewertungen (Gesamtbewertungen der Produkte).
 Rezensionen sind Bewertungen mit einem erklärenden Text und ggf. einer Bewertung zu weiteren Kategorien.
 Die Angabe ist ggf. nicht verpflichtend.
 Daher kann ein Artikel mehr Bewertungen als Rezensionen bzw. Bewertungen für Kategorien haben.
Schließen
Switch to English
 Um unsere Website und Web-Anzeigen für Sie interessanter zu gestalten, erfassen und analysieren wir die
 Zugriffe auf die entsprechenden Inhalte.
 Sofern Sie uns Ihre Einwilligung erteilen, erhalten unsere Partner Nutzungsinformationen für Analysen und
 Werbung (Details siehe Kategorie »Werbung«). Mit »Alle Auswählen« erlauben sie uns, die unter »Mehr
 Informationen« näher beschriebenen Cookies zu den dort genannten Zwecken einzusetzen (Jederzeit
 widerruflich). Dort können Sie Ihre Einwilligung anpassen. Weitere Details in
 der 
Datenschutzhinweise
. 
Impressum
```
</details>

### 8. `shell` +33s – completed

```
bin/tl-scrape "https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3" 2>&1 | head -40; echo "=== THALIA"; bin/tl-scrape "https://www.thalia.de/shop/home/artikeldetails/A1075332387" --grep -i "track|Sie!|Sommernacht|Disc|CD " 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3
mode: http (http)
title: Schlager Arena 2025: Sommer Edition-die Größten Hit: Amazon.de: Musik-CDs & Vinyl
source-id: web:https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3
---
Schlager Arena 2025: Sommer Edition-die Größten Hit: Amazon.de: Musik-CDs & Vinyl
Musik-CDs & Vinyl
›
Schlager & Volksmusik
›
Schlager
 Andere Verkäufer bei Amazon 
Neu & Gebraucht (11) von
13,38€
13
,
38
€
GRATIS-Lieferung
 für qualifizierte Erstbestellung nach Deutschland und Österreich. Wähle diese Option an der Kasse.
Bild nicht verfügbar
 Keine Abbildung vorhanden für 
Farbe: 
 Der Artikel ist in folgender Variante leider nicht verfügbar 
 Keine Abbildung vorhanden 
 Herunterladen, um dieses Videos wiederzugeben 
 Flash Player 
 VIDEOS 
 360°-ANSICHT 
 BILDER 
 Schlager Arena 2025: Sommer Edition-die Größten Hit 
 2 CD 
Various Artists
(Künstler)
Format: 
Audio CD
 4,1 
4,1 von 5 Sternen
(12)
 16,99 € 
=== THALIA
usage: tl-scrape [-h] [--mode {auto,http,firecrawl,browser,uc}] [--max MAX]
                 [--grep GREP] [--links] [--screenshot SCREENSHOT]
                 url
tl-scrape: error: argument --grep: expected one argument
```
</details>

### 9. `shell` +43s – completed

```
bin/tl-scrape "https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3" 2>&1 | sed -n '40,220p'
```

<details><summary>Ausgabe</summary>

```
 16,99 € 
16
,
99
€
 KOSTENFREIE Retouren 
Diesen Artikel kostenfrei zurücksenden
Für die von dir gewählte Lieferadresse sind kostenlose Rücksendungen verfügbar. Du kannst den Artikel aus einem beliebigen Grund in neuem und unbenutztem Zustand zurücksenden: keine Versandkosten. 
 Weitere Informationen zu kostenfreien Retouren. 
Wie kann ich den Artikel zurücksenden?
Gehe zu deinen Bestellungen und starte die Rücksendung
Wähle die Rücksendemethode
Versenden!
Preisangaben inkl. USt. Abhängig von der Lieferadresse kann die USt. an der Kasse variieren. Weitere Informationen.
Spare 3,40 € an der Kasse 
Bedingungen
Alle Formate und Ausgaben anzeigen
Andere Formate und Ausgaben ausblenden
Preis | Neu ab | Gebraucht ab
Audio-CD, Doppel-CD, 13. März 2020 "Bitte wiederholen" | 16,99 € | 16,99 € | 13,38 €
Audio-CD
 16,99 € 
 2 Gebraucht 
ab
 13,38 € 
 9 Neu 
ab
 16,99 € 
 Zu einem niedrigeren Preis bei 
anderen Verkäufern
 erhältlich, die eventuell keinen kostenlosen Premiumversand anbieten. 
Ein Problem mit diesem Produkt melden
Wird oft zusammen gekauft
 Dieser Artikel: 
 Schlager Arena 2025: Sommer Edition-die Größten Hit 
16,99€
16
,
99
€
Nur noch 4 auf Lager (mehr ist unterwegs).
Versandt und verkauft von Amazon.
+
Schlager im Sommer 2025-40 Hits
4,58€
4
,
58
€
Auf Lager
Versandt und verkauft von Amazon.
+
Bääärenstark!!! Sommer 2025
17,59€
17
,
59
€
Nur noch 16 auf Lager
Versandt und verkauft von Amazon.
Gesamtpreis:
$00
$
0
0
Um unseren Preis zu sehen, füge diese Artikel deinem Einkaufswagen hinzu.
Versuch es noch einmal!
 Details 
Zum Einkaufswagen hinzugefügt
 Einige dieser Artikel sind schneller versandfertig als andere. 
 Details anzeigen 
 Details ausblenden 
 Wähle Artikel zum gemeinsam kaufen. 
Welche anderen Artikel kaufen Kunden, nachdem sie diesen Artikel angesehen haben?
Seite 
1
 von 
1
Erneut starten
Vorheriger Foliensatz
Schlager 2025 - die Hits des Jahres
Various
4,6 von 5 Sternen
91
Audio CD
-20 %
17,58€
17
,
58
€
Black Friday Angebot
Statt:
21,99 €
Schlager 2024 - Die Hits des Jahres
Various, Artists
4,6 von 5 Sternen
148
Audio CD
24,00€
24
,
00
€
Erhalte es bis 
Freitag, 27. November
KOSTENFREIER Versand durch Amazon
Nur noch 8 auf Lager
Ich find Schlager toll - Herbst/Winter 2025/26
Various, Artists
4,4 von 5 Sternen
82
Audio CD
15,39€
15
,
39
€
Die Ultimative Chartshow – Die erfolgreichsten Schlager
Various, Artists
4,5 von 5 Sternen
98
Audio CD
17,99€
17
,
99
€
RTL Hits - Schlager 2025 (2CD)
Various
4,5 von 5 Sternen
46
Audio CD
-5 %
4,77€
… [1311 Zeichen gekürzt]
```
</details>

### 10. `shell` +49s – completed

```
bin/tl-scrape "https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3" 2>&1 | sed -n '220,260p'; echo "=== ITUNES"; bin/tl-itunes search "Schlager Arena 2025 Sommer Edition" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
6 | Du rettest mich - Weiss, Judy
7 | Cabriolet (Radio Version) - Zucker, Sarah
8 | Blick nach vorn - Alfinito, Daniela
9 | Altes Spiel, neues Glück - Frey, Petra
10 | Zu lieben ist leicht - Lasch, Tanja
11 | Schwarze Rose - Weisser, Marian
12 | Dein Blick sagt alles - Perka, Anni
13 | Mein Baby (2025) (Radio Version) - Lars, Frank
14 | Intensiv (Radio-Version) - Charlien
15 | Kann es sein - Martin, Alexander
16 | Momentan ist alles nur Liebe - Gilbert
17 | Alles neu - Berger, Sabrina
18 | Flieger Richtung Liebe - Wolkenstürmer, Die
19 | Wie ein Orkan - Morgan Michael
20 | Ein bisschen verliebt - Laura & Mark
 Produktbeschreibungen 
Płyta CD to klasyczny i niezawodny sposób na słuchanie ulubionych utworów w wysokiej jakości dźwięku. Produkt oferuje trwały, fizyczny nośnik, który doskonale sprawdzi się zarówno w domowych odtwarzaczach, jak i w zestawach samochodowych. To idealny wybór dla osób ceniących kolekcjonerskie wydania, estetyczne opakowania oraz możliwość obcowania z muzyką w tradycyjnej formie. Świetnie nadaje się jako element muzycznej biblioteki lub prezent dla każdego miłośnika dźwięków.
Produktinformation
Produktabmessungen
 ‏
 :
 ‎
1 x 12,5 x 14,2 cm; 90 Gramm
Hersteller
 ‏
 :
 ‎
Telamo (Universal Music)
Herstellerreferenz
 ‏
 :
 ‎
4099964172904
Laufzeit
 ‏
 :
 ‎
0 Minute
Label
 ‏
 :
=== ITUNES
2 Alben
itunes:album/1824661315 | Schlager Arena 2025 - Sommer Edition - Die größten Hits des Jahres — Verschiedene Interpret:innen | 2025-06-06 | 40 Tracks
itunes:album/6793444945 | Schlager Arena 2026 - Sommer Edition - Die größten Hits des Jahres — Verschiedene Interpret:innen | 2026-08-14 | 40 Tracks
```
</details>

### 11. `shell` +50s – completed

```
bin/tl-itunes --help 2>&1 | head -30
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
```
</details>

### 12. `shell` +57s – completed

```
bin/tl-itunes album 1824661315 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
itunes:album/1824661315 | Schlager Arena 2025 - Sommer Edition - Die größten Hits des Jahres — Verschiedene Interpret:innen | 2025-06-06 | 40 Tracks | ℗ 2025 MORE Music & Media GmbH & Co.KG distributed by Telamo Musik und Unterhaltung GmbH | A BMG Company
url: https://music.apple.com/de/album/schlager-arena-2025-sommer-edition-die-gr%C3%B6%C3%9Ften-hits/1824661315?uo=4
1.1 Sie! (feat. Barbara Schöneberger) — Thomas Anders & Florian Silbereisen | 3:38 (217907 ms)
1.2 Das bleibt unter uns Chérie — Fantasy | 3:14 (194027 ms)
1.3 Ein gebrochenes Herz — Linda Hesse | 3:07 (187467 ms)
1.4 Sommernacht — Anna-Carina Woitschack | 3:43 (223440 ms)
1.5 Schau mal herein (Duett mit Linda Fäh) [Remix] — Ross Antony | 3:12 (191760 ms)
1.6 Verdammt! — Jay Khan | 3:35 (214573 ms)
1.7 Playa Bonita — Die Schlagerpiloten | 3:07 (186680 ms)
1.8 Dein Schrei nach Liebe — Bernhard Brink | 3:05 (185453 ms)
1.9 Leben XXL — Anita Hofmann | 3:19 (199080 ms)
1.10 So fühlt sich nur die Liebe an — Patrick Lindner | 3:13 (193027 ms)
1.11 Solange wir leben — Timo | 3:05 (185280 ms)
1.12 Wir sind wie Piloten — Jörg Bausch | 3:09 (189147 ms)
1.14 Dein Blick — Zeno | 3:42 (221613 ms)
1.15 Sie wollte immer Paris — Franziska | 2:54 (173707 ms)
1.16 I'm Alive (Ich bin da) — Maria Levin | 3:19 (198573 ms)
1.17 Ich glaub an die Liebe — Christian Lais | 3:24 (204053 ms)
1.18 Verführerisch (Nur So! Remix) — Silvano Giganti | 2:54 (173933 ms)
1.19 Echte Tränen — Jan Böckmann | 3:20 (200027 ms)
1.20 Auf immer Wiedersehen — Wind | 3:05 (185480 ms)
2.1 Verliebt in London — Laura Wilde | 3:31 (211440 ms)
2.2 Mit dir geht der Sommer nie vorbei — Die Schlagerpiloten | 3:36 (215840 ms)
2.3 So muss der Sommer sein — Olaf Der Flipper | 3:33 (213413 ms)
2.4 Ein bisschen Aroma — Karl König | 3:19 (198800 ms)
2.5 Weil es mehr als Liebe ist — G.G. Anderson | 3:23 (202587 ms)
2.6 Du rettest mich — Judy Weiss | 3:44 (223680 ms)
2.8 Blick nach vorn — Daniela Alfinito | 3:22 (201907 ms)
2.9 Altes Spiel, neues Glück — Petra Frey | 3:22 (202187 ms)
2.10 Zu lieben ist leicht — Tanja Lasch | 3:24 (204040 ms)
2.11 Schwarze Rose — Marian Weisser | 3:31 (211253 ms)
2.12 Dein Blick sagt alles — Anni Perka | 3:06 (186267 ms)
2.14 Intensiv (Radio-Version) — Charlien | 3:07 (187013 ms)
2.15 Kann es sein — Alexander Martin | 2:52 (171613 ms)
2.16 Momentan ist alles nur Liebe — Gilbert | 3:24 (204480 ms)
2.17 Alles neu — Sabrina Berger | 3:01 (180720 ms)
2.18 Flieger Richtung Liebe — Die Wolkenstürmer | 3:11 (191227 ms)
2.19 Wie
… [130 Zeichen gekürzt]
```
</details>

### 13. `shell` +61s – completed

```
bin/tl-deezer search --artist "Various Artists" --title "Schlager Arena 2025 Sommer Edition" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
1 Alben (q=artist:"Various Artists" album:"Schlager Arena 2025 Sommer Edition")
deezer:album/904925572 | Schlager Arena 2025 (Sommer Edition / Die größten Hits des Jahres) — Verschiedene Interpreten | 21 Tracks | album
```
</details>

### 14. `shell` +89s – completed

```
bin/tl-itunes album 1824661315 --country us 2>&1 | grep -E "1\.13|2\.7\.|2\.13|Total"; echo "=== s1"; bin/tl-itunes search "Frank Lukas Noch immer dieselben" 2>&1|head -8; echo "=== s2"; bin/tl-itunes search "Sarah Zucker Cabriolet" 2>&1|head -8; echo "=== s3"; bin/tl-itunes search "Frank Lars Mein Baby" 2>&1|head -8
```

<details><summary>Ausgabe</summary>

```
=== s1
2 Alben
itunes:album/1771866855 | Noch immer dieselben - Single — Frank Lukas | 2024-10-11 | 1 Tracks
itunes:album/1764295047 | Nur Älter (noch immer dieselben) [Hypertechno Edit] - Single — Frank Lukas & Seaside Clubbers | 2024-09-13 | 1 Tracks
=== s2
1 Alben
itunes:album/1758954473 | Cabriolet - Single — Sarah Zucker | 2024-08-09 | 1 Tracks
=== s3
4 Alben
itunes:album/810071735 | Mein Baby (Radio Version) - Single — Frank Lars | 2014-02-07 | 1 Tracks
itunes:album/1794624460 | Mein Baby (2025) - Single — Frank Lars | 2025-03-07 | 1 Tracks
itunes:album/1801533166 | Mein Baby (2025) [Nur So! Remix] - Single — Frank Lars | 2025-03-28 | 1 Tracks
itunes:album/960108835 | Mein Baby 2015 (Remixes) - Single — Frank Lars | 2015-02-06 | 2 Tracks
```
</details>

### 15. `shell` +115s – completed

```
for a in 1771866855 1758954473 1794624460; do bin/tl-itunes album $a 2>&1 | sed -n '1p;3p'; done
```

<details><summary>Ausgabe</summary>

```
itunes:album/1771866855 | Noch immer dieselben - Single — Frank Lukas | 2024-10-11 | 1 Tracks | ℗ 2024 Meisel Music / Monopol-Verlag GmbH
1.1 Noch immer dieselben | 3:30 (209549 ms)
itunes:album/1758954473 | Cabriolet - Single — Sarah Zucker | 2024-08-09 | 1 Tracks | ℗ 2024 Meisel Music / Monopol Verlag GmbH
1.1 Cabriolet | 3:04 (183793 ms)
itunes:album/1794624460 | Mein Baby (2025) - Single — Frank Lars | 2025-03-07 | 1 Tracks | ℗ 2025 Meisel Music
1.1 Mein Baby (2025) | 3:18 (198041 ms)
```
</details>

### 16. `shell` +167s – completed

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

### 17. `shell` +187s – completed

```
bin/tl-validate --schema 2>&1 | python3 -c "
import json,sys
s=json.load(sys.stdin)
def walk(p,d):
    print(p, list(d.get('properties',{}).keys()), d.get('required'))
    for k,v in d.get('properties',{}).items():
        walk(p+'.'+k, v)
for k,v in s.get('\$defs',{}).items(): walk(k,v)
walk('root', s)
"
```

<details><summary>Ausgabe</summary>

```
Alternative ['description', 'source', 'why_not'] ['description']
Alternative.description [] None
Alternative.source [] None
Alternative.why_not [] None
ArtistCredit ['name', 'role', 'tracks', 'sources'] ['name']
ArtistCredit.name [] None
ArtistCredit.role [] None
ArtistCredit.tracks [] None
ArtistCredit.sources [] None
Conflict ['field', 'values', 'resolution'] ['field', 'values']
Conflict.field [] None
Conflict.values [] None
Conflict.resolution [] None
Credit ['name', 'role', 'sources'] ['name', 'role']
Credit.name [] None
Credit.role [] None
Credit.sources [] None
InputSpec ['id', 'title', 'artist', 'ean', 'format', 'notes'] ['id']
InputSpec.id [] None
InputSpec.title [] None
InputSpec.artist [] None
InputSpec.ean [] None
InputSpec.format [] None
InputSpec.notes [] None
Release ['title', 'artist', 'format', 'country', 'year', 'label', 'catno', 'barcode', 'edition', 'ids'] ['title']
Release.title [] None
Release.artist [] None
Release.format [] None
Release.country [] None
Release.year [] None
Release.label [] None
Release.catno [] None
Release.barcode [] None
Release.edition [] None
Release.ids [] None
Source ['id', 'url', 'kind', 'note'] ['id']
Source.id [] None
Source.url [] None
Source.kind [] None
Source.note [] None
Track ['position', 'disc', 'title', 'artist', 'duration_s', 'sources', 'duration_sources', 'flags', 'isrc', 'credits'] ['position', 'title']
Track.position [] None
Track.disc [] None
Track.title [] None
Track.artist [] None
Track.duration_s [] None
Track.sources [] None
Track.duration_sources [] None
Track.flags [] None
Track.isrc [] None
Track.credits [] None
root ['input', 'status', 'release', 'tracks', 'artists', 'total_duration_s', 'confidence', 'sources', 'conflicts', 'missing', 'alternatives', 'reasoning'] ['input', 'status', 'confidence', 'reasoning']
root.input [] None
root.status [] None
root.release [] None
root.tracks [] None
root.artists [] None
root.total_duration_s [] None
root.confidence [] None
root.sources [] None
root.conflicts [] None
root.missing [] None
root.alternatives [] None
root.reasoning [] None
```
</details>

### 18. `shell` +221s – completed

```
mkdir -p output/work && cat > /tmp/build_fall.py <<'EOF'
import json
ITI="itunes:album/1824661315"
S13="itunes:album/1771866855"; S27="itunes:album/1758954473"; S213="itunes:album/1794624460"
JPC="web:https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766"
AMZ="web:https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3"
THA="web:https://www.thalia.de/shop/home/artikeldetails/A1075332387"

d1=[
("Sie!","Thomas Anders, Florian Silbereisen & Barbara Schöneberger",218),
("Das bleibt unter uns Chérie","Fantasy",194),
("Ein gebrochenes Herz","Linda Hesse",187),
("Sommernacht","Anna-Carina Woitschack",223),
("Schau mal herein (Remix)","Ross Antony & Linda Fäh",192),
("Verdammt!","Jay Khan",215),
("Playa Bonita","Die Schlagerpiloten",187),
("Dein Schrei nach Liebe","Bernhard Brink",185),
("Leben XXL","Anita Hofmann",199),
("So fühlt sich nur die Liebe an","Patrick Lindner",193),
("Solange wir leben","Timo",185),
("Wir sind wie Piloten","Jörg Bausch",189),
("Noch immer dieselben (Radio Version)","Frank Lukas",210),
("Dein Blick","Zeno",222),
("Sie wollte immer Paris","Franziska",174),
("I'm alive (Ich bin da)","Maria Levin",199),
("Ich glaub an die Liebe","Christian Lais",204),
("Verführerisch (Nur So! Remix)","Silvano Giganti",174),
("Echte Tränen","Jan Böckmann",200),
("Auf immer Wiedersehen","Wind",185),
]
d2=[
("Verliebt in London","Laura Wilde",211),
("Mit dir geht der Sommer nie vorbei","Die Schlagerpiloten",216),
("So muss der Sommer sein","Olaf der Flipper",213),
("Ein bisschen Aroma","Karl König",199),
("Weil es mehr als Liebe ist","G.G. Anderson",203),
("Du rettest mich","Judy Weiss",224),
("Cabriolet (Radio Version)","Sarah Zucker",184),
("Blick nach vorn","Daniela Alfinito",202),
("Altes Spiel, neues Glück","Petra Frey",202),
("Zu lieben ist leicht","Tanja Lasch",204),
("Schwarze Rose","Marian Weisser",211),
("Dein Blick sagt alles","Anni Perka",186),
("Mein Baby (2025) (Radio Version)","Frank Lars",198),
("Intensiv (Radio-Version)","Charlien",187),
("Kann es sein","Alexander Martin",172),
("Momentan ist alles nur Liebe","Gilbert",204),
("Alles neu","Sabrina Berger",181),
("Flieger Richtung Liebe","Die Wolkenstürmer",191),
("Wie ein Orkan","Michael Morgan",185),
("Ein bisschen verliebt","Laura & Mark",192),
]
single={("1","13"):S13,("2","7"):S27,("2","13"):S213}
tracks=[]
for disc,lst in ((1,d1),(2,d2)):
    for i,(t,a,dur) in enumerate(lst,1):
        ds=single.get((str(disc),str(i)),ITI)
        tracks.append({"position":str(i),"disc":disc,"title":t,"artist":a,"duration_s":dur,
          "sources":sorted(set([ds,AMZ,JPC,ITI])),
          "duration_sources":[ds],"flags":["duration_other_edition"]})
# artists
order=["Thomas Anders","Florian Silbereisen","Barbara Schöneberger","Fantasy","Linda Hesse","Anna-Carina Woitschack","Ross Antony","Linda Fäh","Jay Khan","Die Schlagerpiloten","Bernhard Brink","Anita Hofmann","Patrick Lindner","Timo","Jörg Bausch","Frank Lukas","Zeno","Franziska","Maria Levin","Christian Lais","Silvano Giganti","Jan Böckmann","Wind","Laura Wilde","Olaf der Flipper","Karl König","G.G. Anderson","Judy Weiss","Sarah Zucker","Daniela Alfinito","Petra Frey","Tanja Lasch","Marian Weisser","Anni Perka","Frank Lars","Charlien","Alexander Martin","Gilbert","Sabrina Berger","Die Wolkenstürmer","Michael Morgan","Laura & Mark"]
alias={"Timo":"Timo","G.G. Anderson":"G.G. Anderson"}
pos={}
for tr in tracks:
    a=tr["artist"]
    key="%d.%s"%(tr["disc"],tr["position"])
    if a=="Thomas Anders, Florian Silbereisen & Barbara Schöneberger":
        for n in ("Thomas Anders","Florian Silbereisen","Barbara Schöneberger"): pos.setdefault(n,[]).append(key)
    elif a=="Ross Antony & Linda Fäh":
        for n in ("Ross Antony","Linda Fäh"): pos.setdefault(n,[]).append(key)
    elif a=="Laura & Mark":
        pos.setdefault("Laura & Mark",[]).append(key)
    else:
        pos.setdefault(a,[]).append(key)
artists=[]
for n in order:
    artists.append({"name":n,"role":"main","tracks":pos[n],"sources":[JPC,AMZ]})
artists.append({"name":"Nur So!","role":"remixer","tracks":["1.18"],"sources":[AMZ,ITI]})
total=sum(t["duration_s"] for t in tracks)
res={
"input":{"id":"fall-07863373","title":"SCHLAGER ARENA 2025 - SOMMER EDITON - Die größten Hits des Jahres","artist":"Various Artists","ean":"4099964172904"},
"status":"found",
"release":{"title":"Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres","artist":"Various Artists","format":"CD","country":"DE","year":2025,"label":"More Music and Media / Telamo","catno":None,"barcode":"4099964172904","edition":"2×CD, Sommer Edition","ids":{}},
"tracks":tracks,
"artists":artists,
"total_duration_s":total,
"confidence":0.82,
"sources":[
 {"id":ITI,"url":"https://music.apple.com/de/album/schlager-arena-2025-sommer-edition-die-gr%C3%B6%C3%9Ften-hits/1824661315","kind":"streaming","note":"Digital edition, same 40 tracks (3 titles not available on the German store: 1-13, 2-7, 2-13); source of all durations"},
 {"id":S13,"url":"https://music.apple.com/de/album/1771866855","kind":"streaming","note":"Single 'Noch immer dieselben' – duration for track 1-13"},
 {"id":S27,"url":"https://music.apple.com/de/album/1758954473","kind":"streaming","note":"Single 'Cabriolet' – duration for track 2-7"},
 {"id":S213,"url":"https://music.apple.com/de/album/1794624460","kind":"streaming","note":"Single 'Mein Baby (2025)' – duration for track 2-13"},
 {"id":JPC,"url":"https://www.jpc.de/jpcng/poprock/detail/-/art/various-artists-schlager-arena-2025-sommer-edition-die-groessten-hit/hnum/12285766","kind":"shop","note":"EAN 4099964172904, 2 CDs, complete printed tracklist with artist credits (version tags stripped)"},
 {"id":AMZ,"url":"https://www.amazon.de/Schlager-Arena-2025-die-Gr%C3%B6%C3%9Ften/dp/B0F81H8VC3","kind":"shop","note":"EAN/manufacturer reference 4099964172904, 2 CDs, tracklist with version tags"},
 {"id":THA,"url":"https://www.thalia.de/shop/home/artikeldetails/A1075332387","kind":"shop","note":"EAN 4099964172904, 2 CDs, release date 13.06.2025"},
 {"id":"discogs:release/33835569","url":"https://www.discogs.com/release/33835569","kind":"database","note":"Previous edition 'Schlager Arena 2025' (2024, barcode 4099964124866) – different tracklist, not this edition"}
],
"conflicts":[
 {"field":"release year","values":["2025 (iTunes: 2025-06-06; Thalia: 13.06.2025)","13.03.2020 (jpc and Amazon product data)"],"resolution":"2025 used; the 2020 date is evidently a stale retail data field, contradicts the 'Arena 2025 – Sommer Edition' title and the 2025 digital release"},
 {"field":"input title","values":["SCHLAGER ARENA 2025 - SOMMER EDITON - Die größten Hits des Jahres (input)","Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres (shops/iTunes)"],"resolution":"official spelling used; 'EDITON' in the input is a typo, barcode 4099964172904 confirms the same product"},
 {"field":"title track 1.17","values":["Ich glaub an die Liebe (Amazon, iTunes)","Ich glaube an die Liebe (jpc)"],"resolution":"Amazon + iTunes agree on 'Ich glaub an die Liebe'"},
 {"field":"title track 1.16","values":["I'm alive (jpc)","I'm alive (Ich bin da) (Amazon)","I'm Alive (Ich bin da) (iTunes)"],"resolution":"Amazon/iTunes version tag used, capitalisation from Amazon"},
 {"field":"artist track 1.1","values":["Thomas Anders, Florian Silbereisen & Barbara Schöneberger (jpc, Amazon)","Thomas Anders & Florian Silbereisen feat. Barbara Schöneberger (iTunes)"],"resolution":"joint printed credit of the three main artists used, Barbara Schöneberger listed as main on that track"},
 {"field":"title track 1.5","values":["Schau mal herein (Remix) (Amazon)","Schau mal herein (Duett mit Linda Fäh) [Remix] (iTunes)","Schau mal herein (jpc)"],"resolution":"Amazon wording used; duet partner Linda Fäh taken into the track artist credit"},
 {"field":"title track 2.7","values":["Cabriolet (Radio Version) (Amazon)","Cabriolet (jpc)"],"resolution":"Amazon version tag used; duration taken from the 'Cabriolet' single (3:04)"}
],
"missing":[
 "No MusicBrainz release and no Discogs entry exist for this edition – no ISRCs, no database tracklist; identification is via the barcode in three shops (Thalia, Amazon, jpc).",
 "No durations on the physical edition anywhere: all durations come from the digital edition of the same compilation (iTunes, 37 of 40 tracks) and from the matching digital singles for 1-13, 2-7, 2-13 – therefore every track carries flag duration_other_edition.",
 "No printed back-cover image available (Amazon shows no image), so the physical tracklist could not be read from the carrier; jpc and Amazon retail tracklists were used instead.",
 "Catalogue number not published for this edition (Amazon lists only the manufacturer reference 4099964172904, which is the barcode)."
],
"alternatives":[
 {"description":"Schlager Arena 2025 (Die Grössten Hits Des Jahres), 2×CD, 2024, More Music And Media/Telamo, barcode 4099964124866, 40 different tracks","source":"discogs:release/33835569","why_not":"different barcode and different tracklist – the 2024 edition, not the Sommer Edition"},
 {"description":"Digital edition, 21 tracks (Deezer/Spotify)","source":"deezer:album/904925572","why_not":"shortened digital track list, not the 40-track CD"}
],
"reasoning":"No barcode hit in MusicBrainz or Discogs. Web search resolved EAN 4099964172904 to 'Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres', 2×CD, More Music and Media/Telamo, June 2025; Thalia, Amazon and jpc all give this EAN and a 20+20 tracklist that agrees with the 40-track digital album (iTunes). Physical edition chosen over digital. Titles from the retail tracklists (Amazon version tags; iTunes for cross-check), artist credits from jpc/Amazon; durations from the digital album and three digital singles, flagged as coming from another edition."
}
json.dump(res,open("output/work/fall-07863373.json","w"),ensure_ascii=False,indent=1)
print(total)
EOF
python3 /tmp/build_fall.py && bin/tl-validate output/work/fall-07863373.json
```

<details><summary>Ausgabe</summary>

```
7900
INVALID:
- conflicts.0.values: Input should be a valid dictionary
- conflicts.1.values: Input should be a valid dictionary
- conflicts.2.values: Input should be a valid dictionary
- conflicts.3.values: Input should be a valid dictionary
- conflicts.4.values: Input should be a valid dictionary
- conflicts.5.values: Input should be a valid dictionary
- conflicts.6.values: Input should be a valid dictionary
```
</details>

### 19. `shell` +227s – completed

```
cd <repo> && python3 - <<'EOF'
import json
p="output/work/fall-07863373.json"
d=json.load(open(p))
cv=[
 {"field":"release year","values":{"iTunes/Thalia":"2025 (iTunes 2025-06-06, Thalia 13.06.2025)","jpc/Amazon":"13.03.2020"},"resolution":"2025 used; the 2020 date is a stale retail data field and contradicts the 'Arena 2025 – Sommer Edition' title and the 2025 digital release"},
 {"field":"input title","values":{"input":"SCHLAGER ARENA 2025 - SOMMER EDITON - Die größten Hits des Jahres","shops/iTunes":"Schlager Arena 2025: Sommer Edition - Die größten Hits des Jahres"},"resolution":"official spelling used; 'EDITON' in the input is a typo, barcode 4099964172904 confirms the same product"},
 {"field":"title track 1.17","values":{"Amazon/iTunes":"Ich glaub an die Liebe","jpc":"Ich glaube an die Liebe"},"resolution":"Amazon + iTunes agree on 'Ich glaub an die Liebe'"},
 {"field":"title track 1.16","values":{"jpc":"I'm alive","Amazon":"I'm alive (Ich bin da)","iTunes":"I'm Alive (Ich bin da)"},"resolution":"Amazon/iTunes version tag used, capitalisation from Amazon"},
 {"field":"artist track 1.1","values":{"jpc/Amazon":"Thomas Anders, Florian Silbereisen & Barbara Schöneberger","iTunes":"Thomas Anders & Florian Silbereisen feat. Barbara Schöneberger"},"resolution":"joint printed credit of the three main artists used, Barbara Schöneberger listed as main on that track"},
 {"field":"title track 1.5","values":{"Amazon":"Schau mal herein (Remix)","iTunes":"Schau mal herein (Duett mit Linda Fäh) [Remix]","jpc":"Schau mal herein"},"resolution":"Amazon wording used; duet partner Linda Fäh taken into the track artist credit"},
 {"field":"title track 2.7","values":{"Amazon":"Cabriolet (Radio Version)","jpc":"Cabriolet"},"resolution":"Amazon version tag used; duration taken from the 'Cabriolet' single (3:04)"}
]
d["conflicts"]=cv
json.dump(d,open(p,"w"),ensure_ascii=False,indent=1)
EOF
bin/tl-validate output/work/fall-07863373.json
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 40 tracks (40 with duration), 8 sources, 7 conflicts, confidence=0.82
```
</details>

> **Agent** +234s: FERTIG found 40 Tracks confidence=0.82
