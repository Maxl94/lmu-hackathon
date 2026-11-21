"""Kosten-Darstellung: pro Lauf (Tabelle nach Baustein + Gesamtwert) und über alle Läufe (Seite „Kosten“).

Datenquellen pro Lauf (output/):
  runs.jsonl            Modus, Agent-Modell, Zeiten, cost{agent_usd, vision_usd, judge_usd, total_usd, saia_requests}
  <id>.trace.jsonl      Agent-Tokens (input, output, cache read) aus opencode
  <id>.usage.jsonl      jeder Bildlese-/Prüfaufruf mit Modell, Tokens, Kosten
  <id>.score.json       Prüfmodell, Tokens, Dauer, Kosten
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

# Listenpreise (USD/MTok in, out) für Modelle, die bei uns kostenlos laufen (SAIA) – zeigt, was es im Betrieb kosten würde
LIST_PRICE = {"qwen3.5-397b-a17b": (0.45, 3.00), "glm-5.3": (0.07, 1.40), "mistral-large-4-1t-a52b": (0.70, 2.10),
              "deepseek-v4.1-flash-1017": (0.15, 0.60)}
ICON = {"grün": "🟢", "gelb": "🟡", "rot": "🔴"}


def _jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text(errors="replace").splitlines():
        if line.startswith("{"):
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def agent_tokens(trace: Path) -> dict:
    t = {"in": 0, "out": 0, "cache": 0, "steps": 0}
    for e in _jsonl(trace):
        if e.get("type") == "step_finish":
            tk = (e.get("part") or {}).get("tokens") or {}
            t["in"] += tk.get("input") or 0
            t["out"] += (tk.get("output") or 0) + (tk.get("reasoning") or 0)
            t["cache"] += (tk.get("cache") or {}).get("read") or 0
            t["steps"] += 1
    return t


def _secs(x) -> str:
    return "–" if x is None else f"{x:.0f} s"


def _tok(i: int, o: int, cache: int = 0) -> str:
    k = lambda n: f"{n / 1000:.1f}k" if n >= 1000 else str(n)  # noqa: E731
    return f"{k(i)}" + (f" (+{k(cache)} Cache)" if cache else "") + f" / {k(o)}"


def breakdown(out: Path, cid: str, meta: dict, sc: dict | None) -> tuple[list[dict], float | None]:
    """Zeilen pro Baustein + Gesamtkosten. Ältere Läufe ohne Kostenerfassung → nur, was bekannt ist."""
    cost = (meta or {}).get("cost") or {}
    j = (sc or {}).get("judge") or {}
    usage = _jsonl(out / f"{cid}.usage.jsonl")
    rows = []
    if meta.get("mode") == "fast":
        rows.append({"Baustein": "⚡ Schnellweg", "Modell": "Code (MusicBrainz + Discogs)", "Aufrufe": "–", "Tokens ein / aus": "–",
                     "Zeit": _secs(meta.get("wall_s")), "Kosten ($)": 0.0, "Hinweis": "ohne KI"})
    elif meta:
        model = (meta.get("model") or "?").split("/")[-1]
        tk = agent_tokens(out / f"{cid}.trace.jsonl")
        note = ""
        agent_usd = cost.get("agent_usd", 0.0)
        if cost.get("saia_requests"):
            note = "SAIA: kostenlos"
            if model in LIST_PRICE:
                pi, po = LIST_PRICE[model]
                note += f" · zum Listenpreis ≈ ${(tk['in'] + tk['cache']) * pi / 1e6 + tk['out'] * po / 1e6:.3f}"
        rows.append({"Baustein": "🤖 Recherche-Agent", "Modell": model,
                     "Aufrufe": f"{tk['steps'] or meta.get('steps', '?')} Schritte · {meta.get('tool_calls', '?')} Tools",
                     "Tokens ein / aus": _tok(tk["in"], tk["out"], tk["cache"]) if tk["steps"] else "–",
                     "Zeit": _secs(meta.get("wall_s")), "Kosten ($)": agent_usd, "Hinweis": note})
    vis = [u for u in usage if u.get("tool") == "tl-vision"]
    if vis:
        models = sorted({(u.get("model") or "?").replace("claude-", "") for u in vis})
        rows.append({"Baustein": "🖼️ Bildlesen", "Modell": ", ".join(models), "Aufrufe": f"{len(vis)} Bilder",
                     "Tokens ein / aus": _tok(sum(u.get("input_tokens") or 0 for u in vis), sum(u.get("output_tokens") or 0 for u in vis)),
                     "Zeit": "in Agent-Zeit", "Kosten ($)": round(sum(u.get("cost_usd") or 0 for u in vis), 5),
                     "Hinweis": "Rückseiten/Cover lesen"})
    if j:
        rows.append({"Baustein": "🔍 Prüfung", "Modell": (j.get("model") or "?").replace("claude-", ""), "Aufrufe": "1",
                     "Tokens ein / aus": _tok(j.get("tokens_in") or 0, j.get("tokens_out") or 0),
                     "Zeit": _secs(j.get("seconds")), "Kosten ($)": j.get("cost_usd") or 0.0, "Hinweis": "Regelkatalog + Bedenken"})
    total = cost.get("total_usd") if cost else (sum(r["Kosten ($)"] or 0 for r in rows) if rows else None)
    return rows, total


def render_run(out: Path, cid: str, meta: dict, sc: dict | None):
    """Kostenblock auf der Ergebnisseite: Gesamtwert, Hochrechnung, Tabelle pro Baustein."""
    rows, total = breakdown(out, cid, meta or {}, sc)
    st.markdown("#### 💶 Kosten dieses Laufs")
    if not rows:
        st.caption("Für diesen Lauf liegen keine Kostendaten vor (älterer Lauf).")
        return
    secs = ((meta or {}).get("wall_s") or 0) + (((sc or {}).get("judge") or {}).get("seconds") or 0)
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Gesamt", f"${total:.4f}" if total is not None else "–")
    k2.metric("in Cent", f"{total * 100:.2f} ct" if total is not None else "–")
    k3.metric("≈ pro 1.000 Tonträger", f"${total * 1000:,.0f}" if total is not None else "–",
              help="Hochrechnung: Kosten dieses Laufs × 1.000 (gleiche Art von Fall)")
    k4.metric("Zeit gesamt", f"{int(secs // 60)}:{int(secs % 60):02d} min")
    df = pd.DataFrame(rows)
    df["Anteil"] = [(r["Kosten ($)"] or 0) / total if total else 0 for r in rows]
    df = pd.concat([df, pd.DataFrame([{"Baustein": "Σ Gesamt", "Modell": "", "Aufrufe": "", "Tokens ein / aus": "",
                                       "Zeit": _secs(secs), "Kosten ($)": total, "Hinweis": "", "Anteil": 1.0 if total else 0}])],
                   ignore_index=True)
    st.dataframe(df[["Baustein", "Modell", "Aufrufe", "Tokens ein / aus", "Zeit", "Kosten ($)", "Anteil", "Hinweis"]],
                 hide_index=True, use_container_width=True,
                 column_config={"Kosten ($)": st.column_config.NumberColumn(format="$%.4f"),
                                "Anteil": st.column_config.ProgressColumn(format="percent", min_value=0, max_value=1)})


def all_runs(out: Path) -> pd.DataFrame:
    last: dict[str, dict] = {}
    for r in _jsonl(out / "runs.jsonl"):
        if r.get("cost"):
            last[r["id"]] = r
    rows = []
    for cid, r in last.items():
        c = r["cost"]
        rows.append({"Lauf": cid, "Modus": "⚡ Schnellweg" if r.get("mode") == "fast" else "🤖 Agent",
                     "Agent-Modell": "–" if r.get("mode") == "fast" else (r.get("model") or "").split("/")[-1],
                     "Ampel": ICON.get(r.get("level"), "–"), "Tracks": r.get("tracks"),
                     "Agent ($)": c.get("agent_usd", 0.0), "Bildlesen ($)": c.get("vision_usd", 0.0),
                     "Prüfung ($)": c.get("judge_usd", 0.0), "Gesamt ($)": c.get("total_usd", 0.0),
                     "Bilder": c.get("vision_calls", 0), "SAIA-Anfragen": c.get("saia_requests", 0),
                     "Zeit (s)": (r.get("wall_s") or 0) + (r.get("judge_s") or 0), "Zeitpunkt": r.get("ts", "")})
    return pd.DataFrame(rows)


def render_page(out: Path):
    st.title("💶 Kosten")
    st.caption("Alle Läufe mit Kostenerfassung (output/runs.jsonl, jeweils der letzte Lauf pro Fall). "
               "Preise: Listenpreise von Google (Gemini API – die Rechnung geht über den GEMA-Schlüssel an die GEMA), "
               "Anthropic und OpenRouter; SAIA ist für Hochschulen kostenlos (Kontingent).")
    df = all_runs(out)
    if df.empty:
        st.info("Noch keine Läufe mit Kostenerfassung.")
        return
    groups = {"Eingabeliste (Fälle „01-…“, z. B. GEMA-Daten)": df["Lauf"].str.match(r"^\d\d-"),
              "Testfälle (Beispiele, Fallen)": ~df["Lauf"].str.match(r"^\d\d-"),
              "alle Läufe": df["Lauf"].notna()}
    pick = st.radio("Auswahl", list(groups), horizontal=True, key="cost_pick")
    df = df[groups[pick]]
    if df.empty:
        st.info("Keine Läufe in dieser Auswahl.")
        return
    fast, agent = df[df["Modus"].str.contains("Schnellweg")], df[df["Modus"].str.contains("Agent")]
    total = df["Gesamt ($)"].sum()
    m = st.columns(5)
    m[0].metric("Tonträger", len(df))
    m[1].metric("Kosten gesamt", f"${total:.3f}")
    m[2].metric("Ø pro Tonträger", f"${total / len(df):.4f}")
    m[3].metric("Ø Schnellweg-Fall", f"${fast['Gesamt ($)'].mean():.4f}" if len(fast) else "–", help=f"{len(fast)} Fälle")
    m[4].metric("Ø Agent-Fall", f"${agent['Gesamt ($)'].mean():.4f}" if len(agent) else "–", help=f"{len(agent)} Fälle")
    avg = total / len(df)
    st.markdown(f"**Hochrechnung** bei gleicher Mischung ({len(fast)} Schnellweg / {len(agent)} Agent): "
                f"1.000 Tonträger ≈ **${avg * 1000:,.0f}** · 100.000 Tonträger ≈ **${avg * 100000:,.0f}** · "
                f"Ø Zeit pro Tonträger {df['Zeit (s)'].mean():.0f} s")

    st.markdown("#### Wofür das Geld ausgegeben wird")
    comp = pd.DataFrame([{"Baustein": k.replace(" ($)", ""), "Kosten ($)": df[k].sum(),
                          "Anteil": df[k].sum() / total if total else 0, "Ø pro Tonträger ($)": df[k].mean()}
                         for k in ("Agent ($)", "Bildlesen ($)", "Prüfung ($)")])
    c1, c2 = st.columns([1, 1.3])
    c1.dataframe(comp, hide_index=True, use_container_width=True,
                 column_config={"Kosten ($)": st.column_config.NumberColumn(format="$%.4f"),
                                "Ø pro Tonträger ($)": st.column_config.NumberColumn(format="$%.4f"),
                                "Anteil": st.column_config.ProgressColumn(format="percent", min_value=0, max_value=1)})
    by_model = agent.groupby("Agent-Modell").agg(Fälle=("Lauf", "count"), Ø_Gesamt=("Gesamt ($)", "mean"),
                                                 Ø_Agent=("Agent ($)", "mean"), Ø_Zeit=("Zeit (s)", "mean")).reset_index()
    if not by_model.empty:
        c2.dataframe(by_model.rename(columns={"Ø_Gesamt": "Ø gesamt ($)", "Ø_Agent": "Ø Agent ($)", "Ø_Zeit": "Ø Zeit (s)"}),
                     hide_index=True, use_container_width=True,
                     column_config={"Ø gesamt ($)": st.column_config.NumberColumn(format="$%.4f"),
                                    "Ø Agent ($)": st.column_config.NumberColumn(format="$%.4f"),
                                    "Ø Zeit (s)": st.column_config.NumberColumn(format="%.0f s")})

    st.markdown("#### Kosten pro Lauf")
    chart = df.set_index("Lauf")[["Agent ($)", "Bildlesen ($)", "Prüfung ($)"]].sort_values("Agent ($)", ascending=False)
    st.bar_chart(chart, horizontal=True, height=max(220, 26 * len(chart)), color=["#1f4e9c", "#7fb0f0", "#e0a030"])
    st.dataframe(df.sort_values("Zeitpunkt", ascending=False), hide_index=True, use_container_width=True,
                 column_config={k: st.column_config.NumberColumn(format="$%.4f")
                                for k in ("Agent ($)", "Bildlesen ($)", "Prüfung ($)", "Gesamt ($)")}
                 | {"Zeit (s)": st.column_config.NumberColumn(format="%.0f s")})
    st.download_button("⬇ Kosten als CSV", df.to_csv(index=False), "kosten.csv", "text/csv")
