"""Credits pro Track (Komponist, Texter, Autor, Arrangeur, Produzent) + ISRC – deterministisch, ohne KI.

Quelle sind nur die Ausgaben, die das Ergebnis bereits belegt (release.ids):
  MusicBrainz  Aufnahme → Werk → composer/lyricist/writer/arranger; Aufnahme → producer; ISRC der Aufnahme
  Discogs      Track-Credits (Written-By, Music By, Composed By, Lyrics By, Producer, Arranged By)
Zuordnung über die Reihenfolge (Disc, Track) – nur wenn die Trackanzahl übereinstimmt, sonst wird nichts übernommen.
Credits sind getrennt von den ausführenden Künstlern; fehlen sie, bleibt die Liste leer (nicht raten).

  uv run python -m tracklist.credits output/<id>.json      → ergänzt tracks[].credits / tracks[].isrc in der Datei
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from tracklist.cli.discogs import BASE as DG, hdr
from tracklist.cli.mb import BASE as MB, ua
from tracklist.common import get_json

MB_ROLES = {"composer": "composer", "lyricist": "lyricist", "writer": "writer", "arranger": "arranger",
            "librettist": "lyricist", "producer": "producer"}
DG_ROLES = {"written-by": "writer", "music by": "composer", "composed by": "composer", "lyrics by": "lyricist",
            "words by": "lyricist", "producer": "producer", "produced by": "producer", "arranged by": "arranger",
            "songwriter": "writer"}


def _mb_tracks(mbid: str) -> list[list[dict]]:
    r = get_json(f"{MB}/release/{mbid}", headers=ua(), params={
        "inc": "recordings+isrcs+artist-credits+recording-level-rels+work-rels+work-level-rels+artist-rels", "fmt": "json"})
    media = []
    for m in r.get("media") or []:
        tracks = []
        for t in m.get("tracks") or []:
            rec = t.get("recording") or {}
            credits = []
            for rel in rec.get("relations") or []:
                if rel.get("target-type") == "artist" and rel.get("type") in MB_ROLES:
                    credits.append((rel["artist"]["name"], MB_ROLES[rel["type"]]))
                if rel.get("target-type") == "work":
                    for wrel in (rel.get("work") or {}).get("relations") or []:
                        if wrel.get("target-type") == "artist" and wrel.get("type") in MB_ROLES:
                            credits.append((wrel["artist"]["name"], MB_ROLES[wrel["type"]]))
            tracks.append({"credits": credits, "isrc": (rec.get("isrcs") or [None])[0], "ac": t.get("artist-credit"),
                           "number": t.get("number") or t.get("position")})
        media.append(tracks)
    return media


def _merge_artist(res: dict, name: str, role: str, pos: str | None, src: str) -> bool:
    """Künstler in res['artists'] ergänzen (nie doppelt). True, wenn neu."""
    if not name or name.lower() in ("various artists", "various", "va"):
        return False
    arts = res.setdefault("artists", [])
    n1 = name.lower().strip()
    for a in arts:
        n2 = a["name"].lower().strip()
        if n1 == n2 or n1 in n2.split() or n2 in n1.split() or n1.replace(".", "") == n2.replace(".", ""):
            if pos and a.get("tracks") and pos not in a["tracks"]:
                a["tracks"].append(pos)
            if src not in a.setdefault("sources", []):
                a["sources"].append(src)
            return False
    arts.append({"name": name, "role": role, "tracks": [pos] if pos else [], "sources": [src]})
    return True


def _dg_tracks(did: str) -> list[list[tuple[str, str]]]:
    r = get_json(f"{DG}/releases/{did}", headers=hdr())
    out = []
    order = [t.get("position") for t in r.get("tracklist") or [] if t.get("type_") == "track"]

    def positions(spec: str) -> set[str]:
        got = set()
        for part in (spec or "").split(","):
            part = part.strip()
            if " to " in part:
                a, b = (x.strip() for x in part.split(" to ", 1))
                if a in order and b in order:
                    got |= set(order[order.index(a):order.index(b) + 1])
            elif part:
                got.add(part)
        return got
    rel_feat = [(re.sub(r" \(\d+\)$", "", x.get("name") or ""), positions(x.get("tracks")))
                for x in r.get("extraartists") or [] if "featuring" in (x.get("role") or "").lower() and x.get("tracks")]
    rel_cred = []
    for x in r.get("extraartists") or []:
        for role in (x.get("role") or "").split(","):
            k = re.sub(r"\[.*?\]", "", role).strip().lower()
            if k in DG_ROLES and x.get("tracks"):
                rel_cred.append((re.sub(r" \(\d+\)$", "", x.get("name") or ""), DG_ROLES[k], positions(x.get("tracks"))))
    for t in r.get("tracklist") or []:
        if t.get("type_") != "track":
            continue
        cr = []
        for x in t.get("artists") or []:
            cr.append((re.sub(r" \(\d+\)$", "", x.get("name") or x.get("anv") or ""), "performer"))
        for name, pos in rel_feat:
            if t.get("position") in pos:
                cr.append((name, "featured"))
        for name, role, pos in rel_cred:
            if t.get("position") in pos:
                cr.append((name, role))
        for x in t.get("extraartists") or []:
            if "featuring" in (x.get("role") or "").lower():
                cr.append((re.sub(r" \(\d+\)$", "", x.get("name") or x.get("anv") or ""), "featured"))
            for role in (x.get("role") or "").split(","):
                k = role.strip().lower()
                if k in DG_ROLES:
                    cr.append((x.get("anv") or x.get("name"), DG_ROLES[k]))
        out.append(cr)
    return out


def _norm(s: str | None) -> str:
    return re.sub(r"[^a-z0-9äöüß]+", " ", re.sub(r"\(.*?\)|\[.*?\]|feat\..*$", "", (s or "").lower())).strip()


def _mb_other_edition(res: dict, add, skip_id: str | None) -> tuple[int, str | None]:
    """Credits hängen am Werk, nicht an der Ausgabe: andere MusicBrainz-Ausgabe desselben Albums, Zuordnung über den Titel."""
    from rapidfuzz import fuzz
    rel = res.get("release") or {}
    title, artist = rel.get("title") or "", rel.get("artist") or ""
    if not title or not artist or artist.lower().startswith("various"):
        return 0, None
    q = f'release:"{title}" AND artist:"{artist}"'
    cands = get_json(f"{MB}/release", params={"query": q, "fmt": "json", "limit": 8}, headers=ua()).get("releases", [])
    for c in cands[:4]:
        if c["id"] == skip_id or c.get("score", 0) < 85:
            continue
        media = _mb_tracks_titles(c["id"])
        flat = [t for m in media for t in m]
        hits = 0
        src = f"musicbrainz:release/{c['id']}"
        for t in res.get("tracks") or []:
            if t.get("credits"):
                continue
            best = max(flat, key=lambda x: fuzz.ratio(_norm(x["title"]), _norm(t.get("title"))), default=None)
            if best and fuzz.ratio(_norm(best["title"]), _norm(t.get("title"))) >= 90 and best["credits"]:
                for name, role in best["credits"]:
                    add(t, name, role, src)
                hits += 1
        if hits:
            return hits, src
    return 0, None


def _mb_tracks_titles(mbid: str) -> list[list[dict]]:
    media = _mb_tracks(mbid)
    r = get_json(f"{MB}/release/{mbid}", headers=ua(), params={"inc": "recordings", "fmt": "json"})
    for m, mm in zip(media, r.get("media") or []):
        for t, tt in zip(m, mm.get("tracks") or []):
            t["title"] = tt.get("title")
    return media


def _genius(res: dict, add) -> tuple[int, list[str]]:
    """Songwriter/Produzent pro Song von Genius (nur für Tracks ohne Credits; Titel und Künstler müssen passen)."""
    from rapidfuzz import fuzz

    from tracklist.common import env
    token = env("GENIUS_ACCESS_TOKEN")
    if not token:
        return 0, []
    h = {"Authorization": f"Bearer {token}"}
    rel_artist = (res.get("release") or {}).get("artist") or ""
    hits, srcs = 0, []
    for t in res.get("tracks") or []:
        if t.get("credits"):
            continue
        artist = (t.get("artist") or rel_artist or "").split(" feat")[0]
        if not artist or artist.lower().startswith("various"):
            continue
        d = get_json("https://api.genius.com/search", params={"q": f"{t.get('title')} {artist}"}, headers=h)
        song = None
        for hit in (d.get("response") or {}).get("hits") or []:
            s = hit.get("result") or {}
            if (fuzz.ratio(_norm(s.get("title")), _norm(t.get("title"))) >= 88
                    and fuzz.token_set_ratio(_norm((s.get("primary_artist") or {}).get("name")), _norm(artist)) >= 85):
                song = s
                break
        if not song:
            continue
        full = (get_json(f"https://api.genius.com/songs/{song['id']}", headers=h).get("response") or {}).get("song") or {}
        src = f"genius:song/{song['id']}"
        got = False
        for key, role in (("writer_artists", "writer"), ("producer_artists", "producer")):
            for a in full.get(key) or []:
                add(t, a.get("name"), role, src)
                got = True
        if got:
            hits += 1
            srcs.append((src, full.get("url")))
    for src, url in srcs:
        if src not in {s.get("id") for s in res.get("sources") or []}:
            res.setdefault("sources", []).append({"id": src, "url": url, "kind": "database", "note": "song credits (writer/producer)"})
    return hits, [s for s, _ in srcs]


def enrich(res: dict) -> dict:
    """Ergänzt credits/isrc in res['tracks'] und gibt eine Zusammenfassung zurück."""
    rel = res.get("release") or {}
    ids = rel.get("ids") or {}
    tracks = res.get("tracks") or []
    if not tracks:
        return {"credits_tracks": 0, "note": "no tracks"}
    for t in tracks:
        t.setdefault("credits", [])
    notes = []
    added_artists: list[str] = []
    srcs = {s.get("id") for s in res.get("sources") or []}

    def add(t, name, role, src):
        for c in t["credits"]:
            if c["name"].lower() == name.lower() and c["role"] == role:
                if src not in c["sources"]:
                    c["sources"].append(src)
                return
        t["credits"].append({"name": name, "role": role, "sources": [src]})

    if ids.get("musicbrainz"):
        src = f"musicbrainz:release/{ids['musicbrainz']}"
        try:
            media = _mb_tracks(ids["musicbrainz"])
            by_disc: dict[int, list[dict]] = {}
            for t in tracks:
                by_disc.setdefault(t.get("disc") or 1, []).append(t)
            if [len(by_disc.get(i + 1, [])) for i in range(len(media))] == [len(m) for m in media]:
                from tracklist.fasttrack import credited
                main = {a["name"].lower() for a in res.get("artists") or [] if a.get("role") == "main"}
                for i, m in enumerate(media):
                    for t, mt in zip(by_disc[i + 1], m):
                        for name, role in mt["credits"]:
                            add(t, name, role, src)
                        for name, role in credited(mt.get("ac")):  # Sicherheitsnetz: Gast-/Track-Künstler
                            if role == "main" and name.lower() in main:
                                continue
                            added_artists.append(name) if _merge_artist(res, name, role, t.get("position"), src) else None
                        if mt["isrc"] and not t.get("isrc"):
                            t["isrc"] = mt["isrc"]
                if src not in srcs:
                    res.setdefault("sources", []).append({"id": src, "url": f"https://musicbrainz.org/release/{ids['musicbrainz']}",
                                                          "kind": "database", "note": "credits/ISRC"})
            else:
                notes.append("MusicBrainz track count differs per disc – credits not taken over")
        except Exception as e:  # noqa: BLE001
            notes.append(f"MusicBrainz credits failed: {str(e)[:80]}")
    if ids.get("discogs"):
        src = f"discogs:release/{ids['discogs']}"
        try:
            dg = _dg_tracks(str(ids["discogs"]))
            if len(dg) == len(tracks):
                main = {a["name"].lower() for a in res.get("artists") or [] if a.get("role") == "main"}
                for t, cr in zip(tracks, dg):
                    for name, role in cr:
                        if role in ("performer", "featured"):
                            if not (role == "performer" and name.lower() in main):
                                added_artists.append(name) if _merge_artist(
                                    res, name, "featured" if role == "featured" else "main", t.get("position"), src) else None
                            continue
                        add(t, name, role, src)
                if src not in srcs:
                    res.setdefault("sources", []).append({"id": src, "url": f"https://www.discogs.com/release/{ids['discogs']}",
                                                          "kind": "database", "note": "credits"})
            else:
                notes.append("Discogs track count differs – credits not taken over")
        except Exception as e:  # noqa: BLE001
            notes.append(f"Discogs credits failed: {str(e)[:80]}")
    # Credits hängen am Werk: fehlende aus anderer MusicBrainz-Ausgabe und Genius ergänzen
    if any(not t["credits"] for t in tracks):
        try:
            k, src = _mb_other_edition(res, add, ids.get("musicbrainz"))
            if k:
                notes.append(f"credits for {k} tracks from another MusicBrainz edition ({src})")
                if src not in {s.get("id") for s in res.get("sources") or []}:
                    res.setdefault("sources", []).append({"id": src, "url": f"https://musicbrainz.org/release/{src.split('/')[-1]}",
                                                          "kind": "database", "note": "other edition of the same album: work credits"})
        except Exception as e:  # noqa: BLE001
            notes.append(f"MusicBrainz other edition failed: {str(e)[:80]}")
    if any(not t["credits"] for t in tracks):
        try:
            k, _ = _genius(res, add)
            if k:
                notes.append(f"credits for {k} tracks from Genius")
        except Exception as e:  # noqa: BLE001
            notes.append(f"Genius failed: {str(e)[:80]}")
    n = sum(1 for t in tracks if t["credits"])
    res["missing"] = [m for m in res.get("missing") or [] if not m.startswith("credits missing for")]
    if n < len(tracks):
        res.setdefault("missing", [])
        msg = f"credits missing for {len(tracks) - n} of {len(tracks)} tracks"
        if msg not in res["missing"]:
            res["missing"].append(msg)
    if added_artists:
        notes.append(f"artists added from database credits: {', '.join(added_artists[:8])}")
    return {"credits_tracks": n, "isrc_tracks": sum(1 for t in tracks if t.get("isrc")), "notes": notes,
            "artists_added": added_artists}


def main():
    for p in sys.argv[1:]:
        f = Path(p)
        res = json.loads(f.read_text())
        info = enrich(res)
        f.write_text(json.dumps(res, ensure_ascii=False, indent=1))
        print(f"{f.name}: credits for {info['credits_tracks']}/{len(res.get('tracks') or [])} tracks, "
              f"ISRC {info.get('isrc_tracks', 0)}" + (f" · {'; '.join(info.get('notes') or [])}" if info.get("notes") else ""))


if __name__ == "__main__":
    main()
