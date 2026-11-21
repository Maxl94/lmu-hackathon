# Tracklist Finder – GEMA hackathon prototype

Given partial metadata for a physical release (barcode, title, artist – any of them may be missing or wrong), the prototype finds the **correct edition** and returns its tracklist with **performing artists**, disc/side positions, durations, credits (composer, lyricist, producer) and ISRCs. Every value carries its source. A traffic light says whether the result can be taken over or needs a human look, and why.

Design goal: **research must cost less than the royalties it unlocks.** An obscure demo tape in 50 copies earns almost nothing, so the research for it has to cost cents, not a person's research time.

## Results on the 25 development records

All 25 records of the workshop dataset (`data/development.csv` in the workshop repository; copy here: `data/gema-sample.csv`) ran automatically; nothing in the results was edited by hand. Final outputs are in [`results/`](results/).

| Outcome | Count | Meaning |
|---|---|---|
| ✅ Supported match | **15** | traffic light green – edition, tracklist and sources hold up (9 of them with a "check durations" hint) |
| 🔎 Needs review | **10** | 8 yellow (quick check), 2 red (manual research) – each with the reason |
| ❌ No match | 0 | |
| ⚠️ Technical failure | 0 | |

- **Cost:** $0.58 for all 25, Ø 2.3 cents per record (agent, image reading and judge; databases and search are free). 3 records went through the fast path without the research agent (only the judge: 0.14 cents).
- **Credits:** 238 of 357 tracks (67 %), on 19 of 25 releases – from open sources only.
- **Showcase cases:** Die Fantastischen Vier – *Long Player (RSD)* (barcode, 6 competing editions → RSD 2×LP 2025, green) · Paula Linke (no barcode → CD rather than the digital album, green) · Tindersticks (barcode "0" → 7" single, 500 copies, yellow) · *Schlager Arena 2025* (2×CD sampler, 40 tracks, 43 artists, yellow) · *Jackfruit Traxx 1* (title is the label name → *Traxx Salad Vol. 1*, but Vol. 2 exists too → red).
- **Fresh cases** (not in the 25, not prepared): Peter Fox – *Love Songs* without barcode → green, 11 tracks, 3 guests, credits 11/11, 1.1 cents · Kenshi Yonezu – *STRAY SHEEP* / *BOOTLEG* without barcode → yellow (4–5 physical editions each, tracklist confirmed) · Bushido – *Demotape* (self-released cassette 1999) → found, 15 tracks, 6 guests, but red: competing database entry, duration conflicts.

### How far can the results be trusted?

| Check | Result | Where |
|---|---|---|
| Judge model vs. strongest model (Claude Opus) | Haiku judge sets the same traffic light in 94 % of cases, never a false green | `eval/judge-ladder-v3.md` |
| Cheap agent vs. expensive agent (Gemini 4) on 12 releases | same edition 12/12, 25× cheaper ($0.19 vs. $4.87) | `eval/compare-expensive-vs-cheap.md` |
| Traps: wrong EAN, invented album, artist mismatch, wrong format | 4 of 4 red | `data/traps.csv` |
| Image reading (back covers), 67 images | Gemini 3.8 Flash: barcode 93 %, durations 100 %, 0.28 cents per image | `eval/vision-ladder.md` |

There is **no verified ground truth** for the 25 records. The next step would be a sample check against GEMA's own work data.

## How it works

```
input ──► 1 fast path ──► 2 research agent ──► 3 credits + ISRC ──► 4 independent judge ──► traffic light
          code only        cheap LLM + tools    code only            LLM rubric + code gates
```

1. **Fast path (no LLM).** If the barcode hits exactly one physical release and MusicBrainz and Discogs agree on titles and durations, the result is written directly (`src/tracklist/fasttrack.py`).
2. **Research agent.** An [opencode](https://opencode.ai) agent (`prompts/agent.md`, `.opencode/`) with a cheap model (DeepSeek v4.1 Flash via OpenRouter, ~2 cents per case) picks its own tools. It escalates to Gemini 4 only if there is no valid result. The tools are small CLI programs in `bin/tl-*`:

   | Tool | Purpose |
   |---|---|
   | `tl-gtin` | barcode check digit, EAN-13 ↔ UPC-A variants |
   | `tl-mb` | MusicBrainz: search, release, **all releases of a release group** |
   | `tl-discogs` | Discogs: search, release (notes explain editions), **all versions of a master** |
   | `tl-itunes`, `tl-deezer` | digital catalogues – evidence only, physical wins |
   | `tl-lastfm` | community cross-check |
   | `tl-caa` + `tl-vision` | cover images; a vision model reads printed tracklists (max 3 images per case) |
   | `tl-search` | web search (Brave) |
   | `tl-scrape` | read shop/collector pages: HTTP → Firecrawl → real browser (Selenium) for blocked pages |
   | `tl-validate` | checks the output contract; the agent must fix what fails |

   Rules for the agent: physical before digital, every value with a source, missing values marked as missing, use only the input fields.
3. **Credits + ISRC (no LLM, `src/tracklist/credits.py`).** Credits belong to the *work*, not the edition: MusicBrainz recording → work relations (composer, lyricist, writer, arranger) and recording-level producers, Discogs track and release credits, Genius writers/producers. ISRCs from MusicBrainz. Also a safety net for featured artists.
4. **Independent judge (`src/tracklist/scoring.py`, `prompts/judge.md`, `prompts/rubric.toml`).** A second model (Claude Haiku, 0.4 cents) that did not do the research rates edition, tracklist and sources on a 1–5 rubric, writing the check for each level before the rating. Code computes the facts (barcode match, format match, duration coverage, source families) and hard gates: wrong barcode, wrong format, digital instead of physical, uncertain edition or tracklist → never green. Durations and credits are shown as extra badges and do not block green.

Output contract: `src/tracklist/schema.py` (pydantic). Each result has `release`, `tracks[]` (position, disc, title, artists, duration, ISRC, credits, sources), `artists[]` with role and track positions, `alternatives[]` (other editions and why not), `sources[]`, `missing[]`, `conflicts[]`, `status`.

## Processing 1,000 records

| Item | Per 1,000 | Basis |
|---|---|---|
| AI and APIs | ~$23 | measured: Ø 2.3 cents over 25 |
| Databases, search | $0 | MusicBrainz, Discogs free; search within free tier |
| Runtime | ~4–7 h | Ø 2–4 min per record, 10 in parallel; bottleneck MusicBrainz 1 req/s (database dumps would remove it) |
| Human review | ~39–59 h | **assumption:** 32 % yellow × 5 min + 8 % red × 5–20 min + 36 % "check durations" × 1 min = 2.4–3.6 min per record |

**How long manual research takes is an assumption – we did not measure it.** Scenarios for 1,000 records:

| Manual research per record | Fully manual | With the prototype (review only) | Saved |
|---|---|---|---|
| 5 min | ~83 h | ~39–59 h | ~29–53 % |
| 10 min | ~167 h | ~39–59 h | ~64–76 % |
| 20 min | ~333 h | ~39–59 h | ~82–88 % |

Break-even: the prototype saves time as long as manual research takes longer than about 2.4–3.6 minutes per record on average.

## Running it

Requirements: Python ≥ 3.12 with [uv](https://docs.astral.sh/uv/), [opencode](https://opencode.ai) ≥ 2.3, and API keys in `.env` (see `.env.example`; never commit `.env`).

```bash
uv sync
cp .env.example .env               # fill in the keys you have

# browse the committed final run without re-running anything
TL_OUT_DIR=results uv run streamlit run ui/app.py
# several records at once: UI → 🔍 Neue Recherche → CSV-Import (runs in the background, progress under 🛰️ Live)

# run records
bin/tl-mb search --barcode 4019593960000                       # single tool
uv run python runner/run.py --csv data/gema-sample.csv --parallel 3
uv run python runner/run.py --title "Love Songs" --artist "Peter Fox" --format CD --id my-case
uv run python runner/score.py output/*.json                     # re-judge existing results
uv run python ui/smoke_test.py                                  # render every page and result
```

Keys: `OPENROUTER_API_KEY` (agent; the OpenRouter provider must be available in opencode), `ANTHROPIC_API_KEY` (judge), `GEMA_GEMINI_API_KEY` (image reading, escalation; the `gema` provider in `opencode.jsonc`), `BRAVE_SEARCH_API_KEY` (web search). Optional: `DISCOGS_USER_TOKEN`, `GENIUS_ACCESS_TOKEN` (credits), `LASTFM_API_KEY`, `FIRECRAWL_API_KEY`.

## Repository layout

| Path | Content |
|---|---|
| `prompts/` | all LLM prompts and the judge rubric (English) |
| `.opencode/` | agent definition and skills (edition disambiguation, deep sources, cover reading) |
| `bin/tl-*`, `src/tracklist/cli/` | agent tools |
| `src/tracklist/` | HTTP cache and rate limits, schema, fast path, credits, scoring, LLM wrapper, cost tracking |
| `runner/` | batch runner, re-scoring, trace rendering |
| `ui/` | Streamlit interface (German labels): overview, new research, live view, results, costs, evaluation |
| `data/` | development records, traps, reference |
| `results/` | final run: per record `.json`, `.score.json`, `.trace.md` (agent trace), `.events.jsonl`, `.usage.jsonl`; `runs.jsonl` summary. Local paths and e-mail addresses from scraped pages are redacted. |
| `eval/` | judge, model and vision comparisons |
| `examples/` | early examples from 19 Nov (older output format without artist list; agent traces omitted because they contain scraped third-party contact data) |
| `DOKU.md`, `AGENTS.md` | running notes and learnings, developer guide (German) |

## Limitations

- No verified ground truth for the 25 records; trust rests on sources, the judge and the traps.
- Credits come from community databases: a starting point for matching against GEMA's work data, not a legal basis. A third of the tracks have none.
- Vinyl releases often have no published durations of their own; durations are then taken from another edition and flagged.
- Some sites block automated access; the agent falls back to other sources and says so.
- Run-to-run variance of the agent was not measured systematically.
- **The judge varies on borderline cases.** *Jackfruit Traxx 1* led to the same edition in two runs (*Traxx Salad Vol. 1*, JFXX1, same four tracks), but the judge rated the edition 2 (red) once and 4 (green) the other time – once "Vol. 2 exists, weak signals", once "the 1 in the input rules out Vol. 2". Both readings are defensible; the honest light would be yellow (title does not match literally, Discogs is the only database, no primary source). A deterministic rule such as "no barcode and the title does not match the input → at most yellow" would take such cases out of the model's hands; it is not implemented.
- Depends on external services (MusicBrainz, Discogs, model APIs) and their rate limits.
