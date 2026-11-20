import csv
import hashlib
import json
import logging
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from app.agent_client import (
    AgentFallbackError,
    AgentFallbackProvider,
    AgentTrack,
    extract_discogs_release_ids,
)
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
    QueueJobDetailOut,
    ReleaseOut,
    TrackOut,
)
from app.normalizer import normalize_input, normalize_text
from app.repository import PipelineRepository

logger = logging.getLogger(__name__)


@dataclass
class DiscogsHandoff:
    input_id: int
    norm: NormalizedInput
    queries_attempted: list[dict[str, Any]]
    fetched_ids: set[int]
    candidates_checked: int
    source_label: str
    allow_discogs_bridge: bool
    warning: str | None = None
    discogs_error_detail: str = ""
    discogs_error_http_code: int | None = None
    discogs_error_type: str = ""
    discogs_rejection_reasons: list[str] = field(default_factory=list)
    replace_matches: bool = True

    def to_context_dict(self) -> dict[str, Any]:
        return {
            "input_id": self.input_id,
            "norm": self.norm.model_dump(),
            "queries_attempted": self.queries_attempted,
            "fetched_ids": sorted(self.fetched_ids),
            "candidates_checked": self.candidates_checked,
            "source_label": self.source_label,
            "allow_discogs_bridge": self.allow_discogs_bridge,
            "warning": self.warning,
            "discogs_error_detail": self.discogs_error_detail,
            "discogs_error_http_code": self.discogs_error_http_code,
            "discogs_error_type": self.discogs_error_type,
            "discogs_rejection_reasons": self.discogs_rejection_reasons,
            "replace_matches": self.replace_matches,
        }

    @classmethod
    def from_context_dict(cls, data: dict[str, Any]) -> "DiscogsHandoff":
        return cls(
            input_id=int(data["input_id"]),
            norm=NormalizedInput.model_validate(data["norm"]),
            queries_attempted=list(data.get("queries_attempted") or []),
            fetched_ids={int(x) for x in (data.get("fetched_ids") or [])},
            candidates_checked=int(data.get("candidates_checked") or 0),
            source_label=str(data.get("source_label") or "discogs_live"),
            allow_discogs_bridge=bool(data.get("allow_discogs_bridge", True)),
            warning=data.get("warning"),
            discogs_error_detail=str(data.get("discogs_error_detail") or ""),
            discogs_error_http_code=data.get("discogs_error_http_code"),
            discogs_error_type=str(data.get("discogs_error_type") or ""),
            discogs_rejection_reasons=list(data.get("discogs_rejection_reasons") or []),
            replace_matches=bool(data.get("replace_matches", True)),
        )


@dataclass
class DiscogsStageOutcome:
    completed: LookupSuccessResponse | LookupNotFoundResponse | None = None
    handoff: DiscogsHandoff | None = None


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


def _format_duration_raw(duration_sec: int | None) -> str:
    if duration_sec is None or duration_sec < 0:
        return ""
    if duration_sec >= 3600:
        hours, rem = divmod(duration_sec, 3600)
        mins, secs = divmod(rem, 60)
        return f"{hours}:{mins:02d}:{secs:02d}"
    mins, secs = divmod(duration_sec, 60)
    return f"{mins}:{secs:02d}"


def _agent_tracks_to_track_outs(
    tracks: list[AgentTrack],
) -> tuple[list[tuple[int, TrackOut]], str]:
    has_multi_disc = any(t.disc > 1 for t in tracks)
    numbered: list[tuple[int, TrackOut]] = []
    signature_items: list[list[Any]] = []
    for order, t in enumerate(tracks, start=1):
        pos = f"{t.disc}-{t.number}" if has_multi_disc else str(t.number)
        dur_sec = t.length_sec if (t.length_sec is not None and t.length_sec >= 0) else None
        track_out = TrackOut(
            track_order=order,
            disc_number=t.disc,
            disc_label=f"Disc {t.disc}" if has_multi_disc else "",
            position=pos,
            entry_type="track",
            parent_position="",
            title=t.title,
            duration_raw=_format_duration_raw(dur_sec),
            duration_sec=dur_sec,
            performing_artists=[],
            performing_artist_display="",
            has_valid_duration=dur_sec is not None,
            has_resolved_performer=False,
        )
        numbered.append((t.number, track_out))
        signature_items.append([t.disc, normalize_text(t.title), dur_sec])
    tracklist_hash = hashlib.sha256(
        json.dumps(signature_items, ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    return numbered, tracklist_hash


class LookupService:
    def __init__(
        self,
        repo: PipelineRepository,
        provider: CatalogProvider,
        settings: Settings,
        agent_provider: AgentFallbackProvider | None = None,
    ) -> None:
        self._repo = repo
        self._provider = provider
        self._settings = settings
        self._agent_provider = agent_provider

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
        selected_agent_id = latest_run.get("selected_agent_fallback_id")
        status = "needs_review" if latest_run["status"] == "needs_review" else "matched"
        summary = latest_run.get("evaluation_summary_json") or {}

        if selected_id is None and selected_agent_id is not None:
            loaded = self._repo.get_agent_fallback(int(selected_agent_id))
            if loaded is None:
                return None
            agent_fb, tracks = loaded
            dur_cov = (
                float(summary["duration_coverage"])
                if "duration_coverage" in summary
                else (
                    round(
                        sum(1 for t in tracks if t.has_valid_duration) / len(tracks), 4
                    )
                    if tracks
                    else 0.0
                )
            )
            inferred_discs = max((t.disc_number for t in tracks), default=1)
            disc_consistent = (
                bool(summary["disc_format_consistent"])
                if "disc_format_consistent" in summary
                else not (
                    norm.format_hint.qty
                    and norm.format_hint.qty > 1
                    and inferred_discs < norm.format_hint.qty
                )
            )
            evaluation = EvaluationOut(
                match_confidence=float(summary.get("match_confidence", 0.0)),
                match_method=str(summary.get("match_method", "gemini_agent_search")),
                candidates_checked=int(latest_run.get("candidates_checked", 0)),
                candidates_passing=int(summary.get("candidates_passing", 0)),
                editions_agree=bool(summary.get("editions_agree", False)),
                track_count=len(tracks),
                duration_coverage=dur_cov,
                performer_coverage=float(summary.get("performer_coverage", 0.0)),
                writer_credit_coverage=float(summary.get("writer_credit_coverage", 0.0)),
                producer_credit_coverage=float(summary.get("producer_credit_coverage", 0.0)),
                disc_format_consistent=disc_consistent,
                discogs_data_quality="",
                review_reasons=list(latest_run.get("review_reasons_json") or []),
                rejection_reasons=list(summary.get("rejection_reasons") or []),
            )
            return LookupSuccessResponse(
                status=status,
                http_code=200,
                source=source_override,
                fallback_used=True,
                warning=warning,
                input_id=input_id,
                normalized_input=norm,
                release=None,
                agent_result=agent_fb,
                tracks=tracks,
                alternatives=[],
                evaluation=evaluation,
            )

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
        return LookupSuccessResponse(
            status=status,
            http_code=200,
            source=source_override,
            fallback_used=fallback_used,
            warning=warning,
            input_id=input_id,
            normalized_input=norm,
            release=_release_to_out(selected_rel),
            agent_result=None,
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

    def has_agent_fallback(self) -> bool:
        return self._agent_provider is not None and self._settings.enable_agent_fallback

    def _run_agent_fallback(
        self,
        input_id: int,
        norm: NormalizedInput,
        queries_attempted: list[dict[str, Any]],
        candidates_checked: int,
        already_fetched_ids: set[int],
        force_refresh: bool,
        allow_discogs_bridge: bool,
        source_label: str,
        warning: str | None = None,
        discogs_error_detail: str = "",
        discogs_rejection_reasons: list[str] | None = None,
        replace_matches: bool = True,
        progress_cb: Callable[[str, int | None], None] | None = None,
    ) -> LookupSuccessResponse | None:
        if self._agent_provider is None or not self._settings.enable_agent_fallback:
            return None

        try:
            research_with_progress = getattr(
                self._agent_provider, "research_album_with_progress", None
            )
            if callable(research_with_progress):
                def _on_agent_progress(attempt: int, _total: int, msg: str) -> None:
                    if progress_cb is not None:
                        progress_cb(msg, attempt)

                answer = research_with_progress(
                    norm.barcode_raw,
                    norm.album_title_raw,
                    norm.album_artist_raw,
                    on_progress=_on_agent_progress,
                )
            else:
                if progress_cb is not None:
                    progress_cb(
                        f"Searching via Gemini agent ({self._agent_provider.model_name})",
                        1,
                    )
                answer = self._agent_provider.research_album(
                    norm.barcode_raw, norm.album_title_raw, norm.album_artist_raw
                )
        except AgentFallbackError as exc:
            queries_attempted.append(
                {
                    "tier": "agent_fallback",
                    "model": self._agent_provider.model_name,
                    "error": str(exc),
                }
            )
            return None

        queries_attempted.append(
            {
                "tier": "agent_fallback",
                "model": self._agent_provider.model_name,
                "track_count": len(answer.tracks),
                "sources": answer.sources,
            }
        )
        if not answer.tracks:
            return None

        rejection_reasons = list(discogs_rejection_reasons or [])
        if allow_discogs_bridge:
            bridge_ids = [
                rid
                for rid in extract_discogs_release_ids(answer.sources)
                if rid not in already_fetched_ids
            ][: self._settings.max_candidates_to_fetch]
            if bridge_ids:
                if progress_cb is not None:
                    progress_cb(
                        f"Verifying Discogs release URL(s) {bridge_ids} from agent sources",
                        None,
                    )
                bridged_releases: list[ExtractedRelease] = []
                bridge_methods: dict[int, str] = {}
                bridge_error = False
                for rid in bridge_ids:
                    already_fetched_ids.add(rid)
                    try:
                        raw_rel, _ = self._provider.get_release(
                            rid, bypass_cache=force_refresh
                        )
                    except DiscogsError as exc:
                        bridge_error = True
                        queries_attempted.append(
                            {
                                "tier": "agent_discogs_bridge",
                                "release_ids": bridge_ids,
                                "error": str(exc),
                            }
                        )
                        break
                    if not raw_rel or "id" not in raw_rel:
                        continue
                    extracted = extract_release(raw_rel)
                    self._repo.upsert_release_with_tracks(extracted)
                    bridged_releases.append(extracted)
                    bridge_methods[rid] = "agent_discogs_url"

                if not bridge_error:
                    bridge_bundle = (
                        evaluate_candidates(norm, bridged_releases, bridge_methods)
                        if bridged_releases
                        else None
                    )
                    bridge_matched = (
                        bridge_bundle is not None
                        and bridge_bundle.status != "not_found"
                        and bridge_bundle.selected is not None
                    )
                    queries_attempted.append(
                        {
                            "tier": "agent_discogs_bridge",
                            "release_ids": bridge_ids,
                            "fetched": len(bridged_releases),
                            "matched": bridge_matched,
                        }
                    )
                    if bridge_matched:
                        assert bridge_bundle is not None
                        assert bridge_bundle.selected is not None
                        total_checked = candidates_checked + len(bridged_releases)
                        eval_out = build_evaluation_out(bridge_bundle, total_checked)
                        matches_rows = self._bundle_to_match_rows(bridge_bundle)
                        self._repo.save_matches_and_run(
                            input_id=input_id,
                            status=bridge_bundle.status,
                            http_code=200,
                            source="discogs_via_agent",
                            selected_release_id=bridge_bundle.selected.discogs_release_id,
                            selected_agent_fallback_id=None,
                            queries_attempted=queries_attempted,
                            candidates_checked=total_checked,
                            evaluation_summary=eval_out.model_dump(),
                            review_reasons=eval_out.review_reasons,
                            matches=matches_rows,
                            replace_matches=True,
                        )
                        return LookupSuccessResponse(
                            status=bridge_bundle.status,
                            http_code=200,
                            source="discogs_via_agent",
                            fallback_used=True,
                            warning="Recovered Discogs release via Gemini agent source URL.",
                            input_id=input_id,
                            normalized_input=norm,
                            release=_release_to_out(bridge_bundle.selected),
                            agent_result=None,
                            tracks=[
                                extracted_track_to_out(t)
                                for t in bridge_bundle.selected.tracks
                            ],
                            alternatives=bridge_bundle.alternatives,
                            evaluation=eval_out,
                        )
                    if bridge_bundle is not None:
                        rejection_reasons.extend(bridge_bundle.rejection_reasons)

        numbered_tracks, tracklist_hash = _agent_tracks_to_track_outs(answer.tracks)
        track_outs = [t for _, t in numbered_tracks]
        agent_fb = self._repo.save_agent_fallback(
            input_id=input_id,
            model_name=self._agent_provider.model_name,
            sources=answer.sources,
            tracks=numbered_tracks,
            tracklist_hash=tracklist_hash,
            raw_json=answer.model_dump(),
            input_tokens=answer.input_tokens,
            output_tokens=answer.output_tokens,
            cost_usd=answer.cost_usd,
        )
        valid_dur = sum(1 for t in track_outs if t.has_valid_duration)
        inferred_discs = max((t.disc_number for t in track_outs), default=1)
        disc_consistent = not (
            norm.format_hint.qty
            and norm.format_hint.qty > 1
            and inferred_discs < norm.format_hint.qty
        )
        review_reasons = [
            f"Discovered via Gemini agent search ({self._agent_provider.model_name}); Discogs credits unavailable."
        ]
        if warning:
            review_reasons.append(warning)
        if not disc_consistent:
            review_reasons.append(
                "Inferred disc count in tracklist does not match release format quantity."
            )

        eval_out = EvaluationOut(
            match_confidence=0.0,
            match_method="gemini_agent_search",
            candidates_checked=candidates_checked,
            candidates_passing=0,
            editions_agree=False,
            track_count=len(track_outs),
            duration_coverage=round(valid_dur / len(track_outs), 4),
            performer_coverage=0.0,
            writer_credit_coverage=0.0,
            producer_credit_coverage=0.0,
            disc_format_consistent=disc_consistent,
            discogs_data_quality="",
            review_reasons=review_reasons,
            rejection_reasons=list(dict.fromkeys(rejection_reasons)),
        )
        self._repo.save_matches_and_run(
            input_id=input_id,
            status="needs_review",
            http_code=200,
            source=source_label,
            selected_release_id=None,
            selected_agent_fallback_id=agent_fb.agent_fallback_id,
            queries_attempted=queries_attempted,
            candidates_checked=candidates_checked,
            evaluation_summary=eval_out.model_dump(),
            review_reasons=review_reasons,
            matches=[],
            error_detail=discogs_error_detail,
            replace_matches=replace_matches,
        )
        return LookupSuccessResponse(
            status="needs_review",
            http_code=200,
            source=source_label,
            fallback_used=True,
            warning=warning,
            input_id=input_id,
            normalized_input=norm,
            release=None,
            agent_result=agent_fb,
            tracks=track_outs,
            alternatives=[],
            evaluation=eval_out,
        )

    def run_discogs_stage(
        self,
        req: LookupRequest,
        source_tag: str = "api",
        progress_cb: Callable[[str, int | None], None] | None = None,
    ) -> DiscogsStageOutcome:
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
                        return DiscogsStageOutcome(completed=stored)
                elif latest_run["status"] == "not_found":
                    created_at: datetime = latest_run["created_at"]
                    if created_at.tzinfo is None:
                        created_at = created_at.replace(tzinfo=timezone.utc)
                    cutoff = datetime.now(timezone.utc) - timedelta(
                        hours=self._settings.not_found_ttl_hours
                    )
                    if created_at >= cutoff:
                        summary = latest_run.get("evaluation_summary_json") or {}
                        return DiscogsStageOutcome(
                            completed=LookupNotFoundResponse(
                                http_code=404,
                                source="database_cache",
                                input_id=input_id,
                                normalized_input=norm,
                                queries_attempted=list(
                                    latest_run.get("queries_attempted_json") or []
                                ),
                                candidates_checked=int(
                                    latest_run.get("candidates_checked", 0)
                                ),
                                rejection_reasons=list(
                                    summary.get("rejection_reasons") or []
                                ),
                            )
                        )

            local_hit = self._try_local_cross_input_match(
                input_id=input_id,
                norm=norm,
                source_label="database",
            )
            if local_hit is not None:
                return DiscogsStageOutcome(completed=local_hit)

        # Live/Cached Discogs cascading search
        queries_attempted: list[dict[str, Any]] = []
        candidate_ids: list[int] = []
        candidate_methods: dict[int, str] = {}
        all_from_cache = True

        def _run_search(tier: str, params: dict[str, Any], method: str) -> int:
            nonlocal all_from_cache
            if progress_cb is not None:
                progress_cb(f"Discogs {tier} search", None)
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

        fetched_releases: list[ExtractedRelease] = []
        fetched_ids: set[int] = set()

        try:
            def _fetch_new_candidates(ids_to_consider: list[int]) -> None:
                nonlocal all_from_cache
                newly_fetched = 0
                for rid in ids_to_consider:
                    if rid in fetched_ids:
                        continue
                    if newly_fetched >= self._settings.max_candidates_to_fetch:
                        break
                    fetched_ids.add(rid)
                    if progress_cb is not None:
                        progress_cb(f"Fetching Discogs candidate #{rid}", None)
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
            logger.warning(
                "Discogs stage failed for %s - %s: %s",
                norm.album_artist_raw,
                norm.album_title_raw,
                exc,
            )
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
                        selected_release_id=(
                            fallback_resp.release.discogs_release_id
                            if fallback_resp.release
                            else None
                        ),
                        selected_agent_fallback_id=(
                            fallback_resp.agent_result.agent_fallback_id
                            if fallback_resp.agent_result
                            else None
                        ),
                        queries_attempted=queries_attempted,
                        candidates_checked=fallback_resp.evaluation.candidates_checked,
                        evaluation_summary=fallback_resp.evaluation.model_dump(),
                        review_reasons=fallback_resp.evaluation.review_reasons,
                        matches=[],
                        error_detail=str(exc),
                        replace_matches=False,
                    )
                    return DiscogsStageOutcome(completed=fallback_resp)

            local_fb = self._try_local_cross_input_match(
                input_id=input_id,
                norm=norm,
                source_label="database_fallback",
                fallback_used=True,
                warning=warning_msg,
                error_detail=str(exc),
            )
            if local_fb is not None:
                return DiscogsStageOutcome(completed=local_fb)

            http_code = 503 if isinstance(exc, DiscogsRateLimitError) else 502
            return DiscogsStageOutcome(
                handoff=DiscogsHandoff(
                    input_id=input_id,
                    norm=norm,
                    queries_attempted=queries_attempted,
                    fetched_ids=fetched_ids,
                    candidates_checked=len(fetched_releases),
                    source_label="discogs_live",
                    allow_discogs_bridge=False,
                    warning=f"Live Discogs lookup failed ({exc}); served Gemini agent fallback.",
                    discogs_error_detail=str(exc),
                    discogs_error_http_code=http_code,
                    discogs_error_type=type(exc).__name__,
                    discogs_rejection_reasons=[],
                    replace_matches=False,
                )
            )

        source_label = (
            "discogs_cached"
            if (all_from_cache and not req.force_refresh and queries_attempted)
            else "discogs_live"
        )

        if bundle.status == "not_found" or bundle.selected is None:
            return DiscogsStageOutcome(
                handoff=DiscogsHandoff(
                    input_id=input_id,
                    norm=norm,
                    queries_attempted=queries_attempted,
                    fetched_ids=fetched_ids,
                    candidates_checked=len(fetched_releases),
                    source_label=source_label,
                    allow_discogs_bridge=True,
                    warning=None,
                    discogs_error_detail="",
                    discogs_error_http_code=None,
                    discogs_error_type="",
                    discogs_rejection_reasons=list(bundle.rejection_reasons),
                    replace_matches=True,
                )
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
        return DiscogsStageOutcome(
            completed=LookupSuccessResponse(
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
        )

    def finalize_without_agent(self, handoff: DiscogsHandoff) -> LookupNotFoundResponse:
        if handoff.discogs_error_http_code is not None:
            self._repo.save_matches_and_run(
                input_id=handoff.input_id,
                status="upstream_error",
                http_code=handoff.discogs_error_http_code,
                source="discogs_live",
                selected_release_id=None,
                queries_attempted=handoff.queries_attempted,
                candidates_checked=0,
                evaluation_summary={},
                review_reasons=[],
                matches=[],
                error_detail=handoff.discogs_error_detail,
                replace_matches=False,
            )
            raise UpstreamServiceError(
                status_code=handoff.discogs_error_http_code,
                detail=handoff.discogs_error_detail,
                error_type=handoff.discogs_error_type or "DiscogsError",
            )

        self._repo.save_matches_and_run(
            input_id=handoff.input_id,
            status="not_found",
            http_code=404,
            source=handoff.source_label,
            selected_release_id=None,
            queries_attempted=handoff.queries_attempted,
            candidates_checked=handoff.candidates_checked,
            evaluation_summary={"rejection_reasons": handoff.discogs_rejection_reasons},
            review_reasons=[],
            matches=[],
            replace_matches=handoff.replace_matches,
        )
        return LookupNotFoundResponse(
            http_code=404,
            source=handoff.source_label,
            input_id=handoff.input_id,
            normalized_input=handoff.norm,
            queries_attempted=handoff.queries_attempted,
            candidates_checked=handoff.candidates_checked,
            rejection_reasons=handoff.discogs_rejection_reasons,
        )

    def run_agent_stage(
        self,
        handoff: DiscogsHandoff,
        force_refresh: bool = False,
        progress_cb: Callable[[str, int | None], None] | None = None,
    ) -> LookupSuccessResponse | LookupNotFoundResponse:
        agent_source_label = (
            "gemini_agent_fallback"
            if handoff.discogs_error_http_code is not None
            else "gemini_agent"
        )
        agent_resp = self._run_agent_fallback(
            input_id=handoff.input_id,
            norm=handoff.norm,
            queries_attempted=handoff.queries_attempted,
            candidates_checked=handoff.candidates_checked,
            already_fetched_ids=set(handoff.fetched_ids),
            force_refresh=force_refresh,
            allow_discogs_bridge=handoff.allow_discogs_bridge,
            source_label=agent_source_label,
            warning=handoff.warning,
            discogs_error_detail=handoff.discogs_error_detail,
            discogs_rejection_reasons=handoff.discogs_rejection_reasons,
            replace_matches=handoff.replace_matches,
            progress_cb=progress_cb,
        )
        if agent_resp is not None:
            return agent_resp
        return self.finalize_without_agent(handoff)

    def run_agent_only_for_input(
        self,
        barcode: str,
        album_title: str,
        album_artist: str,
        input_id: int | None = None,
        force_refresh: bool = True,
        source_tag: str = "queue_agent",
        progress_cb: Callable[[str, int | None], None] | None = None,
    ) -> LookupSuccessResponse | LookupNotFoundResponse:
        norm = normalize_input(barcode, album_title, album_artist)
        resolved_input_id = input_id or self._repo.upsert_input_record(
            norm, source_tag=source_tag
        )
        if progress_cb is not None:
            progress_cb("Preparing Gemini agent search", None)
        handoff = DiscogsHandoff(
            input_id=resolved_input_id,
            norm=norm,
            queries_attempted=[],
            fetched_ids=set(),
            candidates_checked=0,
            source_label="agent_only",
            allow_discogs_bridge=True,
            warning=None,
            discogs_error_detail="",
            discogs_error_http_code=None,
            discogs_rejection_reasons=["Direct Gemini agent lookup/retry requested."],
            replace_matches=True,
        )
        return self.run_agent_stage(
            handoff, force_refresh=force_refresh, progress_cb=progress_cb
        )

    def lookup(
        self, req: LookupRequest, source_tag: str = "api"
    ) -> LookupSuccessResponse | LookupNotFoundResponse:
        outcome = self.run_discogs_stage(req, source_tag=source_tag)
        if outcome.completed is not None:
            return outcome.completed
        assert outcome.handoff is not None
        return self.run_agent_stage(outcome.handoff, force_refresh=req.force_refresh)

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
                            discogs_release_id=(
                                result.release.discogs_release_id
                                if result.release
                                else None
                            ),
                            agent_fallback_id=(
                                result.agent_result.agent_fallback_id
                                if result.agent_result
                                else None
                            ),
                            release_url=(
                                result.release.url
                                if result.release
                                else (
                                    result.agent_result.sources[0]
                                    if result.agent_result and result.agent_result.sources
                                    else None
                                )
                            ),
                            agent_sources=(
                                list(result.agent_result.sources)
                                if result.agent_result
                                else []
                            ),
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

    def write_job_reports(self, detail: QueueJobDetailOut) -> tuple[str, str] | None:
        if not detail.job.output_path:
            return None

        outcomes: list[BatchRowOutcome] = []
        matched_count = 0
        needs_review_count = 0
        not_found_count = 0
        error_count = 0

        for item in detail.items:
            if item.stage == "cancelled":
                continue
            status = item.result_status or "not_found"
            if status == "matched":
                matched_count += 1
            elif status == "needs_review":
                needs_review_count += 1
            elif status == "not_found":
                not_found_count += 1
            else:
                error_count += 1

            release_url: str | None = None
            agent_sources: list[str] = []
            if item.selected_release_id is not None:
                rel = self._repo.get_extracted_release(item.selected_release_id)
                release_url = rel.url if rel is not None else None
            elif item.selected_agent_fallback_id is not None:
                fb = self._repo.get_agent_fallback(item.selected_agent_fallback_id)
                if fb is not None:
                    agent_sources = list(fb[0].sources)
                    release_url = agent_sources[0] if agent_sources else None

            outcomes.append(
                BatchRowOutcome(
                    row_number=item.row_number,
                    barcode=item.barcode,
                    album_title=item.album_title,
                    album_artist=item.album_artist,
                    http_code=item.result_http_code or 0,
                    status=status,
                    source=item.result_source or "",
                    fallback_used=(item.result_source or "")
                    in {"gemini_agent", "gemini_agent_fallback", "discogs_via_agent", "database_fallback"},
                    input_id=item.input_id,
                    discogs_release_id=item.selected_release_id,
                    agent_fallback_id=item.selected_agent_fallback_id,
                    release_url=release_url,
                    agent_sources=agent_sources,
                    track_count=item.track_count,
                    error_detail=item.error_detail or None,
                )
            )

        out_json = Path(detail.job.output_path)
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_md = out_json.with_suffix(".md")

        summary = BatchSummaryResponse(
            total_processed=len(outcomes),
            matched_count=matched_count,
            needs_review_count=needs_review_count,
            not_found_count=not_found_count,
            error_count=error_count,
            output_json_path=str(out_json),
            output_markdown_path=str(out_md),
            outcomes=outcomes,
        )
        out_json.write_text(
            json.dumps(
                {
                    "summary": summary.model_dump(),
                    "job": detail.job.model_dump(),
                    "items": [i.model_dump() for i in detail.items],
                },
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        out_md.write_text(self._render_markdown_report(summary), encoding="utf-8")
        return str(out_json), str(out_md)

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
