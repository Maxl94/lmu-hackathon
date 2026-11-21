# Schnellweg: 10-calexico-the-black-light

Ohne Agent, deterministisch.

```
$ MusicBrainz search barcode:(4027795500399): 1 hits
  musicbrainz:release/a4a09112-9569-4f65-97cc-f0aa66aa3839 | The Black Light — Calexico | 1998-05-18 DE | CD | Official
$ MusicBrainz release a4a09112-9569-4f65-97cc-f0aa66aa3839: 17 tracks, 17 with duration
$ Discogs search barcode=4027795500399 format=None: 1 hits
  discogs:release/11507547 | The Black Light | Germany 2016 | 17 tracks, 17 with duration
✓ 17 tracks: titles agree, 17 durations in both sources, 1 difference(s) > 2 s (rule: MusicBrainz)
```
