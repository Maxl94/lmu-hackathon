"""Batch-Bericht „Welche Künstler sind auf dem Tonträger?“ für einen Lauf über eine Eingabedatei.

  uv run python eval/artists_report.py data/gema-sample.csv [--dir output]
  → eval/<name>-artists.md (Übersicht) + eval/<name>-artists.csv (eine Zeile pro Tonträger × Künstler)
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "runner"))
spec = importlib.util.spec_from_file_location("run", ROOT / "runner/run.py")
run = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run)

ICON = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}
ROLE = {"main": "", "featured": " (feat.)", "remixer": " (Remix)", "other": " (sonst.)"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv")
    p.add_argument("--dir", default=str(ROOT / "output"))
    a = p.parse_args()
    out_dir, name = Path(a.dir), Path(a.csv).stem
    runs = {}
    if (out_dir / "runs.jsonl").exists():
        for line in (out_dir / "runs.jsonl").read_text().splitlines():
            r = json.loads(line)
            runs[r["id"]] = r
    cases = run.load_cases(a.csv)
    md = [f"# Künstler pro Tonträger – {name}", "",
          "| # | Eingabe (Interpret – Titel, EAN) | Status | Ampel | gefundene Ausgabe | Tracks | Künstler | Modus | Zeit | Kosten |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    rows, stats = [], {"found": 0, "ambiguous": 0, "not_found": 0, "missing": 0}
    for c in cases:
        f, sp = out_dir / f"{c['id']}.json", out_dir / f"{c['id']}.score.json"
        res = json.loads(f.read_text()) if f.exists() else None
        sc = json.loads(sp.read_text()) if sp.exists() else {}
        m = runs.get(c["id"], {})
        if not res:
            stats["missing"] += 1
            md.append(f"| {c['id'][:2]} | {c['artist']} – {c['title']} {c['ean']} | ❌ kein Ergebnis | – | – | – | – | {m.get('mode', '–')} | {m.get('wall_s', '–')} s | – |")
            continue
        stats[res["status"]] = stats.get(res["status"], 0) + 1
        rel = res.get("release") or {}
        arts = res.get("artists") or []
        names = ", ".join(x["name"] + ROLE.get(x.get("role"), "") for x in arts[:12]) + (f" … (+{len(arts) - 12})" if len(arts) > 12 else "")
        found = f"{rel.get('artist') or ''} – {rel.get('title') or ''} ({rel.get('format') or '?'}, {rel.get('year') or '?'}, {rel.get('country') or '?'})" if rel else "–"
        cost = (m.get("cost") or {}).get("total_usd")
        md.append(f"| {c['id'][:2]} | {c['artist']} – {c['title']} {c['ean']} | {res['status']} | {ICON.get(sc.get('level'), '–')} {sc.get('overall') or ''} | "
                  f"{found} | {len(res.get('tracks') or [])} | {len(arts)}: {names} | {m.get('mode', '–')} | {m.get('wall_s', '–')} s | "
                  f"{'–' if cost is None else f'${cost:.3f}'} |")
        for x in arts:
            rows.append([c["id"], c["ean"], c["artist"], c["title"], res["status"], sc.get("level", ""), rel.get("title", ""),
                         rel.get("format", ""), (rel.get("ids") or {}).get("musicbrainz", ""), (rel.get("ids") or {}).get("discogs", ""),
                         x["name"], x.get("role", ""), " ".join(x.get("tracks") or []), " ".join(x.get("sources") or [])])
    total_cost = sum((runs.get(c["id"], {}).get("cost") or {}).get("total_usd") or 0 for c in cases)
    md[1:1] = ["", f"**{len(cases)} Tonträger** · gefunden {stats['found']} · mehrdeutig {stats['ambiguous']} · nicht gefunden "
               f"{stats['not_found']} · ohne Ergebnis {stats['missing']} · {len(rows)} Künstler-Zeilen · Kosten gesamt ${total_cost:.2f}", ""]
    (ROOT / f"eval/{name}-artists.md").write_text("\n".join(md) + "\n")
    with open(ROOT / f"eval/{name}-artists.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["case", "ean", "input_artist", "input_title", "status", "ampel", "release_title", "format", "musicbrainz", "discogs",
                    "artist", "role", "tracks", "sources"])
        w.writerows(rows)
    print("\n".join(md))


if __name__ == "__main__":
    main()
