# AGENTS.md – Entwicklung im Repo (für Coding-Agenten und Team)

Dieses Repo ist ein Prototyp für den GEMA-Hackathon: Ein **opencode-Agent** (`.opencode/agents/tracklist.md`) findet zu lückenhaften Metadaten die richtige Tonträger-Ausgabe und deren Trackliste. Die Recherche-Anweisungen stehen **nicht** hier, sondern in der Agent-Datei und den Skills.

## Struktur

| Pfad | Inhalt |
|---|---|
| `.opencode/agents/tracklist.md` | Recherche-Agent: Ablauf, Regeln, Ausgabevertrag |
| `.opencode/skills/*/SKILL.md` | Wissen auf Abruf: Editionen unterscheiden, tiefe Quellen, Cover lesen |
| `opencode.jsonc` | Projekt-Config (Modell, Permissions); Provider/MCP aus der globalen Config |
| `bin/tl-*` | Tools für den Agenten (Symlinks auf `bin/tl` → `src/tracklist/cli/<name>.py`) |
| `src/tracklist/common.py` | HTTP-Cache, Rate-Limit pro Host (prozessübergreifend), Proxy pro Dienst, Ausgabe-Helfer |
| `src/tracklist/schema.py` | Ausgabevertrag (pydantic), geprüft von `tl-validate` |
| `src/tracklist/scoring.py` | Bewertung: Regelkatalog (Stufen 1–5), Fakten (Code), Prüfmodell (Claude), Ampel |
| `src/tracklist/fasttrack.py` | Schnellweg ohne Agent für eindeutige Barcode-Fälle |
| `src/tracklist/usage.py` | Kostenerfassung bezahlter Modell-Aufrufe (`$TL_USAGE_LOG`) |
| `runner/score.py` | vorhandene Ergebnisse (neu) bewerten |
| `runner/run.py` | Batch-Runner: eine opencode-Session pro Release, parallel, Trace + Validierung |
| `runner/agenttrace.py` | JSONL-Trace → Markdown + Kennzahlen |
| `data/samples.csv`, `data/hard.csv`, `data/traps.csv` | Testfälle (normal, schwer, Fallen) · Referenz in `data/expected.json` |
| `results/` | **finaler Lauf** (25 GEMA-Datensätze + 4 frische Fälle), Pfade/E-Mails geschwärzt · Oberfläche: `TL_OUT_DIR=results` |
| `examples/` | frühe Beispiele vom 19.11. (altes Format ohne Künstlerliste) · `output/` ist gitignored |
| `README.md`, `.env.example` | Überblick (Englisch) und benötigte Keys (nur Namen) |
| `tools/` | Infra-Checks (Keys, Cloudflare) |

## Neues Tool hinzufügen

1. `src/tracklist/cli/<name>.py` mit `main()` und Docstring (wird als `--help` genutzt), `run_cli(main)` am Ende.
2. HTTP nur über `common.http/get_json` (Cache, Rate-Limit, Proxy). Keys über `common.env()`; nie ausgeben.
3. Ausgabe knapp: eine Zeile pro Datensatz, Quellen-ID vorn (`<dienst>:<typ>/<id>`), URL, `clip()` für lange Listen.
4. `ln -s tl bin/tl-<name>` und in der Tool-Tabelle in `.opencode/agents/tracklist.md` ergänzen.

## Ausführen

```bash
uv sync
bin/tl-mb search --barcode 4019593960000           # Tools einzeln testen
uv run python runner/run.py --csv data/samples.csv --only kok-cd2004
uv run python runner/run.py --csv data/samples.csv --parallel 3 --repeat 2   # Konsistenz messen
uv run python tools/key_check.py                    # alle Keys prüfen
uv run python ui/smoke_test.py --examples           # Oberfläche: jede Seite + jedes Ergebnis rendern (vor jeder Demo!)
TL_OUT_DIR=results uv run streamlit run ui/app.py   # finalen Lauf ansehen, ohne neu zu rechnen
```

## Regeln

- Keine Secrets in Code, Doku oder Git – nur `.env` (gitignored).
- Laufende Doku: `DOKU.md` bei jeder Infra-/Setup-Änderung und wichtigen Erkenntnis ergänzen (Log mit Datum).
- Tool-Ausgaben sind Modellkontext: knapp halten, Rauschen weglassen.
