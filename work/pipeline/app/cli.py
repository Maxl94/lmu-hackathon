import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

from psycopg_pool import ConnectionPool

from app.agent_client import AgentFallbackProvider, GeminiAgentClient
from app.config import Settings, get_settings
from app.discogs_client import CatalogProvider, DiscogsClient
from app.models import BatchRequest, LookupNotFoundResponse, LookupRequest
from app.repository import PipelineRepository
from app.service import LookupService, UpstreamServiceError


def _parse_rows(rows_arg: str | None) -> list[int] | None:
    if not rows_arg:
        return None
    return [int(part.strip()) for part in rows_arg.split(",") if part.strip()]


def main(
    argv: list[str] | None = None,
    provider: CatalogProvider | None = None,
    agent_provider: AgentFallbackProvider | None = None,
    settings: Settings | None = None,
) -> int:
    parser = argparse.ArgumentParser(description="Discogs tracklist discovery CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    lookup_cmd = sub.add_parser("lookup", help="Look up a single release")
    lookup_cmd.add_argument("--barcode", default="", help="EAN/UPC barcode")
    lookup_cmd.add_argument("--title", default="", help="Album title")
    lookup_cmd.add_argument("--artist", default="", help="Album artist")
    lookup_cmd.add_argument("--refresh", action="store_true", help="Bypass fresh DB cache")

    batch_cmd = sub.add_parser("batch", help="Process rows from a CSV file")
    batch_cmd.add_argument(
        "--csv", default="/app/data/development.csv", help="Path to CSV input"
    )
    batch_cmd.add_argument(
        "--rows",
        default="",
        help="Comma-separated 1-indexed data row numbers (e.g. 1,3,7,13,16)",
    )
    batch_cmd.add_argument(
        "--output",
        default="/app/outputs/batch_report.json",
        help="Output JSON report path (also writes companion .md)",
    )
    batch_cmd.add_argument("--refresh", action="store_true", help="Bypass fresh DB cache")

    enq_batch = sub.add_parser(
        "enqueue-batch",
        help="Enqueue a CSV batch into PostgreSQL queue_jobs for background API workers",
    )
    enq_batch.add_argument(
        "--csv", default="/app/data/development.csv", help="Path to CSV input"
    )
    enq_batch.add_argument(
        "--rows",
        default="",
        help="Comma-separated 1-indexed data row numbers (e.g. 1,3,7,13,16)",
    )
    enq_batch.add_argument(
        "--output",
        default="/app/outputs/batch_report.json",
        help="Output JSON report path (also writes companion .md)",
    )
    enq_batch.add_argument("--refresh", action="store_true", help="Bypass fresh DB cache")

    sub.add_parser(
        "retry-not-found",
        help="Enqueue all eligible not_found records for Gemini agent retry",
    )

    args = parser.parse_args(argv)
    cfg = settings or get_settings()
    pool = ConnectionPool(conninfo=cfg.database_url, min_size=1, max_size=5, open=True)
    repo = PipelineRepository(pool)
    repo.ensure_schema()
    own_client: DiscogsClient | None = None
    active_provider = provider
    if active_provider is None:
        own_client = DiscogsClient(cfg, cache_store=repo)
        active_provider = own_client

    own_agent_client: GeminiAgentClient | None = None
    active_agent_provider = agent_provider
    if active_agent_provider is None and cfg.is_agent_configured():
        own_agent_client = GeminiAgentClient(cfg)
        active_agent_provider = own_agent_client

    service = LookupService(
        repo=repo,
        provider=active_provider,
        settings=cfg,
        agent_provider=active_agent_provider,
    )

    try:
        if args.command == "lookup":
            req = LookupRequest(
                barcode=args.barcode,
                album_title=args.title,
                album_artist=args.artist,
                force_refresh=args.refresh,
            )
            try:
                res = service.lookup(req, source_tag="cli")
            except UpstreamServiceError as exc:
                print(
                    json.dumps(
                        {
                            "status": "upstream_error",
                            "http_code": exc.status_code,
                            "detail": exc.detail,
                        },
                        indent=2,
                    )
                )
                return 2
            print(json.dumps(res.model_dump(), indent=2, ensure_ascii=False))
            return 1 if isinstance(res, LookupNotFoundResponse) else 0

        if args.command == "batch":
            req = BatchRequest(
                csv_path=args.csv,
                rows=_parse_rows(args.rows),
                force_refresh=args.refresh,
                output_path=args.output,
            )
            summary = service.run_batch(req)
            print(json.dumps(summary.model_dump(), indent=2, ensure_ascii=False))
            return 0

        if args.command == "enqueue-batch":
            csv_file = Path(args.csv)
            if not csv_file.exists():
                print(
                    json.dumps({"error": f"CSV file not found: {csv_file}"}),
                    file=sys.stderr,
                )
                return 2
            with csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
                all_rows = list(csv.DictReader(handle))
            selected_rows = _parse_rows(args.rows)
            selected_indices = (
                set(selected_rows) if selected_rows else set(range(1, len(all_rows) + 1))
            )
            items: list[dict[str, Any]] = []
            for idx, row in enumerate(all_rows, start=1):
                if idx not in selected_indices:
                    continue
                items.append(
                    {
                        "row_number": idx,
                        "barcode": str(row.get("barcode") or ""),
                        "album_title": str(row.get("album_title") or ""),
                        "album_artist": str(row.get("album_artist") or ""),
                        "force_refresh": args.refresh,
                        "mode": "full",
                        "stage": "queued_discogs",
                        "status_message": "Queued for Discogs",
                    }
                )
            job = repo.create_queue_job(
                job_type="batch_csv",
                label=f"Batch: {csv_file.name}",
                items=items,
                csv_path=args.csv,
                output_path=args.output,
                force_refresh=args.refresh,
            )
            print(json.dumps(job.model_dump(), indent=2, ensure_ascii=False))
            return 0

        if args.command == "retry-not-found":
            if not service.has_agent_fallback():
                print(
                    json.dumps(
                        {"error": "Gemini agent fallback is not configured or disabled."}
                    ),
                    file=sys.stderr,
                )
                return 2
            records = repo.list_not_found_records_for_agent_retry()
            items = [
                {
                    "row_number": idx,
                    "input_id": int(rec["id"]),
                    "barcode": rec["barcode_raw"],
                    "album_title": rec["album_title_raw"],
                    "album_artist": rec["album_artist_raw"],
                    "force_refresh": True,
                    "mode": "agent_only",
                    "stage": "queued_agent",
                    "status_message": "Queued for Gemini agent retry",
                }
                for idx, rec in enumerate(records, start=1)
            ]
            job = repo.create_queue_job(
                job_type="agent_retry",
                label=f"Retry not_found ({len(items)} records)",
                items=items,
                force_refresh=True,
            )
            print(json.dumps(job.model_dump(), indent=2, ensure_ascii=False))
            return 0
    finally:
        if own_agent_client is not None:
            own_agent_client.close()
        if own_client is not None:
            own_client.close()
        pool.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
