"""tl-vision <image-url-or-path> [--context "Bushido – King of Kingz, CD 2004"] [--json] — read a tracklist from an image.

For back covers, booklets, inlays, labels, shop/eBay photos, screenshots (tl-scrape --screenshot).
Reads with a vision model (TL_VISION_MODEL, default gemini-3.8-flash; max 3 images per case) exactly what is printed – invents nothing,
marks illegible entries. Output: title/label/cat. no./barcode + tracks with position and duration (if printed).
Source ID: image:<url> (or image:<path>)
"""
from __future__ import annotations

import argparse
import io
import json
from pathlib import Path

from PIL import Image
from pydantic import BaseModel, Field

from tracklist import llm, prompts
from tracklist.common import ToolError, env, fetch_bytes, run_cli

MAX_SIDE = 2000


class VisionTrack(BaseModel):
    position: str = Field(description="as printed, e.g. '1', 'A1', '2-03'; empty if not printed")
    title: str
    artist: str | None = None
    duration: str | None = Field(default=None, description="as printed, e.g. '4:35'; null if not printed")
    uncertain: bool = Field(default=False, description="true if hard to read")


class CoverReading(BaseModel):
    image_kind: str = Field(description="e.g. back cover, booklet, tray inlay, cassette j-card, label, shop photo, screenshot, other")
    readable: bool
    release_title: str | None = None
    artist: str | None = None
    label: str | None = None
    catalog_number: str | None = None
    barcode: str | None = None
    format_hints: str | None = Field(default=None, description="e.g. 'CD', 'MC side A/B', 'LP', 'Bonus Track'")
    tracks: list[VisionTrack] = Field(default_factory=list)
    notes: str | None = Field(default=None, description="notable points: bonus tracks, hidden tracks, deviating order, illegible parts")


PROMPT = prompts.text("vision.md").strip()  # prompts/vision.md


def load_image(src: str) -> tuple[bytes, str]:
    if src.startswith(("http://", "https://")):
        data, ctype = fetch_bytes(src)
    else:
        p = Path(src)
        if not p.exists():
            raise ToolError(f"file not found: {src}")
        data, ctype = p.read_bytes(), "image/" + (p.suffix.lstrip(".").lower().replace("jpg", "jpeg") or "png")
    img = Image.open(io.BytesIO(data))
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    if max(img.size) > MAX_SIDE or len(data) > 4_500_000 or ctype not in ("image/jpeg", "image/png", "image/webp", "image/gif"):
        img.thumbnail((MAX_SIDE, MAX_SIDE))
        buf = io.BytesIO()
        img.convert("RGB").save(buf, "JPEG", quality=88)
        return buf.getvalue(), "image/jpeg"
    return data, ctype


VISION_MODEL_DEFAULT = "gemini-3.8-flash@low"  # 0,28 ct/Bild, wenig Denken: halb so teuer, gleiche Qualität (eval/vision-ladder.md)
VISION_MAX = 3  # Bilder pro Fall (TL_VISION_MAX) – Kosten deckeln; die Rückseite mit Barcode reicht als Beweis


def read_cover(src: str, context: str | None, model: str | None = None) -> tuple[CoverReading | None, str]:
    """Bild → CoverReading. Modell: TL_VISION_MODEL (gemini-* über die Gemini API, claude-* über Anthropic)."""
    log = env("TL_USAGE_LOG")
    limit = int(env("TL_VISION_MAX") or VISION_MAX)
    if log and Path(log).exists() and sum('"tl-vision"' in x for x in Path(log).read_text().splitlines()) >= limit:
        raise ToolError(f"image budget for this case used up ({limit} images) – rely on the sources already read")
    data, media = load_image(src)
    model = model or env("TL_VISION_MODEL") or VISION_MODEL_DEFAULT
    prompt = PROMPT + (f"\n\nContext (orientation only, do not copy): {context}" if context else "")
    reading, meta = llm.structured(model, None, [llm.image(data, media), llm.text(prompt)], CoverReading,
                                   tool="tl-vision", image=src[:200])
    if reading is None:
        return None, f"no reading ({meta['stop_reason']})"
    return reading, f"{meta['model']}, in {meta['tokens_in']} / out {meta['tokens_out']} tokens, {meta['seconds']} s"


def main():
    p = argparse.ArgumentParser(prog="tl-vision", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("image")
    p.add_argument("--context")
    p.add_argument("--json", action="store_true", help="print raw JSON")
    a = p.parse_args()
    reading, info = read_cover(a.image, a.context)
    print(f"source-id: image:{a.image}\nmodel: {info}")
    if reading is None:
        print("ERROR: model refused")
        return
    if a.json:
        print(json.dumps(reading.model_dump(), ensure_ascii=False, indent=1))
        return
    r = reading
    print(f"kind: {r.image_kind} | readable: {r.readable}")
    for k in ("release_title", "artist", "label", "catalog_number", "barcode", "format_hints"):
        v = getattr(r, k)
        if v:
            print(f"{k}: {v}")
    for t in r.tracks:
        print(f"{t.position or '-'} {t.title}" + (f" — {t.artist}" if t.artist else "")
              + f" | {t.duration or 'no duration printed'}" + (" [uncertain]" if t.uncertain else ""))
    print(f"{len(r.tracks)} tracks read" + (f"\nnotes: {r.notes}" if r.notes else ""))


if __name__ == "__main__":
    run_cli(main)
