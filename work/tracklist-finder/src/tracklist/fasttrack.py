"""Schnellweg ohne Agent: eindeutige Fälle deterministisch in Sekunden lösen.

Bedingungen (alle müssen erfüllt sein, sonst → Agent):
1. EAN vorhanden, Prüfziffer stimmt.
2. MusicBrainz: 1–5 offizielle Ausgaben mit diesem Barcode (nach Format-Filter); bei mehreren (Länderausgaben)
   müssen alle dieselbe Trackliste haben – gewählt wird DE > Europa > die mit den meisten Dauern.
3. Titel/Interpret der Eingabe passen zur gefundenen Ausgabe.
4. Discogs: Ausgabe(n) mit diesem Barcode + Format; alle mit derselben Trackanzahl wie MusicBrainz.
5. Titel stimmen überein, ≥ 90 % der Tracks haben in beiden Quellen eine Dauer, höchstens 10 % weichen > 2 s ab
   (→ feste Regel: MusicBrainz, ms-genau; als Konflikt markiert).
Das Ergebnis ist ein normaler Ausgabevertrag (tl-validate) – die Bewertung (Prüfmodell) läuft danach wie beim Agenten.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from rapidfuzz import fuzz

from tracklist.cli.discogs import BASE as DG, hdr
from tracklist.cli.mb import BASE as MB, credit, ua
from tracklist.common import get_json, parse_duration
from tracklist.scoring import check_digit, digits, norm_format

DG_FORMAT = {"CD": "CD", "Vinyl": "Vinyl", "Kassette": "Cassette"}


def _n(s: str) -> str:
    return re.sub(r"[^a-z0-9äöüß]+", " ", (s or "").lower()).strip()


def _same_title(a: str, b: str) -> bool:
    a, b = _n(a), _n(b)
    return fuzz.token_set_ratio(a, b) >= 90 or fuzz.ratio(a.replace(" ", ""), b.replace(" ", "")) >= 88


def credited(ac) -> list[tuple[str, str]]:
    """MusicBrainz artist-credit → [(name, role)]; wer nach „feat./with/ft.“ kommt, ist featured."""
    out, feat = [], False
    for c in ac or []:
        name = c.get("name") or (c.get("artist") or {}).get("name") or ""
        if name:
            out.append((name, "featured" if feat else "main"))
        # ab „feat./with/mit“ ist alles Weitere Gast – auch hinter „&“ („A feat. B & C“)
        feat = feat or bool(re.search(r"feat|\bft\b|\bwith\b|\bmit\b", c.get("joinphrase") or "", re.I))
    return out


def artist_list(release_ac, tracks: list[dict], src: str) -> list[dict]:
    """Jeder Künstler einmal: Release-Künstler (ganze Ausgabe) + Track-Künstler mit Positionen. „Various Artists“ entfällt."""
    res: dict[str, dict] = {}
    main = {n for n, _ in credited(release_ac) if n.lower() not in ("various artists", "various")}
    for n in main:
        res[n.lower()] = {"name": n, "role": "main", "tracks": [], "sources": [src]}
    for t in tracks:
        for n, role in credited(t.get("ac")):
            if n.lower() in ("various artists", "various") or (n in main and role == "main"):
                continue
            e = res.setdefault(n.lower(), {"name": n, "role": role, "tracks": [], "sources": [src]})
            if e["tracks"] is not None and str(t["number"]) not in e["tracks"] and n not in main:
                e["tracks"].append(str(t["number"]))
    return list(res.values())


def try_fast(case: dict, out: Path, emit=None) -> tuple[bool, list[str]]:
    log: list[str] = []

    def add(msg: str):
        log.append(msg)
        if emit:
            emit(msg)

    def no(reason: str):
        add(f"→ no fast path: {reason}")
        return False, log

    e = digits(case.get("ean"))
    if not e:
        return no("no EAN")
    if len(e) not in (8, 12, 13, 14) or check_digit(e[:-1]) != int(e[-1]):
        return no(f"EAN {e} has a wrong check digit/length – agent should correct it")
    fmt = norm_format(case.get("format"))
    variants = sorted({e, e.lstrip("0"), "0" + e if len(e) == 12 else e})
    q = "barcode:(" + " OR ".join(variants) + ")"
    rels = get_json(f"{MB}/release", params={"query": q, "fmt": "json", "limit": 25}, headers=ua()).get("releases", [])
    add(f"$ MusicBrainz search {q}: {len(rels)} hits")
    for r in rels:
        add(f"  musicbrainz:release/{r['id']} | {r.get('title')} — {credit(r.get('artist-credit'))} | {r.get('date')} "
                   f"{r.get('country')} | {'+'.join(m.get('format') or '?' for m in r.get('media') or [])} | {r.get('status')}")
    rels = [r for r in rels if (r.get("status") or "Official") == "Official"]
    # physisch vor digital: digitale MusicBrainz-Ausgaben nie im Schnellweg
    rels = [r for r in rels if not any(norm_format(m.get("format")) == "Digital" for m in r.get("media") or [])]
    if fmt:
        rels = [r for r in rels if all(norm_format(m.get("format")) == fmt for m in r.get("media") or [{}])]
    if not 1 <= len(rels) <= 5:
        return no(f"{len(rels)} matching official MusicBrainz releases (fast path only for 1–5 identical ones)")

    def mb_tracklist(r):
        out = []
        for m in r.get("media") or []:
            for t in m.get("tracks") or []:
                ms = t.get("length") or (t.get("recording") or {}).get("length")
                out.append({"disc": m.get("position") or 1, "number": t.get("number"), "title": t.get("title"),
                            "artist": credit(t.get("artist-credit")), "ac": t.get("artist-credit"),
                            "dur": round(ms / 1000) if ms else None})
        return out

    full = [get_json(f"{MB}/release/{r['id']}", headers=ua(),
                     params={"inc": "recordings+artist-credits+labels+isrcs+release-groups", "fmt": "json"}) for r in rels]
    lists = [mb_tracklist(r) for r in full]
    if len({len(x) for x in lists}) != 1 or any(not _same_title(a["title"], b["title"])
                                                 for x in lists[1:] for a, b in zip(lists[0], x)):
        return no("MusicBrainz releases with the same barcode have different tracklists")
    order = sorted(range(len(full)), key=lambda i: (full[i].get("country") != "DE", full[i].get("country") not in ("XE", "EU"),
                                                    -sum(1 for t in lists[i] if t["dur"])))
    mbr, mb_tracks = full[order[0]], lists[order[0]]
    mb_others = [full[i] for i in order[1:]]
    rel_artist = credit(mbr.get("artist-credit"))
    if case.get("title") and fuzz.token_set_ratio(_n(case["title"]), _n(mbr.get("title"))) < 85:
        return no(f"input title \"{case['title']}\" ≠ MusicBrainz \"{mbr.get('title')}\"")
    if case.get("artist") and fuzz.token_set_ratio(_n(case["artist"]), _n(rel_artist)) < 85:
        return no(f"input artist \"{case['artist']}\" ≠ MusicBrainz \"{rel_artist}\"")
    add(f"$ MusicBrainz release {mbr['id']}: {len(mb_tracks)} tracks, {sum(1 for t in mb_tracks if t['dur'])} with duration")

    params = {"type": "release", "barcode": e, "per_page": 50}
    if fmt in DG_FORMAT:
        params["format"] = DG_FORMAT[fmt]
    dres = get_json(f"{DG}/database/search", params=params, headers=hdr()).get("results", [])
    if not dres and e.startswith("0"):
        params["barcode"] = e[1:]
        dres = get_json(f"{DG}/database/search", params=params, headers=hdr()).get("results", [])
    add(f"$ Discogs search barcode={params['barcode']} format={params.get('format')}: {len(dres)} hits")
    if not dres:
        return no("no Discogs release with this barcode")
    if len(dres) > 4:
        return no(f"{len(dres)} Discogs releases with this barcode – agent should disambiguate")
    dgs = []
    for d in dres:
        r = get_json(f"{DG}/releases/{d['id']}", headers=hdr())
        tl = r.get("tracklist") or []
        if any(t.get("type_") == "index" or t.get("sub_tracks") for t in tl):
            return no(f"discogs:release/{d['id']} has index/sub-tracks")
        tr = [t for t in tl if t.get("type_") == "track"]
        add(f"  discogs:release/{r['id']} | {r.get('title')} | {r.get('country')} {r.get('released') or r.get('year')} | "
                   f"{len(tr)} tracks, {sum(1 for t in tr if parse_duration(t.get('duration')))} with duration")
        dgs.append((r, tr))
    counts = {len(tr) for _, tr in dgs}
    if counts != {len(mb_tracks)}:
        return no(f"track count MusicBrainz {len(mb_tracks)} vs. Discogs {sorted(counts)}")
    dg, dtr = max(dgs, key=lambda x: sum(1 for t in x[1] if parse_duration(t.get("duration"))))
    both, conflicts_title, dur_conf = 0, [], {}
    for i, (m, d) in enumerate(zip(mb_tracks, dtr), 1):
        if not _same_title(m["title"], d.get("title")):
            return no(f"track {i}: title MusicBrainz \"{m['title']}\" ≠ Discogs \"{d.get('title')}\"")
        if _n(m["title"]) != _n(d.get("title")):
            conflicts_title.append((i, m, d))
        dd = parse_duration(d.get("duration"))
        if m["dur"] and dd:
            if abs(m["dur"] - dd) > 2:
                dur_conf[i] = dd
            both += 1
    if both < 0.9 * len(mb_tracks):
        return no(f"only {both}/{len(mb_tracks)} tracks with a duration in both sources")
    if len(dur_conf) > max(1, int(0.1 * len(mb_tracks))):
        return no(f"{len(dur_conf)} duration differences > 2 s between MusicBrainz and Discogs – agent should resolve")
    add(f"✓ {len(mb_tracks)} tracks: titles agree, {both} durations in both sources, "
               f"{len(dur_conf)} difference(s) > 2 s (rule: MusicBrainz)")

    mb_id, dg_id = f"musicbrainz:release/{mbr['id']}", f"discogs:release/{dg['id']}"
    tracks = []
    for i, (m, d) in enumerate(zip(mb_tracks, dtr), 1):
        dd = parse_duration(d.get("duration"))
        tracks.append({"position": str(m["number"] or i), "disc": m["disc"], "title": m["title"],
                       "artist": m["artist"] if m["artist"] and m["artist"] != rel_artist else None,
                       "duration_s": m["dur"] if m["dur"] is not None else dd,
                       "sources": [mb_id, dg_id],
                       "duration_sources": [mb_id] if i in dur_conf else [x for x, v in ((mb_id, m["dur"]), (dg_id, dd)) if v],
                       "flags": ["duration_conflict"] if i in dur_conf else ([] if (m["dur"] or dd) else ["duration_missing"])})
    media = mbr.get("media") or []
    li = (mbr.get("label-info") or [{}])[0]
    result = {
        "input": {k: v for k, v in case.items() if v and k in ("id", "title", "artist", "ean", "format", "notes")},
        "status": "found",
        "release": {"title": mbr.get("title"), "artist": rel_artist, "format": norm_format(media[0].get("format")) if media else None,
                    "country": mbr.get("country"), "year": int(mbr["date"][:4]) if (mbr.get("date") or "")[:4].isdigit() else None,
                    "label": (li.get("label") or {}).get("name"), "catno": li.get("catalog-number"), "barcode": mbr.get("barcode"),
                    "edition": "; ".join(x for x in (f"{len(media)}×{media[0].get('format')}" if len(media) > 1 else None,
                                                     mbr.get("disambiguation")) if x) or None,
                    "ids": {"musicbrainz": mbr["id"], "discogs": str(dg["id"])}},
        "tracks": tracks,
        "artists": artist_list(mbr.get("artist-credit"), mb_tracks, mb_id),
        "total_duration_s": sum(t["duration_s"] or 0 for t in tracks),
        "confidence": 0.9 if (conflicts_title or dur_conf) else 0.95,
        "sources": [{"id": mb_id, "url": f"https://musicbrainz.org/release/{mbr['id']}", "kind": "database", "note": "durations in ms"},
                    {"id": dg_id, "url": f"https://www.discogs.com/release/{dg['id']}", "kind": "database", "note": None}],
        "conflicts": [{"field": f"title track {i}", "values": {mb_id: m["title"], dg_id: d.get("title")},
                       "resolution": "MusicBrainz spelling (rule: MusicBrainz before Discogs)"} for i, m, d in conflicts_title]
                     + [{"field": f"duration track {tracks[i - 1]['position']}",
                         "values": {mb_id: f"{mb_tracks[i - 1]['dur'] // 60}:{mb_tracks[i - 1]['dur'] % 60:02d}",
                                    dg_id: f"{dd // 60}:{dd % 60:02d}"},
                         "resolution": "MusicBrainz (ms precision) by fixed rule"} for i, dd in dur_conf.items()],
        "missing": [f"duration track {t['position']}" for t in tracks if t["duration_s"] is None],
        "alternatives": [{"description": f"Discogs {r.get('country')} {r.get('released') or r.get('year')}, same tracklist",
                          "source": f"discogs:release/{r['id']}", "why_not": "same barcode and same tracklist - irrelevant for the tracklist"}
                         for r, _ in dgs if r["id"] != dg["id"]]
                        + [{"description": f"MusicBrainz {r.get('country')} {r.get('date')}, same tracklist",
                            "source": f"musicbrainz:release/{r['id']}", "why_not": "same barcode, other country edition - identical tracklist"}
                           for r in mb_others],
        "reasoning": (f"Fast path without agent: barcode {e} matches {len(full)} official MusicBrainz release(s) with the same tracklist and "
                      f"{len(dgs)} Discogs release(s) in format {fmt or 'any'}; track count ({len(tracks)}), titles and "
                      f"durations ({both} tracks in both sources, {len(dur_conf)} difference(s) > 2 s resolved by rule) agree."),
    }
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1))
    return True, log
