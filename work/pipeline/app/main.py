from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from psycopg_pool import ConnectionPool

from app.config import Settings, get_settings
from app.discogs_client import DiscogsClient
from app.extractor import extracted_track_to_out
from app.models import (
    BatchRequest,
    BatchSummaryResponse,
    HealthResponse,
    LookupNotFoundResponse,
    LookupRequest,
    LookupSuccessResponse,
    RecordDetailOut,
    RecordSummaryOut,
    ReleaseOut,
)
from app.repository import PipelineRepository
from app.service import LookupService, UpstreamServiceError


def create_app(
    settings: Settings | None = None,
    provider: Any | None = None,
) -> FastAPI:
    cfg = settings or get_settings()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        pool = ConnectionPool(conninfo=cfg.database_url, min_size=1, max_size=10, open=True)
        repo = PipelineRepository(pool)
        repo.ensure_schema()

        client: DiscogsClient | None = None
        active_provider = provider
        if active_provider is None:
            client = DiscogsClient(cfg, cache_store=repo)
            active_provider = client

        app.state.settings = cfg
        app.state.pool = pool
        app.state.repo = repo
        app.state.service = LookupService(repo=repo, provider=active_provider, settings=cfg)
        try:
            yield
        finally:
            if client is not None:
                client.close()
            pool.close()

    app = FastAPI(
        title="Discogs Tracklist Discovery & Evaluation API",
        version="1.0.0",
        description=(
            "Discogs tracklist lookup with PostgreSQL 3-layer deduplication, "
            "per-track credit extraction, deterministic edition evaluation, and offline fallback."
        ),
        lifespan=lifespan,
    )

    @app.get("/health", response_model=HealthResponse)
    def health(request: Request) -> HealthResponse:
        repo: PipelineRepository = request.app.state.repo
        s: Settings = request.app.state.settings
        try:
            db_ok = repo.ping()
        except Exception:
            db_ok = False
        token = (s.discogs_token or "").strip()
        token_configured = bool(token and token != "PASTE_YOUR_DISCOGS_PERSONAL_ACCESS_TOKEN")
        return HealthResponse(
            status="ok" if db_ok else "degraded",
            database_ok=db_ok,
            discogs_token_configured=token_configured,
        )

    @app.post(
        "/lookup",
        response_model=LookupSuccessResponse,
        responses={
            404: {"model": LookupNotFoundResponse, "description": "Release not found or rejected"},
            502: {"description": "Upstream Discogs auth/server error with no DB fallback"},
            503: {"description": "Upstream Discogs rate limit (429) with no DB fallback"},
        },
    )
    def lookup(payload: LookupRequest, request: Request):
        service: LookupService = request.app.state.service
        try:
            result = service.lookup(payload, source_tag="api")
        except UpstreamServiceError as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content={
                    "status": "upstream_error",
                    "http_code": exc.status_code,
                    "error_type": exc.error_type,
                    "detail": exc.detail,
                },
            )

        if isinstance(result, LookupNotFoundResponse):
            return JSONResponse(status_code=404, content=result.model_dump())
        return result

    @app.post("/batch/csv", response_model=BatchSummaryResponse)
    def batch_csv(payload: BatchRequest, request: Request) -> BatchSummaryResponse:
        service: LookupService = request.app.state.service
        try:
            return service.run_batch(payload)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get("/records", response_model=list[RecordSummaryOut])
    def list_records(
        request: Request, limit: int = Query(default=100, ge=1, le=500)
    ) -> list[RecordSummaryOut]:
        repo: PipelineRepository = request.app.state.repo
        return repo.list_records(limit=limit)

    @app.get("/records/{input_id}", response_model=RecordDetailOut)
    def get_record(input_id: int, request: Request) -> RecordDetailOut:
        repo: PipelineRepository = request.app.state.repo
        detail = repo.get_record_detail(input_id)
        if detail is None:
            raise HTTPException(status_code=404, detail=f"Input record {input_id} not found.")
        return detail

    @app.get("/releases/{discogs_release_id}")
    def get_release(discogs_release_id: int, request: Request) -> dict[str, Any]:
        repo: PipelineRepository = request.app.state.repo
        rel = repo.get_extracted_release(discogs_release_id)
        if rel is None:
            raise HTTPException(
                status_code=404, detail=f"Release {discogs_release_id} not found in database."
            )
        return {
            "release": ReleaseOut(
                discogs_release_id=rel.discogs_release_id,
                master_id=rel.master_id,
                url=rel.url,
                title=rel.title,
                artist_display=rel.artist_display,
                year=rel.year,
                country=rel.country,
                formats=rel.formats,
                identifiers=rel.identifiers,
                labels=rel.labels,
                data_quality=rel.data_quality,
                community_status=rel.community_status,
                community_have=rel.community_have,
                tracklist_hash=rel.tracklist_hash,
                unscoped_credits=rel.unscoped_credits,
            ).model_dump(),
            "tracks": [extracted_track_to_out(t).model_dump() for t in rel.tracks],
        }

    return app


app = create_app()
