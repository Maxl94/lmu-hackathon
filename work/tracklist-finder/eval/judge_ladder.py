"""Prüfmodell-Leiter: Wie gut stimmen günstigere Prüfmodelle mit Opus überein?

  uv run python eval/judge_ladder.py [v2]   (liest eval/judge-ladder/<version>/<tag>/*.score.json → eval/judge-ladder-<version>.md)

Referenz: opus-a. opus-b = zweiter Opus-Lauf → Rauschgrenze (so oft ist Opus mit sich selbst einig).
"""
from __future__ import annotations

import json
import statistics as stt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from tracklist.scoring import aggregate, upgrade_score  # noqa: E402
from tracklist.usage import cost_usd  # noqa: E402

VERSION = sys.argv[1] if len(sys.argv) > 1 else "v2"
DIR = ROOT / "eval/judge-ladder" / VERSION
CATS = ("edition", "tracklist", "sources")
PRICE = {"opus-a": "$4 / $20", "opus-b": "$4 / $20", "sonnet": "$2 / $10", "haiku": "$0.10 / $0.50", "gemini-3.8-flash": "$0.83 / $4.13 (GEMA)", "gemini-3.1-pro-preview": "$2 / $12 (GEMA)",
         "gemini-4-argon": "$2 / $10 (GEMA)", "gemini-4-carbon": "$2 / $10 (GEMA)", "gemini-4-hydrogen": "$1.50 / $7.50? (GEMA)",
         "gemini-4-neon": "? (GEMA)"}


def _fair(sc: dict) -> dict:
    """Ampel ohne die Regel „Ausgabevertrag verletzt“ neu berechnen – alte Ergebnisse haben noch kein Feld artists."""
    f = {k: v for k, v in (sc.get("facts") or {}).items() if k != "validation_errors"}
    return dict(sc, **aggregate(sc["categories"], f))


def load(tag: str) -> dict[str, dict]:
    return {f.name: _fair(upgrade_score(json.loads(f.read_text()))) for f in sorted((DIR / tag).glob("*.score.json"))}


def main():
    ref = load("opus-a")
    tags = [t for t in ("opus-b", "sonnet", "haiku") if (DIR / t).exists()] + sorted(d.name for d in DIR.iterdir() if d.is_dir() and d.name.startswith("gemini"))
    md = [f"# Prüfmodell-Leiter ({VERSION})", "", f"Referenz: Opus 5.5 (Lauf A), {len(ref)} Ergebnisse. Opus Lauf B zeigt die Rauschgrenze.", "",
          "| Prüfmodell | Preis in/out pro MTok | Ampel gleich | Stufe gleich | Stufe ± 1 | Fallen rot | Ø Kosten | Ø Dauer |",
          "|---|---|---|---|---|---|---|---|"]
    rows = {}
    for tag in ["opus-a"] + tags:
        cur = load(tag)
        common = [k for k in ref if k in cur]
        lv = [ref[k]["level"] == cur[k]["level"] for k in common]
        ex, near = [], []
        for k in common:
            for c in CATS:
                a, b = ref[k]["categories"][c]["rating"], cur[k]["categories"][c]["rating"]
                ex.append(a == b)
                near.append(abs(a - b) <= 1)
        traps = [cur[k]["level"] != "grün" for k in common if "trap-" in k]
        costs = [(cur[k]["judge"].get("cost_usd") or cost_usd(cur[k]["judge"].get("model") or tag,
                                                              {"input_tokens": cur[k]["judge"].get("tokens_in") or 0,
                                                               "output_tokens": cur[k]["judge"].get("tokens_out") or 0}) or 0)
                 for k in common if cur[k].get("judge")]
        secs = [(cur[k].get("judge") or {}).get("seconds") or 0 for k in common if cur[k].get("judge")]
        rows[tag] = (lv, ex, near)
        pct = lambda x: f"{sum(x) / len(x):.0%}" if x else "–"  # noqa: E731
        md.append(f"| {tag} | {PRICE.get(tag, '?')} | {pct(lv)} ({sum(lv)}/{len(lv)}) | {pct(ex)} | {pct(near)} | "
                  f"{sum(traps)}/{len(traps)} | ${stt.mean(costs) if costs else 0:.4f} | {stt.mean(secs) if secs else 0:.0f} s |")
    md += ["", "## Abweichungen der Ampel (gegenüber Opus A)", "", "| Ergebnis | Opus A | " + " | ".join(tags) + " |",
           "|---|---|" + "---|" * len(tags)]
    all_tags = {t: load(t) for t in tags}
    icon = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}
    for k, r in ref.items():
        vals = [all_tags[t].get(k, {}).get("level") for t in tags]
        if any(v and v != r["level"] for v in vals):
            stufen = lambda s: "/".join(str(s["categories"][c]["rating"]) for c in CATS)  # noqa: E731
            md.append(f"| {k.replace('.score.json', '')} | {icon[r['level']]} {stufen(r)} | "
                      + " | ".join(f"{icon.get(v, '–')} {stufen(all_tags[t][k]) if k in all_tags[t] else ''}" for t, v in zip(tags, vals)) + " |")
    md += ["", "Stufen = edition/tracklist/sources (Prüfmodell); durations bewertet immer der Code."]
    (ROOT / f"eval/judge-ladder-{VERSION}.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
