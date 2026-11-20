import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from app.config import Settings
from app.discogs_client import CatalogProvider, DiscogsError, DiscogsRateLimitError
from app.evaluator import (
    EvaluationBundle,
    build_evaluation_out,
    evaluate_candidates,
)
from app.extractor import ExtractedRelease, extract_release, extracted_track_to_out
from app.models import (
    AlternativeEditionOut,
    BatchRequest,
    BatchRowOutcome,
    BatchSummaryResponse,
    EvaluationOut,
    LookupNotFoundResponse,
    LookupRequest,
    LookupSuccessResponse,
    NormalizedInput,
    ReleaseOut,
)
from app.normalizer import normalize_input
from app.repository import PipelineRepository


class UpstreamServiceError(Exception):
    def __init__(self, status_code: int, detail: str, error_type: str = "upstream_error") -> None:
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail
        self.error_type = error_type


def _release_to_out(rel: ExtractedRelease) -> ReleaseOut:
    return ReleaseOut(
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
    )


class LookupService:
    def __init__(
        self,
        repo: PipelineRepository,
        provider: CatalogProvider,
        settings: Settings,
    ) -> None:
        self._repo = repo
        self._provider = provider
        self._settings = settings

    def _build_success_from_stored(
        self,
        input_id: int,
        norm: NormalizedInput,
        latest_run: dict[str, Any],
        source_override: str,
        fallback_used: bool = False,
        warning: str | None = None,
    ) -> LookupSuccessResponse | None:
        selected_id = latest_run.get("selected_release_id")
        if selected_id is None:
            return None
        selected_rel = self._repo.get_extracted_release(int(selected_id))
        if selected_rel is None:
            return None

        matches = self._repo.get_input_matches(input_id)
        alternatives: list[AlternativeEditionOut] = []
        for m in matches:
            rid = int(m["discogs_release_id"])
            if rid == selected_rel.discogs_release_id:
                continue
            alt_rel = self._repo.get_extracted_release(rid)
            if alt_rel is None:
                continue
            diff_msg = (
                "Identical tracklist"
                if alt_rel.tracklist_hash == selected_rel.tracklist_hash
                else f"Different tracklist ({alt_rel.track_count} tracks vs {selected_rel.track_count})"
            )
            alternatives.append(
                AlternativeEditionOut(
                    discogs_release_id=alt_rel.discogs_release_id,
                    url=alt_rel.url,
                    title=alt_rel.title,
                    artist_display=alt_rel.artist_display,
                    year=alt_rel.year,
                    country=alt_rel.country,
                    formats=alt_rel.formats,
                    track_count=alt_rel.track_count,
                    tracklist_hash=alt_rel.tracklist_hash,
                    score=float(m["score"]),
                    match_method=str(m["match_method"]),
                    diff_summary=diff_msg,
                )
            )

        summary = latest_run.get("evaluation_summary_json") or {}
        evaluation = EvaluationOut(
            match_confidence=float(summary.get("match_confidence", 0.0)),
            match_method=str(summary.get("match_method", "database")),
            candidates_checked=int(latest_run.get("candidates_checked", 0)),
            candidates_passing=int(summary.get("candidates_passing", len(matches))),
            editions_agree=bool(summary.get("editions_agree", True)),
            track_count=selected_rel.track_count,
            duration_coverage=float(summary.get("duration_coverage", 0.0)),
            performer_coverage=float(summary.get("performer_coverage", 0.0)),
            writer_credit_coverage=float(summary.get("writer_credit_coverage", 0.0)),
            producer_credit_coverage=float(summary.get("producer_credit_coverage", 0.0)),
            disc_format_consistent=bool(summary.get("disc_format_consistent", True)),
            discogs_data_quality=selected_rel.data_quality,
            review_reasons=list(latest_run.get("review_reasons_json") or []),
            rejection_reasons=list(summary.get("rejection_reasons") or []),
        )
        status = "needs_review" if latest_run["status"] == "needs_review" else "matched"
        return LookupSuccessResponse(
            status=status,
            http_code=200,
            source=source_override,
            fallback_used=fallback_used,
            warning=warning,
            input_id=input_id,
            normalized_input=norm,
            release=_release_to_out(selected_rel),
            tracks=[extracted_track_to_out(t) for t in selected_rel.tracks],
            alternatives=alternatives,
            evaluation=evaluation,
        )

    def _try_local_cross_input_match(
        self,
        input_id: int,
        norm: NormalizedInput,
        source_label: str,
        fallback_used: bool = False,
        warning: str | None = None,
        error_detail: str = "",
    ) -> LookupSuccessResponse | None:
        method_map: dict[int, str] = {}
        candidate_ids: list[int] = []

        for rid in self._repo.find_release_ids_by_barcodes(norm.barcode_variants):
            if rid not in method_map:
                method_map[rid] = "local_db_barcode"
                candidate_ids.append(rid)

        for rid in self._repo.find_release_ids_by_artist_title(
            norm.artist_norm, norm.title_norm, norm.is_compilation
        ):
            if rid not in method_map:
                method_map[rid] = "local_db_title_artist"
                candidate_ids.append(rid)

        if not candidate_ids:
            return None

        local_releases: list[ExtractedRelease] = []
        for rid in candidate_ids:
            rel = self._repo.get_extracted_release(rid)
            if rel is not None:
                local_releases.append(rel)

        if not local_releases:
            return None

        bundle = evaluate_candidates(norm, local_releases, method_map)
        if bundle.status == "not_found" or bundle.selected is None:
            return None

        eval_out = build_evaluation_out(bundle, len(local_releases))
        matches_rows = self._bundle_to_match_rows(bundle)
        self._repo.save_matches_and_run(
            input_id=input_id,
            status=bundle.status,
            http_code=200,
            source=source_label,
            selected_release_id=bundle.selected.discogs_release_id,
            queries_attempted=[{"tier": "local_db", "candidates": candidate_ids}],
            candidates_checked=len(local_releases),
            evaluation_summary=eval_out.model_dump(),
            review_reasons=eval_out.review_reasons,
            matches=matches_rows,
            error_detail=error_detail,
            replace_matches=True,
        )
        return LookupSuccessResponse(
            status=bundle.status,
            http_code=200,
            source=source_label,
            fallback_used=fallback_used,
            warning=warning,
            input_id=input_id,
            normalized_input=norm,
            release=_release_to_out(bundle.selected),
            tracks=[extracted_track_to_out(t) for t in bundle.selected.tracks],
            alternatives=bundle.alternatives,
            evaluation=eval_out,
        )

    @staticmethod
    def _bundle_to_match_rows(bundle: EvaluationBundle) -> list[dict[str, Any]]:
        assert bundle.selected is not None
        rows: list[dict[str, Any]] = []
        for idx, (rel, ev) in enumerate(bundle.ranked, start=1):
            rows.append(
                {
                    "discogs_release_id": rel.discogs_release_id,
                    "is_selected": rel.discogs_release_id == bundle.selected.discogs_release_id,
                    "match_rank": idx,
                    "match_method": ev.match_method,
                    "score": ev.score,
                    "evaluation_json": {
                        "barcode_matched": ev.barcode_matched,
                        "title_sim": ev.title_sim,
                        "artist_sim": ev.artist_sim,
                        "format_matched": ev.format_matched,
                        "disc_format_consistent": ev.disc_format_consistent,
                        "duration_coverage": ev.duration_coverage,
                        "performer_coverage": ev.performer_coverage,
                        "writer_credit_coverage": ev.writer_credit_coverage,
                        "producer_credit_coverage": ev.producer_credit_coverage,
                        "review_reasons": ev.review_reasons,
                    },
                }
            )
        return rows

    def lookup(
        self, req: LookupRequest, source_tag: str = "api"
    ) -> LookupSuccessResponse | LookupNotFoundResponse:
        norm = normalize_input(req.barcode, req.album_title, req.album_artist)
        input_id = self._repo.upsert_input_record(norm, source_tag=source_tag)

        # Layer 1 & Layer 2 DB deduplication when not forcing refresh
        if not req.force_refresh:
            latest_run = self._repo.find_latest_run(input_id)
            if latest_run is not None:
                if latest_run["status"] in ("matched", "needs_review"):
                    stored = self._build_success_from_stored(
                        input_id=input_id,
                        norm=norm,
                        latest_run=latest_run,
                        source_override="database",
                    )
                    if stored is not None:
                        return stored
                elif latest_run["status"] == "not_found":
                    created_at: datetime = latest_run["created_at"]
                    if created_at.tzinfo is None:
                        created_at = created_at.replace(tzinfo=timezone.utc)
                    cutoff = datetime.now(timezone.utc) - timedelta(
                        hours=self._settings.not_found_ttl_hours
                    )
                    if created_at >= cutoff:
                        summary = latest_run.get("evaluation_summary_json") or {}
                        return LookupNotFoundResponse(
                            http_code=404,
                            source="database_cache",
                            input_id=input_id,
                            normalized_input=norm,
                            queries_attempted=list(latest_run.get("queries_attempted_json") or []),
                            candidates_checked=int(latest_run.get("candidates_checked", 0)),
                            rejection_reasons=list(summary.get("rejection_reasons") or []),
                        )

            local_hit = self._try_local_cross_input_match(
                input_id=input_id,
                norm=norm,
                source_label="database",
            )
            if local_hit is not None:
                return local_hit

        # Live/Cached Discogs cascading search
        queries_attempted: list[dict[str, Any]] = []
        candidate_ids: list[int] = []
        candidate_methods: dict[int, str] = {}
        all_from_cache = True

        def _run_search(tier: str, params: dict[str, Any], method: str) -> int:
            nonlocal all_from_cache
            payload, from_cache = self._provider.search_releases(
                params, bypass_cache=req.force_refresh
            )
            if not from_cache:
                all_from_cache = False
            results = list(payload.get("results") or [])
            queries_attempted.append(
                {
                    "tier": tier,
                    "params": params,
                    "result_count": len(results),
                    "from_cache": from_cache,
                }
            )
            added = 0
            for item in results:
                rid_raw = item.get("id")
                if rid_raw is None:
                    continue
                rid = int(rid_raw)
                if rid not in candidate_methods:
                    candidate_methods[rid] = method
                    candidate_ids.append(rid)
                    added += 1
            return added

        try:
            fetched_releases: list[ExtractedRelease] = []
            fetched_ids: set[int] = set()

            def _fetch_new_candidates(ids_to_consider: list[int]) -> None:
                nonlocal all_from_cache
                newly_fetched = 0
                for rid in ids_to_consider:
                    if rid in fetched_ids:
                        continue
                    if newly_fetched >= self._settings.max_candidates_to_fetch:
                        break
                    fetched_ids.add(rid)
                    raw_rel, from_cache = self._provider.get_release(
                        rid, bypass_cache=req.force_refresh
                    )
                    if not from_cache:
                        all_from_cache = False
                    if not raw_rel or "id" not in raw_rel:
                        continue
                    extracted = extract_release(raw_rel)
                    self._repo.upsert_release_with_tracks(extracted)
                    fetched_releases.append(extracted)
                    newly_fetched += 1

            # Tier 1: Barcode search (with 12 <-> 13 leading-zero variants)
            for idx, b_var in enumerate(norm.barcode_variants):
                method = "barcode_exact" if idx == 0 else "barcode_variant"
                _run_search("tier1_barcode", {"barcode": b_var}, method)
                if candidate_ids:
                    break

            if candidate_ids:
                _fetch_new_candidates(candidate_ids)

            bundle = evaluate_candidates(norm, fetched_releases, candidate_methods)

            # Tier 2 & Tier 3 fallback if barcode search missed OR all Tier 1 candidates failed evaluation
            if (not candidate_ids or bundle.status == "not_found") and norm.title_clean:
                tier1_count = len(candidate_ids)
                t2_params: dict[str, Any] = {"release_title": norm.title_clean}
                if norm.artist_clean and not norm.is_compilation:
                    t2_params["artist"] = norm.artist_clean
                added_t2 = _run_search(
                    "tier2_structured", t2_params, "title_artist_structured"
                )

                if added_t2 == 0:
                    q_parts = []
                    if norm.artist_clean and not norm.is_compilation:
                        q_parts.append(norm.artist_clean)
                    q_parts.append(norm.title_clean)
                    _run_search("tier3_freetext", {"q": " ".join(q_parts)}, "freetext_q")

                fallback_ids = candidate_ids[tier1_count:]
                if fallback_ids:
                    _fetch_new_candidates(fallback_ids)
                    bundle = evaluate_candidates(norm, fetched_releases, candidate_methods)

        except DiscogsError as exc:
            warning_msg = f"Live Discogs lookup failed ({exc}); served stored database fallback."
            prior_ok = self._repo.find_latest_run(
                input_id, statuses=("matched", "needs_review")
            )
            if prior_ok is not None:
                fallback_resp = self._build_success_from_stored(
                    input_id=input_id,
                    norm=norm,
                    latest_run=prior_ok,
                    source_override="database_fallback",
                    fallback_used=True,
                    warning=warning_msg,
                )
                if fallback_resp is not None:
                    self._repo.save_matches_and_run(
                        input_id=input_id,
                        status=prior_ok["status"],
                        http_code=200,
                        source="database_fallback",
                        selected_release_id=fallback_resp.release.discogs_release_id,
                        queries_attempted=queries_attempted,
                        candidates_checked=fallback_resp.evaluation.candidates_checked,
                        evaluation_summary=fallback_resp.evaluation.model_dump(),
                        review_reasons=fallback_resp.evaluation.review_reasons,
                        matches=[],
                        error_detail=str(exc),
                        replace_matches=False,
                    )
                    return fallback_resp

            local_fb = self._try_local_cross_input_match(
                input_id=input_id,
                norm=norm,
                source_label="database_fallback",
                fallback_used=True,
                warning=warning_msg,
                error_detail=str(exc),
            )
            if local_fb is not None:
                return local_fb

            http_code = 503 if isinstance(exc, DiscogsRateLimitError) else 502
            self._repo.save_matches_and_run(
                input_id=input_id,
                status="upstream_error",
                http_code=http_code,
                source="discogs_live",
                selected_release_id=None,
                queries_attempted=queries_attempted,
                candidates_checked=0,
                evaluation_summary={},
                review_reasons=[],
                matches=[],
                error_detail=str(exc),
                replace_matches=False,
            )
            raise UpstreamServiceError(
                status_code=http_code,
                detail=str(exc),
                error_type=type(exc).__name__,
            ) from exc

        source_label = (
            "discogs_cached"
            if (all_from_cache and not req.force_refresh and queries_attempted)
            else "discogs_live"
        )

        if bundle.status == "not_found" or bundle.selected is None:
            self._repo.save_matches_and_run(
                input_id=input_id,
                status="not_found",
                http_code=404,
                source=source_label,
                selected_release_id=None,
                queries_attempted=queries_attempted,
                candidates_checked=len(fetched_releases),
                evaluation_summary={"rejection_reasons": bundle.rejection_reasons},
                review_reasons=[],
                matches=[],
                replace_matches=True,
            )
            return LookupNotFoundResponse(
                http_code=404,
                source=source_label,
                input_id=input_id,
                normalized_input=norm,
                queries_attempted=queries_attempted,
                candidates_checked=len(fetched_releases),
                rejection_reasons=bundle.rejection_reasons,
            )

        eval_out = build_evaluation_out(bundle, len(fetched_releases))
        matches_rows = self._bundle_to_match_rows(bundle)
        self._repo.save_matches_and_run(
            input_id=input_id,
            status=bundle.status,
            http_code=200,
            source=source_label,
            selected_release_id=bundle.selected.discogs_release_id,
            queries_attempted=queries_attempted,
            candidates_checked=len(fetched_releases),
            evaluation_summary=eval_out.model_dump(),
            review_reasons=eval_out.review_reasons,
            matches=matches_rows,
            replace_matches=True,
        )
        return LookupSuccessResponse(
            status=bundle.status,
            http_code=200,
            source=source_label,
            fallback_used=False,
            warning=None,
            input_id=input_id,
            normalized_input=norm,
            release=_release_to_out(bundle.selected),
            tracks=[extracted_track_to_out(t) for t in bundle.selected.tracks],
            alternatives=bundle.alternatives,
            evaluation=eval_out,
        )

    def run_batch(self, req: BatchRequest) -> BatchSummaryResponse:
        csv_file = Path(req.csv_path)
        if not csv_file.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_file}")

        with csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            all_rows = list(reader)

        selected_indices = (
            set(req.rows) if req.rows else set(range(1, len(all_rows) + 1))
        )

        outcomes: list[BatchRowOutcome] = []
        full_results: list[dict[str, Any]] = []
        matched_count = 0
        needs_review_count = 0
        not_found_count = 0
        error_count = 0

        for idx, row in enumerate(all_rows, start=1):
            if idx not in selected_indices:
                continue

            barcode = str(row.get("barcode") or "")
            album_title = str(row.get("album_title") or "")
            album_artist = str(row.get("album_artist") or "")

            try:
                lookup_req = LookupRequest(
                    barcode=barcode,
                    album_title=album_title,
                    album_artist=album_artist,
                    force_refresh=req.force_refresh,
                )
                result = self.lookup(lookup_req, source_tag=f"batch_row_{idx}")
                full_results.append({"row_number": idx, "result": result.model_dump()})

                if isinstance(result, LookupSuccessResponse):
                    if result.status == "matched":
                        matched_count += 1
                    else:
                        needs_review_count += 1
                    outcomes.append(
                        BatchRowOutcome(
                            row_number=idx,
                            barcode=barcode,
                            album_title=album_title,
                            album_artist=album_artist,
                            http_code=200,
                            status=result.status,
                            source=result.source,
                            fallback_used=result.fallback_used,
                            input_id=result.input_id,
                            discogs_release_id=result.release.discogs_release_id,
                            release_url=result.release.url,
                            track_count=result.evaluation.track_count,
                            match_confidence=result.evaluation.match_confidence,
                            duration_coverage=result.evaluation.duration_coverage,
                            performer_coverage=result.evaluation.performer_coverage,
                            writer_credit_coverage=result.evaluation.writer_credit_coverage,
                            review_reasons=result.evaluation.review_reasons,
                        )
                    )
                else:
                    not_found_count += 1
                    outcomes.append(
                        BatchRowOutcome(
                            row_number=idx,
                            barcode=barcode,
                            album_title=album_title,
                            album_artist=album_artist,
                            http_code=404,
                            status="not_found",
                            source=result.source,
                            input_id=result.input_id,
                            rejection_reasons=result.rejection_reasons,
                        )
                    )
            except UpstreamServiceError as exc:
                error_count += 1
                full_results.append(
                    {"row_number": idx, "error": {"http_code": exc.status_code, "detail": exc.detail}}
                )
                outcomes.append(
                    BatchRowOutcome(
                        row_number=idx,
                        barcode=barcode,
                        album_title=album_title,
                        album_artist=album_artist,
                        http_code=exc.status_code,
                        status="upstream_error",
                        source="discogs_live",
                        error_detail=exc.detail,
                    )
                )
            except ValueError as exc:
                error_count += 1
                detail = str(exc)
                full_results.append(
                    {"row_number": idx, "error": {"http_code": 422, "detail": detail}}
                )
                outcomes.append(
                    BatchRowOutcome(
                        row_number=idx,
                        barcode=barcode,
                        album_title=album_title,
                        album_artist=album_artist,
                        http_code=422,
                        status="validation_error",
                        source="input_validation",
                        error_detail=detail,
                    )
                )

        summary = BatchSummaryResponse(
            total_processed=len(outcomes),
            matched_count=matched_count,
            needs_review_count=needs_review_count,
            not_found_count=not_found_count,
            error_count=error_count,
            outcomes=outcomes,
        )

        if req.output_path:
            out_json = Path(req.output_path)
            out_json.parent.mkdir(parents=True, exist_ok=True)
            out_md = out_json.with_suffix(".md")
            summary.output_json_path = str(out_json)
            summary.output_markdown_path = str(out_md)

            out_json.write_text(
                json.dumps(
                    {
                        "summary": summary.model_dump(),
                        "details": full_results,
                    },
                    indent=2,
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            out_md.write_text(self._render_markdown_report(summary), encoding="utf-8")

        return summary

    @staticmethod
    def _render_markdown_report(summary: BatchSummaryResponse) -> str:
        lines = [
            "# Batch Evaluation Report",
            "",
            f"- **Processed:** {summary.total_processed}",
            f"- **Matched:** {summary.matched_count}",
            f"- **Needs review:** {summary.needs_review_count}",
            f"- **Not found (404):** {summary.not_found_count}",
            f"- **Errors:** {summary.error_count}",
            "",
            "| Row | Barcode | Title | Artist | HTTP | Status | Source | Tracks | Confidence | Duration Cov | Performer Cov | Writer Cov | Release URL |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for o in summary.outcomes:
            conf = f"{o.match_confidence:.2f}" if o.match_confidence is not None else "-"
            dur = f"{o.duration_coverage:.0%}" if o.duration_coverage is not None else "-"
            perf = f"{o.performer_coverage:.0%}" if o.performer_coverage is not None else "-"
            wri = f"{o.writer_credit_coverage:.0%}" if o.writer_credit_coverage is not None else "-"
            url = o.release_url or "-"
            lines.append(
                f"| {o.row_number} | {o.barcode or '-'} | {o.album_title} | {o.album_artist} | "
                f"{o.http_code} | {o.status} | {o.source} | {o.track_count} | {conf} | {dur} | {perf} | {wri} | {url} |"
            )
        return "\n".join(lines) + "\n"
