from typing import Any, Literal
from pydantic import BaseModel, Field, model_validator


class FormatHint(BaseModel):
    medium: str = ""
    qty: int | None = None
    tags: list[str] = Field(default_factory=list)


class NormalizedInput(BaseModel):
    barcode_raw: str = ""
    album_title_raw: str = ""
    album_artist_raw: str = ""
    barcode_norm: str = ""
    barcode_variants: list[str] = Field(default_factory=list)
    title_clean: str = ""
    title_norm: str = ""
    artist_clean: str = ""
    artist_norm: str = ""
    format_hint: FormatHint = Field(default_factory=FormatHint)
    is_compilation: bool = False
    input_hash: str


class LookupRequest(BaseModel):
    barcode: str = ""
    album_title: str = ""
    album_artist: str = ""
    force_refresh: bool = False

    @model_validator(mode="after")
    def validate_has_identifier_or_title(self) -> "LookupRequest":
        digits = "".join(ch for ch in (self.barcode or "") if ch.isdigit())
        has_barcode = bool(digits and set(digits) != {"0"})
        has_title = bool((self.album_title or "").strip())
        if not has_barcode and not has_title:
            raise ValueError(
                "Supply at least a valid non-zero barcode or a non-empty album_title."
            )
        return self


class TrackArtistOut(BaseModel):
    discogs_artist_id: int | None = None
    name: str
    anv: str = ""
    join: str = ""
    inherited: bool = False


class TrackCreditOut(BaseModel):
    discogs_artist_id: int | None = None
    artist_name: str
    anv: str = ""
    role_raw: str
    role_category: str
    credit_source: str


class TrackOut(BaseModel):
    track_order: int
    disc_number: int = 1
    disc_label: str = ""
    position: str = ""
    entry_type: str = "track"
    parent_position: str = ""
    title: str
    duration_raw: str = ""
    duration_sec: int | None = None
    performing_artists: list[TrackArtistOut] = Field(default_factory=list)
    performing_artist_display: str = ""
    has_valid_duration: bool = False
    has_resolved_performer: bool = False
    credits: dict[str, list[TrackCreditOut]] = Field(
        default_factory=lambda: {
            "composers": [],
            "lyricists": [],
            "producers": [],
            "featured": [],
            "other": [],
        }
    )


class ReleaseOut(BaseModel):
    discogs_release_id: int
    master_id: int | None = None
    url: str
    title: str
    artist_display: str = ""
    year: int | None = None
    country: str = ""
    formats: list[dict[str, Any]] = Field(default_factory=list)
    identifiers: list[dict[str, Any]] = Field(default_factory=list)
    labels: list[dict[str, Any]] = Field(default_factory=list)
    data_quality: str = ""
    community_status: str = ""
    community_have: int = 0
    tracklist_hash: str = ""
    unscoped_credits: list[dict[str, Any]] = Field(default_factory=list)


class AlternativeEditionOut(BaseModel):
    discogs_release_id: int
    url: str
    title: str
    artist_display: str = ""
    year: int | None = None
    country: str = ""
    formats: list[dict[str, Any]] = Field(default_factory=list)
    track_count: int = 0
    tracklist_hash: str = ""
    score: float
    match_method: str
    diff_summary: str = ""


class EvaluationOut(BaseModel):
    match_confidence: float
    match_method: str
    candidates_checked: int
    candidates_passing: int = 0
    editions_agree: bool
    track_count: int
    duration_coverage: float
    performer_coverage: float
    writer_credit_coverage: float
    producer_credit_coverage: float
    disc_format_consistent: bool
    discogs_data_quality: str = ""
    review_reasons: list[str] = Field(default_factory=list)
    rejection_reasons: list[str] = Field(default_factory=list)


class LookupSuccessResponse(BaseModel):
    status: Literal["matched", "needs_review"]
    http_code: int = 200
    source: str
    fallback_used: bool = False
    warning: str | None = None
    input_id: int
    normalized_input: NormalizedInput
    release: ReleaseOut
    tracks: list[TrackOut]
    alternatives: list[AlternativeEditionOut] = Field(default_factory=list)
    evaluation: EvaluationOut


class LookupNotFoundResponse(BaseModel):
    status: Literal["not_found"] = "not_found"
    http_code: int = 404
    source: str
    input_id: int
    normalized_input: NormalizedInput
    queries_attempted: list[dict[str, Any]] = Field(default_factory=list)
    candidates_checked: int = 0
    rejection_reasons: list[str] = Field(default_factory=list)


class BatchRequest(BaseModel):
    csv_path: str = "/app/data/development.csv"
    rows: list[int] | None = None
    force_refresh: bool = False
    output_path: str = "/app/outputs/batch_report.json"


class BatchRowOutcome(BaseModel):
    row_number: int
    barcode: str
    album_title: str
    album_artist: str
    http_code: int
    status: str
    source: str
    fallback_used: bool = False
    input_id: int | None = None
    discogs_release_id: int | None = None
    release_url: str | None = None
    track_count: int = 0
    match_confidence: float | None = None
    duration_coverage: float | None = None
    performer_coverage: float | None = None
    writer_credit_coverage: float | None = None
    review_reasons: list[str] = Field(default_factory=list)
    rejection_reasons: list[str] = Field(default_factory=list)
    error_detail: str | None = None


class BatchSummaryResponse(BaseModel):
    total_processed: int
    matched_count: int
    needs_review_count: int
    not_found_count: int
    error_count: int
    output_json_path: str | None = None
    output_markdown_path: str | None = None
    outcomes: list[BatchRowOutcome] = Field(default_factory=list)


class RecordSummaryOut(BaseModel):
    input_id: int
    barcode_raw: str
    album_title_raw: str
    album_artist_raw: str
    barcode_norm: str
    title_norm: str
    artist_norm: str
    format_hint: dict[str, Any] = Field(default_factory=dict)
    is_compilation: bool
    latest_status: str | None = None
    latest_http_code: int | None = None
    latest_source: str | None = None
    selected_release_id: int | None = None
    selected_release_url: str | None = None
    latest_checked_at: str | None = None


class RecordDetailOut(BaseModel):
    record: RecordSummaryOut
    runs: list[dict[str, Any]] = Field(default_factory=list)
    matches: list[dict[str, Any]] = Field(default_factory=list)
    selected_release: ReleaseOut | None = None
    tracks: list[TrackOut] = Field(default_factory=list)


class HealthResponse(BaseModel):
    status: str
    database_ok: bool
    discogs_token_configured: bool
