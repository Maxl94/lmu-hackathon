"""Tracklist-Finder – Demo-Oberfläche.

  uv run streamlit run ui/app.py

Neue Recherche (startet den opencode-Agenten, zeigt Schritte live) · Ergebnisse ansehen (Ampel, Quellen, Konflikte,
Alternativen, Agent-Trace) · Evaluation (eval/report.md).
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "ui"))
import costs as costmod  # noqa: E402
import overview as ovmod  # noqa: E402
import live as livemod  # noqa: E402
from tracklist.scoring import RUBRIC, WEIGHTS, upgrade_score  # noqa: E402

# TL_OUT_DIR=results shows the committed final run without re-running anything.
OUT = Path(os.environ.get("TL_OUT_DIR") or "output")
OUT = OUT if OUT.is_absolute() else ROOT / OUT
EXAMPLES = ROOT / "examples"
MODELS = ["openrouter/deepseek/deepseek-v4.1-flash-1017", "gema/gemini-4-hydrogen", "gema/gemini-4-argon", "gema/gemini-3.8-flash", "kisski/qwen3.5-397b-a17b", "kisski/glm-5.3", "kisski/deepseek-v4.1-flash-1017", "kisski/mistral-large-4-1t-a52b",
          "anthropic/claude-opus-5-5", "anthropic/claude-sonnet-5-5"]

st.set_page_config(page_title="Tracklist-Finder", page_icon="💿", layout="wide")


ROLE_DE = {"composer": "Musik", "lyricist": "Text", "writer": "Autor", "arranger": "Arr.", "producer": "Prod.", "other": "sonst."}


def mmss(s):
    if s is None:
        return "–"
    s = int(s)
    return f"{s // 60}:{s % 60:02d}" if s < 3600 else f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"


def ampel(t: dict) -> str:
    flags = set(t.get("flags") or [])
    if t.get("duration_s") is None or "duration_missing" in flags:
        return "🔴"
    if flags & {"duration_conflict", "title_conflict"} or len(set(t.get("duration_sources") or [])) < 2:
        return "🟡"
    return "🟢"


def short(src: str) -> str:
    return re.sub(r"^(\w+):(release/|album/)?", r"\1:", src)[:38]


def load_trace(path: Path) -> list[dict]:
    if not path.exists():
        return []
    ev = []
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("{"):
            try:
                ev.append(json.loads(line))
            except ValueError:
                pass
    return ev


def tool_steps(events: list[dict]) -> list[tuple[str, str, str]]:
    steps = []
    for e in events:
        if e.get("type") == "tool_use":
            st_ = (e.get("part") or {}).get("state") or {}
            inp = st_.get("input") or {}
            steps.append((inp.get("command") or (e.get("part") or {}).get("tool") or "?", st_.get("status", ""),
                          (st_.get("output") or "")[:4000]))
    return steps


def sidecar(f: Path, suffix: str) -> Path:
    return f.with_name(f.stem + suffix)


def run_meta(f: Path) -> dict:
    runs = f.parent / "runs.jsonl"
    row = {}
    if runs.exists():
        for line in runs.read_text().splitlines():
            try:
                m = json.loads(line)
            except ValueError:
                continue
            if m.get("id") == f.stem:
                row = dict(m, _dir=str(f.parent))
    return row


BARCODE_DE = {"exact": "exakt", "after check-digit correction": "nach Prüfziffer-Korrektur", "result has no barcode": "Ergebnis ohne Barcode"}


def dots(n: int) -> str:
    return "●" * n + "○" * (5 - n)


def render_score(sc: dict, meta: dict):
    sc = upgrade_score(sc)
    icon = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}[sc["level"]]
    box = {"grün": st.success, "gelb": st.warning, "rot": st.error}[sc["level"]]
    mode = "⚡ Schnellweg (ohne Agent)" if sc.get("mode") == "fast" else "🤖 Agent"
    bon = sc.get("bonus") or {}
    dur = {"ok": "⏱ Dauern ✓ belegt", "partial": "⏱ Dauern ≈ eine Quelle/andere Ausgabe", "missing": "⏱ Dauern ✗ fehlen"}.get(bon.get("durations"), "")
    cr = bon.get("credits") or {}
    crt = f"🎼 Credits {cr.get('tracks', 0)}/{cr.get('of', 0)} Tracks" if cr else ""
    box(f"**{icon} {sc['label'][:1].upper() + sc['label'][1:]}** · Gesamt **{sc['overall']:.1f} / 5** · {mode}"
        + (f"  \nZusatzangaben: {dur}" + (f" · {crt}" if crt else "") if dur else "")
        + ("  \nK.-o.-Regel: " + " · ".join(sc["gates"]) if sc.get("gates") else ""))
    cols = st.columns(4)
    for col, (k, w) in zip(cols, WEIGHTS.items()):
        c, r = sc["categories"][k], RUBRIC[k]
        col.metric(f"{r['name']} · {int(w * 100)} %" if w else f"{r['name']} · Zusatzangabe", dots(c["rating"]), help=r["question"])
        col.caption(f"Stufe {c['rating']} · bewertet von {'Prüfmodell' if c['by'] == 'judge' else 'Code'}")
        with col.expander("Warum?"):
            st.markdown(f"**{c.get('summary') or ''}**")
            if c.get("check") and c["check"] != c.get("summary"):
                st.caption(c["check"])
            if c.get("evidence"):
                st.caption("Belege: " + ", ".join(f"`{short(b)}`" for b in c["evidence"][:6]))
            st.markdown("**Stufen**  \n" + "  \n".join(
                (f"**▶ {n}: {t}**" if n == c["rating"] else f"{n}: {t}") for n, t in sorted(r["levels"].items(), reverse=True)))
    concerns = sc.get("concerns") or sc.get("bedenken") or []
    if concerns:
        with st.expander(f"⚠️ Bedenken des Prüfmodells ({len(concerns)})", expanded=sc["level"] != "grün"):
            for b in concerns:
                st.markdown(f"- {b}")
    f, j = sc.get("facts") or {}, sc.get("judge") or {}
    fact_txt = " · ".join(x for x in (
        "Barcode: " + BARCODE_DE.get(f["barcode_match"], f["barcode_match"].replace("NO (input", "NEIN (Eingabe")
                                     .replace("result", "Ergebnis")) if f.get("barcode_match") else None,
        f"Format passt: {'ja' if f['format_match'] else 'nein'}" if f.get("format_match") is not None else None,
        f"Quellenfamilien: {', '.join(f.get('source_families') or [])}",
        f"Selbsteinschätzung Agent: {f.get('agent_confidence')}") if x)
    st.caption("Fakten (Code): " + fact_txt
               + (f"  \nPrüfmodell: {j.get('model')}, {j.get('tokens_in')} / {j.get('tokens_out')} Tokens" if j else ""))


def run_cost(meta: dict, sc: dict | None) -> tuple[float | None, list[str]]:
    """Kosten dieses Laufs: (gesamt in USD, Aufschlüsselung). Ältere Läufe ohne Kostenerfassung: nur die Prüfung."""
    cost = (meta or {}).get("cost") or {}
    j = (sc or {}).get("judge") or {}
    parts = []
    if (meta or {}).get("mode") == "fast":
        parts.append("Schnellweg (Code) $0")
    elif cost:
        model = (meta.get("model") or "").split("/")[-1]
        if cost.get("saia_requests"):
            parts.append(f"Agent {model}: {cost['saia_requests']} SAIA-Anfragen (kostenlos)")
        else:
            parts.append(f"Agent {model} ${cost.get('agent_usd', 0):.3f}")
    if cost.get("vision_calls"):
        parts.append(f"Bildlesen {cost['vision_calls']}× ${cost['vision_usd']:.3f}")
    jc = cost.get("judge_usd") if cost else j.get("cost_usd")
    if jc is not None:
        parts.append(f"Prüfung ({(j.get('model') or '').replace('claude-', '')}) ${jc:.3f}")
    total = cost.get("total_usd") if cost else jc
    if not cost and total is not None:
        parts.append("ältere Lauf-Daten: nur Prüfkosten bekannt")
    t = []
    if (meta or {}).get("wall_s") is not None:
        t.append(f"Recherche {meta['wall_s']:.0f} s")
    js = j.get("seconds") or (meta or {}).get("judge_s")
    if js:
        t.append(f"Prüfung {js:.0f} s")
    return total, parts + t


def outcome(res: dict, sc: dict | None) -> str:
    """Ergebnis in den Begriffen der GEMA-Aufgabe."""
    if not res:
        return "⚙️ Technical failure (technischer Fehler)"
    if res.get("status") == "not_found":
        return "∅ No match found (kein Treffer)"
    if sc and sc.get("level") == "grün" and res.get("status") == "found":
        return "✅ Supported match (gestützter Treffer)"
    return "🔎 Needs review (zur Prüfung)"


def render_result(res: dict, trace_path: Path | None, sc: dict | None = None, meta: dict | None = None):
    rel = res.get("release") or {}
    status = res.get("status")
    badge = {"found": "✔ gefunden", "ambiguous": "≈ mehrdeutig", "not_found": "✗ nicht gefunden"}.get(status, status)
    st.subheader(f"{rel.get('artist') or '?'} – {rel.get('title') or res['input'].get('title')}")
    st.caption(" · ".join(str(x) for x in (rel.get("format"), rel.get("country"), rel.get("year"), rel.get("label"),
                                           rel.get("catno"), rel.get("barcode"), rel.get("edition")) if x))
    tracks = res.get("tracks") or []
    inp = res.get("input") or {}
    total_cost, cost_parts = run_cost(meta or {}, sc)
    c1, c2, c3, c4, c5, c6 = st.columns([1.6, 1, 0.7, 1.05, 0.7, 0.95])
    oc_short = {"✅": "✅ Treffer", "🔎": "🔎 Prüfen", "∅": "∅ Kein Treffer", "⚙️": "⚙️ Fehler"}
    oc = outcome(res, sc)
    c1.metric("Ergebnis", next((v for k, v in oc_short.items() if oc.startswith(k)), oc), help=oc + " · Status des Agenten: " + badge)
    c2.metric("Bewertung", f"{sc['overall']:.1f} / 5" if sc else f"{res.get('confidence', 0):.0%}",
              help="Regelkatalog (Code + Prüfmodell), siehe unten" if sc else "Selbsteinschätzung des Agenten")
    c3.metric("Tracks", len(tracks))
    c4.metric("Gesamtdauer", mmss(res.get("total_duration_s")))
    c5.metric("Quellen", len(res.get("sources") or []))
    c6.metric("Kosten", "–" if total_cost is None else f"${total_cost:.3f}",
              help="Kosten dieses Laufs (Agent + Bildlesen + Prüfung). " + " · ".join(cost_parts))

    st.caption("Input: " + " · ".join(f"{k}={v}" for k, v in inp.items() if v and k != "id"))
    if rel.get("ids"):
        links = []
        for k, v in rel["ids"].items():
            url = {"musicbrainz": f"https://musicbrainz.org/release/{v}", "discogs": f"https://www.discogs.com/release/{v}"}.get(k)
            links.append(f"[{k}: {v}]({url})" if url else f"{k}: {v}")
        st.markdown("IDs: " + " · ".join(links))
    if sc:
        render_score(sc, meta or {})
    meta = meta or {}
    costmod.render_run(Path(meta["_dir"]) if meta.get("_dir") else OUT, res["input"]["id"], meta, sc)
    st.info(res.get("reasoning") or "", icon="🧭")

    arts = res.get("artists") or []
    st.markdown(f"#### Künstler auf dem Tonträger ({len(arts)})")
    if arts:
        role_de = {"main": "Haupt", "featured": "Gast (feat.)", "remixer": "Remix", "other": "sonstige"}
        st.dataframe([{"Künstler": a["name"], "Rolle": role_de.get(a.get("role"), a.get("role")),
                       "Tracks": ", ".join(a.get("tracks") or []) or "alle",
                       "Quellen": ", ".join(short(x) for x in a.get("sources") or [])} for a in arts],
                     use_container_width=True, hide_index=True, height=min(35 * (len(arts) + 1) + 3, 420))
    else:
        st.caption("Keine Künstlerliste im Ergebnis (ältere Ergebnisse vor Einführung des Felds `artists`).")

    st.markdown("#### Trackliste")
    st.caption("🟢 Dauer von ≥ 2 Quellen bestätigt · 🟡 nur eine Quelle oder Konflikt · 🔴 Dauer fehlt")
    st.dataframe(
        [{"": ampel(t), "Disc": t.get("disc", 1), "Pos.": t.get("position"), "Titel": t.get("title"),
          "Interpret": t.get("artist") or "", "Dauer": mmss(t.get("duration_s")),
          "Credits": "; ".join(f"{c['name']} ({ROLE_DE.get(c['role'], c['role'])})" for c in t.get("credits") or []),
          "ISRC": t.get("isrc") or "",
          "Quellen (Dauer)": ", ".join(short(s) for s in t.get("duration_sources") or []),
          "Flags": ", ".join(t.get("flags") or [])} for t in tracks],
        use_container_width=True, hide_index=True, height=min(35 * (len(tracks) + 1) + 3, 760))

    cl, cr = st.columns(2)
    with cl:
        st.markdown("#### Quellen")
        for s in res.get("sources") or []:
            st.markdown(f"- **{s.get('kind')}** · [{short(s['id'])}]({s.get('url') or '#'})" + (f" – {s['note']}" if s.get("note") else ""))
        if res.get("missing"):
            st.markdown("#### Fehlt")
            for m in res["missing"]:
                st.markdown(f"- 🔴 {m}")
    with cr:
        if res.get("conflicts"):
            st.markdown("#### Konflikte")
            for c in res["conflicts"]:
                vals = " · ".join(f"{short(k)}: **{v}**" for k, v in (c.get("values") or {}).items())
                st.markdown(f"- 🟡 **{c.get('field')}** – {vals}" + (f"  \n  ↳ {c['resolution']}" if c.get("resolution") else ""))
        if res.get("alternatives"):
            st.markdown("#### Andere Ausgaben (nicht gewählt)")
            for a in res["alternatives"]:
                st.markdown(f"- {a.get('description')}" + (f" (`{short(a['source'])}`)" if a.get("source") else "")
                            + (f"  \n  ↳ {a['why_not']}" if a.get("why_not") else ""))


    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["disc", "position", "title", "artist", "duration_s", "duration", "sources", "duration_sources", "flags"])
    for t in tracks:
        w.writerow([t.get("disc"), t.get("position"), t.get("title"), t.get("artist") or "", t.get("duration_s"),
                    mmss(t.get("duration_s")), " ".join(t.get("sources") or []), " ".join(t.get("duration_sources") or []),
                    " ".join(t.get("flags") or [])])
    abuf = io.StringIO()
    aw = csv.writer(abuf)
    aw.writerow(["artist", "role", "tracks", "sources"])
    for a in res.get("artists") or []:
        aw.writerow([a["name"], a.get("role"), " ".join(a.get("tracks") or []), " ".join(a.get("sources") or [])])
    d1, d2, d3, _ = st.columns([1, 1, 1.3, 3])
    d3.download_button("⬇ Künstler CSV", abuf.getvalue(), f"{res['input']['id']}.artists.csv", "text/csv")
    d1.download_button("⬇ JSON", json.dumps(res, ensure_ascii=False, indent=1), f"{res['input']['id']}.json", "application/json")
    d2.download_button("⬇ CSV", buf.getvalue(), f"{res['input']['id']}.csv", "text/csv")

    if trace_path and trace_path.exists():
        steps = tool_steps(load_trace(trace_path))
        with st.expander(f"🔎 Agent-Trace: {len(steps)} Tool-Aufrufe"):
            for i, (cmd, stat, out) in enumerate(steps, 1):
                st.markdown(f"**{i}.** `{cmd[:220]}` – {stat}")
                if out:
                    st.code(out[:1500], language="text")


def result_files(with_examples: bool = False) -> list[Path]:
    files = []
    for d in (OUT, EXAMPLES) if with_examples else (OUT,):
        files += [f for f in d.glob("*.json") if not f.name.startswith(("runs", "report")) and not f.name.endswith(".score.json")]
    return sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)


# ------------------------------------------------------------------ Seiten

def _runner():
    """runner/run.py als Modul laden (nur für load_cases: gleicher toleranter CSV-Import wie in der Kommandozeile)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("tl_runner", ROOT / "runner/run.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_batch(cases: list[dict], batch: str, folder: Path) -> Path:
    """Ausgewählte Fälle als normalisierte CSV mit eindeutigen IDs (Präfix = Batch) – überschreibt keine alten Ergebnisse."""
    path = folder / f"{batch}.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "artist", "ean", "format", "notes"])
        w.writeheader()
        for c in cases:
            w.writerow({"id": f"{batch}-{c['id']}"[:64], **{k: c.get(k) or "" for k in ("title", "artist", "ean", "format", "notes")}})
    return path


def csv_import():
    st.caption("CSV mit einer Zeile pro Tonträger. Erkannt werden Kodierung, Trennzeichen (, ; Tab) und Spaltennamen wie "
               "barcode/ean, album_title/titel, album_artist/interpret, format. Unbekannte Spalten gehen als Hinweis an den Agenten.")
    up = st.file_uploader("CSV-Datei", type=["csv", "tsv", "txt"], key="csv_up")
    if not up:
        return
    raw = up.getvalue()
    folder = ROOT / "output" / "uploads"
    folder.mkdir(parents=True, exist_ok=True)
    src = folder / f"upload-{hashlib.sha1(raw).hexdigest()[:10]}.csv"
    if not src.exists():
        src.write_bytes(raw)
    try:
        cases = [c for c in _runner().load_cases(str(src)) if c["title"] or c["ean"]]
    except Exception as e:  # noqa: BLE001 – kaputte Datei soll die Seite nicht abstürzen lassen
        st.error(f"CSV nicht lesbar: {e}")
        return
    if not cases:
        st.warning("Keine Zeile mit Titel oder Barcode gefunden.")
        return
    table = pd.DataFrame([{"starten": True, "Titel": c["title"], "Interpret": c["artist"], "Barcode": c["ean"],
                           "Format": c["format"], "Hinweis": c["notes"]} for c in cases])
    edited = st.data_editor(table, hide_index=True, use_container_width=True, key=f"csv_ed_{src.stem}",
                            disabled=["Titel", "Interpret", "Barcode", "Format", "Hinweis"])
    pick = [c for c, keep in zip(cases, edited["starten"]) if keep]
    c1, c2, c3 = st.columns([2, 1, 2])
    model = c1.selectbox("Modell", MODELS, key="csv_model")
    par = c2.number_input("parallel", 1, 10, min(3, max(1, len(pick))), key="csv_par")
    fast = c3.checkbox("Schnellweg erlauben", value=True, key="csv_fast")
    st.caption(f"{len(pick)} von {len(cases)} Fällen ausgewählt · erwartete Kosten ca. ${len(pick) * 0.023:.2f} "
               f"(Ø 2,3 Cent pro Fall) · je Fall 1–5 min")
    if OUT != ROOT / "output":
        st.info(f"Neue Läufe landen in output/ – die Oberfläche zeigt gerade {OUT.name}/ (TL_OUT_DIR).")
    if st.button(f"{len(pick)} Fälle starten", type="primary", disabled=not pick, key="csv_go"):
        batch = "csv-" + time.strftime("%m%d-%H%M%S")
        path = write_batch(pick, batch, folder)
        args = [sys.executable, str(ROOT / "runner/run.py"), "--csv", str(path), "--parallel", str(int(par)), "-m", model]
        log = (folder / f"{batch}.log").open("w")
        subprocess.Popen(args + ([] if fast else ["--no-fast"]), cwd=ROOT, stdout=log, stderr=subprocess.STDOUT,
                         start_new_session=True)
        st.session_state["csv_batch"] = (batch, len(pick))
    if st.session_state.get("csv_batch"):
        batch, n = st.session_state["csv_batch"]
        st.success(f"{n} Fälle gestartet ({batch}). Fortschritt unter 🛰️ Live, fertige Ergebnisse unter 📂 Ergebnisse "
                   f"(IDs beginnen mit {batch}). Protokoll: output/uploads/{batch}.log")


page = st.sidebar.radio("Ansicht", ["📋 Überblick", "🔍 Neue Recherche", "🛰️ Live", "📂 Ergebnisse", "💶 Kosten", "📊 Evaluation"])
st.sidebar.caption("Agent: opencode + tl-Tools · Modelle: Gemini API (GEMA), SAIA (GWDG), Claude")

if page == "🔍 Neue Recherche":
    st.title("💿 Tracklist-Finder")
    st.caption("Lückenhafte Angaben rein → richtige Ausgabe + Trackliste mit Dauern, Quellen und Konflikten raus.")
    tab_one, tab_csv = st.tabs(["Einzelner Fall", "📄 CSV-Import (mehrere Fälle)"])
    with tab_csv:
        csv_import()
    with tab_one:
        with st.form("q"):
            c1, c2 = st.columns(2)
            title = c1.text_input("Titel", "King of Kingz")
            artist = c2.text_input("Interpret (optional)", "Bushido")
            c3, c4, c5 = st.columns(3)
            ean = c3.text_input("EAN / Barcode (optional)", "")
            fmt = c4.selectbox("Format (optional)", ["", "CD", "Vinyl", "Kassette", "Digital"])
            model = c5.selectbox("Modell", MODELS)
            fast = st.checkbox("Schnellweg erlauben (eindeutiger Barcode, MusicBrainz = Discogs → ohne Agent)", value=True)
            go = st.form_submit_button("Recherche starten", type="primary")
        if go:
            rid = "ui-" + re.sub(r"[^a-z0-9]+", "-", f"{artist} {title} {fmt}".lower()).strip("-")[:40] + time.strftime("-%H%M%S")
            args = [sys.executable, str(ROOT / "runner/run.py"), "--id", rid, "-m", model] + ([] if fast else ["--no-fast"])
            for flag, val in (("--title", title), ("--artist", artist), ("--ean", ean), ("--format", fmt)):
                if val:
                    args += [flag, val]
            proc = subprocess.Popen(args, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            st.session_state["run"] = rid
            trace = OUT / f"{rid}.trace.jsonl"
            ph = st.empty()
            while proc.poll() is None:
                with ph.container():
                    livemod.render(OUT, rid)
                time.sleep(1.5)
            with ph.container():
                livemod.render(OUT, rid)
            res_path = OUT / f"{rid}.json"
            if res_path.exists():
                scp = sidecar(res_path, ".score.json")
                render_result(json.loads(res_path.read_text()), trace, json.loads(scp.read_text()) if scp.exists() else None,
                              run_meta(res_path))
            else:
                st.error("Kein Ergebnis geschrieben – siehe Trace.")
                steps = tool_steps(load_trace(trace))
                st.write(steps[-3:])

elif page == "🛰️ Live":
    st.title("🛰️ Live")
    st.caption("Alle Läufe der letzten 2 Stunden – auch Batch-Läufe aus der Kommandozeile (runner/run.py). Aktualisiert alle 2 s.")

    @st.fragment(run_every="2s")
    def board():
        rs = livemod.runs(OUT)
        if not rs:
            st.info("Gerade keine Läufe. Start: 🔍 Neue Recherche oder `uv run python runner/run.py --csv …`")
            return
        active = [cid for cid, s in rs if not s["done"]]
        st.markdown(f"**{len(active)} aktiv** · {len(rs) - len(active)} fertig")
        st.dataframe([{"Lauf": cid, "Phase": {"fast": "⚡ Schnellweg", "agent": "🤖 Agent", "judge": "🔍 Prüfung",
                                               "done": "🏁 fertig"}.get(s["current"], "⏳"),
                       "Gerade": livemod.activity(s).replace("**", "").replace("`", ""),
                       "Ampel": livemod.LEVEL.get((s["done"] or {}).get("level"), "")} for cid, s in rs],
                     use_container_width=True, hide_index=True)
        pick = st.selectbox("Details", [cid for cid, _ in rs], key="live_pick")
        livemod.render(OUT, pick)

    board()

elif page == "📋 Überblick":
    ovmod.render_page(OUT)

elif page == "💶 Kosten":
    costmod.render_page(OUT)

elif page == "📂 Ergebnisse":
    show_ex = st.sidebar.toggle("Alte Beispiele (examples/) zeigen", value=False)
    files = result_files(show_ex)
    if not files:
        st.warning("Noch keine Ergebnisse.")
    else:
        labels = {f"{f.parent.name}/{f.stem}": f for f in files}
        pick = st.sidebar.selectbox("Ergebnis", list(labels))
        f = labels[pick]
        res = json.loads(f.read_text())
        scp = sidecar(f, ".score.json")
        render_result(res, sidecar(f, ".trace.jsonl") if sidecar(f, ".trace.jsonl").exists() else None,
                      json.loads(scp.read_text()) if scp.exists() else None, run_meta(f))
        md = f.with_name(f.stem + ".trace.md")
        if md.exists() and not f.with_name(f.stem + ".trace.jsonl").exists():
            with st.expander("🔎 Agent-Trace (Markdown)"):
                st.markdown(md.read_text()[:60000])

else:
    rep = ROOT / "eval/report.md"
    if st.button("Neu berechnen"):
        subprocess.run([sys.executable, str(ROOT / "eval/evaluate.py")], cwd=ROOT, capture_output=True)
    st.markdown(rep.read_text() if rep.exists() else "Noch keine Auswertung – `uv run python eval/evaluate.py`")
