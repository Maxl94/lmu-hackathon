from pathlib import Path
from typing import Any

from psycopg.rows import dict_row
from psycopg.types.json import Jsonb
from psycopg_pool import ConnectionPool

from app.extractor import ExtractedCredit, ExtractedRelease, ExtractedTrack
from app.models import NormalizedInput, RecordDetailOut, RecordSummaryOut, ReleaseOut, TrackArtistOut, TrackOut
from app.extractor import extracted_track_to_out


class PipelineRepository:
    def __init__(self, pool: ConnectionPool) -> None:
        self._pool = pool

    def ensure_schema(self) -> None:
        sql_path = Path(__file__).resolve().parent.parent / "sql" / "init.sql"
        ddl = sql_path.read_text(encoding="utf-8")
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(ddl)
            conn.commit()

    def ping(self) -> bool:
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        return True

    def get_api_cache(self, cache_key: str) -> dict[str, Any] | None:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """
                    SELECT cache_key, endpoint, status_code, payload_json, fetched_at
                    FROM api_cache
                    WHERE cache_key = %s
                    """,
                    (cache_key,),
                )
                return cur.fetchone()

    def set_api_cache(
        self, cache_key: str, endpoint: str, status_code: int, payload: dict[str, Any]
    ) -> None:
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO api_cache (cache_key, endpoint, status_code, payload_json, fetched_at)
                    VALUES (%s, %s, %s, %s, NOW())
                    ON CONFLICT (cache_key) DO UPDATE SET
                        endpoint = EXCLUDED.endpoint,
                        status_code = EXCLUDED.status_code,
                        payload_json = EXCLUDED.payload_json,
                        fetched_at = NOW()
                    """,
                    (cache_key, endpoint, status_code, Jsonb(payload)),
                )
            conn.commit()

    def upsert_input_record(
        self, norm: NormalizedInput, source_tag: str = "api"
    ) -> int:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """
                    INSERT INTO input_records (
                        barcode_raw, album_title_raw, album_artist_raw,
                        barcode_norm, title_norm, artist_norm,
                        format_hint, is_compilation, input_hash, source_tag, updated_at
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
                    ON CONFLICT (input_hash) DO UPDATE SET
                        barcode_raw = EXCLUDED.barcode_raw,
                        album_title_raw = EXCLUDED.album_title_raw,
                        album_artist_raw = EXCLUDED.album_artist_raw,
                        updated_at = NOW()
                    RETURNING id
                    """,
                    (
                        norm.barcode_raw,
                        norm.album_title_raw,
                        norm.album_artist_raw,
                        norm.barcode_norm,
                        norm.title_norm,
                        norm.artist_norm,
                        Jsonb(norm.format_hint.model_dump()),
                        norm.is_compilation,
                        norm.input_hash,
                        source_tag,
                    ),
                )
                row = cur.fetchone()
            conn.commit()
        return int(row["id"])

    def upsert_release_with_tracks(self, rel: ExtractedRelease) -> None:
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO releases (
                        discogs_release_id, master_id, url, resource_url,
                        title, title_norm, artist_display, artist_norm,
                        year, country, formats_json, identifiers_json, labels_json,
                        data_quality, community_status, community_have, community_want,
                        notes, track_count, tracklist_hash, unscoped_credits_json,
                        raw_json, fetched_at
                    )
                    VALUES (
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, %s, %s, %s,
                        %s, NOW()
                    )
                    ON CONFLICT (discogs_release_id) DO UPDATE SET
                        master_id = EXCLUDED.master_id,
                        url = EXCLUDED.url,
                        resource_url = EXCLUDED.resource_url,
                        title = EXCLUDED.title,
                        title_norm = EXCLUDED.title_norm,
                        artist_display = EXCLUDED.artist_display,
                        artist_norm = EXCLUDED.artist_norm,
                        year = EXCLUDED.year,
                        country = EXCLUDED.country,
                        formats_json = EXCLUDED.formats_json,
                        identifiers_json = EXCLUDED.identifiers_json,
                        labels_json = EXCLUDED.labels_json,
                        data_quality = EXCLUDED.data_quality,
                        community_status = EXCLUDED.community_status,
                        community_have = EXCLUDED.community_have,
                        community_want = EXCLUDED.community_want,
                        notes = EXCLUDED.notes,
                        track_count = EXCLUDED.track_count,
                        tracklist_hash = EXCLUDED.tracklist_hash,
                        unscoped_credits_json = EXCLUDED.unscoped_credits_json,
                        raw_json = EXCLUDED.raw_json,
                        fetched_at = NOW()
                    """,
                    (
                        rel.discogs_release_id,
                        rel.master_id,
                        rel.url,
                        rel.resource_url,
                        rel.title,
                        rel.title_norm,
                        rel.artist_display,
                        rel.artist_norm,
                        rel.year,
                        rel.country,
                        Jsonb(rel.formats),
                        Jsonb(rel.identifiers),
                        Jsonb(rel.labels),
                        rel.data_quality,
                        rel.community_status,
                        rel.community_have,
                        rel.community_want,
                        rel.notes,
                        rel.track_count,
                        rel.tracklist_hash,
                        Jsonb(rel.unscoped_credits),
                        Jsonb(rel.raw_json),
                    ),
                )

                cur.execute(
                    "DELETE FROM release_barcodes WHERE discogs_release_id = %s",
                    (rel.discogs_release_id,),
                )
                for b_norm, b_raw in rel.barcode_entries:
                    cur.execute(
                        """
                        INSERT INTO release_barcodes (discogs_release_id, barcode_norm, barcode_raw)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (discogs_release_id, barcode_norm) DO UPDATE SET
                            barcode_raw = EXCLUDED.barcode_raw
                        """,
                        (rel.discogs_release_id, b_norm, b_raw),
                    )

                cur.execute(
                    "DELETE FROM tracks WHERE discogs_release_id = %s",
                    (rel.discogs_release_id,),
                )
                for track in rel.tracks:
                    cur.execute(
                        """
                        INSERT INTO tracks (
                            discogs_release_id, track_order, disc_number, disc_label,
                            position, entry_type, parent_position, title,
                            duration_raw, duration_sec, performing_artists_json,
                            performing_artist_display, has_valid_duration, has_resolved_performer
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id
                        """,
                        (
                            rel.discogs_release_id,
                            track.track_order,
                            track.disc_number,
                            track.disc_label,
                            track.position,
                            track.entry_type,
                            track.parent_position,
                            track.title,
                            track.duration_raw,
                            track.duration_sec,
                            Jsonb([a.model_dump() for a in track.performing_artists]),
                            track.performing_artist_display,
                            track.has_valid_duration,
                            track.has_resolved_performer,
                        ),
                    )
                    track_id = cur.fetchone()[0]
                    for credit in track.credits:
                        cur.execute(
                            """
                            INSERT INTO track_credits (
                                track_id, discogs_artist_id, artist_name, anv,
                                role_raw, role_category, credit_source
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (track_id, artist_name, role_raw, credit_source) DO NOTHING
                            """,
                            (
                                track_id,
                                credit.discogs_artist_id,
                                credit.artist_name,
                                credit.anv,
                                credit.role_raw,
                                credit.role_category,
                                credit.credit_source,
                            ),
                        )
            conn.commit()

    def get_extracted_release(self, discogs_release_id: int) -> ExtractedRelease | None:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    "SELECT * FROM releases WHERE discogs_release_id = %s",
                    (discogs_release_id,),
                )
                rel_row = cur.fetchone()
                if rel_row is None:
                    return None

                cur.execute(
                    "SELECT barcode_norm, barcode_raw FROM release_barcodes WHERE discogs_release_id = %s",
                    (discogs_release_id,),
                )
                barcode_rows = cur.fetchall()

                cur.execute(
                    "SELECT * FROM tracks WHERE discogs_release_id = %s ORDER BY track_order ASC",
                    (discogs_release_id,),
                )
                track_rows = cur.fetchall()

                track_ids = [r["id"] for r in track_rows]
                credits_by_track: dict[int, list[ExtractedCredit]] = {tid: [] for tid in track_ids}
                if track_ids:
                    cur.execute(
                        "SELECT * FROM track_credits WHERE track_id = ANY(%s) ORDER BY id ASC",
                        (track_ids,),
                    )
                    for cr in cur.fetchall():
                        credits_by_track[cr["track_id"]].append(
                            ExtractedCredit(
                                discogs_artist_id=cr["discogs_artist_id"],
                                artist_name=cr["artist_name"],
                                anv=cr["anv"],
                                role_raw=cr["role_raw"],
                                role_category=cr["role_category"],
                                credit_source=cr["credit_source"],
                            )
                        )

        tracks: list[ExtractedTrack] = []
        for tr in track_rows:
            artists = [
                TrackArtistOut(**a) for a in (tr["performing_artists_json"] or [])
            ]
            tracks.append(
                ExtractedTrack(
                    track_order=tr["track_order"],
                    disc_number=tr["disc_number"],
                    disc_label=tr["disc_label"],
                    position=tr["position"],
                    entry_type=tr["entry_type"],
                    parent_position=tr["parent_position"],
                    title=tr["title"],
                    duration_raw=tr["duration_raw"],
                    duration_sec=tr["duration_sec"],
                    performing_artists=artists,
                    performing_artist_display=tr["performing_artist_display"],
                    has_valid_duration=tr["has_valid_duration"],
                    has_resolved_performer=tr["has_resolved_performer"],
                    credits=credits_by_track.get(tr["id"], []),
                )
            )

        return ExtractedRelease(
            discogs_release_id=int(rel_row["discogs_release_id"]),
            master_id=rel_row["master_id"],
            url=rel_row["url"],
            resource_url=rel_row["resource_url"],
            title=rel_row["title"],
            title_norm=rel_row["title_norm"],
            artist_display=rel_row["artist_display"],
            artist_norm=rel_row["artist_norm"],
            year=rel_row["year"],
            country=rel_row["country"],
            formats=rel_row["formats_json"] or [],
            identifiers=rel_row["identifiers_json"] or [],
            labels=rel_row["labels_json"] or [],
            data_quality=rel_row["data_quality"],
            community_status=rel_row["community_status"],
            community_have=int(rel_row["community_have"]),
            community_want=int(rel_row["community_want"]),
            notes=rel_row["notes"],
            track_count=int(rel_row["track_count"]),
            tracklist_hash=rel_row["tracklist_hash"],
            unscoped_credits=rel_row["unscoped_credits_json"] or [],
            raw_json=rel_row["raw_json"] or {},
            barcode_entries=[(b["barcode_norm"], b["barcode_raw"]) for b in barcode_rows],
            tracks=tracks,
        )

    def find_latest_run(
        self, input_id: int, statuses: tuple[str, ...] | None = None
    ) -> dict[str, Any] | None:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                if statuses:
                    cur.execute(
                        """
                        SELECT * FROM lookup_runs
                        WHERE input_id = %s AND status = ANY(%s)
                        ORDER BY created_at DESC, id DESC
                        LIMIT 1
                        """,
                        (input_id, list(statuses)),
                    )
                else:
                    cur.execute(
                        """
                        SELECT * FROM lookup_runs
                        WHERE input_id = %s
                        ORDER BY created_at DESC, id DESC
                        LIMIT 1
                        """,
                        (input_id,),
                    )
                return cur.fetchone()

    def get_input_matches(self, input_id: int) -> list[dict[str, Any]]:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """
                    SELECT * FROM input_matches
                    WHERE input_id = %s
                    ORDER BY is_selected DESC, match_rank ASC
                    """,
                    (input_id,),
                )
                return cur.fetchall()

    def find_release_ids_by_barcodes(self, variants: list[str]) -> list[int]:
        if not variants:
            return []
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT DISTINCT discogs_release_id
                    FROM release_barcodes
                    WHERE barcode_norm = ANY(%s)
                    """,
                    (variants,),
                )
                return [int(r[0]) for r in cur.fetchall()]

    def find_release_ids_by_artist_title(
        self, artist_norm: str, title_norm: str, is_compilation: bool = False
    ) -> list[int]:
        if not title_norm:
            return []
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                if is_compilation or not artist_norm:
                    cur.execute(
                        """
                        SELECT discogs_release_id
                        FROM releases
                        WHERE title_norm = %s
                        LIMIT 10
                        """,
                        (title_norm,),
                    )
                else:
                    cur.execute(
                        """
                        SELECT discogs_release_id
                        FROM releases
                        WHERE title_norm = %s AND artist_norm = %s
                        LIMIT 10
                        """,
                        (title_norm, artist_norm),
                    )
                return [int(r[0]) for r in cur.fetchall()]

    def save_matches_and_run(
        self,
        input_id: int,
        status: str,
        http_code: int,
        source: str,
        selected_release_id: int | None,
        queries_attempted: list[dict[str, Any]],
        candidates_checked: int,
        evaluation_summary: dict[str, Any],
        review_reasons: list[str],
        matches: list[dict[str, Any]],
        error_detail: str = "",
        replace_matches: bool = True,
    ) -> int:
        with self._pool.connection() as conn:
            with conn.cursor() as cur:
                if replace_matches:
                    cur.execute("DELETE FROM input_matches WHERE input_id = %s", (input_id,))
                    for m in matches:
                        cur.execute(
                            """
                            INSERT INTO input_matches (
                                input_id, discogs_release_id, is_selected,
                                match_rank, match_method, score, evaluation_json
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (input_id, discogs_release_id) DO UPDATE SET
                                is_selected = EXCLUDED.is_selected,
                                match_rank = EXCLUDED.match_rank,
                                match_method = EXCLUDED.match_method,
                                score = EXCLUDED.score,
                                evaluation_json = EXCLUDED.evaluation_json
                            """,
                            (
                                input_id,
                                m["discogs_release_id"],
                                m["is_selected"],
                                m["match_rank"],
                                m["match_method"],
                                m["score"],
                                Jsonb(m.get("evaluation_json", {})),
                            ),
                        )

                cur.execute(
                    """
                    INSERT INTO lookup_runs (
                        input_id, status, http_code, source, selected_release_id,
                        queries_attempted_json, candidates_checked,
                        evaluation_summary_json, review_reasons_json, error_detail
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (
                        input_id,
                        status,
                        http_code,
                        source,
                        selected_release_id,
                        Jsonb(queries_attempted),
                        candidates_checked,
                        Jsonb(evaluation_summary),
                        Jsonb(review_reasons),
                        error_detail,
                    ),
                )
                run_id = int(cur.fetchone()[0])
            conn.commit()
        return run_id

    def list_records(self, limit: int = 100) -> list[RecordSummaryOut]:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """
                    SELECT
                        ir.id AS input_id,
                        ir.barcode_raw,
                        ir.album_title_raw,
                        ir.album_artist_raw,
                        ir.barcode_norm,
                        ir.title_norm,
                        ir.artist_norm,
                        ir.format_hint,
                        ir.is_compilation,
                        lr.status AS latest_status,
                        lr.http_code AS latest_http_code,
                        lr.source AS latest_source,
                        lr.selected_release_id,
                        r.url AS selected_release_url,
                        lr.created_at AS latest_checked_at
                    FROM input_records ir
                    LEFT JOIN LATERAL (
                        SELECT * FROM lookup_runs
                        WHERE input_id = ir.id
                        ORDER BY created_at DESC, id DESC
                        LIMIT 1
                    ) lr ON TRUE
                    LEFT JOIN releases r ON r.discogs_release_id = lr.selected_release_id
                    ORDER BY ir.id DESC
                    LIMIT %s
                    """,
                    (limit,),
                )
                rows = cur.fetchall()

        return [
            RecordSummaryOut(
                input_id=int(row["input_id"]),
                barcode_raw=row["barcode_raw"],
                album_title_raw=row["album_title_raw"],
                album_artist_raw=row["album_artist_raw"],
                barcode_norm=row["barcode_norm"],
                title_norm=row["title_norm"],
                artist_norm=row["artist_norm"],
                format_hint=row["format_hint"] or {},
                is_compilation=bool(row["is_compilation"]),
                latest_status=row["latest_status"],
                latest_http_code=row["latest_http_code"],
                latest_source=row["latest_source"],
                selected_release_id=row["selected_release_id"],
                selected_release_url=row["selected_release_url"],
                latest_checked_at=(
                    row["latest_checked_at"].isoformat() if row["latest_checked_at"] else None
                ),
            )
            for row in rows
        ]

    def get_record_detail(self, input_id: int) -> RecordDetailOut | None:
        with self._pool.connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """
                    SELECT
                        ir.id AS input_id,
                        ir.barcode_raw,
                        ir.album_title_raw,
                        ir.album_artist_raw,
                        ir.barcode_norm,
                        ir.title_norm,
                        ir.artist_norm,
                        ir.format_hint,
                        ir.is_compilation,
                        lr.status AS latest_status,
                        lr.http_code AS latest_http_code,
                        lr.source AS latest_source,
                        lr.selected_release_id,
                        r.url AS selected_release_url,
                        lr.created_at AS latest_checked_at
                    FROM input_records ir
                    LEFT JOIN LATERAL (
                        SELECT * FROM lookup_runs
                        WHERE input_id = ir.id
                        ORDER BY created_at DESC, id DESC
                        LIMIT 1
                    ) lr ON TRUE
                    LEFT JOIN releases r ON r.discogs_release_id = lr.selected_release_id
                    WHERE ir.id = %s
                    """,
                    (input_id,),
                )
                row = cur.fetchone()
                if row is None:
                    return None

                cur.execute(
                    """
                    SELECT id, status, http_code, source, selected_release_id,
                           queries_attempted_json, candidates_checked,
                           evaluation_summary_json, review_reasons_json,
                           error_detail, created_at
                    FROM lookup_runs
                    WHERE input_id = %s
                    ORDER BY created_at DESC, id DESC
                    """,
                    (input_id,),
                )
                runs = [
                    {**r, "created_at": r["created_at"].isoformat()}
                    for r in cur.fetchall()
                ]

                cur.execute(
                    """
                    SELECT im.discogs_release_id, im.is_selected, im.match_rank,
                           im.match_method, im.score, im.evaluation_json,
                           r.url, r.title, r.artist_display
                    FROM input_matches im
                    JOIN releases r ON r.discogs_release_id = im.discogs_release_id
                    WHERE im.input_id = %s
                    ORDER BY im.is_selected DESC, im.match_rank ASC
                    """,
                    (input_id,),
                )
                matches = cur.fetchall()

        selected_release_out: ReleaseOut | None = None
        tracks_out: list[TrackOut] = []
        if row["selected_release_id"] is not None:
            extracted = self.get_extracted_release(int(row["selected_release_id"]))
            if extracted is not None:
                selected_release_out = ReleaseOut(
                    discogs_release_id=extracted.discogs_release_id,
                    master_id=extracted.master_id,
                    url=extracted.url,
                    title=extracted.title,
                    artist_display=extracted.artist_display,
                    year=extracted.year,
                    country=extracted.country,
                    formats=extracted.formats,
                    identifiers=extracted.identifiers,
                    labels=extracted.labels,
                    data_quality=extracted.data_quality,
                    community_status=extracted.community_status,
                    community_have=extracted.community_have,
                    tracklist_hash=extracted.tracklist_hash,
                    unscoped_credits=extracted.unscoped_credits,
                )
                tracks_out = [extracted_track_to_out(t) for t in extracted.tracks]

        return RecordDetailOut(
            record=RecordSummaryOut(
                input_id=int(row["input_id"]),
                barcode_raw=row["barcode_raw"],
                album_title_raw=row["album_title_raw"],
                album_artist_raw=row["album_artist_raw"],
                barcode_norm=row["barcode_norm"],
                title_norm=row["title_norm"],
                artist_norm=row["artist_norm"],
                format_hint=row["format_hint"] or {},
                is_compilation=bool(row["is_compilation"]),
                latest_status=row["latest_status"],
                latest_http_code=row["latest_http_code"],
                latest_source=row["latest_source"],
                selected_release_id=row["selected_release_id"],
                selected_release_url=row["selected_release_url"],
                latest_checked_at=(
                    row["latest_checked_at"].isoformat() if row["latest_checked_at"] else None
                ),
            ),
            runs=runs,
            matches=matches,
            selected_release=selected_release_out,
            tracks=tracks_out,
        )
