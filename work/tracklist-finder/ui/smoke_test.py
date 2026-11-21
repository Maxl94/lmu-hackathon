"""Rauchtest der Oberfläche: jede Seite und jedes einzelne Ergebnis einmal rendern, Fehler sammeln.

  uv run python ui/smoke_test.py          (mit alten Beispielen: --examples)
Nutzt streamlit.testing (kein Browser). Exit-Code 1, wenn irgendwo eine Exception auftritt.
"""
from __future__ import annotations

import sys
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent / "app.py")
PAGES = ["📋 Überblick", "🔍 Neue Recherche", "🛰️ Live", "📂 Ergebnisse", "💶 Kosten", "📊 Evaluation"]


def errors(at) -> list[str]:
    return [str(e.value)[:300] for e in at.exception]


def main():
    with_examples = "--examples" in sys.argv
    fails = []
    for page in PAGES:
        at = AppTest.from_file(APP, default_timeout=120)
        at.run()
        at.sidebar.radio[0].set_value(page).run()
        if errors(at):
            fails.append((page, errors(at)))
        print(f"{'❌' if errors(at) else '✓'} Seite {page}", flush=True)
        if page == "💶 Kosten":
            for opt in at.radio(key="cost_pick").options:
                at.radio(key="cost_pick").set_value(opt).run()
                if errors(at):
                    fails.append((f"Kosten/{opt}", errors(at)))
                print(f"   {'❌' if errors(at) else '✓'} Auswahl {opt}", flush=True)
        if page == "📂 Ergebnisse":
            if with_examples:
                at.sidebar.toggle[0].set_value(True).run()
            sel = at.sidebar.selectbox[0]
            for opt in sel.options:
                at.sidebar.selectbox[0].set_value(opt).run()
                e = errors(at)
                if e:
                    fails.append((opt, e))
                print(f"   {'❌' if e else '✓'} {opt}" + (f"  → {e[0][:160]}" if e else ""), flush=True)
    print(f"\n{len(fails)} Fehler" if fails else "\nalles fehlerfrei")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
