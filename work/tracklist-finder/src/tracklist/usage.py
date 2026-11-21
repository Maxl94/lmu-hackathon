"""Kosten-Erfassung: jeder bezahlte Modell-Aufruf (Vision, Prüfmodell) schreibt eine Zeile nach $TL_USAGE_LOG.

Der Runner setzt TL_USAGE_LOG=output/<id>.usage.jsonl für den Agenten und summiert danach.
Preise: USD pro Million Tokens (Stand 11/2026, Anthropic-Preisliste).
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

# (input, output, cache_read, cache_write_5min)
PRICES = {
    "claude-opus-5-5": (4.0, 20.0, 0.20, 5.0),
    "claude-sonnet-5-5": (2.0, 10.0, 0.10, 2.5),
    "claude-haiku-5-5": (0.10, 0.50, 0.01, 0.125),  # bis 100K Prompt-Tokens; darüber 0.50 / 2.50
    # Gemini API (bezahlt die GEMA) – Listenpreise laut OpenRouter-Modellliste 20.11.2026; Ausgabe inkl. Denk-Tokens
    "gemini-3.8-flash": (0.825, 4.125, 0.21, 0.825),
    "gemini-3.7-flash": (0.75, 3.75, 0.19, 0.75),
    "gemini-3.6-flash": (0.75, 3.75, 0.19, 0.75),
    "gemini-3.5-flash-lite": (0.30, 2.50, 0.075, 0.30),
    "gemini-3.5-flash": (1.50, 9.00, 0.375, 1.50),
    "gemini-3.1-flash-lite": (0.25, 1.50, 0.06, 0.25),
    "gemini-3.1-pro-preview": (2.00, 12.00, 0.50, 2.00),
    "gemini-3-flash-preview": (0.50, 3.00, 0.125, 0.50),
    "gemini-2.5-flash-lite": (0.10, 0.40, 0.025, 0.10),
    "gemini-2.5-flash": (0.30, 2.50, 0.075, 0.30),
    # Gemini 4 laut Drittquellen (fourweekmba, eesel.ai, pricepertoken; Google-Preisseite nicht geprüft):
    # Argon/Carbon Einführungspreis bis 30.11.2026 (danach 4 / 20), Hydrogen unbestätigt, Neon unbekannt
    "gemini-4-argon": (2.00, 10.00, 0.50, 2.00),
    "gemini-4-carbon": (2.00, 10.00, 0.50, 2.00),
    "gemini-4-hydrogen": (1.50, 7.50, 0.375, 1.50),
}


def _price(model: str):
    """Längster passender Präfix (sonst träfe „gemini-3.5-flash“ auch „gemini-3.5-flash-lite“)."""
    model = (model or "").split("/")[-1]
    keys = [k for k in PRICES if model.startswith(k)]
    return PRICES[max(keys, key=len)] if keys else None


def cost_usd(model: str, usage) -> float | None:
    p = _price(model or "")
    if not p:
        return None
    g = (lambda k: getattr(usage, k, None) or 0) if not isinstance(usage, dict) else (lambda k: usage.get(k) or 0)
    return round((g("input_tokens") * p[0] + g("output_tokens") * p[1] + g("cache_read_input_tokens") * p[2]
                  + g("cache_creation_input_tokens") * p[3]) / 1e6, 5)


def log_usage(tool: str, model: str, usage, log: str | Path | None = None, **extra) -> dict:
    row = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "tool": tool, "model": model,
           "input_tokens": getattr(usage, "input_tokens", 0) or 0, "output_tokens": getattr(usage, "output_tokens", 0) or 0,
           "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", 0) or 0,
           "cost_usd": cost_usd(model, usage), **extra}
    path = log or os.environ.get("TL_USAGE_LOG")
    if path:
        with open(path, "a") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def read_usage(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip().startswith("{")]
