"""tl-validate <output.json> — checks the result against the output contract (schema + plausibility).

Exit 0 = OK (possibly with WARN), exit 1 = INVALID with a list of errors. Only report done when OK.
Show schema: tl-validate --schema
"""
import json
import sys
from collections import Counter

from pydantic import ValidationError

from tracklist.schema import Result


def check(path: str) -> tuple[list[str], list[str], Result | None]:
    errors, warns = [], []
    try:
        raw = json.load(open(path))
    except FileNotFoundError:
        return [f"file missing: {path}"], [], None
    except ValueError as e:
        return [f"not valid JSON: {e}"], [], None
    try:
        r = Result.model_validate(raw)
    except ValidationError as e:
        return [f"{'.'.join(str(x) for x in err['loc'])}: {err['msg']}" for err in e.errors()][:25], [], None

    src_ids = {s.id for s in r.sources}
    if r.status == "found":
        if not r.release:
            errors.append("status=found but release is missing")
        if not r.tracks:
            errors.append("status=found but tracks are empty")
        if not r.sources:
            errors.append("status=found but no sources")
    if r.status == "ambiguous" and not r.alternatives:
        errors.append("status=ambiguous: fill alternatives (which editions are possible?)")
    if r.status == "not_found" and not r.missing:
        warns.append("status=not_found: record in missing what is missing / what was searched")

    if r.tracks and not r.artists:
        errors.append("artists is empty: list every distinct artist on the carrier (main, featured, remixer), each once")
    names = [a.name.strip().lower() for a in r.artists]
    dupa = sorted({n for n in names if names.count(n) > 1})
    if dupa:
        errors.append(f"artists listed twice: {dupa} (one entry per artist; list all track positions there)")
    for a in r.artists:
        if any(x in a.name.lower() for x in (" feat. ", " feat ", " ft. ", " featuring ")):
            errors.append(f"artist '{a.name}' contains a featuring string – split it into separate entries (role featured)")
        unknown = [s for s in a.sources if s not in src_ids]
        if unknown:
            errors.append(f"artist '{a.name}': source IDs not in sources: {unknown}")
    dup = [k for k, n in Counter((t.disc, t.position) for t in r.tracks).items() if n > 1]
    if dup:
        errors.append(f"duplicate positions: {dup}")
    for t in r.tracks:
        ref = f"Track {t.position} ({t.title[:30]})"
        unknown = [s for s in t.sources + t.duration_sources if s not in src_ids]
        if unknown:
            errors.append(f"{ref}: source IDs not in sources: {unknown}")
        if not t.sources:
            errors.append(f"{ref}: no sources")
        if t.duration_s is None:
            if "duration_missing" not in t.flags and not any(t.position in m or t.title in m for m in r.missing):
                errors.append(f"{ref}: duration missing → set flag 'duration_missing' and list it in missing")
        else:
            if not (5 <= t.duration_s <= 3600):
                errors.append(f"{ref}: implausible duration {t.duration_s} s")
            if not t.duration_sources:
                errors.append(f"{ref}: duration_sources empty")
    durs = [t.duration_s for t in r.tracks if t.duration_s is not None]
    if r.total_duration_s is not None and durs and len(durs) == len(r.tracks):
        if abs(sum(durs) - r.total_duration_s) > max(3, len(durs)):
            errors.append(f"total_duration_s {r.total_duration_s} ≠ sum of tracks {sum(durs)}")
    if r.status == "found" and len({s.id.split('/')[0].split(':')[0] for s in r.sources}) < 2:
        warns.append("only one source (type) – cross-check with a second independent source if possible")
    if r.status == "found" and r.confidence > 0.9 and r.conflicts:
        warns.append("high confidence despite open conflicts – justify or lower it")
    return errors, warns, r


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)
    if sys.argv[1] == "--schema":
        print(json.dumps(Result.model_json_schema(), indent=1, ensure_ascii=False))
        return
    errors, warns, r = check(sys.argv[1])
    assert r is not None or errors
    for w in warns:
        print(f"WARN: {w}")
    if errors:
        print("INVALID:")
        print("\n".join(f"- {e}" for e in errors))
        sys.exit(1)
    assert r is not None
    n_dur = sum(1 for t in r.tracks if t.duration_s is not None)
    print(f"OK: status={r.status}, {len(r.tracks)} tracks ({n_dur} with duration), {len(r.sources)} sources, "
          f"{len(r.conflicts)} conflicts, confidence={r.confidence}")


if __name__ == "__main__":
    main()
