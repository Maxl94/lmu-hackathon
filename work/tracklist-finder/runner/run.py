"""Batch-Runner: eine opencode-Session pro Release, parallel, mit Trace und Validierung.

  uv run python runner/run.py --title "King of Kingz" --artist Bushido --ean 4019593960000 --format CD --id kok-cd2004
  uv run python runner/run.py --csv data/samples.csv [--only kok-cd2004,ram-cd] [--parallel 3] [--repeat 2]
  Optionen: -m/--model kisski/glm-5.3 · --agent tracklist · --timeout 900

Ablauf pro Fall: Schnellweg (eindeutiger Barcode, MB = Discogs → ohne Agent) · sonst opencode-Agent ·
danach Bewertung (Regelkatalog: Code + Prüfmodell) und Kosten.
  --no-fast  immer Agent · --no-judge  keine Bewertung

Ergebnisse: output/<id>.json (Ergebnis), output/<id>.score.json (Bewertung), output/<id>.trace.jsonl (roh),
            output/<id>.trace.md (lesbar), output/<id>.usage.jsonl (bezahlte Modell-Aufrufe),
            output/runs.jsonl (eine Zeile pro Lauf: Status, Ampel, Tracks, Zeit, Tokens, Kosten, Validierung)
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "runner"))

import agenttrace as tracemod  # noqa: E402
from tracklist import credits, fasttrack, prompts, scoring  # noqa: E402
from tracklist.cli.validate import check  # noqa: E402
from tracklist.usage import cost_usd, read_usage  # noqa: E402

OUT = ROOT / "output"
# Auftrag pro Fall: prompts/task.md ($input, $out)


COLUMNS = {  # Spaltennamen beliebiger Lieferungen → unser Eingabeformat
    "id": ("id", "case_id", "fall", "nr", "lfd_nr"),
    "title": ("title", "album_title", "titel", "album", "release", "release_title", "trägertitel", "traegertitel", "tontraeger"),
    "artist": ("artist", "album_artist", "interpret", "künstler", "kuenstler", "release_artist"),
    "ean": ("ean", "barcode", "upc", "gtin", "ean_code", "ean13"),
    "format": ("format", "trägerart", "traegerart", "medium", "carrier", "tonträger"),
    "notes": ("notes", "notiz", "bemerkung", "hinweis", "comment"),
}


def clean_ean(raw: str) -> tuple[str, str]:
    """→ (ziffern, hinweis). Excel-Schäden: 4.01959E+12 (Ziffern verloren), 4019593960000.0, „0“ als Platzhalter."""
    raw = (raw or "").strip()
    if re.search(r"\d[.,]\d+[eE]\+\d+", raw):
        return "", f"EAN unreadable (Excel scientific notation: {raw})"
    raw = re.sub(r"[.,]0+$", "", raw)
    d = re.sub(r"\D", "", raw)
    return ("" if set(d) <= {"0"} else d), ""


def load_cases(path: str) -> list[dict]:
    """Toleranter Import: Kodierung (UTF-8/Windows-1252), Trennzeichen (, ; Tab), Spaltennamen-Synonyme;
    unbekannte Spalten wandern als „Spalte: Wert“ in notes (der Agent liest sie)."""
    raw = Path(path).read_bytes()
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("cp1252")
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    cases = []
    for i, r in enumerate(csv.DictReader(io.StringIO(text), dialect=dialect), 1):
        c, extra = {}, []
        for k, v in r.items():
            key, v = (k or "").strip().lower().replace(" ", "_"), (v or "").strip()
            target = next((t for t, syn in COLUMNS.items() if key in syn), None)
            if target:
                c[target] = v
            elif v:
                extra.append(f"{k.strip()}: {v}")
        ean, hint = clean_ean(c.get("ean", ""))
        notes = "; ".join(x for x in [c.get("notes", ""), hint, *extra] if x)
        cid = c.get("id") or f"{i:02d}-" + slug(f"{c.get('artist', '')} {c.get('title', '')}")[:40]
        cases.append({"id": cid, "title": c.get("title", ""), "artist": c.get("artist", ""), "ean": ean,
                      "format": c.get("format", ""), "notes": notes})
    return cases


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


def preflight(model: str) -> None:
    """Vorab-Check: antwortet das SAIA-Modell gerade schnell genug? (GLM-5.3 brauchte am 20.11. ~100 s pro Anfrage.)"""
    if not model.startswith("kisski/"):
        return
    from tracklist.common import env
    key, base = env("SAIA_API_KEY"), env("SAIA_BASE_URL") or "https://chat-ai.academiccloud.de/v1"
    if not key:
        return
    import httpx
    t0 = time.time()
    try:
        r = httpx.post(f"{base}/chat/completions", headers={"Authorization": f"Bearer {key}"}, timeout=60,
                       json={"model": model.split("/", 1)[1], "messages": [{"role": "user", "content": "Say OK."}], "max_tokens": 5})
        dt = time.time() - t0
        left = r.headers.get("x-ratelimit-remaining-requests-hour")
        msg = f"Vorab-Check {model}: HTTP {r.status_code} in {dt:.1f}s · SAIA übrig diese Stunde: {left}"
        if r.status_code != 200 or dt > 15:
            msg += "  ⚠️ LANGSAM/FEHLER – anderes Modell wählen (-m kisski/qwen3.5-397b-a17b oder anthropic/claude-sonnet-5-5)"
        print(msg, flush=True)
    except httpx.HTTPError as e:
        print(f"Vorab-Check {model}: ⚠️ keine Antwort in 60 s ({type(e).__name__}) – anderes Modell wählen", flush=True)


def ev(cid: str, event: str, **kw) -> None:
    """Live-Ereignis (Phase) für die Oberfläche: output/<id>.events.jsonl."""
    with open(OUT / f"{cid}.events.jsonl", "a") as f:
        f.write(json.dumps({"ts": round(time.time(), 2), "event": event, **kw}, ensure_ascii=False) + "\n")


def run_agent(case: dict, a, out_json: Path, trace: Path, usage_log: Path) -> tuple[object, dict]:
    """Agent sieht nur eine neutrale Fall-ID und einen neutralen Pfad – die Fall-ID (z. B. „spatzen-…“, „trap-…“)
    darf keine Hinweise auf die Lösung geben. Danach wird input.id zurückgesetzt und das Ergebnis verschoben."""
    cid = case["id"]
    opaque = "fall-" + hashlib.sha1(f"{cid}{time.time()}".encode()).hexdigest()[:8]
    work = OUT / "work"
    work.mkdir(exist_ok=True)
    work_json = work / f"{opaque}.json"
    inp = {k: v for k, v in case.items() if v and k in ("title", "artist", "ean", "format", "notes")}
    inp = {"id": opaque, **inp}
    prompt = prompts.render("task.md", input=json.dumps(inp, ensure_ascii=False), out=str(work_json.relative_to(ROOT)))
    cmd = ["opencode", "run", "--standalone", "--format", "json", "--auto", "--archived",
           "--title", f"tl-{opaque}", "--agent", a.agent, "-m", a.model, prompt]
    env = dict(os.environ, PATH=f"{ROOT / 'bin'}:{os.environ.get('PATH', '')}", TL_USAGE_LOG=str(usage_log),
               TL_LIVE_LOG=str(OUT / f"{cid}.events.jsonl"))
    with open(trace, "w") as fo, open(OUT / f"{cid}.stderr.log", "w") as fe:
        try:
            rc = subprocess.run(cmd, cwd=ROOT, env=env, stdout=fo, stderr=fe, timeout=a.timeout).returncode
        except subprocess.TimeoutExpired:
            rc = "timeout"
    if work_json.exists():
        raw = work_json.read_text()
        try:
            data = json.loads(raw)
            if isinstance(data.get("input"), dict):
                data["input"]["id"] = cid
            raw = json.dumps(data, ensure_ascii=False, indent=1)
        except ValueError:
            pass
        out_json.write_text(raw)
        work_json.unlink()
    events = tracemod.load(trace)
    st = tracemod.stats(events)
    if not st["cost_usd"]:
        # opencode kennt für eigene Anbieter (gema/…) keine Preise → aus Tokens × Listenpreis rechnen
        c = cost_usd(a.model, {"input_tokens": st["tokens_in"], "output_tokens": st["tokens_out"],
                               "cache_read_input_tokens": st["tokens_cache_read"]})
        if c:
            st["cost_usd"], st["cost_estimated"] = c, True
    return rc, {"events": events, **st}


def run_case(case: dict, a) -> dict:
    cid = case["id"]
    out_json, trace = OUT / f"{cid}.json", OUT / f"{cid}.trace.jsonl"
    usage_log, score_path = OUT / f"{cid}.usage.jsonl", OUT / f"{cid}.score.json"
    for p in (out_json, trace, usage_log, score_path, OUT / f"{cid}.events.jsonl"):
        p.unlink(missing_ok=True)
    t0 = time.time()
    ev(cid, "run_start", input={k: v for k, v in case.items() if v and k != "id"}, model=a.model,
       fast=not a.no_fast, judge=not a.no_judge, judge_model=os.environ.get("JUDGE_MODEL") or scoring.JUDGE_MODEL_DEFAULT)
    mode, fast_log = "agent", []
    if not a.no_fast:
        ev(cid, "phase_start", phase="fast", actor="Schnellweg (Code: MusicBrainz + Discogs)")
        try:
            ok, fast_log = fasttrack.try_fast(case, out_json, emit=lambda m: ev(cid, "fast_step", msg=m))
        except Exception as e:  # noqa: BLE001 – Schnellweg darf nie den Lauf kippen
            ok, fast_log = False, [f"→ kein Schnellweg: Fehler {type(e).__name__}: {str(e)[:160]}"]
        mode = "fast" if ok else "agent"
        ev(cid, "phase_end", phase="fast", ok=ok, msg=fast_log[-1] if fast_log else "")
    if mode == "fast":
        rc, st = 0, {"steps": 0, "tool_calls": 0, "tl_calls": [], "tokens_in": 0, "tokens_out": 0,
                     "final": "FERTIG (Schnellweg)", "cost_usd": 0.0}
        (OUT / f"{cid}.trace.md").write_text(f"# Schnellweg: {cid}\n\nOhne Agent, deterministisch.\n\n```\n"
                                             + "\n".join(fast_log) + "\n```\n")
    else:
        ev(cid, "phase_start", phase="agent", actor=f"Recherche-Agent ({a.model})")
        rc, st = run_agent(case, a, out_json, trace, usage_log)
        ev(cid, "phase_end", phase="agent", ok=out_json.exists(), rc=str(rc), tool_calls=st["tool_calls"], steps=st["steps"])
        txt = trace.read_text(errors="replace") if trace.exists() else ""
        if not out_json.exists() and a.fallback_model and ("spending cap" in txt or "provider.rate-limit" in txt):
            # Gemini-Limit (geteiltes GEMA-Projekt) → einmal mit dem Rückfall-Modell wiederholen
            ev(cid, "phase_start", phase="agent", actor=f"Recherche-Agent – Rückfall ({a.fallback_model}, Gemini-Limit)")
            a_fb = argparse.Namespace(**{**vars(a), "model": a.fallback_model})
            rc, st = run_agent(case, a_fb, out_json, trace, usage_log)
            st["fallback_from"] = a.model
            ev(cid, "phase_end", phase="agent", ok=out_json.exists(), rc=str(rc), tool_calls=st["tool_calls"], steps=st["steps"])
        e1, _, r1 = check(str(out_json))
        if a.escalate_model and (e1 or r1 is None or r1.status == "not_found"):
            # Eskalation: nur wenn das günstige Modell nichts Brauchbares liefert – Kosten beider Versuche zählen
            why = "kein gültiges Ergebnis" if (e1 or r1 is None) else "nicht gefunden"
            first = {k: st.get(k) for k in ("cost_usd", "tool_calls", "steps", "tokens_in", "tokens_out")}
            if trace.exists():
                trace.rename(trace.with_suffix(".attempt1.jsonl"))
            if out_json.exists():
                out_json.rename(out_json.with_suffix(".attempt1.json.txt"))
            ev(cid, "phase_start", phase="agent", actor=f"Recherche-Agent – Eskalation ({a.escalate_model}, {why})")
            a_es = argparse.Namespace(**{**vars(a), "model": a.escalate_model})
            rc, st = run_agent(case, a_es, out_json, trace, usage_log)
            for k, v in first.items():
                st[k] = (st.get(k) or 0) + (v or 0)
            st["escalated_from"], st["escalation_reason"] = a.model, why
            ev(cid, "phase_end", phase="agent", ok=out_json.exists(), rc=str(rc), tool_calls=st["tool_calls"], steps=st["steps"])
        md = tracemod.render(st.pop("events"), cid)
        if fast_log:
            md = md.replace("\n", "\n\n> Schnellweg geprüft: " + fast_log[-1].lstrip("→ ") + "\n", 1)
        (OUT / f"{cid}.trace.md").write_text(md)
    wall = round(time.time() - t0, 1)
    errors, warns, res = check(str(out_json))
    if res and not errors and res.tracks:
        ev(cid, "phase_start", phase="credits", actor="Credits + ISRC (Code: MusicBrainz + Discogs)")
        try:
            data = json.loads(out_json.read_text())
            cinfo = credits.enrich(data)
            out_json.write_text(json.dumps(data, ensure_ascii=False, indent=1))
            errors, warns, res = check(str(out_json))
        except Exception as e:  # noqa: BLE001 – Anreicherung darf den Lauf nie kippen
            cinfo = {"notes": [f"{type(e).__name__}: {str(e)[:120]}"]}
        ev(cid, "phase_end", phase="credits", ok=True, msg=f"credits {cinfo.get('credits_tracks', 0)} tracks, ISRC {cinfo.get('isrc_tracks', 0)}")
    sc, score_err, t1 = None, None, time.time()
    if res and not errors and not a.no_judge:
        ev(cid, "phase_start", phase="judge", actor=f"Prüfmodell ({os.environ.get('JUDGE_MODEL') or scoring.JUDGE_MODEL_DEFAULT})")
        try:
            sc = scoring.score_file(out_json, trace if mode == "agent" else None, mode=mode,
                                    evidence="\n".join(fast_log) if mode == "fast" else None)
        except Exception as e:  # noqa: BLE001
            score_err = f"{type(e).__name__}: {str(e)[:200]}"
        ev(cid, "phase_end", phase="judge", ok=sc is not None, level=(sc or {}).get("level"),
           overall=(sc or {}).get("overall"), error=score_err)
    judge_s = round(time.time() - t1, 1)
    usage = read_usage(usage_log)
    vision = [u for u in usage if u.get("tool") == "tl-vision"]
    cost = {"agent_usd": st.get("cost_usd") or 0.0, "vision_usd": round(sum(u.get("cost_usd") or 0 for u in vision), 4),
            "judge_usd": ((sc or {}).get("judge") or {}).get("cost_usd") or 0.0, "vision_calls": len(vision),
            "saia_requests": st["steps"] if a.model.startswith("kisski/") and mode == "agent" else 0}
    cost["total_usd"] = round(cost["agent_usd"] + cost["vision_usd"] + cost["judge_usd"], 4)
    row = {
        "id": cid, "model": ((a.escalate_model if st.get("escalated_from") else a.fallback_model if st.get("fallback_from")
                              else a.model) if mode == "agent" else "-"), "mode": mode,
        "fallback_from": st.get("fallback_from"), "escalated_from": st.get("escalated_from"),
        "escalation_reason": st.get("escalation_reason"), "rc": rc, "wall_s": wall, "judge_s": judge_s,
        "valid": not errors, "status": res.status if res else None, "tracks": len(res.tracks) if res else 0,
        "with_duration": sum(1 for t in res.tracks if t.duration_s is not None) if res else 0,
        "confidence": res.confidence if res else None,
        "level": sc["level"] if sc else None, "overall": sc["overall"] if sc else None, "score_error": score_err,
        "fast_reason": fast_log[-1] if fast_log and mode == "agent" else None,
        "release": (f"{res.release.title} | {res.release.format} {res.release.country} {res.release.year} | "
                    f"{res.release.edition or ''}") if res and res.release else None,
        "steps": st["steps"], "tool_calls": st["tool_calls"], "tokens_in": st["tokens_in"], "tokens_out": st["tokens_out"],
        "tl_calls": st["tl_calls"], "cost": cost, "errors": errors[:5], "warns": warns, "final": st["final"][:200],
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    with open(OUT / "runs.jsonl", "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    ev(cid, "run_end", valid=row["valid"], status=row["status"], level=row["level"], overall=row["overall"],
       tracks=row["tracks"], wall_s=wall, judge_s=judge_s, cost_usd=cost["total_usd"], mode=mode, errors=errors[:3])
    flag = "OK " if row["valid"] else "ERR"
    lvl = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}.get(row["level"], "⚪")
    print(f"[{flag}] {cid}: {lvl} {sc['label'] if sc else (score_err or 'keine Bewertung')} ({row['overall']}) · {mode} · "
          f"{row['status']} · {row['tracks']} Tracks ({row['with_duration']} mit Dauer) · {wall}s + Prüfung {judge_s}s · "
          f"{row['tool_calls']} Tools · ${cost['total_usd']:.3f} · {row['release']}"
          + ("" if row["valid"] else f"\n      Fehler: {errors[:3]}"), flush=True)
    return row


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--csv")
    p.add_argument("--only")
    p.add_argument("--id")
    p.add_argument("--title")
    p.add_argument("--artist")
    p.add_argument("--ean")
    p.add_argument("--format")
    p.add_argument("--notes")
    p.add_argument("-m", "--model", default=os.environ.get("TL_MODEL", "openrouter/deepseek/deepseek-v4.1-flash-1017"))
    p.add_argument("--agent", default="tracklist")
    p.add_argument("--parallel", type=int, default=1)
    p.add_argument("--repeat", type=int, default=1)
    p.add_argument("--timeout", type=int, default=900)
    p.add_argument("--no-fast", action="store_true", help="Schnellweg aus: immer den Agenten nutzen")
    p.add_argument("--no-judge", action="store_true", help="keine Bewertung durch das Prüfmodell")
    p.add_argument("--out-dir", help="Ausgabeordner (Standard output/), z. B. für Modellvergleiche")
    p.add_argument("--fallback-model", default="",
                   help="Agent-Modell, falls das Hauptmodell am Gemini-Limit scheitert (leer = kein Rückfall)")
    p.add_argument("--escalate-model", default="gema/gemini-4-hydrogen",
                   help="stärkeres (teureres) Agent-Modell, nur wenn das günstige kein gültiges Ergebnis oder „not_found“ "
                        "liefert (leer = keine Eskalation)")
    a = p.parse_args()
    global OUT
    if a.out_dir:
        OUT = Path(a.out_dir).resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    if a.csv:
        cases = load_cases(a.csv)
        if a.only:
            keep = set(a.only.split(","))
            cases = [c for c in cases if c["id"] in keep]
    else:
        if not a.title and not a.ean:
            p.error("--csv oder --title/--ean angeben")
        cases = [{"id": a.id or slug(f"{a.artist or ''} {a.title or a.ean} {a.format or ''}"), "title": a.title,
                  "artist": a.artist, "ean": a.ean, "format": a.format, "notes": a.notes}]
    if a.repeat > 1:
        cases = [dict(c, id=f"{c['id']}-r{i}") for c in cases for i in range(1, a.repeat + 1)]
    print(f"{len(cases)} Läufe · Modell {a.model} · parallel {a.parallel}", flush=True)
    preflight(a.model)
    with ThreadPoolExecutor(max_workers=a.parallel) as ex:
        rows = list(ex.map(lambda c: run_case(c, a), cases))
    ok = sum(r["valid"] for r in rows)
    lv = {k: sum(r["level"] == k for r in rows) for k in ("grün", "gelb", "rot")}
    print(f"\n{ok}/{len(rows)} gültig · Ø {sum(r['wall_s'] for r in rows) / len(rows):.0f}s pro Lauf · "
          f"🟢 {lv['grün']} 🟡 {lv['gelb']} 🔴 {lv['rot']} · Kosten ${sum(r['cost']['total_usd'] for r in rows):.3f}")


if __name__ == "__main__":
    main()
