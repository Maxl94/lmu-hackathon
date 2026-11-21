"""Bewertung: Korrektheit gegen Referenz + Konsistenz über Wiederholungen (…-r1, -r2, …).

  uv run python eval/evaluate.py [--dir output] [--md eval/report.md]

Pro Lauf: Ausgabe richtig? Trackanzahl? Titel-Übereinstimmung (fuzzy ≥ 90)? Dauer ±2 s zur Referenz? Erfundene Dauern?
Pro Fall (bei Wiederholungen): gleiche Ausgabe, gleiche Trackanzahl, gleiche Titel, maximale Dauer-Abweichung.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from tracklist.common import get_json, parse_duration  # noqa: E402
from tracklist.cli.mb import ua  # noqa: E402
from tracklist.cli.discogs import hdr  # noqa: E402

EXPECTED = json.loads((ROOT / "data/expected.json").read_text())


def b(x):
    return "✅" if x is True else "❌" if x is False else "–" if x is None else x


def norm(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"\(.*?\)|\[.*?\]|feat\..*$|ft\..*$", "", s)
    return re.sub(r"[^a-z0-9äöüß]+", " ", s).strip()


_ref_cache: dict[str, list[tuple[str, int | None]]] = {}


def reference(ref: str | None):
    if not ref:
        return None
    if ref in _ref_cache:
        return _ref_cache[ref]
    kind, rid = ref.split(":", 1)
    out = []
    if kind == "musicbrainz":
        r = get_json(f"https://musicbrainz.org/ws/2/release/{rid}", params={"inc": "recordings", "fmt": "json"}, headers=ua())
        for m in r.get("media") or []:
            for t in m.get("tracks") or []:
                ms = t.get("length")
                out.append((t.get("title"), round(ms / 1000) if ms else None))
    else:
        r = get_json(f"https://api.discogs.com/releases/{rid}", headers=hdr())
        for t in r.get("tracklist") or []:
            if t.get("type_") == "track":
                out.append((t.get("title"), parse_duration(t.get("duration"))))
    _ref_cache[ref] = out
    return out


def score_run(cid: str, res: dict, sc: dict | None = None) -> dict:
    base = re.sub(r"-r\d+$", "", cid)
    exp = EXPECTED.get(base, {})
    rel = res.get("release") or {}
    ids = {k: str(v) for k, v in (rel.get("ids") or {}).items()}
    tracks = res.get("tracks") or []
    row = {"id": cid, "case": base, "status": res.get("status"), "n": len(tracks), "conf": res.get("confidence"),
           "ids": ids, "titles": [norm(t["title"]) for t in tracks], "durs": [t.get("duration_s") for t in tracks]}
    # Ausgabe richtig?
    ok = None
    acc = exp.get("accept") or {}
    if acc:
        ok = any(ids.get(k) in v for k, v in acc.items())
    if exp.get("accept_barcode"):
        bc = re.sub(r"\D", "", rel.get("barcode") or "")
        ok = (ok or False) or bc in exp["accept_barcode"]
    if exp.get("accept_format"):
        ok = exp["accept_format"] in (rel.get("format") or "").lower()
    if exp.get("expect_ambiguous"):
        ok = (ok is not False) and (res.get("status") == "ambiguous" or len(res.get("alternatives") or []) >= 1)
    row["level"], row["overall"] = (sc or {}).get("level"), (sc or {}).get("overall")
    row["judge_s"] = ((sc or {}).get("judge") or {}).get("seconds")
    row["trap"] = bool(exp.get("trap"))
    if exp.get("trap"):  # Falle: richtig ist, wenn das Ergebnis NICHT zur Übernahme empfohlen wird
        ok = None if not sc else sc.get("level") != "grün"
    row["edition_ok"] = ok
    row["count_ok"] = None if exp.get("tracks") is None else len(tracks) == exp["tracks"]
    # Titel/Dauer gegen Referenz
    try:
        ref = reference(exp.get("ref"))
    except Exception as e:  # noqa: BLE001 – Referenzquelle gerade nicht erreichbar (MB 502/503)
        ref, row["ref_error"] = None, str(e)[:120]
    if ref:
        pairs = list(zip(tracks, ref))
        def same_title(a, b):  # tolerant: „Pit Bull“ = „Pitbull“, „Nute“ ≈ „Nutte“ (auch Referenzen haben Tippfehler)
            a, b = norm(a), norm(b)
            return fuzz.token_set_ratio(a, b) >= 90 or fuzz.ratio(a.replace(" ", ""), b.replace(" ", "")) >= 88
        row["title_match"] = round(sum(same_title(t["title"], r[0]) for t, r in pairs) / max(len(ref), 1), 3)
        with_ref = [(t.get("duration_s"), r[1]) for t, r in pairs if r[1] is not None]
        row["dur_ok"] = round(sum(d is not None and abs(d - rd) <= 2 for d, rd in with_ref) / len(with_ref), 3) if with_ref else None
        invented = [t for t, r in pairs if r[1] is None and t.get("duration_s") is not None]
        row["invented_durations"] = len(invented) if exp.get("durations_exist") is False else None
        row["dur_missing_flagged"] = sum(1 for t in tracks if t.get("duration_s") is None and "duration_missing" in (t.get("flags") or []))
    return row


def consistency(rows: list[dict]) -> dict:
    def same(key):
        vals = [json.dumps(r[key], sort_keys=True) for r in rows]
        return len(set(vals)) == 1
    ed = [json.dumps({k: v for k, v in r["ids"].items() if k in ("discogs", "musicbrainz")}, sort_keys=True) for r in rows]
    spread = 0
    for i in range(min(len(r["durs"]) for r in rows)):
        vals = [r["durs"][i] for r in rows if r["durs"][i] is not None]
        if len(vals) > 1:
            spread = max(spread, max(vals) - min(vals))
    return {"runs": len(rows), "same_edition": len(set(ed)) == 1, "same_status": same("status"), "same_count": same("n"),
            "same_titles": same("titles"), "max_dur_spread_s": spread}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", default=str(ROOT / "output"))
    p.add_argument("--md", default=str(ROOT / "eval/report.md"))
    a = p.parse_args()
    rows = []
    for f in sorted(Path(a.dir).glob("*.json")):
        if f.name.endswith((".input.json", ".score.json")) or f.stem in ("runs",):
            continue
        try:
            res = json.loads(f.read_text())
        except ValueError:
            continue
        if not isinstance(res, dict) or "status" not in res:
            continue
        scp = f.with_name(f.stem + ".score.json")
        rows.append(score_run(f.stem, res, json.loads(scp.read_text()) if scp.exists() else None))
    by_case = defaultdict(list)
    for r in rows:
        by_case[r["case"]].append(r)
    runs_meta = {}
    runs_file = Path(a.dir) / "runs.jsonl"
    if runs_file.exists():
        for line in runs_file.read_text().splitlines():
            m = json.loads(line)
            runs_meta[m["id"]] = m
    md = ["# Evaluation", "", "## Läufe", "",
          "| Lauf | Status | Ampel | Tracks | Ausgabe richtig¹ | Anzahl richtig | Titel ✓ | Dauer ±2 s | erfundene Dauern | Modus | Recherche | Prüfung | Tools | Kosten |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        m = runs_meta.get(r["id"], {})
        amp = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}.get(r["level"], "–") + (f" {r['overall']}" if r["overall"] else "")
        cost = (m.get("cost") or {}).get("total_usd")
        md.append(f"| {r['id']} | {r['status']} | {amp} | {r['n']} | {b(r['edition_ok'])} | {b(r['count_ok'])} | {b(r.get('title_match'))} | "
                  f"{b(r.get('dur_ok'))} | {b(r.get('invented_durations'))} | {m.get('mode', '–')} | {m.get('wall_s', '–')} s | "
                  f"{r['judge_s'] or m.get('judge_s') or '–'} s | "
                  f"{m.get('tool_calls', '–')} | {'–' if cost is None else f'${cost:.3f}'} |")
    md += ["", "¹ bei Fallen (`trap-…`): ✅ = Ergebnis wird **nicht** zur Übernahme empfohlen (Ampel nicht grün)."]
    md += ["", "## Konsistenz (Wiederholungen)", "",
           "| Fall | Läufe | gleiche Ausgabe | gleicher Status | gleiche Anzahl | gleiche Titel | max. Dauer-Spreizung |", "|---|---|---|---|---|---|---|"]
    for case, rs in by_case.items():
        if len(rs) > 1:
            c = consistency(rs)
            md.append(f"| {case} | {c['runs']} | {b(c['same_edition'])} | {b(c['same_status'])} | {b(c['same_count'])} | {b(c['same_titles'])} | {c['max_dur_spread_s']} s |")
    ed = [r["edition_ok"] for r in rows if r["edition_ok"] is not None]
    cnt = [r["count_ok"] for r in rows if r["count_ok"] is not None]
    tm = [r["title_match"] for r in rows if r.get("title_match") is not None]
    du = [r["dur_ok"] for r in rows if r.get("dur_ok") is not None]
    traps = [r["edition_ok"] for r in rows if r["trap"] and r["edition_ok"] is not None]
    lv = {k: sum(r["level"] == k for r in rows if not r["trap"]) for k in ("grün", "gelb", "rot")}
    summary = {"runs": len(rows), "traps_caught": f"{sum(traps)}/{len(traps)}", "levels_non_trap": lv,
               "edition_acc": round(sum(ed) / len(ed), 3) if ed else None,
               "count_acc": round(sum(cnt) / len(cnt), 3) if cnt else None,
               "title_match": round(sum(tm) / len(tm), 3) if tm else None, "dur_ok": round(sum(du) / len(du), 3) if du else None}
    md[1:1] = ["", f"**{summary['runs']} Läufe** · Ausgabe richtig {summary['edition_acc']} · Trackanzahl richtig {summary['count_acc']} · "
               f"Titel-Übereinstimmung {summary['title_match']} · Dauer ±2 s {summary['dur_ok']} · "
               f"Fallen erkannt {summary['traps_caught']} · Ampel (ohne Fallen) 🟢 {lv['grün']} 🟡 {lv['gelb']} 🔴 {lv['rot']}", ""]
    Path(a.md).write_text("\n".join(md) + "\n")
    (Path(a.md).with_suffix(".json")).write_text(json.dumps({"summary": summary, "runs": rows,
        "consistency": {c: consistency(rs) for c, rs in by_case.items() if len(rs) > 1}}, ensure_ascii=False, indent=1))
    print("\n".join(md))


if __name__ == "__main__":
    main()
