"""Output contract: result of one research (output/<id>.json). Checked by tl-validate."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class InputSpec(Strict):
    id: str
    title: str | None = None
    artist: str | None = None
    ean: str | None = None
    format: str | None = None
    notes: str | None = None


class Source(Strict):
    id: str = Field(description="e.g. discogs:release/3057907, musicbrainz:release/<mbid>, web:<url>, image:<url>")
    url: str | None = None
    kind: Literal["database", "streaming", "charts", "collector", "shop", "marketplace", "web", "image", "library", "other"] = "database"
    note: str | None = None


class Track(Strict):
    position: str = Field(description="as on the carrier: '1', 'A1', '2-03'")
    disc: int = 1
    title: str
    artist: str | None = Field(default=None, description="only if different from the release artist (compilations)")
    duration_s: int | None = None
    sources: list[str] = Field(default_factory=list, description="source IDs backing title/position")
    duration_sources: list[str] = Field(default_factory=list, description="source IDs backing the duration (only those supporting the chosen value)")
    flags: list[str] = Field(default_factory=list, description="e.g. duration_missing, duration_conflict, title_conflict, bonus, hidden")
    isrc: str | None = Field(default=None, description="ISRC of the recording (filled by the credits step from MusicBrainz)")
    credits: list[Credit] = Field(default_factory=list, description="composer/lyricist/writer/arranger/producer – filled by the "
                                  "deterministic credits step, separate from performing artists")


class Credit(Strict):
    name: str
    role: Literal["composer", "lyricist", "writer", "arranger", "producer", "other"]
    sources: list[str] = Field(default_factory=list)


class Release(Strict):
    title: str
    artist: str | None = None
    format: str | None = None
    country: str | None = None
    year: int | None = None
    label: str | None = None
    catno: str | None = None
    barcode: str | None = None
    edition: str | None = Field(default=None, description="free text, e.g. 'Exclusive 2004 Edition', 'reissue without indexed tracks', '2×CD'")
    ids: dict[str, str] = Field(default_factory=dict, description="{'musicbrainz': mbid, 'discogs': '3057907'}")


class Conflict(Strict):
    field: str
    values: dict[str, str] = Field(description="source ID → value")
    resolution: str | None = None


class Alternative(Strict):
    description: str
    source: str | None = None
    why_not: str | None = None


class ArtistCredit(Strict):
    name: str = Field(description="one artist or group, as credited (no 'feat.' strings – each featured artist is its own entry)")
    role: Literal["main", "featured", "remixer", "other"] = "main"
    tracks: list[str] = Field(default_factory=list, description="positions the artist appears on; empty = whole release")
    sources: list[str] = Field(default_factory=list, description="source IDs backing the credit")


class Result(Strict):
    input: InputSpec
    status: Literal["found", "ambiguous", "not_found"]
    release: Release | None = None
    tracks: list[Track] = Field(default_factory=list)
    artists: list[ArtistCredit] = Field(default_factory=list, description="EVERY distinct artist performing on the carrier, each once: "
                                        "release artist(s), every track artist on compilations, featured artists, remixers")
    total_duration_s: int | None = None
    confidence: float = Field(ge=0, le=1)
    sources: list[Source] = Field(default_factory=list)
    conflicts: list[Conflict] = Field(default_factory=list)
    missing: list[str] = Field(default_factory=list, description="what is missing, e.g. 'duration track 20'")
    alternatives: list[Alternative] = Field(default_factory=list, description="other fitting editions and why they were not chosen")
    reasoning: str = Field(description="short: why exactly this edition")
