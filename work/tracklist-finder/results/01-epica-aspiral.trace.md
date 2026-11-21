# Schnellweg: 01-epica-aspiral

Ohne Agent, deterministisch.

```
$ MusicBrainz search barcode:(4065629733131): 1 hits
  musicbrainz:release/da26b9bb-57a5-4f13-b80b-b496d258ed40 | Aspiral — Epica | 2025-04-11 US | CD | Official
$ MusicBrainz release da26b9bb-57a5-4f13-b80b-b496d258ed40: 11 tracks, 11 with duration
$ Discogs search barcode=4065629733131 format=None: 1 hits
  discogs:release/33705345 | Aspiral | USA & Europe 2025-04-11 | 11 tracks, 11 with duration
✓ 11 tracks: titles agree, 11 durations in both sources, 0 difference(s) > 2 s (rule: MusicBrainz)
```
