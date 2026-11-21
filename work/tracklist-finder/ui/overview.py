"""Überblick: alle Tonträger mit Ergebnis in den Begriffen der GEMA-Aufgabe + Wirtschaftlichkeit für 1.000.

Ergebnis-Kategorien (README der GEMA): supported match · needs review · no match found · technical failure.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st

OUTCOMES = {"supported": "✅ Supported match", "review": "🔎 Needs review", "nomatch": "∅ No match found",
            "failure": "⚙️ Technical failure"}
ICON = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}


def _jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text().splitlines() if x.startswith("{")]


def outcome_key(res: dict | None, sc: dict | None) -> str:
    if not res:
        return "failure"
    if res.get("status") == "not_found":
        return "nomatch"
    if sc and sc.get("level") == "grün" and res.get("status") == "found":
        return "supported"
    return "review"


def table(out: Path, prepared: bool = True) -> pd.DataFrame:
    runs = {}
    for r in _jsonl(out / "runs.jsonl"):
        runs[r["id"]] = r
    rows = []
    for cid, m in sorted(runs.items()):
        if bool(re.match(r"^\d\d-", cid)) != prepared:
            continue
        f, sp = out / f"{cid}.json", out / f"{cid}.score.json"
        res = json.loads(f.read_text()) if f.exists() else None
        sc = json.loads(sp.read_text()) if sp.exists() else None
        inp = (res or {}).get("input") or {}
        rel = (res or {}).get("release") or {}
        tracks = (res or {}).get("tracks") or []
        k = outcome_key(res, sc) if m.get("valid") or res else "failure"
        bon = (sc or {}).get("bonus") or {}
        rows.append({
            "#": cid[:2], "Eingabe": f"{inp.get('artist') or '–'} – {inp.get('title') or ''}" if inp else cid[3:],
            "EAN": inp.get("ean") or "–", "Ergebnis": OUTCOMES[k], "Ampel": ICON.get((sc or {}).get("level"), "–"),
            "Gefundene Ausgabe": (f"{rel.get('artist') or ''} – {rel.get('title') or ''} · {rel.get('format') or '?'} "
                                  f"{rel.get('year') or ''} {rel.get('country') or ''}") if rel else "–",
            "Tracks": len(tracks), "Künstler": len((res or {}).get("artists") or []),
            "Dauern": {"ok": "✓", "partial": "≈", "missing": "✗"}.get(bon.get("durations"), "") + " "
                      + (f"{sum(1 for t in tracks if t.get('duration_s') is not None)}/{len(tracks)}" if tracks else "–"),
            "Credits": f"{sum(1 for t in tracks if t.get('credits'))}/{len(tracks)}" if tracks else "–",
            "Quellen": len((res or {}).get("sources") or []), "Modus": "⚡" if m.get("mode") == "fast" else "🤖",
            "Zeit (s)": round((m.get("wall_s") or 0) + (m.get("judge_s") or 0)),
            "Kosten ($)": (m.get("cost") or {}).get("total_usd"), "_key": k,
            "_level": (sc or {}).get("level"), "_dur": bon.get("durations")})
    return pd.DataFrame(rows)


def render_page(out: Path):
    st.title("📋 Überblick")
    st.caption("Alle Tonträger der Eingabeliste mit Ergebnis in den Kategorien der Aufgabe. Die Ampel bewertet den Kern "
               "(Ausgabe, Trackliste mit Künstlern, Quellen); Dauern und Credits sind Zusatzangaben: ⏱ ✓ belegt · ≈ eine Quelle/andere "
               "Ausgabe · ✗ fehlt. ✅ Supported match = grün · 🔎 Needs review = gelb/rot · ∅ No match · ⚙️ Technical failure")
    df = table(out)
    if df.empty:
        st.info("Noch keine Läufe der Eingabeliste in output/.")
        return
    cnt = df["_key"].value_counts()
    m = st.columns(5)
    m[0].metric("Tonträger", len(df))
    for col, k in zip(m[1:], ("supported", "review", "nomatch", "failure")):
        col.metric(OUTCOMES[k], int(cnt.get(k, 0)))
    st.dataframe(df[[c for c in df.columns if not c.startswith("_")]], hide_index=True, use_container_width=True,
                 height=min(35 * (len(df) + 1) + 3, 940),
                 column_config={"Kosten ($)": st.column_config.NumberColumn(format="$%.3f")})

    fresh = table(out, prepared=False)
    if not fresh.empty:
        st.markdown("### 🧪 Frische Fälle (nicht vorbereitet, gleicher Workflow)")
        st.dataframe(fresh[[c for c in fresh.columns if not c.startswith("_") and c != "#"]], hide_index=True, use_container_width=True,
                     column_config={"Kosten ($)": st.column_config.NumberColumn(format="$%.3f")})

    st.markdown("### 💶 Was kosten 1.000 Datensätze?")
    st.caption("Hochrechnung aus den gemessenen Läufen oben. Annahmen links anpassen – Prüfaufwand fällt für gelbe und rote "
               "Fälle an, ein kurzer Blick bei grünen mit „Dauern prüfen“; bei „No match“ recherchiert ein Mensch von Grund auf.")
    a, b = st.columns([1, 1.6])
    with a:
        yel_min = st.number_input("Minuten Prüfung pro gelbem Fall", 0, 120, 5, key="ov_rev")
        red_min = st.number_input("Minuten Prüfung pro rotem Fall", 0, 240, 20, key="ov_red")
        dur_min = st.number_input("Minuten pro grünem Fall mit „Dauern prüfen“", 0, 30, 1, key="ov_dur")
        nomatch_min = st.number_input("Minuten Recherche pro „No match“", 0, 240, 20, key="ov_nm")
        rate = st.number_input("Stundensatz Sachbearbeitung (€)", 10, 200, 45, key="ov_rate")
        par = st.number_input("Parallele Läufe", 1, 50, 10, key="ov_par")
        eur = st.number_input("Wechselkurs $ → €", 0.5, 1.5, 0.92, step=0.01, key="ov_fx")
    n = len(df)
    share = {k: cnt.get(k, 0) / n for k in OUTCOMES}
    api = (df["Kosten ($)"].fillna(0).mean() or 0) * 1000 * eur
    runtime_h = df["Zeit (s)"].mean() * 1000 / par / 3600
    sh_yel = (df["_level"] == "gelb").mean()
    sh_red = (df["_level"] == "rot").mean()
    sh_dur = ((df["_key"] == "supported") & (df["_dur"] != "ok")).mean()
    per_rec = sh_yel * yel_min + sh_red * red_min + sh_dur * dur_min + (share["nomatch"] + share["failure"]) * nomatch_min
    review_h = 1000 * per_rec / 60
    with b:
        st.dataframe(pd.DataFrame([
            {"Posten": "KI- und API-Kosten (Agent, Bildlesen, Prüfung)", "pro 1.000": f"{api:,.0f} €",
             "Annahme": f"Ø {df['Kosten ($)'].fillna(0).mean():.3f} $ pro Tonträger aus {n} Läufen"},
            {"Posten": "Laufzeit", "pro 1.000": f"{runtime_h:,.1f} h",
             "Annahme": f"Ø {df['Zeit (s)'].mean():.0f} s pro Tonträger, {par} parallel"},
            {"Posten": "Menschliche Prüfung", "pro 1.000": f"{review_h:,.0f} h ≈ {review_h * rate:,.0f} €",
             "Annahme": f"{sh_yel:.0%} gelb × {yel_min} min + {sh_red:.0%} rot × {red_min} min + {sh_dur:.0%} „Dauern prüfen“ × "
                        f"{dur_min} min + {share['nomatch'] + share['failure']:.0%} ohne Treffer × {nomatch_min} min"},
            {"Posten": "Gesamt (ohne Aufbau)", "pro 1.000": f"{api + review_h * rate:,.0f} €",
             "Annahme": "Datenbanken (MusicBrainz, Discogs) kostenlos; Websuche im Gratis-Kontingent"},
        ]), hide_index=True, use_container_width=True)
        st.markdown("**Zum Vergleich: alles manuell** – wie lange das dauert, ist eine Annahme, nicht gemessen.")
        st.dataframe(pd.DataFrame([
            {"Manuell pro Tonträger": f"{m_} min", "alles manuell": f"{1000 * m_ / 60:,.0f} h ≈ {1000 * m_ / 60 * rate:,.0f} €",
             "mit Prototyp (nur Prüfung)": f"{review_h:,.0f} h ≈ {review_h * rate:,.0f} €",
             "Ersparnis": f"{max(0.0, 1 - review_h / (1000 * m_ / 60)):.0%}"} for m_ in (5, 10, 20)]),
            hide_index=True, use_container_width=True)
        st.caption(f"Break-even: Der Prototyp spart Zeit, solange die manuelle Recherche im Schnitt länger als "
                   f"{per_rec:.1f} min pro Tonträger dauert.")
