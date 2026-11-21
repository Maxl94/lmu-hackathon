"""Live-Ansicht eines Laufs: welche Phase, welcher Akteur, welches Tool gerade arbeitet.

Quellen: output/<id>.events.jsonl (Runner-Phasen + tool_start/tool_end aller tl-Tools) und
output/<id>.trace.jsonl (opencode: Agent-Text, Modell-Schritte, Tokens).
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import streamlit as st

TOOLS = {
    "tl-mb": ("🗄️", "MusicBrainz"), "tl-discogs": ("💿", "Discogs"), "tl-vision": ("🖼️", "Bildlesen · Claude"),
    "tl-scrape": ("🕸️", "Scraper"), "tl-search": ("🔎", "Websuche · Brave"), "tl-caa": ("🖼️", "Cover Art Archive"),
    "tl-itunes": ("🎵", "iTunes"), "tl-deezer": ("🎵", "Deezer"), "tl-lastfm": ("🎵", "Last.fm"),
    "tl-gtin": ("🔢", "Barcode-Prüfung"), "tl-validate": ("✅", "Validator"),
}
PHASES = [("fast", "⚡ Schnellweg", "Code: Barcode → MusicBrainz + Discogs"),
          ("agent", "🤖 Recherche-Agent", ""),
          ("judge", "🔍 Prüfmodell", ""),
          ("done", "🏁 Ergebnis", "")]
LEVEL = {"grün": "🟢 übernehmen", "gelb": "🟡 kurz prüfen", "rot": "🔴 manuell klären"}


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("{"):
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def _ago(sec: float) -> str:
    sec = int(sec)
    return f"{sec} s" if sec < 60 else f"{sec // 60} min {sec % 60:02d} s"


def state(out: Path, cid: str) -> dict:
    evs = _jsonl(out / f"{cid}.events.jsonl")
    trace = _jsonl(out / f"{cid}.trace.jsonl")
    s: dict = {"cid": cid, "events": evs, "phases": {}, "running": [], "timeline": [], "done": None, "start": None,
               "steps": 0, "tokens": 0, "last_step_start": None, "last_activity": None}
    open_tools: list[dict] = []
    for e in evs:
        t, ts = e.get("event"), e.get("ts")
        if t == "run_start":
            s["start"], s["input"], s["model"], s["judge_model"] = ts, e.get("input"), e.get("model"), e.get("judge_model")
            s["fast_enabled"], s["judge_enabled"] = e.get("fast"), e.get("judge")
        elif t == "phase_start":
            s["phases"][e["phase"]] = {"start": ts, "actor": e.get("actor")}
            s["timeline"].append((ts, "▶", e.get("actor") or e["phase"], "startet", None))
        elif t == "phase_end":
            ph = s["phases"].setdefault(e["phase"], {})
            ph.update(end=ts, ok=e.get("ok"), info=e)
        elif t == "fast_step":
            s["timeline"].append((ts, "⚡", "Schnellweg", e.get("msg", ""), None))
        elif t == "tool_start":
            open_tools.append(e)
        elif t == "tool_end":
            for i, o in enumerate(open_tools):
                if o.get("tool") == e.get("tool") and o.get("args") == e.get("args"):
                    open_tools.pop(i)
                    break
            icon, name = TOOLS.get(e.get("tool"), ("🔧", e.get("tool")))
            s["timeline"].append((ts, icon, name, f"`{e.get('tool')} {e.get('args', '')[:140]}`",
                                  f"{e.get('seconds')} s" + ("" if e.get("ok") else " · ❌ Fehler")))
        elif t == "run_end":
            s["done"] = e
    s["running"] = open_tools
    for e in trace:
        ts = (e.get("timestamp") or 0) / 1000
        part = e.get("part") or {}
        if e.get("type") == "step_start":
            s["steps"] += 1
            s["last_step_start"] = ts
        elif e.get("type") == "step_finish":
            tk = part.get("tokens") or {}
            s["tokens"] += (tk.get("input") or 0) + (tk.get("output") or 0) + (tk.get("reasoning") or 0)
        elif e.get("type") == "text" and (part.get("text") or "").strip():
            s["timeline"].append((ts, "💬", "Agent", part["text"].strip()[:400], None))
        elif e.get("type") == "tool_use" and part.get("tool") in ("write", "edit", "skill", "read"):
            inp = (part.get("state") or {}).get("input") or {}
            what = inp.get("name") or inp.get("filePath") or inp.get("path") or ""
            s["timeline"].append((ts, "📝", "Agent", f"{part['tool']} {str(what)[-60:]}", None))
    s["timeline"].sort(key=lambda x: x[0] or 0)
    s["last_activity"] = max([x[0] for x in s["timeline"] if x[0]] + [s["start"] or 0])
    # aktuelle Phase
    cur = None
    for key, *_ in PHASES[:3]:
        ph = s["phases"].get(key)
        if ph and ph.get("start") and not ph.get("end"):
            cur = key
    s["current"] = "done" if s["done"] else cur
    return s


def activity(s: dict) -> str:
    """Eine Zeile: wer arbeitet gerade woran."""
    now = time.time()
    if s["done"]:
        d = s["done"]
        return (f"🏁 fertig · {LEVEL.get(d.get('level'), d.get('status') or '–')} · {d.get('tracks')} Tracks · "
                f"{_ago(d.get('wall_s', 0) + d.get('judge_s', 0))} · ${d.get('cost_usd') or 0:.3f}")
    if s["running"]:
        r = s["running"][-1]
        icon, name = TOOLS.get(r.get("tool"), ("🔧", r.get("tool")))
        return f"{icon} **{name}** · `{r.get('tool')} {r.get('args', '')[:90]}` · läuft seit {_ago(now - r['ts'])}"
    cur = s.get("current")
    if cur == "agent":
        since = now - (s["last_activity"] or now)
        return f"🤖 **Agent denkt nach** (Modell-Schritt {s['steps']}, {s.get('model')}) · seit {_ago(since)}"
    if cur == "judge":
        return f"🔍 **Prüfmodell liest die Belege** ({s.get('judge_model')}) · seit {_ago(now - s['phases']['judge']['start'])}"
    if cur == "fast":
        return "⚡ **Schnellweg** prüft Barcode in MusicBrainz und Discogs …"
    return "⏳ startet …"


def phase_cards(s: dict):
    cols = st.columns(4)
    now = time.time()
    for col, (key, title, sub) in zip(cols, PHASES):
        ph = s["phases"].get(key, {})
        if key == "fast":
            if s.get("fast_enabled") is False:
                txt = "aus"
            elif not ph:
                txt = "wartet"
            elif not ph.get("end"):
                txt = f"🔄 läuft · {_ago(now - ph['start'])}"
            elif ph.get("ok"):
                txt = f"✓ gelöst ohne Agent · {_ago(ph['end'] - ph['start'])}"
            else:
                txt = "→ nicht eindeutig, an Agent"
            sub_txt = sub if not ph.get("info") or ph.get("ok") else (ph["info"].get("msg") or "").replace("→ no fast path: ", "")
        elif key == "agent":
            sub_txt = s.get("model") or ""
            fast = s["phases"].get("fast", {})
            if fast.get("ok"):
                txt = "nicht nötig"
            elif not ph:
                txt = "wartet"
            elif not ph.get("end"):
                n_tools = sum(1 for x in s["timeline"] if x[1] not in ("💬", "▶", "⚡", "📝"))
                txt = f"🔄 arbeitet · {_ago(now - ph['start'])} · {n_tools} Tools · {s['steps']} Schritte"
            else:
                txt = f"✓ fertig · {_ago(ph['end'] - ph['start'])} · {ph.get('info', {}).get('tool_calls', '?')} Tools"
        elif key == "judge":
            sub_txt = s.get("judge_model") or ""
            if s.get("judge_enabled") is False:
                txt = "aus"
            elif not ph:
                txt = "wartet"
            elif not ph.get("end"):
                txt = f"🔄 prüft · {_ago(now - ph['start'])}"
            else:
                i = ph.get("info", {})
                txt = (f"{LEVEL.get(i.get('level'), '–')} ({i.get('overall')}) · {_ago(ph['end'] - ph['start'])}"
                       if i.get("ok") else f"❌ {i.get('error') or 'Fehler'}")
        else:
            d = s.get("done")
            sub_txt = ""
            if d:
                txt = f"✓ {d.get('status')} · {d.get('tracks')} Tracks · ${d.get('cost_usd') or 0:.3f}"
                sub_txt = f"gesamt {_ago(d.get('wall_s', 0) + d.get('judge_s', 0))}"
            else:
                txt = f"läuft seit {_ago(now - (s['start'] or now))}" if s["start"] else "–"
        active = s.get("current") == key
        with col.container(border=True):
            st.markdown(f"**{title}**" + (" ⟵ aktiv" if active else ""))
            st.markdown(txt)
            if sub_txt:
                st.caption(sub_txt[:160])


def render(out: Path, cid: str, max_lines: int = 30):
    s = state(out, cid)
    if not s["events"]:
        st.info("Noch keine Live-Daten für diesen Lauf.")
        return s
    inp = s.get("input") or {}
    st.markdown(f"**{cid}** · " + " · ".join(f"{k}={v}" for k, v in inp.items()))
    phase_cards(s)
    st.markdown("**Gerade:** " + activity(s))
    t0 = s["start"] or 0
    lines = []
    for ts, icon, actor, text, extra in s["timeline"][-max_lines:]:
        rel = f"+{int(ts - t0)}s" if ts and t0 else ""
        if icon == "💬":
            lines.append(f"`{rel:>6}` {icon} *{text}*")
        else:
            lines.append(f"`{rel:>6}` {icon} **{actor}** · {text}" + (f" · {extra}" if extra else ""))
    for r in s["running"]:
        icon, name = TOOLS.get(r.get("tool"), ("🔧", r.get("tool")))
        lines.append(f"`{'jetzt':>6}` {icon} **{name}** · `{r.get('tool')} {r.get('args', '')[:120]}` · 🔄 läuft")
    hidden = len(s["timeline"]) - max_lines
    with st.container(border=True):
        if hidden > 0:
            st.caption(f"… {hidden} frühere Ereignisse")
        st.markdown("  \n".join(lines) or "–")
    return s


def runs(out: Path, minutes: int = 120) -> list[tuple[str, dict]]:
    """Läufe mit Live-Daten der letzten <minutes> Minuten, aktive zuerst."""
    now = time.time()
    res = []
    for f in out.glob("*.events.jsonl"):
        if now - f.stat().st_mtime > minutes * 60:
            continue
        cid = f.name[: -len(".events.jsonl")]
        res.append((cid, state(out, cid)))
    res.sort(key=lambda x: (x[1]["done"] is not None, -(x[1]["last_activity"] or 0)))
    return res
