# Agent-Trace: 17-paula-linke-k-sse-mehr-k-sse

> Schnellweg geprüft: no fast path: no EAN
Start 2026-11-20T15:52:40 · 24 Schritte · 41 Tool-Aufrufe · Tokens in 119867 / out 43377


> **Agent** +5s: I'll start by checking the input and searchingfor this release.

### 1. `shell` +5s – completed

```
bin/tl-search "\"Küsse! Mehr Küsse!\" Paula Linke" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
10 hits for: "Küsse! Mehr Küsse!" Paula Linke
1. KÜSSE! MEHR KÜSSE!, by Paula Linke
   https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
   KÜSSE! MEHR KÜSSE! by Paula Linke, released 03 July 2026 1. Licht und Farbe 2. Papa mit Kind 3. Kühe Gucken 4. Ich leih mir das nur... 5. Einfach aufstehen und weiter (Opa) 6. Sorgen von morgen 7. Tampon Blues 8. Ich ste
   + Auf dem neuen Album von Paula Linke vereinen sich 10 frische Lieder, die sie gemeinsam mit in den letzten Jahren lieb ge | MEHR KÜSSE! via the free Bandcamp app, plus high-quality download in MP3, FLAC and more. Download available in 24-bit/48
2. Paula Linke
   https://paula-linke.de/
   P.S.: Inzwischen kann man das KÜSSE! MEHR KÜSSE! Album auf allen Streamingplattformen hören. Wisset: Spotify ist kacke (zu Künstler:innen und zur Welt), aber auch da findet ihr meine Musik.
   + P.S.: Inzwischen kann man das KÜSSE! MEHR KÜSSE! Album auf allen Streamingplattformen hören. Wisset: Spotify ist kacke ( | Entdecke die Musik und das Leben von Paula Linke, der Leipziger Liedermacherin. Hier erfährst du mehr über ihre Tour, Mu
3. Paula Linke verteilt in Freital „Küsse! Mehr Küsse!“
   https://www.saechsische.de/lokales/saechsische-schweiz-osterzgebirge/paula-linke-verteilt-in-freital-kuesse-mehr-kuesse-7IA4ZKD6PZGWLG2ZKDDXQRRGUI.html
   Mehr Küsse, mehr Brücken, mehr mutiges und freundliches Aufeinanderzugehen.“ Was sie darunter versteht, singt und erzählt die Leipziger Liedermacherin in ihrem neuen Programm „Küsse!
   + Freital. Paula Linke weiß, was uns fehlt: „Unsere Welt braucht mehr Küsse. Mehr Küsse, mehr Brücken, mehr mutiges und fr | Mehr Küsse!“, mit dem sie am Sonnabend zum zweiten Mal im Garten der Spielbühne Freital gastiert. ... Mutig, freundlich 
4. Chansons, Lieder und Folk: Paula Linke - vom Kuh-Glück und Tampon-Blues - BRF1 Radio
   https://1.brf.be/sendungen/chansons/1220767/
   Deutsches Songwriting aus Leipzig: Die gebürtige Sächsin fordert auf ihrem neuen Album nicht bloß "Küsse! Mehr Küsse!", sondern mehr Nähe. Obwohl Texte ihre Lieder dominieren, haben neben Gitarre auch Posaune, Violine, C
   + Deutsches Songwriting aus Leipzig: Die gebürtige Sächsin fordert auf ihrem neuen Album nicht bloß "Küsse! Mehr Küsse!",  | "Küsse! Mehr Küsse!" von Paula Linke ist erschienen am 3.
5. Paula Linke: KÜSSE. MEHR KÜSSE! – Alternatives Akustikkollektiv
   https://akustikkollektiv.de/event/paula-linke-kuesse-mehr-kuesse/
   Lied-Küsse wechseln sich mit kleinen Monolog-Küssen ab, aus Alltagsbeo
… [2551 Zeichen gekürzt]
```
</details>

### 2. `shell` +5s – completed

```
bin/tl-mb search --title "Küsse! Mehr Küsse!" --artist "Paula Linke" 2>&1 | head -40; echo "---DISCOGS---"; bin/tl-discogs search --title "Küsse! Mehr Küsse!" --artist "Paula Linke" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Küsse\! Mehr Küsse\!" AND artist:"Paula Linke")

---DISCOGS---
0 hits (parameters: {'release_title': 'Küsse! Mehr Küsse!', 'artist': 'Paula Linke'})
```
</details>

> **Agent** +94s: The database searches returned nothing. The web search shows a Bandcamp album. Let me check if a physical edition exists and look at the Bandcamp page.

### 3. `shell` +94s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --grep "track|Track|Lied|Minuten|:.*[0-9]" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
elk2go
elk2go
 Hurra, ich könnte vor Freude in die Luft springen! Was für ein tolles Album. Ja es gibt genug Sorgen - und dann soviel Augenzwinkern und neue Lieder voller Kraft und Mut. Vielen lieben Dank - und einen 💋
Lieblingstitel: Geputzte Flügel (Paula & friends).
/
…
KÜSSE! MEHR KÜSSE! auf CD mit Booklet
 Compact Disc (CD) + Digitales Album
 Auf dem neuen Album von Paula Linke vereinen sich 10 frische Lieder, die sie gemeinsam mit in den letzten Jahren lieb gewonnenen Kolleg:innen in einer Oktoberwoche in Berlin/Kreuzberg aufgenommen hat. Die Leipziger Liedermacherin beschreitet damit nach mehreren auf Gitarre und Gesang reduzierten Alben ganz neue Wege. Und die Lieder profitieren davon.
 Enthält unbegrenztes Streaming von 
KÜSSE! MEHR KÜSSE!
…
Teilen
 / Einbetten
1. | Licht und Farbe 03:38 | Lyrics | Titel kaufen
Schon wieder verpennt, der Espresso verbrennt auf dem Herd,
es ist gleich schon um 8.
…
sie rappelt sich aus ihrer Trance,
gibt dem Tag noch ne Chance.
2. | Papa mit Kind 02:55 | Lyrics | Titel kaufen
Da steht ein Papa mit seinem Kind an der gleichen Haltestelle wie ich.
Es ist heiß, ein leises Flirren, der Bus kommt lange noch nicht.
…
Ayayay..., es sieht wie Abenteuer aus.
Ayayay, es sieht so leicht aus – ich wünscht, wir wüchsen da nie raus.
3. | Kühe Gucken 02:47 | Lyrics | Titel kaufen
Ich sitze auf der Alm und gucke Kühe an,
das scheint mir grade eben 'n solider Lebensplan.
…
kann mal atmen, kann ein paar Sekunden warten,
kann die Karten nochmal mischen – und neu starten.
4. | Ich leih mir das nur... 01:51 | Lyrics | Titel kaufen
Ich leih mir dieses Leben und ich leb's, so gut es geht,
aber ich hab überhaupt keinen Plan.
…
Und ich weiß, daran könnte man verzweifeln, aber nicht jetzt.
Nee, denn es steht zu viel auf dem Spiel.
5. | Einfach aufstehen und weiter (Opa) 04:11 | Lyrics | Titel kaufen
Da schiebt ein älteres Paar zu Neujahr einen Wagen mit Kind vor sich her.
Die Haare leicht grau, Mini Fältchen um die Augen, und er strahlt begeistert, als fiele es ihm
…
du, mein Opa,
du, mein großer Superheld."
6. | Sorgen von morgen 03:33 | Lyrics | Titel kaufen
Ein ausgeblichenes Plakat,
neben Vorhängen aus Brokat,
…
Sie sieht mich und sie winkt mich zu sich ran.
Unsere Füße wippen im Takt,
wir wissen – ja! - die Welt ist ganz schön vertrackt,
aber he
… [62 Zeichen gekürzt]
```
</details>

### 4. `shell` +116s – completed

```
bin/tl-mb search --title "Küsse" --artist "Paula Linke" 2>&1 | head -20; echo "---"; bin/tl-mb search --title "Küsse" 2>&1 | head -20; echo "---DISCOGS---"; bin/tl-discogs search --artist "Paula Linke" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"Küsse" AND artist:"Paula Linke")

---
50 Releases (Queries: release:"Küsse")
musicbrainz:release/10ef5b77-bc06-4b76-96d3-147f47d9f393 | Süße Küsse — Schrott nach 8 | 1988 DE | 7" Vinyl | Tracks 2 | Barcode - | Titan 577/0121-7 | Official | score 100
musicbrainz:release/c52d4e10-83e3-4fbd-9fbb-ed8e641339b7 | DIE KUSSE — MEJIBRAY | 2013-02-06 JP | CD+DVD-Video | Tracks 2+4 | Barcode 4948722482284 | Forum WSG-29 | Official | 限定盤Btype | score 100
musicbrainz:release/923a4dba-0ddd-4d21-ab1b-c6634d858354 | DIE KUSSE — MEJIBRAY | 2013-02-06 JP | CD+DVD-Video | Tracks 2+1 | Barcode 4948722482277 | Forum WSG-28 | Official | 限定盤Atype | score 100
musicbrainz:release/8c5b9782-afb7-43b9-874d-4e0258bfe5ce | DIE KUSSE — MEJIBRAY | 2013-02-06 JP | CD | Tracks 3 | Barcode 4948722482291 | Forum WSG-30 | Official | 通常盤 | score 100
musicbrainz:release/2923da1e-e316-4419-83c4-18254a8ab305 | Hunderttausend Küsse — Helga Brauer und Die Flamingos | 1960 XG | 7" Vinyl | Tracks 2 | Barcode - | AMIGA 4 50 146 | Official | score 100
musicbrainz:release/da453544-c421-4d9a-b0be-118eed8bff49 | DIE KUSSE — MEJIBRAY | 2013-02-06 XW | Digital Media | Tracks 3 | Barcode 4948722482291 | Forum WSG-30 | Official | 通常盤 | score 100
musicbrainz:release/8c5690f4-8726-489b-93dc-722f94488032 | Flüchtige Küsse — Goethes Erben | 2020-09-01 XW | CD | Tracks 10 | Barcode 4260223114885 | ? SAM022DRY | Official | score 100
musicbrainz:release/7bd00f64-c31c-430a-ba08-503a5fa1f0f4 | 1000 Küsse — Relax | 2006 DE | CD | Tracks 1 | Barcode 828768314227 | Ariola 82876 83142 2 | Official | score 100
musicbrainz:release/bb62502d-f47e-4bed-9dc6-eb0822965351 | Küsse der Nacht — Andrea Jürgens | 1990-05-28 DE | CD | Tracks 10 | Barcode 4007192607525 | White Records 260 752 | Official | score 87
musicbrainz:release/b0382002-48d5-46ac-b8eb-94e994434880 | Küsse aus Berlin — Zero absolu | 2013-11-20 XW | Digital Media | Tracks 12 | Barcode - | - | Official | score 87
musicbrainz:release/e29135e2-f33f-4747-bb1f-3bddcbb2c434 | Küsse im Mondschein — Pirkko Mannola & Wyn Hoop | 1998 DE | CD | Tracks 19 | Barcode - | - | Official | score 87
musicbrainz:release/876b9f13-276e-4e68-a4f1-e70ae915fbde | Bisse und Küsse — Wolf Maahn | 2003 DE | CD | Tracks 10 | Barcode - | EMI Electrola CDP 538-7 90051 2 | Official | score 87
musicbrainz:release/87ff2307-6bf7-4a28-9972-2d0665e5d852 | Muskeln & Küsse — Jäger 90 | 2008 DE | CD-R | Tracks 4 | Barcode - | Electric Tremor Dessau ETD PROMO 005 | Promotion |
… [1071 Zeichen gekürzt]
```
</details>

> **Agent** +248s: The Bandcamp page shows a physical CD edition ("auf CD mit Booklet") with durations. Let me get the completetracklist.

### 5. `shell` +248s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --grep "^[0-9]+\. \|" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
Teilen
 / Einbetten
1. | Licht und Farbe 03:38 | Lyrics | Titel kaufen
Schon wieder verpennt, der Espresso verbrennt auf dem Herd,
es ist gleich schon um 8.
…
sie rappelt sich aus ihrer Trance,
gibt dem Tag noch ne Chance.
2. | Papa mit Kind 02:55 | Lyrics | Titel kaufen
Da steht ein Papa mit seinem Kind an der gleichen Haltestelle wie ich.
Es ist heiß, ein leises Flirren, der Bus kommt lange noch nicht.
…
Ayayay..., es sieht wie Abenteuer aus.
Ayayay, es sieht so leicht aus – ich wünscht, wir wüchsen da nie raus.
3. | Kühe Gucken 02:47 | Lyrics | Titel kaufen
Ich sitze auf der Alm und gucke Kühe an,
das scheint mir grade eben 'n solider Lebensplan.
…
kann mal atmen, kann ein paar Sekunden warten,
kann die Karten nochmal mischen – und neu starten.
4. | Ich leih mir das nur... 01:51 | Lyrics | Titel kaufen
Ich leih mir dieses Leben und ich leb's, so gut es geht,
aber ich hab überhaupt keinen Plan.
…
Und ich weiß, daran könnte man verzweifeln, aber nicht jetzt.
Nee, denn es steht zu viel auf dem Spiel.
5. | Einfach aufstehen und weiter (Opa) 04:11 | Lyrics | Titel kaufen
Da schiebt ein älteres Paar zu Neujahr einen Wagen mit Kind vor sich her.
Die Haare leicht grau, Mini Fältchen um die Augen, und er strahlt begeistert, als fiele es ihm
…
du, mein Opa,
du, mein großer Superheld."
6. | Sorgen von morgen 03:33 | Lyrics | Titel kaufen
Ein ausgeblichenes Plakat,
```
</details>

### 6. `shell` +248s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --grep "Titel kaufen\|^[0-9]\." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
(keine Zeile passt auf 'Titel kaufen\\|^[0-9]\\.')
```
</details>

> **Agent** +251s: The grep only returned 6 tracks. Let me get the full page via firecrawl.

### 7. `execute` +254s – completed

```
{"code": "const r = await tools[\"firecrawl\"].firecrawl_scrape({url: \"https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\", formats: [\"markdown\"]});\nconst md = r.data?.markdown || r.markdown || \"\";\nconst lines = md.split(\"\\n\");\nconst out = lines.filter(l => /^\\d+\\.|Titel kaufen|Lyrics|^[0-9]{2}:[0-9]{2}/.test(l) || /^\\d+\\./.test(l));\nconsole.log(out.join(\"\\n\"));\n"}
```

<details><summary>Ausgabe</summary>

```
Logs:
1. [music](https://paulalinke.bandcamp.com/music)
2. [merch](https://paulalinke.bandcamp.com/merch)
3. [community](https://paulalinke.bandcamp.com/community)
1. [Facebook](https://www.facebook.com/paula.linke.33/)
2. [paula-linke.de](https://paula-linke.de/)
3. [Instagram](https://www.instagram.com/paula__linke/)
4. [YouTube](https://www.youtube.com/channel/UC45dzi8ydUajJMNSAfMFOsw?view_as=subscriber)
5. [patreon.com](https://www.patreon.com/paulalinke)
```
</details>

> **Agent** +256s: The markdown didn't include the tracklist. Let me try the browser mode or check the raw HTMLfor embedded JSON.

### 8. `shell` +256s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "trackinfo\|data-tralbum\|duration" 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
(keine Zeile passt auf 'trackinfo\\|data-tralbum\\|duration')
```
</details>

### 9. `shell` +261s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode browser --grep "Titel kaufen" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: browser (browser)
title: Client Challenge
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
(keine Zeile passt auf 'Titel kaufen')
```
</details>

> **Agent** +265s: The browser mode hit a Cloudflare challenge. Let me try to extract the embedded JSON from the page.

### 10. `shell` +265s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Tampon|Geputzte|Flügel|Sorgen" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
elk2go
elk2go
 Hurra, ich könnte vor Freude in die Luft springen! Was für ein tolles Album. Ja es gibt genug Sorgen - und dann soviel Augenzwinkern und neue Lieder voller Kraft und Mut. Vielen lieben Dank - und einen 💋
Lieblingstitel: Geputzte Flügel (Paula & friends).
/
Digitales Album
…
du, mein Opa,
du, mein großer Superheld."
6. | Sorgen von morgen 03:33 | Lyrics | Titel kaufen
Ein ausgeblichenes Plakat,
neben Vorhängen aus Brokat,
…
Heute Nacht wird Kraft geschöpft,
getanzt und gelacht und Sekt geköpft,
die Sorgen von morgen könn' uns heute mal.
Zwischenspiel. Wie oben vorspiel. Strophen ab hier die gleichen Akkorde wie oben.
Der Raum ist warm, es lebt die Kunst,
…
Heute Nacht wird Kraft geschöpft,
getanzt und gelacht und Sekt geköpft,
die Sorgen von morgen könn' mich heute mal.“ 
Unsere Füße wippen im Takt,
wir wissen – ja! - wir ham schon wieder verkackt,
…
Denn Kraft und Hoffnung braucht es allemal.
Denn irgendwelche Trottel reißen Stolpersteine raus
7. | Tampon Blues 02:09 | Lyrics | Titel kaufen
Ich bin ne selbstbewusste Frau,
und ich lebe meinen Traum,
…
Aber heute, ich muss wohl ehrlich sein,
blut' ich leider, leider, leider, mein Selbstbewusstsein
in nen Tampon rein.
```
</details>

### 11. `shell` +265s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "data-tralbum|band_id|tralbum_id|current" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
(keine Zeile passt auf 'data-tralbum|band_id|tralbum_id|current')
```
</details>

> **Agent** +269s: The page truncates. Let me try firecrawl with a selector for the tracklist table, or theBandcamp API.

### 12. `shell` +269s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "8\. \||9\. \||10\. \|" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
hätt ich dich lieber, lieber, lieber
für mich ganz allein.
8. | Ich stehe in Ruhe 03:15 | Lyrics | Titel kaufen
Der Filmkonflikt ist aufgeklärt,
der Weg ist frei für den Kuss.
…
lass mich von der Sonne blenden I:Und es tut gut, es ist geschafft, […] 
Und so könnte man's beenden
9. | Geputzte Flügel (Paula & friends) 03:32 | Lyrics | Titel kaufen
Ein Klapptisch, drauf der Kaffeebecher,
Block und Stifte und wir waren uns sicher:
…
Noch hab' ich Flügel...!
Leipzig, November 2020
10. | Die Stunden ziehen vorbei 03:05 | Lyrics | Titel kaufen
Wir sitzen zusammen an einem großen Tisch
und reden übers Leben und alle sind dabei.
```
</details>

### 13. `execute` +270s – completed

```
{"code": "const r = await tools[\"firecrawl\"].firecrawl_scrape({url: \"https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\", formats: [\"markdown\"], onlyMainContent: true});\nconst md = r.data?.markdown || r.markdown || \"\";\nconsole.log(md.slice(0, 3000));\n"}
```

<details><summary>Ausgabe</summary>

```
Logs:
- ×



  - [electronic](https://bandcamp.com/discover/electronic)
  - [metal](https://bandcamp.com/discover/metal)
  - [rock](https://bandcamp.com/discover/rock)
  - [alternative](https://bandcamp.com/discover/alternative)
  - [hip-hop/rap](https://bandcamp.com/discover/hip-hop-rap)
  - [experimental](https://bandcamp.com/discover/experimental)
  - [punk](https://bandcamp.com/discover/punk)
  - [pop](https://bandcamp.com/discover/pop)
  - [ambient](https://bandcamp.com/discover/ambient)
  - [browse all](https://bandcamp.com/discover)

  - all
  - artists & labels
  - albums
  - tracks
  - fans

  - See all results
  - No matching results

    Try a different filter or a new search keyword.

    ![](https://paulalinke.bandcamp.com/img/search/tumbleweed-emptystate-lightbg.gif)


Search all Bandcamp artists, tracks, and albums

cancel

- [0](https://bandcamp.com/cart "cart")
-
sign up


- [log in](https://bandcamp.com/login?from=menubar)

Get fresh music recommendations delivered to your inbox every Friday.

[![](https://f4.bcbits.com/img/0013534201_100.png)](https://paulalinke.bandcamp.com/)

1. [music](https://paulalinke.bandcamp.com/music)
2. [merch](https://paulalinke.bandcamp.com/merch)
3. [community](https://paulalinke.bandcamp.com/community)

## KÜSSE! MEHR KÜSSE!

### by   [Paula Linke](https://paulalinke.bandcamp.com/)

[![](https://f4.bcbits.com/img/a4047130177_2.jpg)](https://f4.bcbits.com/img/a4047130177_10.jpg)

- Share / Embed
- WishlistIn Wishlist[view](https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse#)

[You own this](https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse#)

Unable to save changes to your wishlist.



supported by




[![](https://f4.bcbits.com/img/0005179506_50.jpg)\\
\\
elk2go\\
\\
![elk2go thumbnail](https://f4.bcbits.com/img/0005179506_42.jpg)](https://bandcamp.com/elk65?from=fanthanks)

[elk2go](https://bandcamp.com/elk65?from=fanthanks)
Hurra, ich könnte vor Freude in die Luft springen! Was für ein tolles Album. Ja es gibt genug Sorgen - und dann soviel Augenzwinkern und neue Lieder voller Kraft und Mut. Vielen lieben Dank - und einen 💋


Favorite track: Geputzte Flügel (Paula & friends).

|     |     |     |
| --- | --- | --- |
|  | [Sorgen von morgen](https://paulalinke.bandcamp.com/track/sorgen-von-morgen)00:00<br>/<br>03:33 |
|  |  |  |

- ### Digital Album  Streaming + Download



Includes unlimited streaming via the free Bandcamp app, plus high-quality download in MP3, FLAC and more.




Purchasable wit
… [505 Zeichen gekürzt]
```
</details>

> **Agent** +279s: I now have the full 10-track list from Bandcamp. Let me get release metadata (date, label, barcode) and check MusicBrainz/Discogs by artist.

### 14. `shell` +279s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "released|2026|Label|©|℗|barcode|EAN|LC |Zoundr|Kick" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
Danke an alle, die das Crowdfunding für dieses Album unterstützt haben. Ohne euch wäre das hier niemals möglich gewesen. Ihr seid die liebsten Küsse! Wie schön, dass es euch gibt!
Mitwirkende
 veröffentlicht am 3. Juli 2026
Text & Musik: Paula Linke
Violine: Thekla Apitz
…
Diskographie
KÜSSE! MEHR KÜSSE!
Juli 2026
SCHÖN DURCHEINANDER
Nov. 2023
…
vorgestellt auf 
Bandcamp Radio
Oct 5, 2026
Zum Album
Company
…
vorgestellt auf 
Bandcamp Radio
Apr 6, 2026
Zum Album
Against the Dying of the Light
…
More reflective alternative folk from the Swedish singer and songwriter, empathetic anthems for a world in duress. 
Bandcamp New & Notable 
Mar 24, 2026
Zum Album
innocent as a rose
```
</details>

### 15. `shell` +310s – completed

```
bin/tl-mb search --artist "Paula Linke" 2>&1 | head -20; echo "---"; bin/tl-mb search --title "KÜSSE" --artist "Paula Linke" 2>&1 | head -10
```

<details><summary>Ausgabe</summary>

```
ERROR: give --barcode or --title
---
0 Releases (Queries: release:"KÜSSE" AND artist:"Paula Linke")
```
</details>

> **Agent** +318s: The Bandcamp page says "veröffentlicht am 3. Juli 2026" (released July 3, 2026). Let me look for label/barcode info and read the CD images.

### 16. `shell` +318s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Zoundr|LC |GEMA|Label|Katalognummer|Bestellnummer|EAN|Barcode" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
(keine Zeile passt auf 'Zoundr|LC |GEMA|Label|Katalognummer|Bestellnummer|EAN|Barcode')
```
</details>

### 17. `shell` +321s – completed

```
bin/tl-vision "https://f4.bcbits.com/img/0045436569_10.jpg" --context "Read the back cover of this CD. Extract the tracklist, barcode, label, catalogue number, and any release date. The album is KÜSSE! MEHR KÜSSE! by Paula Linke." 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://f4.bcbits.com/img/0045436569_10.jpg
model: gemini-3.8-flash@low, in 1283 / out 109 tokens, 3.0 s
kind: front cover | readable: False
release_title: KÜSSE! MEHR KÜSSE!
artist: Paula Linke
0 tracks read
notes: Front cover image only; no tracklist, barcode, or catalog number visible.
```
</details>

> **Agent** +325s: The first image is the front cover. Let me try the other package images and search Discogs/MusicBrainz more broadly.

### 18. `shell` +326s – completed

```
bin/tl-discogs search --title "Küsse" --artist "Paula Linke" 2>&1 | head -20; echo "---MB---"; bin/tl-mb search --title "Küsse! Mehr Küsse!" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
0 hits (parameters: {'release_title': 'Küsse', 'artist': 'Paula Linke'})

---MB---
0 Releases (Queries: release:"Küsse\! Mehr Küsse\!")
```
</details>

### 19. `shell` +330s – completed

```
bin/tl-vision "https://f4.bcbits.com/img/0045436572_10.jpg" --context "Read this CD package image. Extract the tracklist, barcode, label, catalogue number, and release date. The album is KÜSSE! MEHR KÜSSE! by Paula Linke." 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://f4.bcbits.com/img/0045436572_10.jpg
model: gemini-3.8-flash@low, in 1280 / out 118 tokens, 4.5 s
kind: other | readable: False
artist: Paula Linke
format_hints: CD
0 tracks read
notes: No tracklist visible. Booklet open to lyrics pages showing titles 'LICHT UND FARBE' and 'PAPA M...', next to the CD disc with a signature.
```
</details>

### 20. `shell` +332s – completed

```
bin/tl-vision "https://f4.bcbits.com/img/0045436570_10.jpg" --context "Read this CD package image. Extract the tracklist, barcode, label, catalogue number, and release date. The album is KÜSSE! MEHR KÜSSE! by Paula Linke." 2>&1 | head -80
```

<details><summary>Ausgabe</summary>

```
source-id: image:https://f4.bcbits.com/img/0045436570_10.jpg
model: gemini-3.8-flash@low, in 1280 / out 102 tokens, 6.6 s
kind: booklet | readable: False
artist: Paula Linke
0 tracks read
notes: Credits, photos, and thank-you text; no tracklist visible on this page.
```
</details>

> **Agent** +346s: The images don't show a back cover. Let me check the artist's website and search for label/barcode anda second source.

### 21. `shell` +346s – completed

```
bin/tl-scrape "https://paula-linke.de/" --grep "Küsse|CD|Shop|Album|Kaufen" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paula-linke.de/
mode: http (http)
title: Paula Linke
source-id: web:https://paula-linke.de/
---
…
DUO ADRIANA
Kontakt
Shop
Pädagogik
Leipziger Liedermacherin
Das Album ist da! KÜSSE! MEHR KÜSSE! kann man jetzt auf Bandcamp hören und sich downloaden. Oder eine CD mit Booklet bestellen. Jippieh!
Erstmal nur auf Bandcamp. 
Zum neuen Album auf Bandcamp
Schön, dass Ihr da seid!
Was gibt es neues?
Ihr Lieben, das Tourjahr neigt sich schon fast seinem Ende. Am 2.10. feierte das KÜSSE! MEHR KÜSSE! Programm seine Derniere. Hinter mir liegen wundervolle Konzerte in verschiedenen wunderschönen Orten dieses Landes, interessierte und aufgeschlossene Gespräche, herrlich umsorgende Veranstalter:innen und ganz, ganz viele Küsse! 
Daneben fanden die schönsten Dinge statt: Liederwerkstätten, Moderationen, Workshops, Konzerte mit Robert Weinkauf, vorerst letzte KonzertLesungen mit Daniel Baierl. Was für ein aufregendes letztes halbes Jahr! 
Der Herbst wird leiser und das ist auch gut so: Denn hier wird schon wieder an neuen Programmen getüftelt. Programmen? Ja, genau. Ich errarbeite parallel nämlich zwei Programme, ein normales Soloprogramm - NOCH HAB' ICH FLÜGEL - und an einem Weihnachtsprogramm! Uh! 
…
KÜSSE! MEHR KÜSSE!
Paula
P.S.: Inzwischen kann man das KÜSSE! MEHR KÜSSE! Album auf allen Streamingplattformen hören. Wisset: Spotify ist kacke (zu Künstler:innen und zur Welt), aber auch da findet ihr meine Musik. Aber vieleicht habt ihr Lust, euch mal die anderen Streamingplattformen anzusehen, die netter sind.^^
Patreon - eine kleine Familie
Die Winterpause wurde dafür genutzt, Konzerte zu planen und am Programm zu basteln, am Album zu basteln, aber eben auch neue Texte zu schreiben. Meine Patron:innen waren ganz nah dran und durften in diesen Prozess hinein linsen. 
Für alle, die auch noch näher am Geschehen dran sein wollen, kann ich unsere kleine, feine Patreon-Gruppe empfehlen. Dort kann man ab 2,- im Monat jede Woche einen kleinen Beitrag lesen, bekommt neue Ohrwürmer zu hören, frisch aus der Liedermacherküche, hat Anteil am Geschehen und den Arbeitsprozessen und vor allem - hat die Möglichkeit, sich einfach zurückzulehnen und zu genießen. Ein bisschen wie Familie. 
Zu Patreon:
…
Copyright © 2026 Paula Linke – Alle Rechte vorbehalten.
Unterstützt von 
Shop
Impressum / Kontakt
Datenschutzerklärung
JETZT ZUM NEWSLETTER ANMELDEN UND MUSIKGESCHENK ERHALTEN. Komm ins Paula-Universum und erhalte zur Begrüßung ein Lied, das es auf noch keinem Album zu Hören gib
… [134 Zeichen gekürzt]
```
</details>

### 22. `shell` +347s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Text & Musik|Violine|Gesang|Gitarre|Bass|Schlagzeug|Produktion|Mix|Master|Label|Zoundr|Leipzig|Aufnahme" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
KÜSSE! MEHR KÜSSE! auf CD mit Booklet
 Compact Disc (CD) + Digitales Album
 Auf dem neuen Album von Paula Linke vereinen sich 10 frische Lieder, die sie gemeinsam mit in den letzten Jahren lieb gewonnenen Kolleg:innen in einer Oktoberwoche in Berlin/Kreuzberg aufgenommen hat. Die Leipziger Liedermacherin beschreitet damit nach mehreren auf Gitarre und Gesang reduzierten Alben ganz neue Wege. Und die Lieder profitieren davon.
 Enthält unbegrenztes Streaming von 
KÜSSE! MEHR KÜSSE!
…
brauch ich nur an dich zu denken!
Noch hab' ich Flügel...!
Leipzig, November 2020
10. | Die Stunden ziehen vorbei 03:05 | Lyrics | Titel kaufen
Wir sitzen zusammen an einem großen Tisch
…
Die erzählten Geschichten sind so schön.
Und die Stunden ziehen vorbei.
Jemand greift zur Gitarre und klimpert darauf rum.
Wir erkennen das Lied und singen mit.
Das klingt manchmal schön und meistens recht krumm,
…
Mitwirkende
 veröffentlicht am 3. Juli 2026
Text & Musik: Paula Linke
Violine: Thekla Apitz
Posaune: Michael Mond
Cajon/Perscussion: Maria Schüritz
Cello: Merle Weißbach
Bass: Maria Jacobi
Klavier: Stefan Ebert
Gesang: Sonja Goll, Nikki Gennrich, Linda Gundermann, Merle Weißbach
Recording/Mixing/Mastering: Jonas Fehrenberg
Foto: Kerstin Neubecker
Lizenz
…
Germany
placeholder
```
</details>

### 23. `shell` +348s – completed

```
bin/tl-search "Paula Linke Küsse Mehr Küsse CD Zoundr Label" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
10 hits for: Paula Linke Küsse Mehr Küsse CD Zoundr Label
1. KÜSSE! MEHR KÜSSE!, by Paula Linke
   https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
   Ihr seid die liebsten Küsse! Wie schön, dass es euch gibt! released July 3, 2026 Text & Musik: Paula Linke Violine: Thekla Apitz Posaune: Michael Mond Cajon/Perscussion: Maria Schüritz Cello: Merle Weißbach Bass: Maria J
   + Auf dem neuen Album von Paula Linke vereinen sich 10 frische Lieder, die sie gemeinsam mit in den letzten Jahren lieb ge | MEHR KÜSSE! via the free Bandcamp app, plus high-quality download in MP3, FLAC and more. Download available in 24-bit/48
2. Paula Linke
   https://paula-linke.de/
   P.S.: Inzwischen kann man das KÜSSE! MEHR KÜSSE! Album auf allen Streamingplattformen hören. Wisset: Spotify ist kacke (zu Künstler:innen und zur Welt), aber auch da findet ihr meine Musik.
   + Im Herbst kommen noch mal drei KÜSSE-Konzerte, am 2.10. die Derniere in Leipzig. Ich freue mich, wenn wir uns entweder i | Ihr Lieben, das Tourjahr neigt sich schon fast seinem Ende. Am 2.10. feiert das KÜSSE! MEHR KÜSSE! Programm seine Dernie
3. Music | Paula Linke
   https://paulalinke.bandcamp.com/
   MEHR KÜSSE! ... ICH WILL NOCH RUNDER WERDEN - das Doppelalbum - SCHICHT FÜR SCHICHT (Studio) + NEUN WEITERE SCHICHTEN (Bonus) ... * 1989 Leipzig Liedermacherin. Von Haus aus Dramaturgin und Theaterpädagogin, lebe ich nun
   + MEHR KÜSSE! ... ICH WILL NOCH RUNDER WERDEN - das Doppelalbum - SCHICHT FÜR SCHICHT (Studio) + NEUN WEITERE SCHICHTEN (B | Paula Linke. Germany. * 1989 Leipzig Liedermacherin. Von Haus aus Dramaturgin und Theaterpädagogin, lebe ich nun wieder 
4. Musik in der Kanzlei: Paula Linke - Sommer & Partner
   https://sommer-partner.de/musik-in-der-kanzlei-paula-linke-2/
   Ein zart Gehauchter, ein leidenschaftlich an all das hier Geschmiegter, ein fröhlich Tanzender oder ein fest Verbissener. Jedenfalls ist da Liebe. Und davon braucht es jetzt noch viel mehr. Und Küsse. Mehr Küsse! Weitere
   + Ein zart Gehauchter, ein leidenschaftlich an all das hier Geschmiegter, ein fröhlich Tanzender oder ein fest Verbissener
5. Chansons, Lieder und Folk: Paula Linke - vom Kuh-Glück und Tampon-Blues - BRF1 Radio
   https://1.brf.be/sendungen/chansons/1220767/
   Deutsches Songwriting aus Leipzig: Die gebürtige Sächsin fordert auf ihrem neuen Album nicht bloß "Küsse! Mehr Küsse!", sondern mehr Nähe. Obwohl Texte ihre Lieder dominieren, haben neben Gitarre auch Posaune, Violine, C
   + Deutsches Songwriting
… [671 Zeichen gekürzt]
```
</details>

> **Agent** +359s: I have tracks 1–5 and 8–10; need 6–7. Let me pull the full numbered tracklist and the license/label section.

### 24. `shell` +359s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Lizenz|Sorgen von morgen|Tampon|Geputzte|Flügel" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
elk2go
 Hurra, ich könnte vor Freude in die Luft springen! Was für ein tolles Album. Ja es gibt genug Sorgen - und dann soviel Augenzwinkern und neue Lieder voller Kraft und Mut. Vielen lieben Dank - und einen 💋
Lieblingstitel: Geputzte Flügel (Paula & friends).
/
Digitales Album
…
du, mein Opa,
du, mein großer Superheld."
6. | Sorgen von morgen 03:33 | Lyrics | Titel kaufen
Ein ausgeblichenes Plakat,
neben Vorhängen aus Brokat,
…
Heute Nacht wird Kraft geschöpft,
getanzt und gelacht und Sekt geköpft,
die Sorgen von morgen könn' uns heute mal.
Zwischenspiel. Wie oben vorspiel. Strophen ab hier die gleichen Akkorde wie oben.
Der Raum ist warm, es lebt die Kunst,
…
Heute Nacht wird Kraft geschöpft,
getanzt und gelacht und Sekt geköpft,
die Sorgen von morgen könn' mich heute mal.“ 
Unsere Füße wippen im Takt,
wir wissen – ja! - wir ham schon wieder verkackt,
…
Denn Kraft und Hoffnung braucht es allemal.
Denn irgendwelche Trottel reißen Stolpersteine raus
7. | Tampon Blues 02:09 | Lyrics | Titel kaufen
Ich bin ne selbstbewusste Frau,
und ich lebe meinen Traum,
…
Aber heute, ich muss wohl ehrlich sein,
blut' ich leider, leider, leider, mein Selbstbewusstsein
in nen Tampon rein.
An jedem noch so andren Tag,
```
</details>

### 25. `shell` +359s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "^[0-9]+\." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
Teilen
 / Einbetten
1. | Licht und Farbe 03:38 | Lyrics | Titel kaufen
Schon wieder verpennt, der Espresso verbrennt auf dem Herd,
es ist gleich schon um 8.
…
sie rappelt sich aus ihrer Trance,
gibt dem Tag noch ne Chance.
2. | Papa mit Kind 02:55 | Lyrics | Titel kaufen
Da steht ein Papa mit seinem Kind an der gleichen Haltestelle wie ich.
Es ist heiß, ein leises Flirren, der Bus kommt lange noch nicht.
…
Ayayay..., es sieht wie Abenteuer aus.
Ayayay, es sieht so leicht aus – ich wünscht, wir wüchsen da nie raus.
3. | Kühe Gucken 02:47 | Lyrics | Titel kaufen
Ich sitze auf der Alm und gucke Kühe an,
das scheint mir grade eben 'n solider Lebensplan.
…
kann mal atmen, kann ein paar Sekunden warten,
kann die Karten nochmal mischen – und neu starten.
4. | Ich leih mir das nur... 01:51 | Lyrics | Titel kaufen
Ich leih mir dieses Leben und ich leb's, so gut es geht,
aber ich hab überhaupt keinen Plan.
…
Und ich weiß, daran könnte man verzweifeln, aber nicht jetzt.
Nee, denn es steht zu viel auf dem Spiel.
5. | Einfach aufstehen und weiter (Opa) 04:11 | Lyrics | Titel kaufen
Da schiebt ein älteres Paar zu Neujahr einen Wagen mit Kind vor sich her.
Die Haare leicht grau, Mini Fältchen um die Augen, und er strahlt begeistert, als fiele es ihm
…
du, mein Opa,
du, mein großer Superheld."
6. | Sorgen von morgen 03:33 | Lyrics | Titel kaufen
Ein ausgeblichenes Plakat,
```
</details>

> **Agent** +362s: Tracks 1–7 confirmed. Now verify 8–10 and the license/label block.

### 26. `shell` +363s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "^8\.|^9\.|^10\." 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
hätt ich dich lieber, lieber, lieber
für mich ganz allein.
8. | Ich stehe in Ruhe 03:15 | Lyrics | Titel kaufen
Der Filmkonflikt ist aufgeklärt,
der Weg ist frei für den Kuss.
…
lass mich von der Sonne blenden I:Und es tut gut, es ist geschafft, […] 
Und so könnte man's beenden
9. | Geputzte Flügel (Paula & friends) 03:32 | Lyrics | Titel kaufen
Ein Klapptisch, drauf der Kaffeebecher,
Block und Stifte und wir waren uns sicher:
…
Noch hab' ich Flügel...!
Leipzig, November 2020
```
</details>

### 27. `shell` +363s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Lizenz" 2>&1 | head -20; echo "===ALL TITLES==="; bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Titel kaufen" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
Recording/Mixing/Mastering: Jonas Fehrenberg
Foto: Kerstin Neubecker
Lizenz
alle Rechte vorbehalten
Tags
===ALL TITLES===
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
Teilen
 / Einbetten
1. | Licht und Farbe 03:38 | Lyrics | Titel kaufen
Schon wieder verpennt, der Espresso verbrennt auf dem Herd,
es ist gleich schon um 8.
…
sie rappelt sich aus ihrer Trance,
gibt dem Tag noch ne Chance.
2. | Papa mit Kind 02:55 | Lyrics | Titel kaufen
Da steht ein Papa mit seinem Kind an der gleichen Haltestelle wie ich.
Es ist heiß, ein leises Flirren, der Bus kommt lange noch nicht.
…
Ayayay..., es sieht wie Abenteuer aus.
Ayayay, es sieht so leicht aus – ich wünscht, wir wüchsen da nie raus.
3. | Kühe Gucken 02:47 | Lyrics | Titel kaufen
Ich sitze auf der Alm und gucke Kühe an,
das scheint mir grade eben 'n solider Lebensplan.
…
kann mal atmen, kann ein paar Sekunden warten,
kann die Karten nochmal mischen – und neu starten.
4. | Ich leih mir das nur... 01:51 | Lyrics | Titel kaufen
Ich leih mir dieses Leben und ich leb's, so gut es geht,
aber ich hab überhaupt keinen Plan.
…
```
</details>

### 28. `shell` +366s – completed

```
bin/tl-scrape "https://1.brf.be/sendungen/chansons/1220767/" --grep "Küsse|Titel|Track|Lied|Label|Zoundr|erschienen|3. Juli" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://1.brf.be/sendungen/chansons/1220767/
mode: http (http)
title: Chansons, Lieder und Folk: Paula Linke - vom Kuh-Glück und Tampon-Blues - BRF1 Radio
source-id: web:https://1.brf.be/sendungen/chansons/1220767/
---
…
Chansons, Lieder und Folk: Paula Linke - vom Kuh-Glück und Tampon-Blues - BRF1 Radio
Zu Inhalt wechseln
Paula Linke versteht sich auf den Kleinkunstbühnen des Landes als ihr eigenes kleines Theater. Nach Jahren als Regieassistentin und Dramaturgin wechselte die Leipzigerin 2019 die Perspektive. Ihr neues Album hat sie mit Crowdfunding finanziert. Mit "Küsse! Mehr Küsse!" meint sie vor allem: Sehnsucht nach echter Nähe und Empathie in einer oft unübersichtlichen Welt.
Die Platte markiert eine deutliche Weiterentwicklung ihrer bisherigen Veröffentlichungen. Begann sie im Jahr 2018 noch mit rohen, einspurig aufgenommenen Onetakes auf Bandcamp, nutzt sie im Studio heute eine breite Dramaturgie. Das akustische Fundament bricht mit dem klischeehaften Bild der einsamen Liedermacher-Gitarre. Die Texte stehen im Vordergrund, werden aber von einem dichten Kammer-Ensemble getragen. Neben klassischen Streichern wie Violine und Cello prägen unkonventionelle Posaunen-Sätze, Klavier und die Rhythmik einer Cajón die Arrangements. In den Stücken verarbeitet sie ihre Erfahrungen aus der Theaterwissenschaft und Soziologie zu präzisen Gesellschaftsstudien. Es geht um verpasste Momente, den Trost im Chaos und die schmerzhaften Brüche im Alltag. Entstanden ist ein Album, das die Hörer*innen mit scharfen Beobachtungen konfrontiert, aber auch Wärme spendet.
"Küsse! Mehr Küsse!" von Paula Linke ist erschienen am 3. Juli im Eigenvertrieb.
Außerdem in dieser Sendung
Lonepsi: Der französische Musiker und Psychologe seziert die Einsamkeit in dichten, cinematischen Klangbildern ("Dans le lointain de ta voix", Lone et la Lune)
```
</details>

### 29. `shell` +366s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --mode http --grep "Die Stunden ziehen vorbei" 2>&1 | head -10
```

<details><summary>Ausgabe</summary>

```
url: https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
mode: http (http)
title: KÜSSE! MEHR KÜSSE! | Paula Linke
source-id: web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse
---
…
Noch hab' ich Flügel...!
Leipzig, November 2020
10. | Die Stunden ziehen vorbei 03:05 | Lyrics | Titel kaufen
Wir sitzen zusammen an einem großen Tisch
```
</details>

### 30. `shell` +368s – completed

```
bin/tl-scrape "https://www.startnext.com/paula-linke-kuesse-mehr-kuesse" --grep "Track|Lied|Titel|CD|Label|Zoundr|Barcode|EAN" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://www.startnext.com/paula-linke-kuesse-mehr-kuesse
mode: http (http)
title: Paula Linke - KÜSSE! MEHR KÜSSE! | Das nächste Album der Leipziger Liedermacherin steht in den Startlöchern!
source-id: web:https://www.startnext.com/paula-linke-kuesse-mehr-kuesse
---
…
Paula Linke - KÜSSE! MEHR KÜSSE! | Das nächste Album der Leipziger Liedermacherin steht in den Startlöchern!
Crowdfinanzieren seit 2010
Das nächste Album der Leipziger Liedermacherin steht in den Startlöchern!
Mutig und freundlich und mit einer großen Portion Humor erzählt Paula Linke pointierte Geschichten aus dem Leben. Mit KÜSSE! MEHR KÜSSE! legt die Hoyschrecke-Gewinnerin ein neues, vielschichtiges Programm vor. Lied für Lied begibt sie sich darin in Gedankenexperimente, in abwechslungsreichen, eingängigen Melodien, klugen Texten und Bildern, - amüsant und überraschend. Am 11.2.2026 soll das Album dazu erscheinen. Hilf mit, das neue Album zu ermöglichen, indem du es dir jetzt schon vorbestellst!
Tausendfacher Dank
5,00 €
…
Hängebeutel - KÜSSE! MEHR KÜSSE!
15,00 €
Ui! Ich bin ein bisschen stolz. Ich habe noch nie etwas anderes als CDs nach den Konzerten angeboten. Aber ich wurde bei den letzten Konzerten immer wieder auf den Namen des Programms angesprochen und darauf, dass es doch cool wäre, wenn es Beutel mit dem Schriftzug gäbe. Und deswegen: Tattaa! Gibt es das jetzt. 
Ich freue mich sehr darüber, dass wir das machen. Und mit meinen Patron:innen zusammen habe ich herausgefunden, dass nicht nur dieser Programm- und Albumtitel, sondern auch die davor, ziemlich gut auf Beutel passen würden. 
Der Versand ist natürlich inklusive. Ich freue mich auf eure Bestellungen!
KÜSSE! MEHR KÜSSE! Digital als Download
18,00 €
Du bekommst den Downloadlink nach Abschluss der Aufnahmen per Mail geschickt und kannst, die Lieder im Ohr, vergnügt im Sessel mit Tee dem Sommer und den Konzerten nachlauschen.
Damit unterstützt du meine Arbeit als Musikerin genauso, wie du dafür sorgst, dass die am Album Beteiligten ordentlich bezahlt werden können. Danke dir dafür!
Ich wünsche dir viel Spaß mit dem Album, sobald es bei dir eintrudelt und bis dahin einen wundervollen Sommer und Herbst! Vielleicht sehen wir uns auf einem der Konzerte?
KÜSSE! MEHR KÜSSE auf CD inkl. Versand
20,00 €
Du bekommst die CD noch vor dem offiziellen Releasedatum zu dir nach Hause geschickt und kannst sie gleich zum kommenden Ostern verschenken, oder aber selbst vergnügt im Sessel mit Tee dem letzten Sommer und den Konzerten nachlausc
… [1982 Zeichen gekürzt]
```
</details>

> **Agent** +376s: BRF1 confirms "erschienen am 3. Juli im Eigenvertrieb" (self-released). Now let me find a second source for durations — the digital release orthe artist's shop.

### 31. `shell` +377s – completed

```
bin/tl-itunes search "Paula Linke Küsse" 2>&1 | head -30; echo "===DEEZER==="; bin/tl-deezer search --artist "Paula Linke" --title "Küsse" 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
1 Alben
itunes:album/6798000134 | Küsse! Mehr Küsse! — Paula Linke | 2026-08-01 | 10 Tracks
===DEEZER===
1 Alben (q=artist:"Paula Linke" album:"Küsse")
deezer:album/1046252222 | Küsse! Mehr Küsse! — Paula Linke | 10 Tracks | album
```
</details>

### 32. `shell` +387s – completed

```
bin/tl-scrape "https://paula-linke.de/shop" --grep "Küsse|CD|Track|Titel|Lied" 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
url: https://paula-linke.de/shop
mode: uc (http → firecrawl → uc)
title: 404 Not Found
source-id: web:https://paula-linke.de/shop
---
(keine Zeile passt auf 'Küsse|CD|Track|Titel|Lied')
```
</details>

> **Agent** +390s: iTunes and Deezer both have the album. Let me pull their tracklists for cross-check.

### 33. `shell` +390s – completed

```
bin/tl-itunes album 6798000134 2>&1 | head -40; echo "===DEEZER==="; bin/tl-deezer album 1046252222 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
itunes:album/6798000134 | Küsse! Mehr Küsse! — Paula Linke | 2026-08-01 | 10 Tracks | ℗ 2026 Paula Linke
url: https://music.apple.com/de/album/k%C3%BCsse-mehr-k%C3%BCsse/6798000134?uo=4
1.1 Licht und Farbe | 3:38 (218000 ms)
1.2 Papa mit Kind | 2:55 (175256 ms)
1.3 Kühe Gucken | 2:48 (167730 ms)
1.4 Ich leih mir das nur... | 1:51 (111441 ms)
1.5 Einfach aufstehen und weiter | 4:11 (251334 ms)
1.6 Sorgen von morgen | 3:34 (213525 ms)
1.7 Tampon Blues | 2:10 (129635 ms)
1.8 Ich stehe in Ruhe | 3:16 (195960 ms)
1.9 Geputzte Flügel (Paula & friends) | 3:33 (212990 ms)
1.10 Die Stunden ziehen vorbei | 3:05 (185204 ms)
Total 31:01 (1861 s)
===DEEZER===
deezer:album/1046252222 | Küsse! Mehr Küsse! — Paula Linke | 2026-08-01 | UPC 4068992790596 | 10 Tracks | Label recordJet
url: https://www.deezer.com/album/1046252222
1.1 Licht und Farbe | 3:38
1.2 Papa mit Kind | 2:55
1.3 Kühe Gucken | 2:47
1.4 Ich leih mir das nur... | 1:51
1.5 Einfach aufstehen und weiter | 4:11
1.6 Sorgen von morgen | 3:33
1.7 Tampon Blues | 2:09
1.8 Ich stehe in Ruhe | 3:15
1.9 Geputzte Flügel (Paula & friends) | 3:33
1.10 Die Stunden ziehen vorbei | 3:05
Total 30:57 (1857 s)
```
</details>

> **Agent** +415s: Both streaming sources agree on 10 tracks. Let me check the output schema and confirm the label details.

### 34. `shell` +415s – completed

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

### 35. `shell` +420s – completed

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

### 36. `shell` +422s – completed

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

> **Agent** +460s: Let me verify there's no MusicBrainz/Discogs entry for the digital UPCand check the barcode.

### 37. `shell` +463s – completed

```
bin/tl-gtin 4068992790596 2>&1 | head -20; echo "===MB==="; bin/tl-mb search --barcode 4068992790596 2>&1 | head -20; echo "===DISCOGS==="; bin/tl-discogs search --barcode 4068992790596 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
input: '4068992790596' → digits: 4068992790596 (13 digits)
type: EAN-13  valid: yes
search variants: 4068992790596
prefix 400–440: assigned in Germany (says nothing about the country of release)
===MB===
0 Releases (Queries: barcode:(4068992790596))

===DISCOGS===
0 hits (parameters: {'barcode': '04068992790596'})
```
</details>

### 38. `shell` +467s – completed

```
bin/tl-mb search --title "KÜSSE! MEHR KÜSSE!" 2>&1 | head -20; echo "===DISCOGS==="; bin/tl-discogs search --title "KÜSSE! MEHR KÜSSE!" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
0 Releases (Queries: release:"KÜSSE\! MEHR KÜSSE\!")

===DISCOGS===
0 hits (parameters: {'release_title': 'KÜSSE! MEHR KÜSSE!'})
```
</details>

> **Agent** +472s: No database entries. Let me check the Bandcamp page's image links to see if a back cover exists (for the missingnote).

### 39. `shell` +473s – completed

```
bin/tl-scrape "https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse" --links 2>&1 | grep -i "bcbits\|img" | head -20
```

<details><summary>Ausgabe</summary>

```
(no output)
```
</details>

> **Agent** +503s: I have enoughevidence. Let me write the result JSON.

### 40. `write` +503s – completed

```
{"path": "output/work/fall-0580f191.json", "content": "{\n  \"input\": {\n    \"id\": \"fall-0580f191\",\n    \"title\": \"Küsse! Mehr Küsse!\",\n    \"artist\": \"Paula Linke\"\n  },\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"KÜSSE! MEHR KÜSSE!\",\n    \"artist\": \"Paula Linke\",\n    \"format\": \"CD\",\n    \"country\": \"DE\",\n    \"year\": 2026,\n    \"label\": \"Eigenvertrieb\",\n    \"catno\": null,\n    \"barcode\": null,\n    \"edition\": \"CD mit Booklet (CD + Digital Album)\",\n    \"ids\": {\n      \"bandcamp\": \"k-sse-mehr-k-sse\",\n      \"itunes\": \"6798000134\",\n      \"deezer\": \"1046252222\"\n    }\n  },\n  \"tracks\": [\n    {\n      \"position\": \"1\",\n      \"disc\": 1,\n      \"title\": \"Licht und Farbe\",\n      \"artist\": null,\n      \"duration_s\": 218,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"2\",\n      \"disc\": 1,\n      \"title\": \"Papa mit Kind\",\n      \"artist\": null,\n      \"duration_s\": 175,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"3\",\n      \"disc\": 1,\n      \"title\": \"Kühe Gucken\",\n      \"artist\": null,\n      \"duration_s\": 167,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"4\",\n      \"disc\": 1,\n      \"title\": \"Ich leih mir das nur...\",\n      \"artist\": null,\n      \"duration_s\": 111,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"5\",\n      \"disc\": 1,\n      \"title\": \"Einfach aufstehen und weiter (Opa)\",\n      \"artist\": null,\n      \"duration_s\": 251,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [\n        \"title_conflict\"\n      ],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"6\",\n      \"disc\": 1,\n      \"title\": \"Sorgen von morgen\",\n      \"artist\": null,\n      \"duration_s\": 213,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"7\",\n      \"disc\": 1,\n      \"title\": \"Tampon Blues\",\n      \"artist\": null,\n      \"duration_s\": 129,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"8\",\n      \"disc\": 1,\n      \"title\": \"Ich stehe in Ruhe\",\n      \"artist\": null,\n      \"duration_s\": 195,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"9\",\n      \"disc\": 1,\n      \"title\": \"Geputzte Flügel (Paula & friends)\",\n      \"artist\": null,\n      \"duration_s\": 212,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    },\n    {\n      \"position\": \"10\",\n      \"disc\": 1,\n      \"title\": \"Die Stunden ziehen vorbei\",\n      \"artist\": null,\n      \"duration_s\": 185,\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"duration_sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\"\n      ],\n      \"flags\": [],\n      \"credits\": [\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"composer\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        },\n        {\n          \"name\": \"Paula Linke\",\n          \"role\": \"lyricist\",\n          \"sources\": [\n            \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n          ]\n        }\n      ]\n    }\n  ],\n  \"artists\": [\n    {\n      \"name\": \"Paula Linke\",\n      \"role\": \"main\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n        \"itunes:album/6798000134\",\n        \"deezer:album/1046252222\",\n        \"web:https://1.brf.be/sendungen/chansons/1220767/\",\n        \"web:https://paula-linke.de/\"\n      ]\n    },\n    {\n      \"name\": \"Thekla Apitz\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Michael Mond\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Maria Schüritz\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Merle Weißbach\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Maria Jacobi\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Stefan Ebert\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Sonja Goll\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Nikki Gennrich\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    },\n    {\n      \"name\": \"Linda Gundermann\",\n      \"role\": \"other\",\n      \"tracks\": [],\n      \"sources\": [\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\"\n      ]\n    }\n  ],\n  \"total_duration_s\": 1856,\n  \"confidence\": 0.85,\n  \"sources\": [\n    {\n      \"id\": \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n      \"url\": \"https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\",\n      \"kind\": \"shop\",\n      \"note\": \"Bandcamp physical CD + digital album listing; 10 tracks with durations; credits; released 3 July 2026; all rights reserved.\"\n    },\n    {\n      \"id\": \"itunes:album/6798000134\",\n      \"url\": \"https://music.apple.com/de/album/k%C3%BCsse-mehr-k%C3%BCsse/6798000134?uo=4\",\n      \"kind\": \"streaming\",\n      \"note\": \"Digital edition released 2026-08-01; 10 tracks; ms durations; ℗ 2026 Paula Linke.\"\n    },\n    {\n      \"id\": \"deezer:album/1046252222\",\n      \"url\": \"https://www.deezer.com/album/1046252222\",\n      \"kind\": \"streaming\",\n      \"note\": \"Digital edition, UPC 4068992790596, label recordJet; 10 tracks.\"\n    },\n    {\n      \"id\": \"web:https://1.brf.be/sendungen/chansons/1220767/\",\n      \"url\": \"https://1.brf.be/sendungen/chansons/1220767/\",\n      \"kind\": \"web\",\n      \"note\": \"Radio review; confirms release 3 July 2026, Eigenvertrieb; mentions Tampon Blues.\"\n    },\n    {\n      \"id\": \"web:https://www.startnext.com/paula-linke-kuesse-mehr-kuesse\",\n      \"url\": \"https://www.startnext.com/paula-linke-kuesse-mehr-kuesse\",\n      \"kind\": \"web\",\n      \"note\": \"Crowdfunding campaign; planned release 11 Feb 2026 (postponed to 3 July 2026); CD and digital rewards.\"\n    },\n    {\n      \"id\": \"web:https://paula-linke.de/\",\n      \"url\": \"https://paula-linke.de/\",\n      \"kind\": \"web\",\n      \"note\": \"Artist website; confirms CD with booklet available, streaming release.\"\n    }\n  ],\n  \"conflicts\": [\n    {\n      \"field\": \"release title\",\n      \"values\": {\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\": \"KÜSSE! MEHR KÜSSE!\",\n        \"itunes:album/6798000134\": \"Küsse! Mehr Küsse!\",\n        \"deezer:album/1046252222\": \"Küsse! Mehr Küsse!\",\n        \"input\": \"Küsse! Mehr Küsse!\"\n      },\n      \"resolution\": \"Use the physical CD/Bandcamp spelling 'KÜSSE! MEHR KÜSSE!'; digital editions use title case.\"\n    },\n    {\n      \"field\": \"title track 5\",\n      \"values\": {\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\": \"Einfach aufstehen und weiter (Opa)\",\n        \"itunes:album/6798000134\": \"Einfach aufstehen und weiter\",\n        \"deezer:album/1046252222\": \"Einfach aufstehen und weiter\"\n      },\n      \"resolution\": \"Use physical CD/Bandcamp spelling with '(Opa)'; digital editions omit it.\"\n    },\n    {\n      \"field\": \"label\",\n      \"values\": {\n        \"web:https://1.brf.be/sendungen/chansons/1220767/\": \"Eigenvertrieb\",\n        \"deezer:album/1046252222\": \"recordJet\"\n      },\n      \"resolution\": \"Physical CD self-released (Eigenvertrieb); digital edition distributed by recordJet.\"\n    },\n    {\n      \"field\": \"release date\",\n      \"values\": {\n        \"web:https://paulalinke.bandcamp.com/album/k-sse-mehr-k-sse\": \"2026-07-03\",\n        \"web:https://1.brf.be/sendungen/chansons/1220767/\": \"2026-07-03\",\n        \"itunes:album/6798000134\": \"2026-08-01\",\n        \"deezer:album/1046252222\": \"2026-08-01\",\n        \"web:https://www.startnext.com/paula-linke-kuesse-mehr-kuesse\": \"2026-02-11 (planned)\"\n      },\n      \"resolution\": \"Physical CD released 3 July 2026; digital release 1 August 2026; startnext date was a planned date that was postponed.\"\n    }\n  ],\n  \"missing\": [\n    \"Physical CD barcode not found; digital UPC 4068992790596 belongs to the digital edition (recordJet).\",\n    \"No formal label; physical CD self-released (Eigenvertrieb); digital distribution via recordJet.\",\n    \"No MusicBrainz or Discogs entry found for this release.\",\n    \"Physical CD back cover not read; tracklist taken from Bandcamp listing and cross-checked with digital editions.\",\n    \"ISRCs not available (no MusicBrainz entry).\",\n    \"No catalogue number found.\"\n  ],\n  \"alternatives\": [\n    {\n      \"description\": \"Digital album (iTunes/Deezer), 10 tracks, released 2026-08-01, UPC 4068992790596, label recordJet.\",\n      \"source\": \"itunes:album/6798000134\",\n      \"why_not\": \"Digital edition; task prefers physical sound carriers. Used as supporting evidence for titles and durations.\"\n    }\n  ],\n  \"reasoning\": \"No barcode or format in input. Identified the physical CD edition 'KÜSSE! MEHR KÜSSE!' via Bandcamp (CD mit Booklet + Digital Album), confirmed by the artist's website and BRF1 (released 3 July 2026, Eigenvertrieb). Tracklist of 10 songs from Bandcamp, cross-checked against iTunes and Deezer digital editions (same 10 tracks; durations agree within 1 s). No MusicBrainz/Discogs entry; physical CD barcode unknown. Digital edition (1 Aug 2026, recordJet) listed as alternative.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-0580f191.json
```
</details>

### 41. `shell` +508s – completed

```
bin/tl-validate output/work/fall-0580f191.json 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 10 tracks (10 with duration), 6 sources, 4 conflicts, confidence=0.85
```
</details>

> **Agent** +510s: FERTIG found 10 Tracks confidence=0.85
