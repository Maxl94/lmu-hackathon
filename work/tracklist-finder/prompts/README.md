# Prompts – alle Modell-Texte an einem Ort

Alles, was ein Sprachmodell zu lesen bekommt, liegt hier (englisch; die Modelle antworten englisch).
Agent und Skills sind Links auf die Dateien, die opencode an festen Orten erwartet – hier bearbeiten genügt.

| Datei | Modell / Rolle | Verwendet in | Platzhalter |
|---|---|---|---|
| `agent.md` → `.opencode/agents/tracklist.md` | Recherche-Agent (Orchestrator, opencode) | `opencode run --agent tracklist` | – |
| `skills/*.md` → `.opencode/skills/<name>/SKILL.md` | Wissen auf Abruf für den Agenten | opencode lädt bei Bedarf | – |
| `task.md` | Auftrag pro Fall an den Agenten | `runner/run.py` | `$input`, `$out` |
| `judge.md` | Prüfmodell (System-Prompt) | `src/tracklist/scoring.py` | `$rubric` |
| `rubric.toml` | Regelkatalog (Stufen 1–5) – Prompt **und** Antwortschema des Prüfmodells **und** Oberfläche | `scoring.py`, `ui/app.py` | – |
| `vision.md` | Bildlesen (Cover/Rückseite → Trackliste) | `src/tracklist/cli/vision.py` | – |

Nicht hier, weil an Code gebunden: Feldbeschreibungen der Antwortschemas (`CoverReading` in `vision.py`,
Ausgabevertrag in `src/tracklist/schema.py`) und die Tool-Hilfen (Docstrings in `src/tracklist/cli/*.py` = `--help`).

Laden: `from tracklist import prompts` → `prompts.text(name)`, `prompts.render(name, **vars)`, `prompts.rubric()`.
