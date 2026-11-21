"""Agent-Modell-Leiter: Qualität vs. Kosten pro Modell (output/ladder/<modell>/).

  uv run python eval/ladder_report.py     → eval/ladder.md

Qualität: richtige Ausgabe, Trackanzahl, Titel, Dauer ± 2 s (gegen data/expected.json), Ampel des Prüfmodells (Opus),
Fallen erkannt. Kosten: Listenpreise (OpenRouter/Anthropic, Stand 20.11.2026) × Tokens aus dem Trace
(inkl. Cache-Lesezugriffen) – auch für SAIA-Läufe, damit man sieht, was das Modell im Betrieb kosten würde.
"""
from __future__ import annotations

import json
import statistics as stt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runner"))
sys.path.insert(0, str(ROOT / "eval"))
sys.path.insert(0, str(ROOT / "src"))
import agenttrace  # noqa: E402
import evaluate  # noqa: E402

# USD pro Million Tokens: (input, output, cache_read) – OpenRouter-Modellliste bzw. Anthropic, 20.11.2026
PRICES = {
    "kisski/qwen3.5-397b-a17b": (0.45, 3.00, 0.45, "Qwen3.5-397B (SAIA; Listenpreis OpenRouter)"),
    "openrouter/deepseek/deepseek-v4.1-flash-1017": (0.15, 0.60, 0.15, "DeepSeek v4.1 Flash"),
    "openrouter/openai/gpt-oss-120b": (0.09, 0.36, 0.09, "gpt-oss-120b"),
    "openrouter/z-ai/glm-5.3-flash": (0.04, 0.078, 0.04, "GLM-5.3 Flash"),
    "anthropic/claude-haiku-5-5": (0.10, 0.50, 0.01, "Claude Haiku 5.5"),
    "anthropic/claude-sonnet-5-5": (2.00, 10.00, 0.10, "Claude Sonnet 5.5"),
    "kisski/glm-5.3": (0.07, 1.40, 0.07, "GLM-5.3 (SAIA)"),
    "kisski/mistral-large-4-1t-a52b": (0.70, 2.10, 0.70, "Mistral Large 4 (SAIA)"),
}


def tokens(trace: Path) -> dict:
    t = {"in": 0, "out": 0, "cache_read": 0, "cache_write": 0, "cost_reported": 0.0}
    for e in agenttrace.load(trace) if trace.exists() else []:
        if e.get("type") == "step_finish":
            p = e.get("part") or {}
            tk = p.get("tokens") or {}
            t["in"] += tk.get("input") or 0
            t["out"] += (tk.get("output") or 0) + (tk.get("reasoning") or 0)
            t["cache_read"] += (tk.get("cache") or {}).get("read") or 0
            t["cache_write"] += (tk.get("cache") or {}).get("write") or 0
            t["cost_reported"] += p.get("cost") or 0
    return t


def main():
    md = ["# Agent-Modell-Leiter", "", "Gleiche Fälle (`data/ladder.csv`, ohne Schnellweg), gleiches Prüfmodell (Opus 5.5).", "",
          "| Modell | Preis in/out | gültig | Ausgabe ✓ | Anzahl ✓ | Titel | Dauer ±2 s | Fallen rot | Ampel | Ø Zeit | Ø Tools | Ø Agent gemeldet | Ø Agent Listenpreis* | Ø Prüfung |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    detail = ["", "## Einzelfälle", "", "| Modell | Fall | Status | Ampel | Tracks | Ausgabe ✓ | Zeit | Tools | Tokens in (+Cache) / out | Agent-Kosten* |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    icon = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}
    for d in sorted((ROOT / "output/ladder").glob("*")):
        if not d.is_dir():
            continue
        runs = {}
        if (d / "runs.jsonl").exists():
            for line in (d / "runs.jsonl").read_text().splitlines():
                r = json.loads(line)
                runs[r["id"]] = r
        if not runs:
            continue
        model = next(iter(runs.values()))["model"]
        pin, pout, pcache, name = PRICES.get(model, (0, 0, 0, model))
        ed, cnt, tm, du, traps, lv, walls, tools, costs, judge, reported = [], [], [], [], [], [], [], [], [], [], []
        for cid, r in sorted(runs.items()):
            res_p, sc_p = d / f"{cid}.json", d / f"{cid}.score.json"
            res = json.loads(res_p.read_text()) if res_p.exists() else None
            sc = json.loads(sc_p.read_text()) if sc_p.exists() else None
            row = evaluate.score_run(cid, res, sc) if res else {}
            tk = tokens(d / f"{cid}.trace.jsonl")
            cost = (tk["in"] * pin + tk["cache_read"] * pcache + tk["out"] * pout) / 1e6
            walls.append(r["wall_s"])
            tools.append(r["tool_calls"])
            costs.append(cost)
            reported.append(tk["cost_reported"])
            if sc and sc.get("judge"):
                judge.append(sc["judge"].get("cost_usd") or 0)
            if row.get("trap"):
                traps.append(bool(sc) and sc["level"] != "grün")
            else:
                if row.get("edition_ok") is not None:
                    ed.append(row["edition_ok"])
                else:
                    ed.append(False)
                if row.get("count_ok") is not None:
                    cnt.append(row["count_ok"])
                if row.get("title_match") is not None:
                    tm.append(row["title_match"])
                if row.get("dur_ok") is not None:
                    du.append(row["dur_ok"])
                lv.append(sc["level"] if sc else None)
            detail.append(f"| {name} | {cid} | {r.get('status') or '❌ ' + str(r.get('rc'))} | {icon.get((sc or {}).get('level'), '–')} "
                          f"{(sc or {}).get('overall') or ''} | {r['tracks']} | {evaluate.b(row.get('edition_ok'))} | {r['wall_s']:.0f} s | "
                          f"{r['tool_calls']} | {tk['in']:,} (+{tk['cache_read']:,}) / {tk['out']:,} | ${cost:.3f} |")
        pct = lambda x: f"{sum(x) / len(x):.0%}" if x else "–"  # noqa: E731
        avg = lambda x: stt.mean(x) if x else 0  # noqa: E731
        amp = " ".join(f"{icon[k]}{sum(1 for x in lv if x == k)}" for k in ("grün", "gelb", "rot")) + (
            f" ⚪{sum(1 for x in lv if x is None)}" if any(x is None for x in lv) else "")
        md.append(f"| {name} | ${pin} / ${pout} | {sum(1 for r in runs.values() if r['valid'])}/{len(runs)} | {pct(ed)} | {pct(cnt)} | "
                  f"{avg(tm):.0%} | {avg(du):.0%} | {sum(traps)}/{len(traps)} | {amp} | {avg(walls):.0f} s | {avg(tools):.0f} | "
                  f"${avg(reported):.3f} | ${avg(costs):.3f} | ${avg(judge):.3f} |")
    md += ["", "\\* Listenpreis × Tokens aus dem Trace (Cache-Lesezugriffe mit Cache-Preis; bei OpenRouter-Modellen grob, dort zählt „gemeldet“ = von opencode berechnet). SAIA selbst ist kostenlos (Kontingent)."]
    out = "\n".join(md + detail) + "\n"
    (ROOT / "eval/ladder.md").write_text(out)
    print(out)


if __name__ == "__main__":
    main()
