---
name: edition-disambiguation
description: Determine the correct edition/pressing of an album when several candidates fit – barcode, format, country, year, label, catalogue number, track count, reissues, censored and unofficial releases.
---

# Determine the correct edition

## Order of criteria
1. **Exact barcode** (after `tl-gtin` normalisation; 12-digit UPC = 13-digit EAN with a leading 0).
   - Caution: one barcode can belong to **several** releases (country pressings, repressings, bootlegs with a copied barcode).
   - The Discogs "Cat#" field is sometimes the barcode without check digit (Sony: `88883716862` ↔ `888837168625`). Do not confuse them.
2. **Format**: CD / vinyl (LP, 12", 2×LP) / cassette (MC). Positions A1/B1 indicate vinyl/cassette.
3. **Country & year**: use input hints (language of the title, German label, EAN prefix 400–440 = assigned in Germany) but do not overweight them.
4. **Label & catalogue number**.
5. **Track count & bonus tracks**: Japanese editions, deluxe, "Exclusive Edition", re-releases often add tracks.
6. **Status**: Official > Promotion > Bootleg/Unofficial.

## Typical traps
- **Reissue ≠ original**: remasters/re-releases can add or **remove** tracks (e.g. indexed/banned songs missing from censored reissues).
- **Digital ≠ physical**: iTunes/Deezer/TIDAL/Bandcamp show the digital version (own UPC, possibly different or bonus tracks). Physical always wins; digital is evidence only. A printed barcode/cat. no. on a back-cover photo (`tl-vision`) proves the physical edition.
- **Release group / master** bundles all editions. To compare: `tl-mb group <rgid>` or `tl-discogs versions <master-id> --format CD`.
- **Discogs notes** (`notes` in `tl-discogs release`) often explain differences explicitly – read them!
- **Samplers/compilations**: give the track artist per track (`artist`), release artist "Various".
- **Multiple media**: 2×CD → `disc` 1/2; vinyl sides stay in `position` (A1…D4).
- **Same title, different series parts** (Folge 1 / Folge 2, Vol. 1 / Vol. 2): if the input does not name the part, it is ambiguous.
- **Same title, different artists** (an artist album and a various-artists box with the same title): if the input has no artist, it is ambiguous.

## Procedure with several candidates
1. Compare the candidates in a table (barcode, format, country, year, label, track count).
2. What the input specifies decides. What the input leaves open does **not** decide – then:
   - The candidates' tracklists do not differ → pick one, `status: found`, the others as `alternatives` ("same tracklist").
   - They differ → `status: ambiguous`, choose the most plausible (official, first release in the input's country), alternatives with `why_not`.
3. In `reasoning` state briefly which criterion was decisive.
