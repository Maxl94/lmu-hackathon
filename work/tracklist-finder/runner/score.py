"""Vorhandene Ergebnisse (neu) bewerten: Regelkatalog + Prüfmodell → <id>.score.json daneben.

  uv run python runner/score.py examples/kok-cd2004.json output/lohnde-mc.json
  uv run python runner/score.py --dir examples [--parallel 4]
  uv run python runner/score.py --dir examples --judge-model claude-haiku-5-5 --out-dir eval/judge-ladder/haiku   (Vergleich)
Belege: <id>.trace.jsonl, sonst <id>.trace.md. Prüfmodell: JUDGE_MODEL (Standard claude-opus-5-5).
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from tracklist import scoring  # noqa: E402


def is_result(f: Path) -> bool:
    return f.suffix == ".json" and not f.name.endswith((".score.json", ".input.json")) and f.stem not in ("runs", "report")


OUT_DIR: Path | None = None


def one(f: Path) -> str:
    res = json.loads(f.read_text())
    trace = next((p for p in (f.with_name(f.stem + ".trace.jsonl"), f.with_name(f.stem + ".trace.md")) if p.exists()), None)
    mode = "fast" if any(x in (res.get("reasoning") or "") for x in ("Schnellweg", "Fast path")) else "agent"
    try:
        sc = scoring.score_file(f, trace, mode=mode, out_path=(OUT_DIR / f"{f.parent.name}__{f.stem}.score.json") if OUT_DIR else None)
    except Exception as e:  # noqa: BLE001
        return f"⚪ {f}: Fehler {type(e).__name__}: {str(e)[:200]}"
    c = sc["categories"]
    lvl = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}[sc["level"]]
    return (f"{lvl} {f.stem}: {sc['label']} ({sc['overall']}) · "
            + " · ".join(f"{k} {c[k]['rating']}" for k in c)
            + f" · {(sc['judge'] or {}).get('seconds') or 0:.0f} s · ${(sc['judge'] or {}).get('cost_usd') or 0:.3f}"
            + (f" · gates: {'; '.join(sc['gates'])}" if sc["gates"] else ""))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("files", nargs="*")
    p.add_argument("--dir")
    p.add_argument("--parallel", type=int, default=4)
    p.add_argument("--judge-model", help="Prüfmodell für diesen Lauf (sonst JUDGE_MODEL bzw. claude-haiku-5-5)")
    p.add_argument("--out-dir", help="Bewertungen hierhin statt neben das Ergebnis (für Modellvergleiche)")
    p.add_argument("--reaggregate", action="store_true",
                   help="kein Modellaufruf: vorhandene Stufen behalten, Ampel/Bonus mit aktuellen Regeln neu rechnen")
    a = p.parse_args()
    global OUT_DIR
    if a.judge_model:
        import os
        os.environ["JUDGE_MODEL"] = a.judge_model
    if a.out_dir:
        OUT_DIR = Path(a.out_dir)
        OUT_DIR.mkdir(parents=True, exist_ok=True)
    files = [Path(x) for x in a.files] + (sorted(f for f in Path(a.dir).glob("*.json") if is_result(f)) if a.dir else [])
    if a.reaggregate:
        for f in files:
            sp = f.with_name(f.stem + ".score.json")
            if not sp.exists():
                continue
            sc = scoring.upgrade_score(json.loads(sp.read_text()))
            res = json.loads(f.read_text())
            from tracklist.cli.validate import check
            errors, warns, _ = check(str(f))
            fct = scoring.facts(res, (errors, warns))
            d, dtxt = scoring.duration_rating(fct)
            sc["categories"]["durations"].update(rating=d, check=dtxt, summary=dtxt)
            sc.update(scoring.aggregate(sc["categories"], fct), facts=fct, weights=scoring.WEIGHTS)
            sc["bonus"]["credits"] = {"tracks": sum(1 for t in res.get("tracks") or [] if t.get("credits")),
                                      "of": len(res.get("tracks") or [])}
            sp.write_text(json.dumps(sc, ensure_ascii=False, indent=1))
            print(f"{sc['level']:5s} {f.stem}: {sc['label']} ({sc['overall']}) · Dauern {sc['bonus']['durations']} · "
                  f"Credits {sc['bonus']['credits']['tracks']}/{sc['bonus']['credits']['of']}")
        return
    with ThreadPoolExecutor(max_workers=a.parallel) as ex:
        for line in ex.map(one, files):
            print(line, flush=True)


if __name__ == "__main__":
    main()
