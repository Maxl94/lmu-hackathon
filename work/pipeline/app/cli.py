import argparse
import json
import sys

from psycopg_pool import ConnectionPool

from app.config import get_settings
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

    args = parser.parse_args(argv)
    settings = get_settings()
    pool = ConnectionPool(conninfo=settings.database_url, min_size=1, max_size=5, open=True)
    repo = PipelineRepository(pool)
    repo.ensure_schema()
    own_client: DiscogsClient | None = None
    active_provider = provider
    if active_provider is None:
        own_client = DiscogsClient(settings, cache_store=repo)
        active_provider = own_client
    service = LookupService(repo=repo, provider=active_provider, settings=settings)

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
    finally:
        if own_client is not None:
            own_client.close()
        pool.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
