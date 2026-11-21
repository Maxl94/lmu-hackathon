"""Ein Aufruf, zwei Anbieter: strukturierte Antwort (pydantic) von Claude (Anthropic) oder Gemini (Gemini API).

  parsed, meta = structured("gemini-3.8-flash", system, [text("…"), image(bytes, "image/jpeg")], MySchema, tool="judge")

Welcher Anbieter: am Modellnamen (claude-* → Anthropic, gemini-* → Gemini API mit GEMA_GEMINI_API_KEY).
meta: model, seconds, tokens_in, tokens_out, cost_usd (Listenpreis, auch wenn die GEMA zahlt), stop_reason.
"""
from __future__ import annotations

import base64
import json
import time
from types import SimpleNamespace

import httpx
from pydantic import BaseModel

from tracklist.common import ToolError, env
from tracklist.usage import log_usage

GEMINI = "https://generativelanguage.googleapis.com/v1beta/models"
# Rückfall, wenn die Gemini API nicht kann (z. B. Ausgabenlimit des GEMA-Projekts erreicht, HTTP 429)
FALLBACK = {"judge": "claude-haiku-5-5", "tl-vision": "claude-sonnet-5-5"}


class QuotaError(ToolError):
    """Gemini-Kontingent/Ausgabenlimit erschöpft."""


def text(t: str) -> dict:
    return {"text": t}


def image(data: bytes, media_type: str) -> dict:
    return {"image": data, "media_type": media_type}


def _inline_refs(schema: dict) -> dict:
    """pydantic-Schema mit $defs/$ref → alles inline (Gemini mag keine Verweise)."""
    defs = schema.get("$defs", {})

    def walk(x):
        if isinstance(x, dict):
            if "$ref" in x:
                return walk(defs[x["$ref"].split("/")[-1]])
            # „title“ nur als Schema-Beschriftung (Text) entfernen – nicht die Eigenschaft namens „title“
            return {k: walk(v) for k, v in x.items() if k != "$defs" and not (k == "title" and isinstance(v, str))}
        if isinstance(x, list):
            return [walk(v) for v in x]
        return x
    return walk(schema)


def _claude(model, system, parts, schema, max_tokens):
    import anthropic
    content = []
    for p in parts:
        if "image" in p:
            content.append({"type": "image", "source": {"type": "base64", "media_type": p["media_type"],
                                                        "data": base64.standard_b64encode(p["image"]).decode()}})
        else:
            content.append({"type": "text", "text": p["text"]})
    kw = dict(model=model, max_tokens=max_tokens, messages=[{"role": "user", "content": content}], output_format=schema)
    if system:
        kw["system"] = system
    resp = anthropic.Anthropic().messages.parse(**kw)
    ok = resp.stop_reason != "refusal"
    return (resp.parsed_output if ok else None), resp.model, resp.usage, resp.stop_reason


def _gemini(model, system, parts, schema, max_tokens):
    # „gemini-3.8-flash@low“ → thinkingLevel low (minimal/low/medium/high); spart Denk-Tokens bei einfachen Aufgaben
    model, _, level = model.partition("@")
    key = env("GEMA_GEMINI_API_KEY") or env("GEMINI_API_KEY")
    if not key:
        raise ToolError("GEMA_GEMINI_API_KEY missing in .env")
    gparts = []
    for p in parts:
        if "image" in p:
            gparts.append({"inline_data": {"mime_type": p["media_type"], "data": base64.standard_b64encode(p["image"]).decode()}})
        else:
            gparts.append({"text": p["text"]})
    body = {"contents": [{"role": "user", "parts": gparts}],
            "generationConfig": {"responseMimeType": "application/json",
                                 "responseJsonSchema": _inline_refs(schema.model_json_schema()),
                                 "maxOutputTokens": max_tokens}}
    if level:
        body["generationConfig"]["thinkingConfig"] = {"thinkingLevel": level}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    last = None
    for attempt in range(4):
        r = httpx.post(f"{GEMINI}/{model}:generateContent", headers={"x-goog-api-key": key}, json=body, timeout=300)
        if r.status_code == 429 and ("spending cap" in r.text or "RESOURCE_EXHAUSTED" in r.text) and attempt >= 1:
            raise QuotaError(f"Gemini {model}: quota/spending cap exhausted (HTTP 429)")
        if r.status_code in (429, 500, 502, 503, 504):
            last = f"HTTP {r.status_code}: {r.text[:200]}"
            time.sleep(2 * (attempt + 1))
            continue
        if r.status_code != 200:
            raise ToolError(f"Gemini {model}: HTTP {r.status_code}: {r.text[:300]}")
        d = r.json()
        u = d.get("usageMetadata") or {}
        usage = SimpleNamespace(input_tokens=u.get("promptTokenCount") or 0,
                                output_tokens=(u.get("candidatesTokenCount") or 0) + (u.get("thoughtsTokenCount") or 0),
                                cache_read_input_tokens=u.get("cachedContentTokenCount") or 0)
        cand = (d.get("candidates") or [{}])[0]
        reason = cand.get("finishReason")
        raw = "".join(p.get("text", "") for p in (cand.get("content") or {}).get("parts", []) if not p.get("thought"))
        try:
            return schema.model_validate_json(raw), model + (f"@{level}" if level else ""), usage, reason
        except ValueError:
            return None, model + (f"@{level}" if level else ""), usage, f"{reason}: invalid JSON ({raw[:120]!r})"
    raise ToolError(f"Gemini {model}: {last}")


def structured(model: str, system: str | None, parts: list[dict], schema: type[BaseModel], tool: str,
               max_tokens: int = 16000, **log_extra) -> tuple[BaseModel | None, dict]:
    t0 = time.time()
    fallback_from = None
    try:
        call = _gemini if model.startswith("gemini") else _claude
        parsed, used_model, usage, reason = call(model, system, parts, schema, max_tokens)
    except QuotaError:
        fb = env(f"TL_FALLBACK_{tool.upper().replace('-', '_')}") or FALLBACK.get(tool)
        if not fb:
            raise
        fallback_from = model
        parsed, used_model, usage, reason = _claude(fb, system, parts, schema, max_tokens)
    secs = round(time.time() - t0, 1)
    u = log_usage(tool, used_model, usage, seconds=secs, fallback_from=fallback_from, **log_extra)
    return parsed, {"model": used_model, "seconds": secs, "tokens_in": u["input_tokens"], "tokens_out": u["output_tokens"],
                    "cost_usd": u["cost_usd"], "stop_reason": reason, "fallback_from": fallback_from}


if __name__ == "__main__":  # Rauchtest: uv run python -m tracklist.llm gemini-3.8-flash
    import sys

    class Ping(BaseModel):
        answer: str

    print(json.dumps(structured(sys.argv[1], "Answer briefly.", [text("Say OK in the field answer.")], Ping, tool="test")[1]))
