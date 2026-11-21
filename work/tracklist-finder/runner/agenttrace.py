"""Agent-Trace aus opencode-JSONL (opencode run --format json) als Markdown + Kennzahlen.

  uv run python runner/agenttrace.py output/<id>.trace.jsonl      → schreibt output/<id>.trace.md
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path


def load(path: Path) -> list[dict]:
    events = []
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
    return events


def stats(events: list[dict]) -> dict:
    tools, cmds, tok_in, tok_out, steps, final, cost, cache = [], [], 0, 0, 0, "", 0.0, 0
    for e in events:
        part = e.get("part") or {}
        if e.get("type") == "tool_use":
            st = part.get("state") or {}
            cmd = (st.get("input") or {}).get("command") or json.dumps(st.get("input") or {}, ensure_ascii=False)[:120]
            tools.append(part.get("tool"))
            cmds.append(cmd)
        elif e.get("type") == "step_finish":
            steps += 1
            t = part.get("tokens") or {}
            tok_in += t.get("input") or 0
            tok_out += (t.get("output") or 0) + (t.get("reasoning") or 0)
            cost += part.get("cost") or 0
            cache += (t.get("cache") or {}).get("read") or 0
        elif e.get("type") == "text":
            final = part.get("text") or final
    tl = [c.split()[0] for c in cmds if c and c.split()[0].startswith("tl-")]
    return {"steps": steps, "tool_calls": len(tools), "tl_calls": tl, "tokens_in": tok_in, "tokens_out": tok_out,
            "final": final.strip(), "cost_usd": round(cost, 5), "tokens_cache_read": cache}


def render(events: list[dict], title: str) -> str:
    out = [f"# Agent-Trace: {title}", ""]
    t0 = next((e.get("timestamp") for e in events if e.get("timestamp")), None)
    n = 0
    for e in events:
        part = e.get("part") or {}
        ts = e.get("timestamp")
        rel = f"+{(ts - t0) / 1000:.0f}s" if ts and t0 else ""
        if e.get("type") == "tool_use":
            n += 1
            st = part.get("state") or {}
            inp = st.get("input") or {}
            cmd = inp.get("command") or json.dumps(inp, ensure_ascii=False)
            output = (st.get("output") or "").rstrip()
            if len(output) > 2500:
                output = output[:2500] + f"\n… [{len(output) - 2500} Zeichen gekürzt]"
            out += [f"### {n}. `{part.get('tool')}` {rel} – {st.get('status')}", "", "```", cmd, "```", "",
                    "<details><summary>Ausgabe</summary>", "", "```", output, "```", "</details>", ""]
        elif e.get("type") == "text" and (part.get("text") or "").strip():
            out += [f"> **Agent** {rel}: " + part["text"].strip().replace("\n", "\n> "), ""]
    s = stats(events)
    when = datetime.fromtimestamp(t0 / 1000).isoformat(timespec="seconds") if t0 else "?"
    out[1:1] = [f"Start {when} · {s['steps']} Schritte · {s['tool_calls']} Tool-Aufrufe · "
                f"Tokens in {s['tokens_in']} / out {s['tokens_out']}", ""]
    return "\n".join(out)


def main():
    p = Path(sys.argv[1])
    events = load(p)
    md = p.with_suffix("").with_suffix(".trace.md") if p.name.endswith(".trace.jsonl") else p.with_suffix(".md")
    md.write_text(render(events, p.name.replace(".trace.jsonl", "")))
    print(md)


if __name__ == "__main__":
    main()
