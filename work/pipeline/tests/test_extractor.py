from app.extractor import (
    classify_role,
    extract_release,
    extracted_track_to_out,
    parse_duration_seconds,
    split_roles,
)
from tests.conftest import make_sample_release


def test_duration_and_role_parsing() -> None:
    assert parse_duration_seconds("3:45") == 225
    assert parse_duration_seconds("1:02:03") == 3723
    assert parse_duration_seconds("0:00") == 0
    assert parse_duration_seconds("") is None
    assert parse_duration_seconds("4:75") is None

    roles = split_roles("Written-By [Track 1, 2], Producer [Co], Lyrics By [German], Guitar")
    assert roles == [
        "Written-By [Track 1, 2]",
        "Producer [Co]",
        "Lyrics By [German]",
        "Guitar",
    ]
    assert [classify_role(r) for r in roles] == [
        "composer",
        "producer",
        "lyricist",
        "other",
    ]
    assert classify_role("Featuring") == "featured"


def test_multidisc_headings_prefixes_vinyl_sides_implicit_reset_and_video_tracks() -> None:
    # 1. Explicit headings
    raw_headings = make_sample_release(
        tracklist=[
            {"type_": "heading", "position": "", "title": "CD 1"},
            {"type_": "track", "position": "1", "title": "One", "duration": "2:00"},
            {"type_": "heading", "position": "", "title": "CD 2"},
            {"type_": "track", "position": "1", "title": "Two", "duration": "2:10"},
        ]
    )
    rel_h = extract_release(raw_headings)
    assert [(t.disc_number, t.disc_label) for t in rel_h.tracks] == [
        (1, "CD 1"),
        (2, "CD 2"),
    ]

    # 2. Disc-prefixed positions
    raw_prefix = make_sample_release(
        tracklist=[
            {"type_": "track", "position": "1-1", "title": "One", "duration": "2:00"},
            {"type_": "track", "position": "CD2-1", "title": "Two", "duration": "2:00"},
            {"type_": "track", "position": "V1", "title": "Enhanced Video", "duration": "3:00"},
        ]
    )
    rel_p = extract_release(raw_prefix)
    assert [t.disc_number for t in rel_p.tracks] == [1, 2, 2]

    # 3. Vinyl sides A/B -> disc 1, C/D -> disc 2
    raw_vinyl = make_sample_release(
        tracklist=[
            {"type_": "track", "position": "A1", "title": "Side A", "duration": "3:00"},
            {"type_": "track", "position": "B2", "title": "Side B", "duration": "3:00"},
            {"type_": "track", "position": "C1", "title": "Side C", "duration": "3:00"},
            {"type_": "track", "position": "D1", "title": "Side D", "duration": "3:00"},
        ]
    )
    rel_v = extract_release(raw_vinyl)
    assert [t.disc_number for t in rel_v.tracks] == [1, 1, 2, 2]

    # 4. 3-disc implicit numeric reset without headings
    raw_reset = make_sample_release(
        tracklist=[
            {"type_": "track", "position": "1", "title": "D1T1", "duration": "2:00"},
            {"type_": "track", "position": "2", "title": "D1T2", "duration": "2:00"},
            {"type_": "track", "position": "1", "title": "D2T1", "duration": "2:00"},
            {"type_": "track", "position": "2", "title": "D2T2", "duration": "2:00"},
            {"type_": "track", "position": "1", "title": "D3T1", "duration": "2:00"},
        ]
    )
    rel_r = extract_release(raw_reset)
    assert [t.disc_number for t in rel_r.tracks] == [1, 1, 2, 2, 3]


def test_subtracks_merge_parent_credits_and_preserve_parent_disc() -> None:
    raw = make_sample_release(
        tracklist=[
            {"type_": "heading", "position": "", "title": "CD 1"},
            {
                "type_": "index",
                "position": "3",
                "title": "Suite",
                "artists": [{"id": 77, "name": "Guest Orchestra (2)", "anv": "Guest Orch", "join": ""}],
                "extraartists": [{"id": 88, "name": "Parent Composer", "anv": "", "role": "Composed By"}],
                "sub_tracks": [
                    {
                        "type_": "track",
                        "position": "3.1",
                        "title": "Movement I",
                        "duration": "1:30",
                        "extraartists": [{"id": 89, "name": "Sub Lyricist", "anv": "", "role": "Lyrics By"}],
                    },
                    {"type_": "track", "position": "3.2", "title": "Movement II", "duration": "2:00"},
                ],
            },
        ],
        extraartists=[],
    )
    rel = extract_release(raw)
    assert rel.track_count == 2
    assert all(t.disc_number == 1 and t.entry_type == "sub_track" and t.parent_position == "3" for t in rel.tracks)
    assert rel.tracks[0].performing_artist_display == "Guest Orch"
    assert rel.tracks[0].performing_artists[0].name == "Guest Orchestra"

    out_0 = extracted_track_to_out(rel.tracks[0])
    assert len(out_0.credits["composers"]) == 1
    assert len(out_0.credits["lyricists"]) == 1


def test_release_level_extraartist_ranges_and_unscoped_fallback() -> None:
    raw = make_sample_release(
        tracklist=[
            {"type_": "track", "position": "01", "title": "One", "duration": "3:00"},
            {"type_": "track", "position": "2", "title": "Two", "duration": "3:00"},
            {"type_": "track", "position": "3", "title": "Three", "duration": "3:00"},
            {"type_": "track", "position": "1-1", "title": "Four", "duration": "3:00"},
            {"type_": "track", "position": "1-2", "title": "Five", "duration": "0:00"},
        ],
        extraartists=[
            {"id": 1, "name": "ZeroPad", "anv": "", "role": "Producer", "tracks": "1"},
            {"id": 2, "name": "EnDash", "anv": "", "role": "Written-By", "tracks": "1–2"},
            {"id": 3, "name": "ToRange", "anv": "", "role": "Lyrics By", "tracks": "2 to 3"},
            {"id": 4, "name": "DiscDash", "anv": "", "role": "Mixed By", "tracks": "1-1 - 1-2"},
            {"id": 5, "name": "Unparsed", "anv": "", "role": "Composed By", "tracks": "Hidden Track"},
        ],
    )
    rel = extract_release(raw)
    assert rel.tracks[0].has_valid_duration is True
    assert rel.tracks[4].has_valid_duration is False

    assert any(c.artist_name == "ZeroPad" for c in rel.tracks[0].credits)
    assert any(c.artist_name == "EnDash" for c in rel.tracks[0].credits)
    assert any(c.artist_name == "EnDash" for c in rel.tracks[1].credits)
    assert any(c.artist_name == "ToRange" for c in rel.tracks[1].credits)
    assert any(c.artist_name == "ToRange" for c in rel.tracks[2].credits)
    assert any(c.artist_name == "DiscDash" for c in rel.tracks[3].credits)
    assert any(c.artist_name == "DiscDash" for c in rel.tracks[4].credits)
    assert len(rel.unscoped_credits) == 1
    assert rel.unscoped_credits[0]["tracks_selector"] == "Hidden Track"


def test_track_artist_join_and_various_detection() -> None:
    raw = make_sample_release(
        artist="Various Artists",
        tracklist=[
            {
                "type_": "track",
                "position": "1",
                "title": "Collab",
                "duration": "4:00",
                "artists": [
                    {"id": 10, "name": "Majid Bekkas", "anv": "", "join": "&"},
                    {"id": 11, "name": "Nguyên Lê", "anv": "", "join": "with"},
                    {"id": 12, "name": "Hamid Drake", "anv": "", "join": ""},
                ],
            },
            {
                "type_": "track",
                "position": "2",
                "title": "Unresolved",
                "duration": "3:00",
            },
        ],
        extraartists=[],
    )
    rel = extract_release(raw)
    assert rel.artist_norm == "various"
    assert rel.tracks[0].performing_artist_display == "Majid Bekkas & Nguyên Lê with Hamid Drake"
    assert rel.tracks[0].has_resolved_performer is True
    assert rel.tracks[1].has_resolved_performer is False
