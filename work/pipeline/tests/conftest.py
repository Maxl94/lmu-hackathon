from typing import Any


def make_sample_release(
    release_id: int = 9900001,
    title: str = "Long Player",
    artist: str = "Die Fantastischen Vier",
    barcode: str = "4262459550239",
    extra_track: bool = False,
    formats: list[dict[str, Any]] | None = None,
    data_quality: str = "Correct",
    community_have: int = 85,
    notes: str = "RSD Exklusive edition",
    tracklist: list[dict[str, Any]] | None = None,
    extraartists: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    default_tracklist: list[dict[str, Any]] = [
        {"type_": "heading", "position": "", "title": "CD 1"},
        {
            "type_": "track",
            "position": "1",
            "title": "Track One",
            "duration": "3:30",
            "extraartists": [
                {"id": 501, "name": "Alice Writer", "anv": "", "role": "Lyrics By"}
            ],
        },
        {
            "type_": "track",
            "position": "2",
            "title": "Track Two",
            "duration": "4:15",
        },
        {
            "type_": "index",
            "position": "3",
            "title": "Medley",
            "sub_tracks": [
                {"type_": "track", "position": "3.1", "title": "Part A", "duration": "1:20"},
                {"type_": "track", "position": "3.2", "title": "Part B", "duration": "2:00"},
            ],
        },
    ]
    if extra_track:
        default_tracklist.append(
            {
                "type_": "track",
                "position": "4",
                "title": "Bonus Track",
                "duration": "2:50",
            }
        )

    default_extra = [
        {
            "id": 601,
            "name": "Bob Composer",
            "anv": "",
            "role": "Written-By, Producer [Additional]",
            "tracks": "1-2",
        },
        {
            "id": 602,
            "name": "Global Producer",
            "anv": "",
            "role": "Executive Producer",
            "tracks": "",
        },
        {
            "id": 603,
            "name": "Mystery Credit",
            "anv": "",
            "role": "Composed By",
            "tracks": "Bonus 99",
        },
    ]

    return {
        "id": release_id,
        "master_id": 8800001,
        "uri": f"https://www.discogs.com/release/{release_id}",
        "resource_url": f"https://api.discogs.com/releases/{release_id}",
        "title": title,
        "artists": [{"id": 101, "name": artist, "anv": "", "join": ""}],
        "year": 2024,
        "country": "Germany",
        "formats": (
            formats
            if formats is not None
            else [{"name": "Vinyl", "qty": "1", "descriptions": ["LP", "Record Store Day"]}]
        ),
        "identifiers": [{"type": "Barcode", "value": barcode}] if barcode else [],
        "labels": [{"name": "Test Label", "catno": "TL-001"}],
        "data_quality": data_quality,
        "community": {"status": "Accepted", "have": community_have, "want": 12},
        "notes": notes,
        "extraartists": default_extra if extraartists is None else extraartists,
        "tracklist": default_tracklist if tracklist is None else tracklist,
    }
