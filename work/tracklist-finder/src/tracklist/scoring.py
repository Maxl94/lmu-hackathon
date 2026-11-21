"""Bewertung eines Ergebnisses: Regelkatalog (Stufen 1–5 mit festen Ankern) + deterministische Fakten → Ampel.

- **Code** berechnet, was zählbar ist: Barcode-/Format-/Interpret-Abgleich, Dauer-Abdeckung, Quellen-Familien,
  Validierung. Die Kategorie „Dauern“ wird nur von Code bewertet.
- **Prüfmodell** (eigener Aufruf, frischer Kontext, andere Modellfamilie als der Rechercheur) bewertet
  edition, tracklist, sources – nur anhand der Belege (Tool-Ausgaben). Pro Kategorie: check (Stufen 5 → 1 abhaken)
  → rating → summary. Prompt: prompts/judge.md, Katalog: prompts/rubric.toml.
- **Gesamt:** gewichtetes Mittel, aber K.-o.-Regeln (z. B. Ausgabe ≤ 2 → rot). Drei Stufen für die Sachbearbeitung:
  grün = übernehmen · gelb = kurz prüfen · rot = manuell klären.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, create_model
from rapidfuzz import fuzz

from tracklist import prompts
from tracklist.common import env

RUBRIC: dict[str, dict] = prompts.rubric()          # edition, tracklist, durations, sources (prompts/rubric.toml)
WEIGHTS = {k: v["weight"] for k, v in RUBRIC.items()}
JUDGED = [k for k, v in RUBRIC.items() if v["by"] == "judge"]
LEVELS = {"grün": "übernehmen", "gelb": "kurz prüfen", "rot": "manuell klären"}


# ------------------------------------------------------------------ deterministische Fakten

def digits(s) -> str:
    return re.sub(r"\D", "", str(s or ""))


def check_digit(body: str) -> int:
    s = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(body)))
    return (10 - s % 10) % 10


def norm_format(s: str | None) -> str | None:
    s = (s or "").lower().strip()
    if not s:
        return None
    if re.search(r"kassette|cassette|\bmc\b|tape", s):
        return "Kassette"
    if re.search(r"vinyl|\blp\b|\d+\s*[\"″]|schallplatte|single 7", s):
        return "Vinyl"
    if re.search(r"\bcd\b|cd-|-cd|compact disc|sacd|shm", s):
        return "CD"
    if re.search(r"digital|file|stream|download", s):
        return "Digital"
    return "Sonstiges"


def family(src_id: str) -> str:
    """Quellen-Familie: musicbrainz, discogs, image, oder Domain bei web:…-Quellen."""
    kind, _, rest = src_id.partition(":")
    if kind in ("web", "shop", "collector", "other") and "://" in rest:
        m = re.search(r"https?://(?:www\.)?([^/]+)", rest)
        return m.group(1) if m else kind
    return kind


def _sim(a: str | None, b: str | None) -> int | None:
    if not a or not b:
        return None
    n = lambda x: re.sub(r"[^a-z0-9äöüß ]+", " ", x.lower())  # noqa: E731
    return int(fuzz.token_set_ratio(n(a), n(b)))


def facts(res: dict, validation: tuple[list[str], list[str]] | None = None) -> dict:
    inp = res.get("input") or {}
    rel = res.get("release") or {}
    tracks = res.get("tracks") or []
    f: dict = {"status": res.get("status"), "tracks": len(tracks),
               "input_fields": [k for k in ("title", "artist", "ean", "format") if inp.get(k)],
               "input_has_barcode": bool(digits(inp.get("ean")))}
    # Barcode
    e = digits(inp.get("ean"))
    if e:
        valid = len(e) in (8, 12, 13, 14) and check_digit(e[:-1]) == int(e[-1])
        f["ean_checksum_ok"] = valid
        rb = digits(rel.get("barcode"))
        if rb:
            corrected = e[:-1] + str(check_digit(e[:-1])) if len(e) > 1 else e
            if rb.lstrip("0") == e.lstrip("0"):
                f["barcode_match"] = "exact"
            elif not valid and rb.lstrip("0") == corrected.lstrip("0"):
                f["barcode_match"] = "after check-digit correction"
            else:
                f["barcode_match"] = f"NO (input {e}, result {rb})"
        else:
            f["barcode_match"] = "result has no barcode"
    # Format / Interpret / Titel
    fi, fr = norm_format(inp.get("format")), norm_format(rel.get("format"))
    f["release_format"] = fr
    if fi:
        f["format_match"] = None if not fr else fi == fr
    if inp.get("artist"):
        f["artist_similarity"] = _sim(inp.get("artist"), rel.get("artist"))
    if inp.get("title"):
        f["title_similarity"] = _sim(inp.get("title"), rel.get("title"))
    # Dauern
    n = len(tracks) or 1
    with_d = [t for t in tracks if t.get("duration_s") is not None]
    confirmed = [t for t in with_d if len({family(s) for s in t.get("duration_sources") or []}) >= 2
                 and not ({"duration_conflict", "duration_other_edition"} & set(t.get("flags") or []))]
    f["dur_other_edition"] = sum("duration_other_edition" in (t.get("flags") or []) for t in tracks)
    f["dur_share"] = round(len(with_d) / n, 3)
    f["dur_confirmed_share"] = round(len(confirmed) / n, 3)
    f["dur_conflicts"] = sum("duration_conflict" in (t.get("flags") or []) for t in tracks)
    # Quellen
    fams = sorted({family(s.get("id", "")) for s in res.get("sources") or []})
    f["source_families"] = fams
    f["source_kinds"] = sorted({s.get("kind") for s in res.get("sources") or [] if s.get("kind")})
    f["conflicts"] = len(res.get("conflicts") or [])
    f["alternatives"] = len(res.get("alternatives") or [])
    f["agent_confidence"] = res.get("confidence")
    if validation is not None:
        f["validation_errors"], f["validation_warnings"] = validation[0][:5], validation[1][:5]
    return f


def duration_rating(f: dict) -> tuple[int, str]:
    share, conf = f["dur_share"], f["dur_confirmed_share"]
    txt = f"{share:.0%} of tracks have a duration, {conf:.0%} confirmed by >= 2 sources, {f['dur_conflicts']} conflicts"
    if f["tracks"] == 0:
        return 1, "no tracks"
    if conf >= 0.9:
        return 5, txt
    if conf >= 0.6 and share >= 0.9:
        return 4, txt
    if share >= 0.9:
        return 3, txt
    if share >= 0.5:
        return 2, txt
    return 1, txt


# ------------------------------------------------------------------ Prüfmodell

def _levels_text(key: str) -> str:
    return "\n".join(f"{n}: {t}" for n, t in sorted(RUBRIC[key]["levels"].items(), reverse=True))


def _rating_model(key: str):
    """Antwortschema pro Kategorie: erst Prüfung Stufe für Stufe, dann die Stufe, dann ein Satz. Bedingungen direkt am Feld."""
    r = RUBRIC[key]
    return create_model(
        f"{key.title()}Rating",
        check=(str, Field(description=f"Question: {r['question']} Go through the levels from 5 down to 1. For each level state "
                                      f"per condition MET or NOT MET with evidence (source IDs/tool calls). Stop at the first "
                                      f"level whose conditions are ALL met.\nLevels:\n{_levels_text(key)}")),
        rating=(Literal[1, 2, 3, 4, 5], Field(description="exactly the level at which your check stopped")),
        summary=(str, Field(description="one sentence: the decisive reason for this rating")),
        evidence=(list[str], Field(default_factory=list, description="source IDs or tool calls the check relies on")),
    )


JudgeOut = create_model(
    "JudgeOut",
    **{k: (_rating_model(k), ...) for k in JUDGED},
    concerns=(list[str], Field(default_factory=list, description="concrete problems: unsupported claims, contradictions with "
                                                                  "the input, errors in the result (with positions/source IDs)")),
)


def rubric_text() -> str:
    out = []
    for k in JUDGED:
        out.append(f"### {k} - {RUBRIC[k]['question']}")
        out += [f"- {n}: {t}" for n, t in sorted(RUBRIC[k]["levels"].items(), reverse=True)]
    return "\n".join(out)


JUDGE_SYSTEM = prompts.render("judge.md", rubric=rubric_text())


def compact_result(res: dict) -> str:
    r = {k: v for k, v in res.items() if k != "tracks"}
    lines = [json.dumps(r, ensure_ascii=False)[:12000], "", "Tracks (disc | pos | title | artist | duration_s | sources | duration_sources | flags):"]
    for t in res.get("tracks") or []:
        lines.append(f"{t.get('disc', 1)} | {t.get('position')} | {t.get('title')} | {t.get('artist') or ''} | {t.get('duration_s')} | "
                     f"{','.join(t.get('sources') or [])} | {','.join(t.get('duration_sources') or [])} | {','.join(t.get('flags') or [])}")
    return "\n".join(lines)


def evidence_from_trace(trace: Path | None, max_chars: int = 60000, per_step: int = 1800) -> str:
    """Tool-Aufrufe + Ausgaben aus dem opencode-Trace (jsonl) oder dem gerenderten trace.md."""
    if not trace or not trace.exists():
        return "(no evidence available)"
    if trace.suffix == ".md":
        lines = trace.read_text(errors="replace").splitlines()
        return "\n".join(x for x in lines if not x.startswith(("# Agent-Trace", "# Schnellweg")))[:max_chars]
    out, total = [], 0
    for line in trace.read_text(errors="replace").splitlines():
        if not line.startswith("{"):
            continue
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if e.get("type") != "tool_use":
            continue
        st = (e.get("part") or {}).get("state") or {}
        inp = st.get("input") or {}
        cmd = inp.get("command") or json.dumps(inp, ensure_ascii=False)[:300]
        if "tl-validate" in cmd or (e.get("part") or {}).get("tool") in ("write", "edit", "read", "skill"):
            continue
        o = (st.get("output") or "").strip()
        block = f"$ {cmd[:400]}\n{o[:per_step]}" + (f"\n… [{len(o) - per_step} chars truncated]" if len(o) > per_step else "")
        if total + len(block) > max_chars:
            out.append("… [further tool calls truncated]")
            break
        out.append(block)
        total += len(block)
    return "\n\n".join(out) or "(no tool calls)"


JUDGE_MODEL_DEFAULT = "claude-haiku-5-5"  # billigster Prüfer ohne Qualitätsverlust: 0,4 ct, 94 % wie Opus, kein falsches Grün (eval/judge-ladder-v3.md)


def judge(res: dict, f: dict, evidence: str) -> tuple[BaseModel | None, dict]:
    from tracklist import llm
    model = env("JUDGE_MODEL") or JUDGE_MODEL_DEFAULT
    # Fall-ID nie zeigen (kann Hinweise enthalten, z. B. „trap-…“)
    res = dict(res, input={k: v for k, v in (res.get("input") or {}).items() if k != "id"})
    user = (f"INPUT:\n{json.dumps(res.get('input') or {}, ensure_ascii=False)}\n\n"
            f"FACTS (code):\n{json.dumps(f, ensure_ascii=False)}\n\n"
            f"RESULT OF THE AGENT:\n{compact_result(res)}\n\n"
            f"EVIDENCE (tool calls of the research):\n{evidence}")
    return llm.structured(model, JUDGE_SYSTEM, [llm.text(user)], JudgeOut, tool="judge")


# ------------------------------------------------------------------ Gesamt

def aggregate(cats: dict[str, dict], f: dict) -> dict:
    s = {k: cats[k]["rating"] for k in WEIGHTS}
    overall = round(sum(WEIGHTS[k] * s[k] for k in WEIGHTS), 2)
    gates = []
    if f.get("status") == "not_found":
        gates.append("not found")
    if f.get("validation_errors"):
        gates.append("result violates the output contract")
    if s["edition"] <= 2:
        gates.append(f"edition only level {s['edition']} - correct edition not secured")
    if s["tracklist"] <= 2:
        gates.append(f"tracklist only level {s['tracklist']}")
    if str(f.get("barcode_match", "")).startswith("NO"):
        gates.append("barcode in the result does not match the input")
    if f.get("format_match") is False:
        gates.append("format in the result does not match the input")
    if f.get("release_format") == "Digital":
        gates.append("digital edition chosen - a physical carrier is expected")
    if gates:
        level = "rot"
    elif overall >= 4.0 and s["edition"] >= 4 and s["tracklist"] >= 4 and f.get("status") == "found":
        level = "grün"
    else:
        level = "gelb"
        if f.get("status") == "ambiguous":
            gates.append("ambiguous: confirm the chosen edition")
    # Zusatzangaben (GEMA-README: „optional bonus“): Dauern und Credits ändern die Ampel nicht, eigene Abzeichen
    d = s["durations"]
    dur_state = "ok" if d >= 4 else ("partial" if d == 3 else "missing")
    label = LEVELS[level] + (" · Dauern prüfen" if level == "grün" and dur_state != "ok" else "")
    return {"overall": overall, "level": level, "label": label, "gates": gates,
            "bonus": {"durations": dur_state, "durations_rating": d}}


def score(res: dict, evidence: str, validation=None, use_judge: bool = True, mode: str = "agent") -> dict:
    f = facts(res, validation)
    d, dtxt = duration_rating(f)
    cats: dict[str, dict] = {"durations": {"rating": d, "check": dtxt, "summary": dtxt, "evidence": [], "by": "code"}}
    meta: dict = {}
    concerns: list[str] = []
    if res.get("status") == "not_found" or not res.get("tracks"):
        for k in JUDGED:
            cats[k] = {"rating": 1, "check": "not found - nothing to rate", "summary": "not found", "evidence": [], "by": "code"}
    elif use_judge:
        out, meta = judge(res, f, evidence)
        if out is None:
            raise RuntimeError(f"judge refused: {meta}")
        for k in JUDGED:
            r = getattr(out, k)
            cats[k] = {"rating": r.rating, "check": r.check, "summary": r.summary, "evidence": r.evidence, "by": "judge"}
        concerns = out.concerns
        # Regeln, die Code sicher weiß, gehen vor: ohne Barcode in der Eingabe ist Ausgabe-Stufe 5 unmöglich
        if not f["input_has_barcode"] and cats["edition"]["rating"] > 4:
            cats["edition"].update(rating=4, capped="code: input has no barcode -> max level 4",
                                   summary=cats["edition"]["summary"] + " [capped to 4 by code: input has no barcode]")
    else:
        raise RuntimeError("no judge - edition/tracklist/sources cannot be rated")
    agg = aggregate(cats, f)
    agg["bonus"]["credits"] = {"tracks": sum(1 for t in res.get("tracks") or [] if t.get("credits")),
                               "of": len(res.get("tracks") or [])}
    return {"version": 2, "mode": mode, "scored_at": time.strftime("%Y-%m-%dT%H:%M:%S"), **agg,
            "categories": {k: cats[k] for k in WEIGHTS}, "concerns": concerns, "facts": f, "judge": meta, "weights": WEIGHTS}


_V1_KEYS = {"ausgabe": "edition", "trackliste": "tracklist", "dauern": "durations", "quellen": "sources"}


def upgrade_score(sc: dict) -> dict:
    """Bewertungen im alten Format (v1, deutsche Schlüssel) ins aktuelle Format bringen."""
    if sc.get("version", 1) >= 2:
        return sc
    cats = {_V1_KEYS[k]: {"rating": v["stufe"], "check": v.get("begruendung", ""), "summary": v.get("begruendung", ""),
                          "evidence": v.get("belege", []), "by": "judge" if v.get("by") == "Prüfmodell" else "code"}
            for k, v in sc["categories"].items()}
    return dict(sc, version=2, categories=cats, concerns=sc.get("bedenken", []))


def score_file(result_path: Path, trace: Path | None = None, mode: str = "agent", evidence: str | None = None,
               out_path: Path | None = None) -> dict:
    from tracklist.cli.validate import check
    res = json.loads(result_path.read_text())
    errors, warns, _ = check(str(result_path))
    ev = evidence if evidence is not None else evidence_from_trace(trace)
    sc = score(res, ev, (errors, warns), mode=mode)
    (out_path or result_path.with_name(result_path.stem + ".score.json")).write_text(json.dumps(sc, ensure_ascii=False, indent=1))
    return sc
