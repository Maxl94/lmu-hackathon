# Schnellweg: 05-casper-live-in-bielefeld

Ohne Agent, deterministisch.

```
$ MusicBrainz search barcode:(4251484708203): 1 hits
  musicbrainz:release/ae36f7c7-c498-4a33-b5e0-7b0d1efbac57 | Live in Bielefeld — Casper | 2024-12-12 DE | 12" Vinyl+12" Vinyl+12" Vinyl | Official
$ MusicBrainz release ae36f7c7-c498-4a33-b5e0-7b0d1efbac57: 28 tracks, 28 with duration
$ Discogs search barcode=4251484708203 format=None: 1 hits
  discogs:release/32548602 | Live in Bielefeld | Germany 2024-12-13 | 28 tracks, 28 with duration
✓ 28 tracks: titles agree, 28 durations in both sources, 0 difference(s) > 2 s (rule: MusicBrainz)
```
