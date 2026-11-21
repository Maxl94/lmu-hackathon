"""Zentrale Prompts aus prompts/ laden (eine Quelle für alle Modell-Texte, siehe prompts/README.md).

  text("vision.md")                       Rohtext
  render("task.md", input=..., out=...)   $platzhalter ersetzen (string.Template, unbekannte bleiben stehen)
  rubric()                                Regelkatalog aus rubric.toml (Stufen als int)
"""
from __future__ import annotations

import string
import tomllib
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / "prompts"


def text(name: str) -> str:
    return (DIR / name).read_text()


def render(name: str, **kw) -> str:
    return string.Template(text(name)).safe_substitute(**kw)


def rubric() -> dict[str, dict]:
    d = tomllib.loads(text("rubric.toml"))
    for v in d.values():
        v["levels"] = {int(n): t for n, t in v["levels"].items()}
    return d
