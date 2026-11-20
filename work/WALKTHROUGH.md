# Walkthrough: Discogs Tracklist Discovery & Evaluation Pipeline

## Changes Made

### 1. Docker Compose & Environment
- **[docker-compose.yml](../docker-compose.yml)**: Orchestrates `db` (`postgres:16-alpine` with `pgdata` volume, `pg_isready` healthcheck, and `init.sql` bootstrap) and `api` (`python:3.12-slim` on port `8000`, mounting `data/` read-only and `outputs/`).
- **[.env.example](../.env.example)**: Added `DISCOGS_TOKEN`, `DISCOGS_USER_AGENT`, and `POSTGRES_*` / `API_PORT` defaults alongside existing Gemini/Vertex AI settings.

### 2. PostgreSQL Schema & Container Setup
- **[Dockerfile](pipeline/Dockerfile)** & **[requirements.txt](pipeline/requirements.txt)**: Python 3.12 container with FastAPI, Uvicorn, HTTPX, `psycopg[binary,pool]`, Pydantic Settings, and `pytest`.
- **[init.sql](pipeline/sql/init.sql)**: Idempotent 8-table schema (`input_records`, `releases`, `release_barcodes`, `tracks`, `track_credits`, `input_matches`, `lookup_runs`, `api_cache`).

### 3. Pipeline Modules & Audit Hardening (`work/pipeline/app/`)
- **[normalizer.py](pipeline/app/normalizer.py)**: Normalizes barcodes (treating `"0"` as missing and generating 12-digit UPC <-> 13-digit EAN variants), strips duplicated `;` artist prefixes (`JETHRO TULL;BALOISE SESSION(2CD)`), extracts format hints case-insensitively without tag duplication, un-inverts `"Fantastischen Vier, Die"`, maps compilation aliases to `"various"`, and computes deterministic `input_hash`.
- **[discogs_client.py](pipeline/app/discogs_client.py)**: Direct `httpx.Client` Discogs REST API v2 adapter behind a `CatalogProvider` protocol, backed by `api_cache`, `X-Discogs-Ratelimit-Remaining` pacing, bounded retries, invalid JSON guarding (`DiscogsUpstreamError`), and typed auth/rate-limit exceptions.
- **[extractor.py](pipeline/app/extractor.py)**: Extracts tracks, `"heading"` disc assignments, unpacked `"index"`/`"sub_tracks"` (merging parent and child `extraartists` and inheriting `parent_position` disc numbers), vinyl side mapping restricted to `A–L` (avoiding false disc numbers on `"V1"` video tracks), 3+ disc numeric resets, implicit disc advancement across unprefixed trailing tracks, inherited release `artists`, merged track + release `extraartists` (including en-dash/em-dash/`to`/disc-prefixed/zero-padded range parsing), separated credit categories, and `tracklist_hash`.
- **[evaluator.py](pipeline/app/evaluator.py)**: Deterministic candidate scoring, compilation & single-act barcode collision rejection, empty-tracklist rejection (`404`), cross-edition `tracklist_hash` comparison (computing `clear_winner` margin specifically against the highest-scoring diverging edition), and per-track quality metrics.
- **[repository.py](pipeline/app/repository.py)** & **[service.py](pipeline/app/service.py)**: Implements 3-layer DB deduplication, cascading Tier 1 -> Tier 2 -> Tier 3 Discogs search (automatically falling back to Tier 2/3 when Tier 1 returns only empty/rejected stubs), offline DB fallback (`source="database_fallback"`, `fallback_used=True`, preserving `candidates_checked`), and separated `upstream_error` vs. `validation_error` batch reporting.
- **[main.py](pipeline/app/main.py)** & **[cli.py](pipeline/app/cli.py)**: FastAPI endpoints (`GET /health` with graceful DB failure degradation, `POST /lookup`, `POST /batch/csv`, `GET /records`, `GET /records/{input_id}`, `GET /releases/{discogs_release_id}`, Swagger UI at `/docs`) and `python -m app.cli` (`lookup`, `batch`) with injectable `provider`.

### 4. Expanded Test Suite (`work/pipeline/tests/`)
- **[conftest.py](pipeline/tests/conftest.py)**: Shared Discogs release payload builder.
- **[test_normalizer.py](pipeline/tests/test_normalizer.py)**: Tests all 25 rows of [development.csv](../data/development.csv), barcode sanitization, UPC/EAN variants, artist un-inversion, compilation aliases, format deduplication, and `LookupRequest` validation.
- **[test_extractor.py](pipeline/tests/test_extractor.py)**: Tests multi-disc headings/prefixes/vinyl sides/3-disc numeric resets, `"V1"` handling, `sub_tracks` credit merging, duration parsing, bracket-aware multi-role splitting, range selectors (`01`, `1–2`, `2 to 3`, `1-1 - 1-2`, unscoped fallback), and artist `join`/`anv`.
- **[test_evaluator.py](pipeline/tests/test_evaluator.py)**: Tests `matched` vs. `needs_review` diverging editions, `clear_winner` margin against diverging pressings, barcode collision rejections (single-act and compilation), empty tracklist rejection, and review flags.
- **[test_discogs_client.py](pipeline/tests/test_discogs_client.py)**: Tests with `httpx.MockTransport` covering missing/placeholder token errors, mandatory `User-Agent`/`Authorization` headers, `api_cache` hit & `bypass_cache`, `429`/`5xx`/network retries, `401`, `404`, and invalid JSON.
- **[test_end_to_end.py](pipeline/tests/test_end_to_end.py)**: End-to-end PostgreSQL + FastAPI + CLI tests covering real `DiscogsClient` (`httpx.MockTransport` + PG `api_cache`), UPC<->EAN DB dedup, idempotent re-upsert, Tier 1 empty stub -> Tier 2/3 fallback, `404` TTL caching & expiry, offline DB fallback (`200` `database_fallback`) vs. `502`/`503` outages, validation errors, degraded `/health`, `/batch/csv`, and CLI exit codes (`0`/`1`/`2`).

---

## Verification Results

After rebuilding (`docker compose up -d --build api`), all checks passed cleanly:

- **`docker compose exec -T api pytest -v`**: **23 passed** (`1.05s`) across all 5 test modules.
- **`curl.exe -s http://localhost:8000/health`**: `{"status":"ok","database_ok":true,"discogs_token_configured":false}`
- **`curl.exe -s http://localhost:8000/records`**: `[]` (confirming test cleanup removed all synthetic rows cleanly).

---

## Next Steps for Live Discogs Runs

1. Create `.env` in the repository root with `DISCOGS_TOKEN="..."` (keep credentials out of Git; `.env` is already gitignored).
2. Reload the API container and run the 5-record batch test:
   ```bash
   docker compose up -d api
   docker compose exec api python -m app.cli batch --csv /app/data/development.csv --rows 1,3,7,13,16 --output /app/outputs/dev5_report.json
   ```
