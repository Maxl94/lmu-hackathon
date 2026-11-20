import logging
import threading
from typing import Any

from pydantic import ValidationError

from app.config import Settings
from app.models import (
    LookupNotFoundResponse,
    LookupRequest,
    LookupSuccessResponse,
)
from app.repository import PipelineRepository
from app.service import DiscogsHandoff, LookupService, UpstreamServiceError

logger = logging.getLogger(__name__)


class QueueManager:
    """PostgreSQL-backed two-stage worker pools for Discogs (serial) and Gemini Agent (parallel)."""

    def __init__(
        self,
        repo: PipelineRepository,
        service: LookupService,
        settings: Settings,
    ) -> None:
        self._repo = repo
        self._service = service
        self._settings = settings
        self._stop_event = threading.Event()
        self._discogs_wakeup = threading.Event()
        self._agent_wakeup = threading.Event()
        self._threads: list[threading.Thread] = []
        self._lifecycle_lock = threading.Lock()
        self._running = False

    @property
    def is_running(self) -> bool:
        return self._running

    @property
    def discogs_worker_count(self) -> int:
        return max(1, self._settings.discogs_queue_concurrency)

    @property
    def agent_worker_count(self) -> int:
        return max(1, self._settings.agent_queue_concurrency)

    def start(self) -> None:
        with self._lifecycle_lock:
            if self._running:
                return
            recovered = self._repo.recover_stale_queue_items()
            if recovered:
                logger.info("Recovered %s stale queue item(s) from previous run", recovered)

            self._stop_event.clear()
            self._discogs_wakeup.clear()
            self._agent_wakeup.clear()
            self._threads = []

            for idx in range(1, self.discogs_worker_count + 1):
                name = f"discogs-{idx}"
                t = threading.Thread(
                    target=self._discogs_loop,
                    args=(name,),
                    name=name,
                    daemon=True,
                )
                self._threads.append(t)
                t.start()

            for idx in range(1, self.agent_worker_count + 1):
                name = f"agent-{idx}"
                t = threading.Thread(
                    target=self._agent_loop,
                    args=(name,),
                    name=name,
                    daemon=True,
                )
                self._threads.append(t)
                t.start()

            self._running = True
            logger.info(
                "QueueManager started (%s Discogs worker(s), %s Agent worker(s))",
                self.discogs_worker_count,
                self.agent_worker_count,
            )

    def stop(self, timeout: float = 5.0) -> None:
        with self._lifecycle_lock:
            if not self._running:
                return
            self._stop_event.set()
            self._discogs_wakeup.set()
            self._agent_wakeup.set()
            threads = list(self._threads)
            self._running = False

        for t in threads:
            t.join(timeout=timeout)
        self._threads.clear()
        logger.info("QueueManager stopped")

    def notify_discogs(self) -> None:
        self._discogs_wakeup.set()

    def notify_agent(self) -> None:
        self._agent_wakeup.set()

    def notify_all(self) -> None:
        self._discogs_wakeup.set()
        self._agent_wakeup.set()

    def _discogs_loop(self, worker_name: str) -> None:
        poll_sec = max(0.05, float(self._settings.queue_poll_interval_sec))
        while not self._stop_event.is_set():
            try:
                item = self._repo.claim_next_queue_item(
                    from_stage="queued_discogs",
                    to_stage="checking_discogs",
                    worker_name=worker_name,
                    status_message="Starting Discogs lookup",
                )
            except Exception:
                logger.exception("[%s] Error claiming Discogs queue item", worker_name)
                self._stop_event.wait(poll_sec)
                continue

            if item is None:
                self._discogs_wakeup.wait(timeout=poll_sec)
                self._discogs_wakeup.clear()
                continue

            self._process_discogs_item(worker_name, item)

    def _agent_loop(self, worker_name: str) -> None:
        poll_sec = max(0.05, float(self._settings.queue_poll_interval_sec))
        while not self._stop_event.is_set():
            try:
                item = self._repo.claim_next_queue_item(
                    from_stage="queued_agent",
                    to_stage="checking_agent",
                    worker_name=worker_name,
                    status_message="Starting Gemini agent lookup",
                )
            except Exception:
                logger.exception("[%s] Error claiming Agent queue item", worker_name)
                self._stop_event.wait(poll_sec)
                continue

            if item is None:
                self._agent_wakeup.wait(timeout=poll_sec)
                self._agent_wakeup.clear()
                continue

            self._process_agent_item(worker_name, item)

    def _finalize_job_report(self, job_id: int) -> None:
        try:
            detail = self._repo.get_queue_job(job_id)
            if detail is None or not detail.job.output_path:
                return
            paths = self._service.write_job_reports(detail)
            if paths is not None:
                self._repo.set_queue_job_report_paths(job_id, paths[0], paths[1])
                logger.info("Job #%s wrote reports to %s and %s", job_id, paths[0], paths[1])
        except Exception:
            logger.exception("Failed writing reports for completed job #%s", job_id)

    def _complete_from_response(
        self,
        item_id: int,
        job_id: int,
        res: LookupSuccessResponse | LookupNotFoundResponse,
    ) -> bool:
        if isinstance(res, LookupSuccessResponse):
            rel_id = res.release.discogs_release_id if res.release else None
            fb_id = res.agent_result.agent_fallback_id if res.agent_result else None
            return self._repo.complete_queue_item(
                item_id=item_id,
                job_id=job_id,
                input_id=res.input_id,
                result_status=res.status,
                result_http_code=200,
                result_source=res.source,
                selected_release_id=rel_id,
                selected_agent_fallback_id=fb_id,
                track_count=len(res.tracks),
                status_message=f"Completed via {res.source} ({res.status})",
                error_detail=res.warning or "",
            )

        return self._repo.complete_queue_item(
            item_id=item_id,
            job_id=job_id,
            input_id=res.input_id,
            result_status="not_found",
            result_http_code=404,
            result_source=res.source,
            track_count=0,
            status_message=f"Not found ({res.source})",
            error_detail="; ".join(res.rejection_reasons[:3]),
        )

    def _process_discogs_item(self, worker_name: str, item: dict[str, Any]) -> None:
        item_id = int(item["id"])
        job_id = int(item["job_id"])
        barcode = str(item.get("barcode") or "")
        title = str(item.get("album_title") or "")
        artist = str(item.get("album_artist") or "")
        logger.info(
            "[%s] Claimed item #%s (job #%s): %s - %s",
            worker_name,
            item_id,
            job_id,
            artist,
            title,
        )

        try:
            req = LookupRequest(
                barcode=barcode,
                album_title=title,
                album_artist=artist,
                force_refresh=bool(item.get("force_refresh", False)),
            )
        except ValidationError as exc:
            just_finished = self._repo.complete_queue_item(
                item_id=item_id,
                job_id=job_id,
                input_id=item.get("input_id"),
                result_status="validation_error",
                result_http_code=422,
                result_source="input_validation",
                status_message="Validation error",
                error_detail=str(exc),
            )
            if just_finished:
                self._finalize_job_report(job_id)
            return

        def _progress(msg: str, attempt: int | None) -> None:
            self._repo.update_queue_item_progress(item_id, msg, attempt=attempt)

        try:
            outcome = self._service.run_discogs_stage(
                req,
                source_tag=f"queue_job_{job_id}_row_{item['row_number']}",
                progress_cb=_progress,
            )
            if outcome.completed is not None:
                just_finished = self._complete_from_response(
                    item_id, job_id, outcome.completed
                )
                if just_finished:
                    self._finalize_job_report(job_id)
                return

            assert outcome.handoff is not None
            handoff = outcome.handoff
            if self._service.has_agent_fallback():
                msg = (
                    f"Discogs failed ({handoff.discogs_error_http_code}); queued for Gemini agent"
                    if handoff.discogs_error_http_code is not None
                    else "Discogs missed; queued for Gemini agent"
                )
                handed_off, just_finished = self._repo.handoff_item_to_agent(
                    item_id=item_id,
                    job_id=job_id,
                    input_id=handoff.input_id,
                    context=handoff.to_context_dict(),
                    status_message=msg,
                )
                if handed_off:
                    logger.info(
                        "[%s] Handed off item #%s (job #%s) -> queued_agent",
                        worker_name,
                        item_id,
                        job_id,
                    )
                    self.notify_agent()
                elif just_finished:
                    self._finalize_job_report(job_id)
                return

            try:
                nf_resp = self._service.finalize_without_agent(handoff)
                just_finished = self._complete_from_response(item_id, job_id, nf_resp)
            except UpstreamServiceError as exc:
                just_finished = self._repo.complete_queue_item(
                    item_id=item_id,
                    job_id=job_id,
                    input_id=handoff.input_id,
                    result_status="upstream_error",
                    result_http_code=exc.status_code,
                    result_source="discogs_live",
                    status_message=f"Discogs error ({exc.status_code})",
                    error_detail=exc.detail,
                )
            if just_finished:
                self._finalize_job_report(job_id)
        except Exception as exc:
            logger.exception("[%s] Unexpected failure on item #%s", worker_name, item_id)
            just_finished = self._repo.complete_queue_item(
                item_id=item_id,
                job_id=job_id,
                input_id=item.get("input_id"),
                result_status="upstream_error",
                result_http_code=500,
                result_source="worker_error",
                status_message="Worker error",
                error_detail=str(exc),
            )
            if just_finished:
                self._finalize_job_report(job_id)

    def _process_agent_item(self, worker_name: str, item: dict[str, Any]) -> None:
        item_id = int(item["id"])
        job_id = int(item["job_id"])
        mode = str(item.get("mode") or "full")
        logger.info(
            "[%s] Claimed agent item #%s (job #%s, mode=%s): %s - %s",
            worker_name,
            item_id,
            job_id,
            mode,
            item.get("album_artist") or "",
            item.get("album_title") or "",
        )

        def _progress(msg: str, attempt: int | None) -> None:
            self._repo.update_queue_item_progress(item_id, msg, attempt=attempt)

        try:
            if mode == "agent_only":
                res = self._service.run_agent_only_for_input(
                    barcode=str(item.get("barcode") or ""),
                    album_title=str(item.get("album_title") or ""),
                    album_artist=str(item.get("album_artist") or ""),
                    input_id=item.get("input_id"),
                    force_refresh=bool(item.get("force_refresh", True)),
                    source_tag=f"queue_job_{job_id}_row_{item['row_number']}",
                    progress_cb=_progress,
                )
            else:
                handoff = DiscogsHandoff.from_context_dict(item.get("context_json") or {})
                res = self._service.run_agent_stage(
                    handoff,
                    force_refresh=bool(item.get("force_refresh", False)),
                    progress_cb=_progress,
                )

            just_finished = self._complete_from_response(item_id, job_id, res)
            logger.info(
                "[%s] Finished agent item #%s (job #%s): status=%s source=%s",
                worker_name,
                item_id,
                job_id,
                res.status,
                res.source,
            )
        except UpstreamServiceError as exc:
            just_finished = self._repo.complete_queue_item(
                item_id=item_id,
                job_id=job_id,
                input_id=item.get("input_id"),
                result_status="upstream_error",
                result_http_code=exc.status_code,
                result_source="discogs_live",
                status_message=f"Discogs & agent failed ({exc.status_code})",
                error_detail=exc.detail,
            )
        except Exception as exc:
            logger.exception("[%s] Unexpected failure on agent item #%s", worker_name, item_id)
            just_finished = self._repo.complete_queue_item(
                item_id=item_id,
                job_id=job_id,
                input_id=item.get("input_id"),
                result_status="upstream_error",
                result_http_code=500,
                result_source="worker_error",
                status_message="Agent worker error",
                error_detail=str(exc),
            )

        if just_finished:
            self._finalize_job_report(job_id)
