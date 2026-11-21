"""Bildlesen-Leiter: liest dieselben Cover-/Rückseiten-Bilder mit mehreren Modellen und vergleicht mit Opus.

  uv run python eval/vision_ladder.py [--src backups/output-*/] [--models a,b,c] [--parallel 8]
  → eval/vision-ladder/<modell>/<bild>.json, Bericht eval/vision-ladder.md

Bilder: alle tl-vision-Aufrufe aus den Usage-Logs (nur http-URLs). Referenz: claude-opus-5-5.
Vergleich pro Bild: Trackanzahl gleich, Titel gleich (fuzzy ≥ 90, je Position), gedruckte Dauern gleich, Barcode gleich.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import re
import statistics as stt
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from tracklist import llm  # noqa: E402
from tracklist.usage import cost_usd  # noqa: E402
from tracklist.cli.vision import PROMPT, CoverReading, load_image  # noqa: E402

OUT = ROOT / "eval/vision-ladder"
REF = "claude-opus-5-5"
MODELS = [REF, "gemini-3.8-flash@low", "claude-sonnet-5-5", "claude-haiku-5-5", "gemini-3.1-pro-preview", "gemini-3.8-flash", "gemini-3.5-flash",
          "gemini-3.1-flash-lite", "gemini-4-neon", "gemini-4-argon", "gemini-4-hydrogen", "gemini-4-carbon"]


def key(url: str) -> str:
    return hashlib.sha1(url.encode()).hexdigest()[:12]


def read(model: str, url: str) -> str:
    p = OUT / model / f"{key(url)}.json"
    if p.exists():
        return "cached"
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        data, media = load_image(url)
        r, meta = llm.structured(model, None, [llm.image(data, media), llm.text(PROMPT)], CoverReading, tool="vision-ladder")
        p.write_text(json.dumps({"url": url, "meta": meta, "reading": r.model_dump() if r else None}, ensure_ascii=False))
        return "ok"
    except Exception as e:  # noqa: BLE001
        p.write_text(json.dumps({"url": url, "meta": {"error": f"{type(e).__name__}: {str(e)[:200]}"}, "reading": None}))
        return "error"


def n(s: str | None) -> str:
    return re.sub(r"[^a-z0-9äöüß]+", " ", (s or "").lower()).strip()


def dur(s: str | None) -> str:
    return re.sub(r"\D", "", s or "").lstrip("0")


def compare(ref: dict, cur: dict) -> dict:
    r, c = ref.get("reading"), cur.get("reading")
    if not r or not c:
        return {"ok": False}
    rt, ct = r["tracks"], c["tracks"]
    out = {"ok": True, "readable_same": r["readable"] == c["readable"], "count_same": len(rt) == len(ct)}
    pairs = list(zip(rt, ct))
    if rt:
        out["titles"] = sum(fuzz.ratio(n(a["title"]), n(b["title"])) >= 90 for a, b in pairs) / len(rt)
        with_d = [(a, b) for a, b in pairs if a.get("duration")]
        if with_d:
            out["durations"] = sum(dur(a["duration"]) == dur(b.get("duration")) for a, b in with_d) / len(with_d)
    if r.get("barcode"):
        out["barcode"] = re.sub(r"\D", "", r["barcode"]) == re.sub(r"\D", "", c.get("barcode") or "")
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--src", default=str(ROOT / "backups/output-*"))
    p.add_argument("--models", default=",".join(MODELS))
    p.add_argument("--parallel", type=int, default=8)
    a = p.parse_args()
    urls = []
    for f in sorted(glob.glob(f"{a.src}/*.usage.jsonl")):
        for line in open(f):
            u = json.loads(line)
            if u.get("tool") == "tl-vision" and str(u.get("image", "")).startswith("http") and u["image"] not in urls:
                urls.append(u["image"])
    models = a.models.split(",")
    print(f"{len(urls)} Bilder × {len(models)} Modelle", flush=True)
    jobs = [(m, u) for m in models for u in urls]
    with ThreadPoolExecutor(max_workers=a.parallel) as ex:
        states = list(ex.map(lambda j: read(*j), jobs))
    print({s: states.count(s) for s in set(states)}, flush=True)

    ref = {key(u): json.loads((OUT / REF / f"{key(u)}.json").read_text()) for u in urls if (OUT / REF / f"{key(u)}.json").exists()}
    md = ["# Bildlesen-Leiter", "", f"{len(urls)} Bilder (Rückseiten, Cover, J-Cards, Shop-Fotos aus den heutigen Läufen). "
          f"Referenz: {REF}. Werte = Übereinstimmung mit der Referenz.", "",
          "| Modell | gelesen | Trackanzahl gleich | Titel gleich | gedruckte Dauern gleich | Barcode gleich | Ø Zeit | Ø Kosten pro Bild | Fehler |",
          "|---|---|---|---|---|---|---|---|---|"]
    pct = lambda x: f"{stt.mean(x):.0%}" if x else "–"  # noqa: E731
    for m in models:
        rows, secs, costs, errs = [], [], [], 0
        for u in urls:
            f = OUT / m / f"{key(u)}.json"
            if not f.exists():
                continue
            cur = json.loads(f.read_text())
            if cur["meta"].get("error") or not cur.get("reading"):
                errs += 1
                continue
            secs.append(cur["meta"].get("seconds") or 0)
            costs.append(cur["meta"].get("cost_usd") or cost_usd(m, {"input_tokens": cur["meta"].get("tokens_in") or 0,
                                                                     "output_tokens": cur["meta"].get("tokens_out") or 0}) or 0)
            if key(u) in ref:
                rows.append(compare(ref[key(u)], cur))
        ok = [r for r in rows if r.get("ok")]
        md.append(f"| {m} | {len(secs)}/{len(urls)} | {pct([r['count_same'] for r in ok])} | {pct([r['titles'] for r in ok if 'titles' in r])} | "
                  f"{pct([r['durations'] for r in ok if 'durations' in r])} | {pct([r['barcode'] for r in ok if 'barcode' in r])} | "
                  f"{stt.mean(secs) if secs else 0:.1f} s | ${stt.mean(costs) if costs else 0:.4f} | {errs} |")
    md += ["", "Gemini-Kosten sind Listenpreise; über den GEMA-Schlüssel bezahlt die GEMA."]
    (ROOT / "eval/vision-ladder.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
