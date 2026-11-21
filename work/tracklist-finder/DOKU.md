# Laufende Doku – GEMA Tracklist-Hackathon

Wird laufend ergänzt: Setup, Infrastruktur, Erkenntnisse, offene Punkte.
**Keine Secrets in diese Datei.** Keys und Passwörter stehen nur in `.env`, und die ist per `.gitignore` ausgeschlossen.

---

## Aufgabe (Kurzfassung)

Hackathon am 20.11.2026, 14–18 Uhr, Kardinal Wendel Haus (GEMA × LMU Career Service).

- **Input:** Titel einer Veröffentlichung, optional Interpret, EAN/Barcode, Format (CD/Vinyl/Kassette). Oft unvollständig.
- **Output:** Trackliste mit Reihenfolge und Spieldauer der **richtigen Ausgabe**.
- **Pflicht:** Quellen angeben, widersprüchliche Treffer und fehlende Angaben kennzeichnen.
- **Demo:** an Beispielen zeigen und begründen, wie zuverlässig der Prototyp ist.

---

## Learnings (laufend ergänzt)

### Daten & Quellen
1. **Ein Barcode passt oft auf viele Ausgaben.** Bei RAM `888837168625` gibt es 27 Discogs-Releases, darunter inoffizielle Kassetten mit kopiertem Barcode. Der Barcode allein reicht also nicht, Format, Land, Jahr, Label und Trackanzahl müssen mitentscheiden.
2. **12 vs. 13 Stellen:** UPC-A `888837168625` = EAN-13 `0888837168625`. Die Datenbanken speichern beide Formen gemischt.
3. **Prüfziffer lohnt sich:** Ein vertippter Barcode (`…626`) wurde über die GTIN-Prüfziffer erkannt und korrigiert, das Ergebnis war die richtige CD.
4. **Katalognummer ≈ Barcode ohne Prüfziffer** (Sony `88883716862`). Verwechslungsgefahr.
5. **Digital ≠ physisch:** Deezer, TIDAL und iTunes kennen meist nur die *digitale* UPC. Physische EANs werden dort selten gefunden. Indizierte Alben (King of Kingz) fehlen in deutschen Stores ganz.
6. **Neuauflagen ändern Tracklisten:** Remixe kommen dazu (2004: 20 statt 16 Tracks), indizierte Songs fallen weg (Digital 2021).
7. **Discogs:** API ohne Token nutzbar (25/min, mit Token 60/min). Die Website hat Cloudflare, die API nicht. **Dauern fehlen oft**, und Felder können `null` sein. Die `notes` erklären Editionen oft explizit.
8. **MusicBrainz:** Dauern auf die Millisekunde, daher die genaueste Quelle. Unter Last kommen aber **502/503** (am Abend mehrfach) → Retries mit Backoff nötig, dazu Ausweichquellen.
9. **musik-sammler.de** ist die stärkste deutsche Zusatzquelle: statisches HTML, Trackliste **mit Dauer und EAN**, auch für Kassetten. Einfacher HTTP-Abruf genügt.
10. **Last.fm-Dauern sind unzuverlässig** (Intro „0:05“ statt 1:55). Nur als Gegenprobe verwenden.
11. **Auch Referenzdaten haben Fehler** (MusicBrainz: „Nute Bounce“). Eine Evaluation muss tolerant vergleichen. Es gibt keine absolute Wahrheit, nur gut belegte Mehrheiten.
12. **Schreibweisen variieren:** „Pittbull“ steht so auf der Rückseite, Discogs und MusicBrainz schreiben „Pitbull“. Ohne klare Regel wählen die Läufe unterschiedlich. Regel: Die gedruckte Schreibweise gewinnt, Abweichungen kommen als Konflikt-Notiz dazu.

### Bildlesen (Vision)
13. **Claude liest Rückseiten zuverlässig:** 20/20 Titel, ca. 16 s, ca. 2k/1k Tokens, also etwa 3 Cent pro Bild.
14. **Rückseiten haben oft keine Dauern.** Vision bestätigt Ausgabe, Titel und Reihenfolge. Die Dauern kommen aus der Datenbank oder Sammlerseite derselben Ausgabe.

### Agent
15. **opencode als Laufzeit trägt:** Projekt-Config, Agenten und Skills werden geladen, `opencode run --format json` liefert eine JSONL, aus der sich der Trace direkt bauen lässt.
16. **Der Agent arbeitet gründlich, wenn der Ausgabevertrag streng ist:**
    - mehrere unabhängige Quellenarten
    - Konflikte mit Begründung
    - Alternativen mit „why not“
    - lädt Skills selbst

    `tl-validate` als Pflichtschritt erzwingt saubere Belege.
17. **Tools dürfen nie mit Traceback abbrechen.** Das Modell soll eine Zeile Fehlertext sehen und dann ein anderes Tool nehmen (`run_cli` fängt alles ab).
18. **Der HTTP-Cache beschleunigt Wiederholungen stark** (61–127 s statt 256 s). Achtung: Konsistenz mit warmem Cache misst die *Entscheidungen* des Agenten, nicht wechselnde Quellen.
19. **SAIA-Budget pro Release:** ca. 20–25 Agent-Schritte = Requests. Bindend ist das **Stundenlimit von 400** (etwa 16 Releases/h), nicht das Tageslimit.

### Harte Fälle (19.11.)
24. **Nur ein Titel genügt, wenn er markant ist:** „Ich sag's dir mit Musik“ + MC → Kastelruther Spatzen, Koch D 221 190. Bestätigt über die J-Card auf den Discogs-Fotos (Vision).
25. **Ehrlichkeit funktioniert:** Musikverein-Kassette ohne Dauern in allen Quellen → 0 erfundene Dauern, alle 10 Tracks `duration_missing`. Der Agent dokumentiert, wo er gesucht hat (MB, musik-sammler, hitparade, Deezer, Last.fm, Web). Der strenge Vertrag plus `tl-validate` wirkt.
26. **Der Agent leitet Indizien her:** Das Jahr (ca. 1991) hat er aus dem Hüllentext erschlossen („1925 gegründet, im 67. Jahr“, vierstellige PLZ, die bis 1993 galt) und das als Schlussfolgerung gekennzeichnet. Beeindruckend, aber als Ableitung und nicht als Fakt darstellen.
27. **Sampler:** Interpreten pro Track werden korrekt gesetzt (2×CD, 40 Tracks). MusicBrainz und Discogs weichen bei ca. 10 % der Tracks um mehr als 2 s ab (Radio-Edits, Rundung) → 10 dokumentierte Konflikte. Welche Quelle als Referenz gilt, verändert die Metrik (Dauer ±2 s: 0,9 gegen Discogs, obwohl der Agent MusicBrainz gewählt hat).
28. **Harte Fälle brauchen mehr Zeit:** 157–324 s und bis zu 36 Tool-Aufrufe (≈ 25–40 SAIA-Requests).
29. **Gesamt nach 18 Läufen:** Ausgabe 18/18 richtig, Trackanzahl 100 %, Titel 100 %, Dauer ±2 s 98,7 %, 0 erfundene Dauern.
30. **`pkill -f "<muster>"` trifft auch die eigene Shell**, wenn das Muster in der Befehlszeile steht. Prozesse besser per PID oder `pkill -f '[s]treamlit'` beenden.

### Bewertung & Prüfmodell (20.11.)
31. **Fall-IDs verraten die Lösung.** Der Agent hat `spatzen-mc-titleonly` als Hinweis auf den Interpreten genutzt, und `trap-wrong-ean` hätte ihm verraten, dass die EAN falsch ist. Das Prüfmodell hat das aufgedeckt. Seitdem gibt der Runner dem Agenten eine neutrale ID (`fall-<hash>`) und einen neutralen Pfad (`output/work/`). Auch das Prüfmodell sieht keine Fall-ID.
32. **Ein unabhängiges Prüfmodell findet, was die eigene Referenz übersehen hat.** „Blasmusik aus Lohnde“ gibt es als Folge 1 *und* Folge 2, die Eingabe ist also wirklich mehrdeutig. Bei Spatzen passt auch eine Reader's-Digest-Box zum Titel. Unsere „18/18 richtig“ waren deshalb zu optimistisch.
33. **Das Prüfmodell erkennt auch Tricks des Agenten.** Er hat den Quellcode von `tl-validate` gelesen, um die Warnschwelle für `confidence` herauszufinden. Und er hat Discogs als Beleg für eine Dauer eingetragen, obwohl Discogs dort widerspricht. Beides steht jetzt als Regel in der Agent-Datei.
34. **Der Regelkatalog braucht für jeden realistischen Fall eine Stufe.** „Eindeutig, aber nur eine Quelle“ fehlte. Ohne diese Stufe wählt das Prüfmodell eine unpassende. Sie ist jetzt als Ausgabe-Stufe 3 ergänzt.
35. **Der Schnellweg braucht Toleranz.** Gibt es bei bis zu 10 % der Tracks eine Dauer-Abweichung über 2 s, gilt die feste Regel „MusicBrainz, millisekundengenau“, und der Konflikt wird markiert. Länderausgaben mit gleichem Barcode und gleicher Trackliste sind erlaubt. Sonst nimmt fast nichts den Schnellweg (King of Kingz hatte 2 von 20 Tracks mit 3 s Abweichung).
36. **Das Prüfmodell kostet mehr als der Agent auf SAIA.** Mit Opus 5.5 sind es 4–23 Cent pro Release, je nach Länge der Belege; die Prüfung dauert 8–25 s. Agent-Läufe auf SAIA kosten nichts, sie gehen nur vom Kontingent ab. Günstiger geht es mit `JUDGE_MODEL=claude-sonnet-5-5`, das kostet etwa die Hälfte.
37. **GLM-5.3 auf SAIA war am Hackathon-Tag überlastet.** Eine triviale Anfrage dauerte etwa 100 s. Alle vier Fallen-Fälle brachen nach 900 s ab, ein Normalfall ebenso. Qwen3.5-397B antwortete in 1,1 s. Deshalb ist Qwen jetzt Standard, und der Runner macht vor jedem Batch einen **Vorab-Check** (Antwortzeit und Rest-Kontingent, Warnung über 15 s).
38. **opencode meldet einen Tool-Aufruf erst, wenn er fertig ist.** Live sieht man darin nicht, was gerade läuft. Deshalb schreiben jetzt alle `tl-*`-Tools selbst `tool_start` und `tool_end` (über `run_cli`, Pfad aus `$TL_LIVE_LOG`). Der Runner schreibt die Phasen in `output/<id>.events.jsonl`.
39. **Alle Texte für die Modelle sind englisch** (seit 20.11. auch die Modell-Ausgaben): Agent, Skills, Runner-Prompt, Prüfmodell (Regelkatalog `RUBRIC_EN`, Antwortschema), Bildlesen, Tool-Hilfen und -Ausgaben, Validator, Schema-Beschreibungen. Freitextfelder im Ergebnis (reasoning, why_not, Bedenken …) schreiben die Modelle laut Anweisung **auf Deutsch**, weil Fachleute der GEMA sie lesen. Die Oberfläche bleibt deutsch.
40. **Parallelität auf SAIA:** 5 parallele Läufe mit einem langsamen Modell führen zu Wiederholungen (`retry` im Trace) und Zeitüberschreitungen. Höchstens `--parallel 3`, mit Qwen gehen 2–3 gut.
41. **Ein kleines Prüfmodell braucht eine genaue Anleitung, dann ist es so gut wie ein großes.** Haiku 5.5 stimmte zuerst nur bei 82 % der Ampeln mit Opus überein, mit 2 falschen Grünen. Drei Änderungen brachten es auf **94 %, ohne falsches Grün**, bei 1/35 der Kosten (0,004 $ statt 0,14 $):
    - Pro Kategorie zuerst `check`: die Stufen 5 → 1 abhaken, jede Bedingung erfüllt oder nicht, mit Beleg. Danach `rating`, danach `summary`.
    - Die Bedingungen stehen direkt am Feld, alles auf Englisch.
    - Fakten zur Eingabe (`input_fields`, `input_has_barcode`) sowie ein Deckel per Code (ohne Barcode in der Eingabe höchstens Stufe 4).

    Der eigentliche Fehler von Haiku war nicht das Verständnis: Es hat den Barcode des *Ergebnisses* für den *Eingabe*-Barcode gehalten. Alles, was zählbar ist, gehört in den Code.
42. **Agent-Modelle im Vergleich** (`eval/ladder.md`, 4 schwierige Fälle ohne Schnellweg):
    - Qwen3.5-397B, DeepSeek v4.1 Flash, Claude Haiku 5.5 und GLM-5.3 Flash: alle 4/4 richtig.
    - gpt-oss-120b fällt ab (1/3 richtig, ein Absturz).
    - Kosten pro Release laut opencode: Haiku ~0,01 $ (fast alles aus dem Prompt-Cache, 47 s), DeepSeek Flash ~0,02 $ (88 s), Qwen auf SAIA 0 $ (356 s; Listenpreis ~0,25 $).
    - Haiku macht nur ~6 Tool-Aufrufe statt ~20: Es prüft weniger gegen, die Dauern sind etwas schwächer.
43. **Was die GEMA wirklich braucht: welche Künstler auf dem Tonträger sind.** Neues Ergebnisfeld `artists`: jeder Künstler einmal, mit Rolle (main/featured/remixer/other), Tracks und Quellen.
    - Der Schnellweg leitet die Künstler aus den MusicBrainz-Credits ab. Alles nach „feat./with“ ist Gast, auch hinter „&“.
    - Der Validator verlangt das Feld und verbietet „feat.“ im Namen sowie doppelte Einträge.
44. **Echte Lieferung der GEMA** (`data/gema-sample.csv`): 25 Tonträger mit den Spalten `barcode, album_title, album_artist`.
    - 15 haben einen Barcode, darunter zwei mit 12 Stellen (UPC). 8 haben keinen, 2 haben „0“.
    - Formatangaben stecken im Titel („(LP)“, „(2CD)“, „CD - …“), der Interpret ist teils umgedreht („Fantastischen Vier, Die“), Sampler heißen „VA“ oder „Various (Sampler)“.
    - Der tolerante Import (`load_cases` in `runner/run.py`) erkennt die Spalten über Synonyme, behandelt „0“ als leer, markiert Barcodes in wissenschaftlicher Schreibweise und gibt unbekannte Spalten als Notiz weiter.
45. **Die GEMA stellt einen Gemini-API-Schlüssel**, der Verbrauch läuft auf ihre Rechnung. In `.env` steht er als `GEMA_GEMINI_API_KEY`, für opencode zusätzlich als `GOOGLE_GENERATIVE_AI_API_KEY` und `GEMINI_API_KEY`.
    - Er gilt für die **Gemini API (AI Studio)**: 66 Modelle, darunter Gemini 3.8 Flash, 3.1 Pro und gemini-4-*.
    - Vertex AI geht damit **nicht** (403), Bedrock ebenfalls nicht.
    - Claude-Modelle gibt es über diese API nicht, nur Gemini.
46. **Eine Schnittstelle für beide Anbieter:** `src/tracklist/llm.py` liefert strukturierte Antworten (pydantic) von `claude-*` (Anthropic) oder `gemini-*` (Gemini API, `responseJsonSchema` mit aufgelösten `$ref`), mit Kosten und Zeit.
    - Prüfung (`JUDGE_MODEL`) und Bildlesen (`TL_VISION_MODEL`) laufen darüber.
    - Der Agent läuft über opencode mit `-m google/gemini-…`.
    - Standard ist jetzt Gemini 3.8 Flash.
47. **Datensicherung vor dem Neustart:** Alle Läufe bis 14:44 liegen in `backups/output-20261120-1444/` (gitignored). `output/` enthält nur noch neue Läufe. Die Oberfläche zeigt die alten Beispiele aus `examples/` nur über einen Schalter.
48. **Vorgaben der GEMA** (Workshop-Repo, README „From Records to Royalties“):
    - 5 Fälle plus 1 frischer, unvorbereiteter Fall.
    - Pro Tonträger: Ausgabe, geordnete Trackliste mit **ausführenden Künstlern**, Disc-Nummer, Quellen-Links.
    - Ergebnis als *supported match / needs review / no match / technical failure*.
    - Bonus: Dauern, **Credits** (Komponist, Texter, Produzent, getrennt vom Interpreten), ISRC.
    - Pitch 10 min mit Kosten für 1.000 Datensätze (API, Laufzeit, Aufbau, **menschliche Prüfung**).
    - Das Workshop-Budget teilen sich alle Teams.
    - Umgesetzt: Seite „📋 Überblick“ (Kategorien, Kostenrechner), Credits-Schritt `src/tracklist/credits.py` (deterministisch aus MusicBrainz/Discogs), ISRC.
49. **Physisch vor digital:** Die GEMA lizenziert Tonträger. Digitale Kataloge (iTunes, Deezer, Bandcamp, MusicBrainz „Digital Media“) dienen nur als Beleg.
    - Der Agent muss eine physische Ausgabe wählen, sonst Status „ambiguous“ mit Vermerk „no physical edition found“.
    - Der Schnellweg ignoriert digitale Ausgaben.
    - Eine gewählte digitale Ausgabe löst eine K.-o.-Regel aus (→ Needs review).
    - Anlass: Paula Linke war digital gewählt, obwohl das CD-Digipak per Bildlesen gelesen war.
50. **Sparkonzept („so billig wie möglich, sonst kommt bei obskuren Releases bei den Künstlern nichts an“):**
    - **Agent:** DeepSeek v4.1 Flash, ~2 Cent. **Eskalation** zu Gemini 4 Hydrogen (~40 Cent) nur bei „kein gültiges Ergebnis“ oder „not_found“.
    - **Prüfung:** Claude Haiku 5.5, 0,4 Cent, 94 % wie Opus. Gemini Flash-Lite ist schlechter (82 %) und teurer, Gemini 4 Argon trifft Opus zu 100 %, kostet aber 5,6 Cent.
    - **Bildlesen:** Gemini 3.8 Flash, 0,4 Cent pro Bild, **höchstens 3 Bilder pro Fall**, hart im Werkzeug.
    - **Kürzere Werkzeug-Ausgaben:** `tl-scrape --max 6000`.
    - **Wo das Geld beim Agenten hingeht:** opencode schickt bei jedem Schritt den ganzen Verlauf erneut (250.000–900.000 Tokens pro Fall). Das erneute Lesen ist der größte Posten. Gemini-4-Agenten kosten deshalb 0,30–0,84 $ pro Fall.
    - Der Hydrogen-Vergleichslauf liegt in `backups/output-gemini-hydrogen-1523/`.
51. **Gemini über opencode:** Der eingebaute `google`-Anbieter bekam „monthly spending cap exceeded“, während direkte Aufrufe mit demselben Schlüssel funktionierten. Lösung: eigener Anbieter `gema` in `opencode.jsonc` über Googles OpenAI-kompatiblen Endpunkt (`…/v1beta/openai`, `{env:GEMA_GEMINI_API_KEY}`). opencode kennt dafür keine Preise, die Kosten rechnet der Runner aus den Tokens (`cost_estimated`).
52. **Teuer gegen günstig auf denselben 12 Tonträgern** (`eval/compare-expensive-vs-cheap.md`): gleiche Ausgabe 12/12, Kosten 4,87 $ → 0,19 $ (**25× günstiger**), Zeit 38 → 18 min.
    - Zwei echte Unterschiede: Die günstige Variante übernahm LP-Dauern aus der CD- bzw. Digitalausgabe (ehrlich vermerkt). Hydrogen ließ sie leer.
    - Bei den Fantastischen Vier übersah die günstige Variante die Gastkünstler. Der Discogs-Eintrag der LP hat keine Credits, Hydrogen fand sie über die CD-Ausgabe bei MusicBrainz.
    - Folgen: neue Markierung `duration_other_edition`, die nicht als bestätigt zählt (→ höchstens 🟡); Agent-Regel „Gastkünstler aus anderen Ausgaben desselben Albums“; Künstler-Sicherheitsnetz im Credits-Schritt (MusicBrainz-Credits, Discogs-Track- und Release-Credits mit Track-Angabe).
53. **Bildlesen mit wenig Nachdenken** (`gemini-3.8-flash@low`, Endung `@low` = `thinkingLevel`): auf 67 Bildern halb so teuer (0,28 Cent), schneller (8,7 s) und ohne Ausfälle, bei gleicher Qualität. Beim Bildlesen ist das Nachdenken der größte Kostenblock, nicht das Bild.
    - Collagen bringen kaum etwas: Bild-Tokens wachsen mit der Fläche, und kleiner Text leidet.
    - `minimal` kennt 3.8 Flash nicht.
54. **Credits sind dünn gesät:** Aus MusicBrainz und Discogs kamen für 9 von 25 Tonträgern Credits, für 4 ISRCs. Der Rest ist ehrlich als „credits missing“ vermerkt. Mehr Abdeckung bräuchte Booklets oder Verlagsdaten, und genau da hat die GEMA eigene Daten.
55. **Die Ampel bewertet nur den Kern** (Ausgabe, Trackliste mit Künstlern, Quellen). Dauern und Credits sind laut GEMA-README Bonus und bekommen eigene Abzeichen: ⏱ ✓ / ≈ (eine Quelle oder andere Ausgabe) / ✗, dazu 🎼 Credits x/n.
    - Grün mit schwachen Dauern heißt jetzt „übernehmen · Dauern prüfen“.
    - Gewichte: Ausgabe 50 %, Trackliste 35 %, Quellen 15 %, Dauern 0.
    - Mit den vorhandenen Ergebnissen ohne neuen Modellaufruf neu gerechnet (`runner/score.py --reaggregate`): 🟢 15 (9 davon mit Dauer-Hinweis), 🟡 8, 🔴 2, vorher 🟢 8, 🟡 15, 🔴 2.
56. **Credits hängen am Werk, nicht an der Ausgabe.** Deshalb dürfen sie aus jeder Ausgabe desselben Songs kommen. Drei neue Quellen im Credits-Schritt:
    - Discogs-Credits auf Release-Ebene mit Track-Angabe.
    - Eine andere MusicBrainz-Ausgabe desselben Albums, zugeordnet über den Titel (≥ 90 %).
    - **Genius** (Songwriter und Produzent, Titel und Künstler müssen passen).
    - Ergebnis: Credits für **19 statt 10 Tonträger, 238 von 357 Tracks (67 %)**. Genius ist stark bei Rap und Pop; Jazz, Krautrock, obskures Vinyl und Sampler bleiben lückenhaft. Der Rest bräuchte die GEMA-Werkdaten.

### Infrastruktur
20. **MusicBrainz begrenzt pro IP** → eigene Ausgangs-IP über Proxy oder Tunnel, wenn viele im selben WLAN arbeiten.
21. **Chromium nimmt keine Proxy-Zugangsdaten per Startoption** → SSH-SOCKS-Tunnel (`ssh -D`).
22. **Cloudflare:** Normales Selenium headless bleibt immer hängen. SeleniumBase UC headless kommt bei Discogs-Web und RYM durch, 45worlds blockt hart.

---

## Lokale Umgebung

| Tool | Version / Status |
|---|---|
| Git | 2.56.1 (Name/E-Mail konfiguriert) |
| uv | 0.13.9 |
| Python | 3.15.2. Getestet: `openai`, `pydantic`, `rapidfuzz`, `musicbrainzngs`, `python3-discogs-client`, `streamlit`, `pandas`, `python-dotenv`, `selenium` |
| IDE | VSCodium mit `ms-python.python`, `ms-pyright.pyright`, `ms-python.debugpy` |
| Browser | Chromium 157 (`/usr/bin/chromium-browser`), Firefox 160 |
| Selenium | Funktioniert headless mit Chromium. Den Treiber lädt Selenium Manager automatisch, kein `chromedriver` nötig |

Für den Fall, dass eine Vorlage eine ältere Python-Version verlangt: `uv python install 3.12`

### `.env` laden

```bash
uv run --env-file .env python script.py
# oder im Code:
from dotenv import load_dotenv; load_dotenv()
```

Bestehende Shell-Variablen werden dabei nicht überschrieben (getestet). Leere Einträge in der `.env` sind also unproblematisch.

---

## Key-Status (19.11., `uv run python tools/key_check.py`)

Das Skript prüft jeden Dienst mit einer Minimal-Anfrage und gibt keine Key-Werte aus. Nur Standardbibliothek.

| Dienst | Status | Detail |
|---|---|---|
| SAIA | ✅ | 14 Modelle. **Limits: 10 Requests/10 s, 400/h, 800/Tag** (Header `x-ratelimit-*-requests-{10s,hour,day}`) |
| Anthropic | ✅ | `claude-opus-5-5` verfügbar |
| OpenRouter | ✅ | |
| Brave | ✅ | 50 Requests/s, kein festes Monatslimit (Policy `50;w=1, 0;w=2592000`) |
| Tavily, Exa | ✅ | |
| SerpAPI | ✅ | Free Plan, 250 Suchen |
| Firecrawl, Jina | ✅ | |
| MusicBrainz | ✅ | User-Agent gesetzt |
| Discogs | ✅ | Token, 60/min |
| TIDAL | ✅ | Barcode-Filter findet die **digitale** UPC (RAM), aber nicht die physische EAN (King of Kingz) |
| Last.fm | ✅ | King of Kingz: 16 Tracks, 15 mit Dauer |
| YouTube | ✅ | |
| Genius | ✅ | Client Access Token, Suche „Bushido King of Kingz“ → 10 Treffer |
| Spotify, eBay, DNB, opengtindb, UPCitemdb, OpenAI, Azure | – | nicht gesetzt (optional) |

**Genius** verlangt beim Anlegen der App eine Website und eine Redirect-URI. Beides ist nur für OAuth mit Nutzer-Login nötig, wir brauchen nur den *Client Access Token*. Beliebige Werte gehen, z. B. die Repo-URL als Website und `http://localhost:8080/callback` als Redirect-URI. Danach *Generate Access Token* klicken.

---

## Datenquellen – Erkenntnisse aus Tests (19.11.)

### Strukturierte APIs

| Quelle | Key | Erkenntnis |
|---|---|---|
| MusicBrainz | nein (User-Agent mit Kontakt Pflicht) | 1 req/s pro IP, unter Last `503`. Barcode-Suche findet die 12- und die 13-stellige Variante. `inc=recordings` liefert Tracks mit Dauer in ms |
| Discogs API | optional (Token: 60 statt 25 req/min) | Ohne Token nutzbar, inklusive Tracklist und Bildern. **Viele Ausgaben, auch inoffizielle, teilen sich einen Barcode** (Daft Punk RAM: 27 Treffer). Dauer als String `"4:35"`, oft leer. Die Website hat Cloudflare, die API nicht |
| iTunes Search | nein | `lookup?upc=<EAN>&entity=song` liefert die volle Trackliste mit ms |
| Deezer | nein | Kennt nur **digitale** UPCs. Physische EANs ergeben meist keinen Treffer |
| Cover Art Archive | nein | Liefert oft auch **Back/Booklet/Tray**, gut als Input für Vision |
| TIDAL | ja | Laut Spec `GET /albums?filter[barcodeId]=…` (EAN-13/UPC-A), noch nicht getestet |
| Spotify | ja | Seit 02/2026: App-Owner braucht Premium, Suche max. 10 Treffer |
| DNB / Deutsches Musikarchiv | Token per Mail | SRU `services.dnb.de/sru/dnb.dma`. Ohne Token kamen `429`, dann `403` |
| Google Custom Search | – | Für Neukunden geschlossen, Abschaltung 01.01.2027 |

### Fallbeispiel: Bushido – King of Kingz

- **MusicBrainz:** 5 Ausgaben: MC 2001 (16 Tracks), 2× CD 2003 (16), CD 2004 Exclusive Edition (20, EAN `4019593960000`), Digital-Re-Release 2021.
- **Discogs:** über 10 Ausgaben, davon allein 7 Kassetten-Varianten.
- **Cover Art Archive:** Front bei allen Ausgaben, Back/Booklet/Tray bei zwei CDs.
- **iTunes:** 0 Treffer, weil das Album indiziert ist (BPjM 2005).
- **Websuche:** widersprüchliche Tracklisten (Demo mit 6, 16 oder 20 Tracks; die Neuauflage ohne indizierte Songs).
- **Lektion:** Das Problem ist meist nicht das *Finden*, sondern die **richtige Ausgabe**.

### Scraping-Ziele: Erreichbarkeit

| Seite | Ergebnis | Weg |
|---|---|---|
| musik-sammler.de | 200, Inhalt direkt im HTML | httpx / Selenium |
| hitparade.ch (und Schwesterseiten) | 200, Tracklisten mit Dauer | httpx |
| discogs.com (Web) | 403 Cloudflare. Selenium: Challenge. **SeleniumBase UC headless: OK** | API bevorzugen, Web per UC als Fallback |
| rateyourmusic | 403 Cloudflare. Selenium: Challenge. **SeleniumBase UC headless: OK** | SeleniumBase UC |
| 45worlds.com | 403. Selenium: Challenge. **UC: Hard-Block „Attention Required“** | Firecrawl testen, ggf. sichtbares Browserfenster mit Klick |
| eBay | 403 | Browse API (GTIN-Suche, Freigabe ca. 1 Werktag) / Firecrawl |
| medimops | 200, aber Bot-Check-Marker | testen |
| portal.dnb.de | Timeout | später erneut testen |

**Scraper-Stufen**, der Agent wählt selbst:
1. `httpx` + Parser
2. Firecrawl
3. Selenium, interaktiv: Formulare, Klicks, Pagination, Screenshots → Claude Vision
4. SeleniumBase UC-Modus (`SB(uc=True, headless2=True, binary_location="/usr/bin/chromium-browser")`) für Seiten mit Cloudflare

**Selenium-Notizen (Test vom 19.11.):**
- Normales Selenium headless bleibt bei Cloudflare immer an „Just a moment…“ hängen.
- Den UC-Modus erkennt man am **Seitentitel**, nicht am HTML. Cloudflare bettet `challenge-platform`-Skripte auch in normale Seiten ein.
- `uc_gui_click_captcha()` braucht ein Display (PyAutoGUI). Headless geht das nicht, ein Xvfb ist nicht installiert.
- Test-Skripte im Repo:
  - `tools/cloudflare_check.py <url…> [--proxy socks5://127.0.0.1:1081]`: normales Selenium vs. UC
  - Abhängigkeiten: `selenium seleniumbase httpx requests python-dotenv`

---

## LLMs

### SAIA (GWDG)

- Base-URL: `https://chat-ai.academiccloud.de/v1` (OpenAI-kompatibel)
- Tool-Calling funktioniert je nach Modell. opencode mit SAIA läuft gut.
- Limits stehen in den Headern `x-ratelimit-*`.
- Modelle abfragen: `GET /v1/models`
- [Doku](https://docs.hpc.gwdg.de/services/ai-services/saia/)

### Anthropic

- Vision (Rückseiten, Booklets) und Final-Judge: `claude-opus-5-5`
- Preise: $4 / $20 pro MTok
- Web-Search kostet $10 pro 1.000 Suchen, Web-Fetch nur die Tokens. [Preise](https://platform.claude.com/docs/en/about-claude/pricing)

**Prinzip:** KI zuerst. API-Knappheit ist kein Grund für weniger KI.

---

## Gerüst: opencode-Agent + tl-Tools (19.11., läuft ✅)

**Struktur** (Details in `AGENTS.md`):
- Agent: `.opencode/agents/tracklist.md` (Ablauf, Regeln, Ausgabevertrag)
- Skills: `.opencode/skills/{edition-disambiguation,deep-sources,cover-reading}/SKILL.md`. Werden geladen, im ersten Lauf hat der Agent selbst einen Skill gezogen
- Tools in `bin/` (Python in `src/tracklist/cli/`):
  - `tl-gtin`, `tl-mb`, `tl-discogs`, `tl-itunes`, `tl-deezer`, `tl-lastfm`, `tl-caa`
  - `tl-search` (Brave), `tl-scrape` (http → firecrawl → uc), `tl-vision` (Claude Opus 5.5), `tl-validate`
- Gemeinsame Infrastruktur (`src/tracklist/common.py`):
  - HTTP-Cache in `.cache/http`
  - **Rate-Limit pro Host über alle parallelen Sessions** (Datei-Lock; MusicBrainz 1,1 s, Discogs 1,05 s, iTunes 3 s)
  - Proxy pro Dienst (`MUSICBRAINZ_PROXY` usw.)
- Ausgabevertrag: `src/tracklist/schema.py` (pydantic, `extra=forbid`). `tl-validate` prüft Schema und Plausibilität: Quellen-IDs vorhanden, Dauer oder Kennzeichnung, Summe, Duplikate, `ambiguous` hat Alternativen
- Runner: `uv run python runner/run.py --csv data/samples.csv [--only id,…] [--parallel N] [--repeat N] [-m provider/model]`
  - erzeugt `output/<id>.json`, `.trace.jsonl`, `.trace.md` und `output/runs.jsonl`
- Beispiele (committet): `examples/`

**Testläufe 19.11. (Modell `kisski/glm-5.3`):**

| Fall | Ergebnis | Zeit | Tools | Bemerkung |
|---|---|---|---|---|
| `kok-cd2004` (EAN, CD) | ✅ found, 20/20 Tracks mit Dauer, conf 0.9 | 256 s | 32 | 4 Quellenarten (MB, Discogs, musik-sammler, Rückseite per Vision); Dauer-Konflikte > 2 s dokumentiert; 4 Alternativen (CD 2003, 2-CD 2005, MC 2001, Digital 2021); Dauern = MusicBrainz |
| `ram-badean` (EAN mit falscher Prüfziffer) | ✅ found, 13/13, conf 0.9 | 164 s | 19 | Prüfziffer erkannt und korrigiert → richtige CD; Japan-CD (14 Tracks), US-CD, 10th Anniversary, Vinyl als Alternativen |
| `kok-mc` (Kassette, ohne EAN) | ✅ found, 16/16, conf 0.85 | 175 s | 19 | Positionen A1–B8, Erstauflage 2001; 2.–6. Auflage als Alternativen (gleiche Trackliste → `found` gemäß Skill) |

- Parallel 2 läuft problemlos.
- **Pro Release ca. 20–25 Agent-Schritte = SAIA-Requests.** Bei 800 Requests pro Tag reicht ein Key also für etwa 30–40 Releases. Für mehr: weitere Keys aus dem Team oder ein anderes Modell per `-m`.
- Vision: ca. 2k Tokens rein und 1k raus pro Bild, also etwa 3 Cent.

## Evaluation & Demo-UI (19.11.)

**Evaluation:** `uv run python eval/evaluate.py` erzeugt `eval/report.md` und `eval/report.json`.
- Referenz: `data/expected.json`. Pro Fall stehen dort die akzeptierten Release-IDs bzw. Barcode oder Format und eine Referenz-Trackliste (MusicBrainz/Discogs, wird live geholt und gecacht).
- **Pro Lauf:**
  - Ausgabe richtig?
  - Trackanzahl richtig?
  - Titel-Übereinstimmung, tolerant: `token_set_ratio ≥ 90` oder ohne Leerzeichen `≥ 88`
  - Dauer ±2 s zur Referenz
  - erfundene Dauern, wenn die Referenz keine hat
- **Pro Fall über Wiederholungen** (`--repeat N` erzeugt `…-r1..rN`): gleiche Ausgabe, gleicher Status, gleiche Anzahl, gleiche Titel, maximale Dauer-Spreizung.

**Konsistenzmessung 19.11.** (SAIA `glm-5.3`, 4 Fälle × 3 Läufe plus 3 Einzelläufe = 15 Läufe):
- **Ausgabe richtig 15/15**
- Trackanzahl 100 %
- Titel 100 % (tolerant)
- Dauer ±2 s 100 %
- **Konsistenz:**
  - gleiche Ausgabe und gleicher Status in allen Wiederholungen
  - Dauer-Spreizung 0 s
  - Titel nur bei `kok-cd2004` uneinheitlich (Pittbull/Pitbull) → Regel zur Schreibweise im Agenten nachgeschärft
- `kok-noartist` (CD ohne Interpret): 3/3 `ambiguous` mit Konfidenz 0,45–0,55 und Alternativen. Genau das gewünschte Verhalten.
- Laufzeit Ø 121 s bei warmem Cache.

**Demo-UI:** `uv run streamlit run ui/app.py --server.address 127.0.0.1`
- *Neue Recherche:* Formular → startet `runner/run.py`, zeigt die Tool-Aufrufe live
- *Ergebnisse:* alle `output/` + `examples/`
  - Kopfzeile mit Status, Konfidenz, Tracks, Gesamtdauer und Quellen
  - Ampel pro Track: 🟢 Dauer von ≥ 2 Quellen, 🟡 eine Quelle oder Konflikt, 🔴 fehlt
  - Quellen mit Links, Konflikte mit Auflösung, Alternativen mit „why not“
  - Download als JSON/CSV
  - Agent-Trace zum Aufklappen
- *Evaluation:* zeigt `eval/report.md`, Button „Neu berechnen“
- Mit Headless-Chromium und Screenshots geprüft, keine Exceptions.

---

## Bewertung, Schnellweg, Kosten (20.11.)

**Ziel:** Für jedes Ergebnis soll klar sein, ob man es übernehmen kann und warum. Die Konfidenz, die der Agent selbst angibt, ist dafür ungeeignet.

**Regelkatalog** (`src/tracklist/scoring.py`, `RUBRIC`): vier Kategorien, jede mit Stufen 1–5. Jede Stufe beschreibt beobachtbare Belege, keine Gefühle.

| Kategorie | Gewicht | bewertet von | 5 heißt … | 1 heißt … |
|---|---|---|---|---|
| Ausgabe | 40 % | Prüfmodell | Barcode exakt in ≥ 2 unabhängigen Quellen, kein Konkurrent | passt nicht, Widerspruch zur Eingabe, nicht gefunden |
| Trackliste | 25 % | Prüfmodell | ≥ 2 Quellen gleich in Anzahl, Reihenfolge, Titeln | Quellen widersprechen sich ungeklärt |
| Dauern | 25 % | Code | ≥ 90 % der Tracks von ≥ 2 Quellen auf ± 2 s bestätigt | < 50 % der Tracks mit Dauer |
| Quellen | 10 % | Prüfmodell | Datenbank + Primärquelle (gelesenes Cover) | nur Websuche/Foren |

- **Code** berechnet die zählbaren Fakten: Barcode- und Format-Abgleich, Ähnlichkeit von Interpret und Titel, Abdeckung der Dauern, Quellenfamilien, Validierung.
- **Prüfmodell** (`JUDGE_MODEL`, Standard `claude-opus-5-5`):
  - Eigener Aufruf mit frischem Kontext und einer anderen Modellfamilie als der Agent (GLM auf SAIA).
  - Es sieht Eingabe (ohne Fall-ID), Fakten, Ergebnis und die Tool-Ausgaben der Recherche als Belege.
  - Es schreibt zuerst die Begründung, dann die Stufe. Dazu kommen **Bedenken**, also konkrete Mängel.
- **Gesamt:** gewichtetes Mittel mit **K.-o.-Regeln**.
  - **Rot (manuell klären):** Ausgabe ≤ 2, Trackliste ≤ 2, Dauern = 1, Barcode oder Format widersprechen der Eingabe, nicht gefunden, oder Vertrag verletzt.
  - **Grün (übernehmen):** Gesamt ≥ 4,0 und Ausgabe, Trackliste und Dauern jeweils ≥ 4.
  - **Gelb (kurz prüfen):** alles dazwischen.
- **Ablage:** `output/<id>.score.json`. Vorhandene Ergebnisse lassen sich neu bewerten: `uv run python runner/score.py --dir examples`.

**Schnellweg** (`src/tracklist/fasttrack.py`) für Fälle ohne Agent. Alle Bedingungen müssen erfüllt sein:
- Die EAN ist gültig und trifft 1–5 offizielle MusicBrainz-Ausgaben mit gleicher Trackliste.
- Titel und Interpret der Eingabe passen.
- Discogs findet höchstens 4 Ausgaben mit gleicher Trackanzahl.
- Die Titel stimmen überein, ≥ 90 % der Tracks haben in beiden Quellen eine Dauer, und höchstens 10 % weichen um mehr als 2 s ab.

Sonst geht der Fall an den Agenten, und der Grund steht im Trace. Auch beim Schnellweg läuft danach das Prüfmodell. `--no-fast` erzwingt den Agenten.

**Kosten:** `runs.jsonl` enthält pro Lauf ein Feld `cost`:
- Agent in USD; bei SAIA zählen nur die Anfragen, sie sind kostenlos und gehen vom Kontingent ab.
- Bildlesen: jeder Aufruf von `tl-vision` schreibt nach `$TL_USAGE_LOG`.
- Prüfmodell und Gesamtsumme.

Die Oberfläche zeigt eine Box mit Ampel, vier Kategorien, „Warum?“ (Begründung, Belege, Bedeutung der Stufen, die erreichte Stufe hervorgehoben), Bedenken, Fakten und Kosten.

**Fallen-Fälle** (`data/traps.csv`, `trap: true` in `expected.json`): Hier ist richtig, dass das Ergebnis **nicht grün** wird.
- falsche EAN (gehört zu Daft Punk)
- ausgedachtes Album
- Interpret passt nicht zum Titel
- falsches Format (Lohnde gibt es nur als Kassette)

---

## Live-Ansicht (20.11.)

- **Seite „🛰️ Live“:** zeigt alle Läufe der letzten 2 Stunden, auch Batch-Läufe aus der Kommandozeile. Sie aktualisiert sich alle 2 s (`st.fragment(run_every="2s")`).
- **Pro Lauf:**
  - Phasenkarten: ⚡ Schnellweg → 🤖 Recherche-Agent (Modell) → 🔍 Prüfmodell (Modell) → 🏁 Ergebnis, jeweils mit Zustand und Zeit.
  - Zeile **„Gerade“**: welches Tool welchen Dienst gerade abfragt und seit wann, ob der Agent nachdenkt (Modell-Schritt n) oder das Prüfmodell liest.
  - **Zeitleiste:** jeder Tool-Aufruf mit Dienst-Symbol (🗄️ MusicBrainz, 💿 Discogs, 🖼️ Bildlesen, 🕸️ Scraper, 🔎 Websuche …), Dauer und ❌ bei Fehlern, dazu die Zwischentexte des Agenten (💬).
- **„Neue Recherche“** zeigt dieselbe Live-Ansicht, während der Lauf arbeitet.
- **Datenquellen:**
  - `output/<id>.events.jsonl` (Runner-Phasen + `tool_start`/`tool_end` der Tools)
  - `output/<id>.trace.jsonl` (opencode: Agent-Text, Schritte, Tokens)
- **Code:** `ui/live.py`.

---

## Architektur-Vorschlag: opencode als Agent-Runtime (19.11., umgesetzt)

Idee: kein eigenes Agent-Framework, sondern **opencode** als Laufzeit. Eigene Frameworks erst, wenn klar ist, was man braucht.

**Lokal vorhanden:**
- opencode **2.3.2**
- Provider `kisski` (SAIA) mit u. a. `qwen3-coder-next`, `deepseek-v4-flash-0731`, `deepseek-v4.1-flash-1017`
- MCP-Server `brave-search` und `firecrawl` (globale opencode-Konfiguration)

**Skizze:**
```
opencode.jsonc     Provider (kisski, anthropic), MCP (brave, firecrawl), Agenten, Permissions
AGENTS.md          Rechercheablauf, Ausgabeschema, Regeln für Quellen und Konflikte
bin/tl-*           mb, discogs, itunes, caa, gtin, scrape (httpx → Firecrawl → Selenium/UC), vision (Claude), validate
runner/batch.py    opencode run --format json --auto --archived --title <id> … pro Release, parallel
eval/              Testset, Metriken, Mehrfachläufe → Übereinstimmung als Zuverlässigkeitsmaß
ui/app.py          Streamlit: Eingabe, Ergebnis mit Ampel, Quellen, Agent-Trace
```

**Verifiziert (19.11., Smoke-Test im Scratchpad):**
- Projektlokale `opencode.jsonc` wird zusätzlich zur globalen geladen (`opencode debug config`).
- Agenten werden gefunden: aus `opencode.jsonc` → `"agents": {"<id>": {"description", "mode": "primary", "model": "kisski/glm-5.3", "prompt"}}` und als Markdown in `.opencode/agent/*.md` **und** `.opencode/agents/*.md` (Frontmatter `description`, `mode`). Prüfen mit `opencode debug agents`.
- Lauf ohne Oberfläche:
  ```bash
  PATH=$PWD/bin:$PATH opencode run --standalone --format json --auto --archived \
    --title <id> --agent <agent> -m kisski/glm-5.3 "<auftrag>" > run.jsonl
  ```
  → **4 s**, Shell-Tool aus `bin/` aufgerufen, `out.json` korrekt geschrieben, Exit-Code 0.
- Die JSONL-Events haben die Typen `step_start`, `tool_use` (mit `part.tool`, `part.state.input.command`, `status`), `text` und `step_finish` (mit `tokens`, `cost`, `reason`). Alle tragen `sessionID`. Daraus lässt sich der Agent-Trace für die UI direkt bauen.
- SAIA-Modelle in opencode: `kisski/glm-5.3`, `glm-5.3-flash`, `qwen3.5-397b-a17b`, `qwen3.6-35b-a3b`, `qwen3.8-27b`, `deepseek-v4-flash-0731`, `deepseek-v4.1-flash-1017`, `mistral-large-4-1t-a52b`, `qwen3-coder-next`, `gemma-4-31b-it` u. a.

---

## GEMA-Formular „Herstellungsmeldung Tonträger“

Quelle: gema.de, Stand 01/2023. So meldet die GEMA selbst Tonträger, das ist ihre Fachsprache.
- Kopf:
  - Trägerart (z. B. CD), Trägertitel, Interpret
  - **Gesamtspieldauer (Min:Sek)**, **Gesamttitelzahl**, **Katalog-/Bestellnummer**
  - Erst- oder Nachauflage, Budget, Compilation-Code
- Titelliste pro Track:
  - Lfd. Nr., **Original-Werktitel + evtl. Alternativtitel**
  - **W/F**: W = Werk (Spieldauer > 1:45), F = Fragment (≤ 1:45)
  - Besetzung, **ISRC**
  - K = Komponist / B = Bearbeiter, T = Textdichter, OV = Originalverlag, SV = Subverlag
  - **Spieldauer (Min:Sek)**
- **Mehrfachträger** (z. B. Doppel-CD): jeder Träger auf einer eigenen Meldung.
- Idee: Export im Aufbau dieser Titelliste.
  - W/F lässt sich aus der Dauer ableiten.
  - ISRC kommt aus MusicBrainz.
  - Unsere Titel-Konflikte werden zu Alternativtiteln.
  - Komponist und Textdichter (MusicBrainz-Werke, Discogs-Credits) als Bonus für die Werkzuordnung.

---

## Offene Punkte

- [x] SAIA-Key prüfen: ok. Limits: 10 Requests/10 s, 400/h, 800/Tag
- [x] Anthropic-Key → `.env` (ok, `claude-opus-5-5` verfügbar)
- [x] Discogs-Token, TIDAL, Last.fm → `.env` (alle ok)
- [x] Genius-Token (ok, liefert keine Laufzeiten)
- [ ] 45worlds: Firecrawl oder sichtbaren Browser mit Captcha-Klick testen
- [ ] Optional: eBay-Developer-Account, DNB-Token (Freigabe dauert)
- [ ] Härtere Fälle vom GEMA-Testset morgen sofort durch `runner/run.py` + `eval/` jagen
- [ ] Modellvergleich (SAIA `qwen3.5-397b`/`mistral-large-4` vs. Claude) auf denselben Fällen
- [ ] Konsistenz mit kaltem Cache messen (Quellen-Schwankungen statt nur Agent-Entscheidungen)

---

## Log

- **21.11.2026:**
  - CSV-Import in der Oberfläche (🔍 Neue Recherche → Reiter CSV-Import): Vorschau mit Auswahl, Start im Hintergrund, IDs mit Batch-Präfix
  - Prüfmodell schwankt bei Grenzfällen: Jackfruit Traxx 1 zweimal gleiche Ausgabe, einmal Stufe 2 (rot), einmal Stufe 4 (grün) → im README unter Grenzen; feste Regel „kein Barcode + Titel passt nicht → höchstens gelb“ wäre die Abhilfe (nicht eingebaut)
  - Abschluss: finaler Lauf als `results/` committet (25 GEMA-Datensätze + 4 frische Fälle: Peter Fox, 2× Kenshi Yonezu, Bushido-Demotape), lokale Pfade und E-Mail-Adressen aus gescrapten Seiten geschwärzt
  - Oberfläche liest per `TL_OUT_DIR=results` den finalen Lauf ohne Neuberechnung; Rauchtest mit `results/` und `output/` fehlerfrei
  - `README.md` (Englisch) und `.env.example` für die Abgabe
  - Doppellauf STRAY SHEEP mit Barcode entfernt (Barcode stammte aus dem ersten Lauf, kein unabhängiger Test)
- **20.11.2026:**
  - Prompts zentral in `prompts/`, Modell-Ausgaben englisch, Prüfmodell v3 (check → rating → summary, Haiku ≈ Opus), Agent- und Prüfmodell-Leiter
  - Ergebnisfeld `artists` (Künstler pro Tonträger), toleranter Import, Lauf über die GEMA-Daten (25 Tonträger)
  - Kosten pro Lauf als Tabelle und eigene Seite „Kosten“; Umstellung auf die Gemini API (GEMA-Schlüssel), Sicherung der alten Läufe, Bildlesen-/Prüfmodell-/Agent-Vergleich mit Gemini
  - GEMA-Vorgaben eingearbeitet (Überblick, Credits/ISRC, physisch vor digital), Sparkonzept (DeepSeek + Eskalation, Haiku, Gemini 3.8 Flash @low, max. 3 Bilder): 1,9 Cent pro Tonträger; Vergleich teuer/günstig; Abschlusslauf
  - Bewertung nach Regelkatalog (Code + Prüfmodell Claude), Ampel mit K.-o.-Regeln, Schnellweg ohne Agent, Kostenerfassung, Fallen-Fälle; Fall-ID-Leck geschlossen
  - Live-Ansicht (Phasen, aktive Tools, Zeitleiste), alle Prompts auf Englisch, Standardmodell Qwen3.5 (GLM überlastet), Vorab-Check
  - Feldaufbau des GEMA-Formulars Herstellungsmeldung/Titelliste
- **19.11.2026:**
  - Umgebung geprüft
  - APIs getestet (MusicBrainz, Discogs, iTunes, Deezer, CAA, DNB)
  - `.env`-Vorlage und `.gitignore` angelegt
  - Repo mit `origin` verbunden
  - Selenium lokal verifiziert
  - SeleniumBase-UC-Test: Discogs-Web und RYM OK, 45worlds hart geblockt
  - Initial-Commit gepusht (`e1a5c69`)
  - Vorschlag: opencode als Agent-Runtime
  - Gerüst gebaut (Agent, 3 Skills, 11 Tools, Runner, Trace)
  - Konsistenzmessung (12 Läufe) und harte Fälle (Sampler, nur Titel, Kassette ohne Dauern): 18/18 Ausgaben richtig
  - Evaluation (`eval/`) und Streamlit-UI (`ui/app.py`)
  - Agent-Regeln: Schreibweise, Format-Vokabular
  - Learnings 1–30
  - 3 Testfälle ok (`examples/`)
  - Smoke-Test opencode + SAIA ok
  - Keys eingetragen, `tools/key_check.py`: 15/22 ok (inkl. Genius), die übrigen sind optional
