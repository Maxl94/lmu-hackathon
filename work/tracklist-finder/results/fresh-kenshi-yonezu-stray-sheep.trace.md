# Agent-Trace: fresh-kenshi-yonezu-stray-sheep

> Schnellweg geprüft: no fast path: no EAN
Start 2026-11-20T16:51:07 · 15 Schritte · 20 Tool-Aufrufe · Tokens in 56969 / out 9264


> **Agent** +0s: I'll start by checking the input and searching for candidates.

### 1. `shell` +1s – completed

```
bin/tl-discogs search --title "STRAY SHEEP" --artist "Kenshi Yonezu" --format CD 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
5 hits (parameters: {'release_title': 'STRAY SHEEP', 'artist': 'Kenshi Yonezu', 'format': 'CD'})
discogs:release/15728633 | Kenshi Yonezu - Stray Sheep | 2020 Japan | CD, Album, Stereo | Label Reissue Records, Sony Music Labels Inc. | Kat.-Nr. SECL 2598 | Barcodes 4547366457933, LLDS-8767 1, IFPI L275 | master 1828690
discogs:release/30395246 | Kenshi Yonezu - Stray Sheep | 2020 Japan | CD, Album, Limited Edition, Stereo, DVD, DVD-Video | Label Reissue Records, Sony Music Labels Inc. | Kat.-Nr. SECL 2595-7 | Barcodes 4547366457919 | master 1828690
discogs:release/30395297 | Kenshi Yonezu - Stray Sheep | 2020 Japan | Box Set, CD, Album, Limited Edition | Label Reissue Records, Sony Music Labels Inc. | Kat.-Nr. SECL 2590-1 | Barcodes 4547366457902 | master 1828690
discogs:release/16115694 | Kenshi Yonezu - Stray Sheep | 2020 Japan | CD, Album, Limited Edition, Stereo, Blu-ray, Album, Stereo | Label Reissue Records, Sony Music Labels Inc. | Kat.-Nr. SECL 2592-4 | Barcodes 4547366457926 | master 1828690
discogs:release/37170435 | Kenshi Yonezu = 米津玄师* - Stray Sheep = 迷途之羊 | 2025 China | CD, Album, Stereo | Label Starsing Records, Sony Music | Kat.-Nr. 19439803992 | Barcodes 9787798443370, 9 787798 443370 > | master 1828690
```
</details>

### 2. `shell` +4s – completed

```
bin/tl-mb search --title "STRAY SHEEP" --artist "Kenshi Yonezu" --format CD 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
1 Releases (Queries: release:"STRAY SHEEP" AND artist:"Kenshi Yonezu")
musicbrainz:release/a39ee600-43e3-4c8d-b369-f28b7d8a0dfe | STRAY SHEEP — Kenshi Yonezu | 2020-08-05 XW | Digital Media | Tracks 15 | Barcode 886448632375 | Sony Music Labels Inc. | Official | score 100
```
</details>

### 3. `shell` +7s – completed

```
bin/tl-mb release a39ee600-43e3-4c8d-b369-f28b7d8a0dfe 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/a39ee600-43e3-4c8d-b369-f28b7d8a0dfe | STRAY SHEEP — Kenshi Yonezu | 2020-08-05 XW | Digital Media | Tracks 15 | Barcode 886448632375 | Sony Music Labels Inc. | Official
release-group: 7bf1777c-48b4-491d-aaea-1405c8dd8845 (Album, first date 2020-08-05) | Cover: front=True back=False images=1
url: https://musicbrainz.org/release/a39ee600-43e3-4c8d-b369-f28b7d8a0dfe
-- Medium 1: Digital Media, 15 Tracks
1.1 [1] Campanella | 3:56 (235720 ms) | ISRC JPU902001654
1.2 [2] Flamingo | 3:16 (196386 ms) | ISRC JPU901803148
1.3 [3] Kanden | 4:25 (264533 ms) | ISRC JPU902001053
1.4 [4] PLACEBO — Kenshi Yonezu + Yojiro Noda | 4:00 (240253 ms) | ISRC JPU902001655
1.5 [5] Paprika | 3:23 (202666 ms) | ISRC JPU901902183
1.6 [6] Uma to Shika | 4:25 (265333 ms) | ISRC JPU901902002
1.7 [7] Yasashii Hito | 3:29 (208853 ms) | ISRC JPU902001656
1.8 [8] Lemon | 4:16 (255826 ms) | ISRC JPU901800227
1.9 [9] Machigai Sagashi | 4:27 (267453 ms) | ISRC JPU902001657
1.10 [10] Himawari | 4:02 (242026 ms) | ISRC JPU902001658
1.11 [11] Stray Sheep | 3:47 (226733 ms) | ISRC JPU902001659
1.12 [12] Décolleté | 3:30 (209573 ms) | ISRC JPU902001660
1.13 [13] TEENAGE RIOT | 3:45 (225213 ms) | ISRC JPU901803149
1.14 [14] Spirits of the Sea | 3:54 (234466 ms) | ISRC JPU901901328
1.15 [15] Canary | 4:58 (298373 ms) | ISRC JPU902001661
Total: 59:33 (3573 s), tracks without duration: 0
```
</details>

### 4. `shell` +7s – completed

```
bin/tl-discogs release 15728633 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
discogs:release/15728633 | Stray Sheep — Kenshi Yonezu | 2020-08-05 Japan | 1× CD (Album, Stereo) | Reissue Records SECL 2598 | master 1828690
url: https://www.discogs.com/release/15728633-Kenshi-Yonezu-Stray-Sheep
identifiers: Barcode: 4547366457933 (From OBI) | Matrix / Runout: LLDS-8767 1 | Mastering SID Code: IFPI L275 | Mould SID Code: IFPI 4562 | Rights Society: JASRAC | Price Code: ¥3,000+税
1 カムパネルラ | duration missing | credits: Vocals, Guitar: Kenshi Yonezu
2 Flamingo | duration missing | credits: Vocals, Guitar: Kenshi Yonezu
3 感電 | duration missing | credits: Vocals: Kenshi Yonezu
4 Placebo | duration missing | credits: Vocals: Yojiro Noda; Vocals, Guitar: Kenshi Yonezu
5 パプリカ | duration missing | credits: Vocals: Kenshi Yonezu
6 馬と鹿 | duration missing | credits: Vocals, Guitar: Kenshi Yonezu
7 優しい人 | duration missing | credits: Vocals: Kenshi Yonezu
8 Lemon | duration missing | credits: Vocals, Guitar: Kenshi Yonezu
9 まちがいさがし | duration missing
10 ひまわり | duration missing
11 迷える羊 | duration missing
12 Décolleté | duration missing
13 Teenage Riot | duration missing
14 海の幽霊 | duration missing
15 カナリヤ | duration missing
15 tracks, total 0:00 (0 s), without duration: 15
images: primary https://i.discogs.com/PqR1FNXdiMe8vLBWwgO5CV1tHWNu_MI6FSQPISFquJA/rs:fit/g:sm/q:90/h:525/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1NzI4/NjMzLTE3MzkyMDM4/MjAtNjI5MC5qcGVn.jpeg | secondary https://i.discogs.com/WTmSPjrHVH0bUSFnfyUIZhBXErJJ5H_LYv60Jl3lemM/rs:fit/g:sm/q:90/h:528/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1NzI4/NjMzLTE3MzkyMDM4/MTktODQ5NS5qcGVn.jpeg | secondary https://i.discogs.com/4MHJtvaffZxrVYbJcixfq9SRmutz6_xyUjiNFEaXgTM/rs:fit/g:sm/q:90/h:593/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1NzI4/NjMzLTE3MjkxMDI3/NzgtNjU0My5qcGVn.jpeg | secondary https://i.discogs.com/mt6ffOClP7FSeb_FMUfJYPATcockXTa4wZ48Y2QNRe4/rs:fit/g:sm/q:90/h:469/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1NzI4/NjMzLTE3MjkxMDI3/NzgtNDc4Ni5qcGVn.jpeg | secondary https://i.discogs.com/r_KKw5i5HIDvqDNQB0PwYxBrUeLDGGUb8iCqZ0czjKw/rs:fit/g:sm/q:90/h:598/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1NzI4/NjMzLTE3MjkxMDI3/NzctNTYxMy5qcGVn.jpeg | secondary https://i.discogs.com/RpGAOEuXj3QSCymcWNPAM73wDe93ZGm4QEkLjqM9g5s/rs:fit/g:sm/q:90/h:593/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE1NzI4/NjMzLTE3MjkxMDI3/NzgtNTY5OC5qcGVn.jpeg
community: have 169 want 72 data_quality Needs Vote
```
</details>

### 5. `shell` +11s – completed

```
bin/tl-mb group 7bf1777c-48b4-491d-aaea-1405c8dd8845 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
9 Releases in release-group 7bf1777c-48b4-491d-aaea-1405c8dd8845
musicbrainz:release/3d0f6897-732b-472f-b629-cdc1953665fc | STRAY SHEEP —  | 2020-08-05 JP | CD+DVD-Video | Tracks 15+27 | Barcode 4547366457919 | Sony Music Labels Inc. SECL-2595; Sony Music Labels Inc. SECL-2596; Sony Music Labels Inc. SECL-2597 | Official | アートブック盤
musicbrainz:release/47b913af-471a-4c7a-8c06-4eb0a2fc9c2e | STRAY SHEEP —  | 2020-08-05 JP | CD | Tracks 15 | Barcode 4547366457902 | Sony Music Labels Inc. SECL-2590; Sony Music Labels Inc. SECL-2591 | Official | おまもり盤
musicbrainz:release/4a2c0fa1-7d3b-47eb-8fb7-9c8dd9a3f1e4 | STRAY SHEEP —  | 2020-08-05 JP | CD+Blu-ray | Tracks 15+27 | Barcode 4547366457926 | Sony Music Labels Inc. SECL-2592; Sony Music Labels Inc. SECL-2593; Sony Music Labels Inc. SECL-2594 | Official | アートブック盤
musicbrainz:release/8b6206c8-2a76-4e84-acbe-6588935d6316 | STRAY SHEEP —  | 2020-08-05 XW | Digital Media | Tracks 15 | Barcode 4547366467345 | Sony Music Labels Inc. SEXX02051B00Z | Official | 24bit/48kHz
musicbrainz:release/95ca245d-1502-4fbe-bda8-bfa4b5b46534 | STRAY SHEEP —  | 2020-10-16 TW | CD | Tracks 15 | Barcode 194398039923 | Sony Music | Official
musicbrainz:release/a39ee600-43e3-4c8d-b369-f28b7d8a0dfe | STRAY SHEEP —  | 2020-08-05 XW | Digital Media | Tracks 15 | Barcode 886448632375 | Sony Music Labels Inc. | Official
musicbrainz:release/a906e17b-1a11-4d51-95b2-551420b366e7 | STRAY SHEEP —  | 2020-08-05 XW | Digital Media | Tracks 15 | Barcode 4547366465235 | Sony Music Labels Inc. | Official
musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f | STRAY SHEEP —  | 2020-08-05 JP | CD | Tracks 15 | Barcode 4547366457933 | Sony Music Labels Inc. SECL-2598 | Official | 通常盤
musicbrainz:release/df0ebd2a-e7c5-4899-bdd0-c3a7ac437ec0 | STRAY SHEEP —  | 2020-08-05 XW | Digital Media | Tracks 15 | Barcode 4547366465419 | - | Official | Apple Digital Master
```
</details>

### 6. `shell` +12s – completed

```
bin/tl-discogs release 30395246 2>&1 | head -40; echo ====; bin/tl-discogs release 30395297 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
discogs:release/30395246 | Stray Sheep — Kenshi Yonezu | 2020-08-05 Japan | 1× CD (Album, Limited Edition, Stereo); 1× DVD (DVD-Video) | Reissue Records SECL 2595-7 | master 1828690
url: https://www.discogs.com/release/30395246-Kenshi-Yonezu-Stray-Sheep
identifiers: Barcode: 4547366457919
notes: This is the CD + DVD + Artbook version
CD-1 カムパネルラ | duration missing
CD-2 Flamingo | duration missing
CD-3 感電 | duration missing
CD-4 Placebo | duration missing | credits: Vocals: Yojiro Noda
CD-5 パプリカ | duration missing
CD-6 馬と鹿 | duration missing
CD-7 優しい人 | duration missing
CD-8 Lemon | duration missing
CD-9 まちがいさがし | duration missing
CD-10 ひまわり | duration missing
CD-11 迷える羊 | duration missing
CD-12 Décolleté | duration missing
CD-13 Teenage Riot | duration missing
CD-14 海の幽霊 | duration missing
CD-15 カナリヤ | duration missing
DVD-1 Flamingo | duration missing
DVD-2 Loser | duration missing
DVD-3 砂の惑星 | duration missing
DVD-4 飛燕 | duration missing
DVD-5 かいじゅうのマーチ | duration missing
DVD-6 アイネクライネ | duration missing
DVD-7 春雷 | duration missing
DVD-8 Moonlight | duration missing
DVD-9 Fogbound | duration missing
DVD-10 Amen | duration missing
DVD-11 Paper Flower | duration missing
DVD-12 Undercover | duration missing
DVD-13 Alice | duration missing
DVD-14 ピースサイン | duration missing
DVD-15 Teenage Riot | duration missing
DVD-16 Nighthawks | duration missing
DVD-17 Orion | duration missing
DVD-18 Lemon | duration missing
DVD-19 ごめんね | duration missing
DVD-20 クランベリーとパンケーキ | duration missing
DVD-21 灰色と青 | duration missing
====
discogs:release/30395297 | Stray Sheep — Kenshi Yonezu | 2020-08-05 Japan | 1× Box Set (); 1× CD (Album, Limited Edition) | Reissue Records SECL 2590-1 | master 1828690
url: https://www.discogs.com/release/30395297-Kenshi-Yonezu-Stray-Sheep
identifiers: Barcode: 4547366457902
notes: Omamori Edition. CD + Box + Keychain.
1 カムパネルラ | duration missing
2 Flamingo | duration missing
3 感電 | duration missing
4 Placebo | duration missing | credits: Vocals: Yojiro Noda
5 パプリカ | duration missing
6 馬と鹿 | duration missing
7 優しい人 | duration missing
8 Lemon | duration missing
9 まちがいさがし | duration missing
10 ひまわり | duration missing
11 迷える羊 | duration missing
12 Décolleté | duration missing
13 Teenage Riot | duration missing
14 海の幽霊 | duration missing
15 カナリヤ | duration missing
15 tracks, total 0:00 (0 s), without duration: 15
images: primary https://i.discogs.com/8zMapLNxpX2LD_GS3KT2A6M9tdipl4On-AMaFmVRt_U/rs:fit/g:sm/q:90/h:500/w:500/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlL
… [1095 Zeichen gekürzt]
```
</details>

### 7. `shell` +17s – completed

```
bin/tl-mb release b5562525-a1a4-4eb3-94fd-4bf205c2449f 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f | STRAY SHEEP — 米津玄師 | 2020-08-05 JP | CD | Tracks 15 | Barcode 4547366457933 | Sony Music Labels Inc. SECL-2598 | Official | 通常盤
release-group: 7bf1777c-48b4-491d-aaea-1405c8dd8845 (Album, first date 2020-08-05) | Cover: front=True back=False images=2
url: https://musicbrainz.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f
-- Medium 1: CD, 15 Tracks
1.1 [1] カムパネルラ | 3:56 (235720 ms) | ISRC JPU902001654
1.2 [2] Flamingo | 3:16 (196386 ms) | ISRC JPU901803148
1.3 [3] 感電 | 4:25 (264533 ms) | ISRC JPU902001053
1.4 [4] PLACEBO — 米津玄師 + 野田洋次郎 | 4:00 (240253 ms) | ISRC JPU902001655
1.5 [5] パプリカ | 3:23 (202666 ms) | ISRC JPU901902183
1.6 [6] 馬と鹿 | 4:25 (265333 ms) | ISRC JPU901902002
1.7 [7] 優しい人 | 3:29 (208853 ms) | ISRC JPU902001656
1.8 [8] Lemon | 4:16 (255826 ms) | ISRC JPU901800227
1.9 [9] まちがいさがし | 4:27 (267453 ms) | ISRC JPU902001657
1.10 [10] ひまわり | 4:02 (242026 ms) | ISRC JPU902001658
1.11 [11] 迷える羊 | 3:47 (226733 ms) | ISRC JPU902001659
1.12 [12] Décolleté | 3:30 (209573 ms) | ISRC JPU902001660
1.13 [13] TEENAGE RIOT | 3:45 (225213 ms) | ISRC JPU901803149
1.14 [14] 海の幽霊 | 3:54 (234466 ms) | ISRC JPU901901328
1.15 [15] カナリヤ | 4:58 (298373 ms) | ISRC JPU902001661
Total: 59:33 (3573 s), tracks without duration: 0
```
</details>

### 8. `shell` +19s – completed

```
bin/tl-deezer search --artist "Kenshi Yonezu" --title "STRAY SHEEP" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
1 Alben (q=artist:"Kenshi Yonezu" album:"STRAY SHEEP")
deezer:album/177754422 | STRAY SHEEP — Kenshi Yonezu | 15 Tracks | album
```
</details>

### 9. `shell` +20s – completed

```
bin/tl-itunes search "Kenshi Yonezu STRAY SHEEP" 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
25 Alben
itunes:album/1538265733 | STRAY SHEEP — Kenshi Yonezu | 2020-08-05 | 15 Tracks
itunes:album/1537460610 | Lemon - Single — Kenshi Yonezu | 2018-03-14 | 3 Tracks
itunes:album/1537458309 | ピースサイン - Peace Sign - EP — Kenshi Yonezu | 2017-06-21 | 4 Tracks
itunes:album/1537279370 | パプリカ - Single — Kenshi Yonezu | 2020-02-03 | 1 Tracks
itunes:album/1776984409 | Azalea - Single — Kenshi Yonezu | 2024-11-18 | 1 Tracks
itunes:album/1676871797 | LADY - Single — Kenshi Yonezu | 2023-03-21 | 1 Tracks
itunes:album/6785367850 | 夜鷹 - Yodaka - Single — Kenshi Yonezu | 2026-07-13 | 1 Tracks
itunes:album/1759899363 | LOST CORNER — Kenshi Yonezu | 2024-08-21 | 20 Tracks
itunes:album/1538275115 | BOOTLEG — Kenshi Yonezu | 2017-11-01 | 14 Tracks
itunes:album/1695666889 | 地球儀 - Spinning Globe - Single — Kenshi Yonezu | 2023-07-17 | 1 Tracks
... 15 weitere ausgeblendet. narrow the filter or raise --limit.
```
</details>

### 10. `shell` +22s – completed

```
bin/tl-deezer album 177754422 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
deezer:album/177754422 | STRAY SHEEP — Kenshi Yonezu | 2020-08-05 | UPC 4547366465235 | 15 Tracks | Label Sony Music Labels Inc.
url: https://www.deezer.com/album/177754422
1.1 Campanella | 3:55
1.2 Flamingo | 3:15
1.3 Kanden | 4:24
1.4 PLACEBO + Yojiro Noda | 4:00
1.5 Paprika | 3:23
1.6 Uma to Shika | 4:28
1.7 Yasashii Hito | 3:28
1.8 Lemon | 4:16
1.9 Machigai Sagashi | 4:27
1.10 Himawari | 4:02
1.11 Stray Sheep | 3:46
1.12 Décolleté | 3:29
1.13 TEENAGE RIOT | 3:45
1.14 Spirits of the Sea | 3:54
1.15 Canary | 4:58
Total 59:30 (3570 s)
```
</details>

### 11. `shell` +23s – completed

```
bin/tl-itunes album 1538265733 2>&1 | head -30
```

<details><summary>Ausgabe</summary>

```
itunes:album/1538265733 | STRAY SHEEP — Kenshi Yonezu | 2020-08-05 | 15 Tracks | ℗ 2020 Sony Music Labels Inc.
url: https://music.apple.com/de/album/stray-sheep/1538265733?uo=4
1.1 カムパネルラ | 3:56 (235723 ms)
1.2 Flamingo | 3:16 (196384 ms)
1.3 感電 | 4:25 (264545 ms)
1.4 PLACEBO + 野田洋次郎 — Kenshi Yonezu & Yojiro Noda | 4:00 (240254 ms)
1.5 パプリカ | 3:23 (202810 ms)
1.6 馬と鹿 | 4:25 (265178 ms)
1.7 優しい人 | 3:29 (208860 ms)
1.8 Lemon | 4:16 (255826 ms)
1.9 まちがいさがし | 4:27 (267448 ms)
1.10 ひまわり | 4:02 (242036 ms)
1.11 迷える羊 | 3:47 (226723 ms)
1.12 Décolleté | 3:30 (209585 ms)
1.13 TEENAGE RIOT | 3:45 (225201 ms)
1.14 海の幽霊 | 3:54 (234470 ms)
1.15 カナリヤ | 4:58 (298363 ms)
Total 59:33 (3573 s)
```
</details>

### 12. `shell` +28s – completed

```
bin/tl-caa b5562525-a1a4-4eb3-94fd-4bf205c2449f 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
caa:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/31571528723 | Front | http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/31571528723-1200.jpg
caa:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672 | Obi | „Some dust/blots removed in post“ | http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg
2 images · read tracklist: tl-vision <url> --context "…"
```
</details>

### 13. `shell` +32s – completed

```
bin/tl-vision "https://i.discogs.com/WTmSPjrHVH0bUSFnfyUIZhBXErJJ5H_LYv60Jl3lemM/rs:fit/g:sm/q:90/h:528/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTE1NzI4NjMzLTE3MzkyMDM4MTktODQ5NS5qcGVn" --context "Back cover of Kenshi Yonezu STRAY SHEEP CD SECL-2598. Transcribe the printed tracklist exactly (numbers + titles, capitalization) and any durations/barcode." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
ERROR: HTTP 403 beim Laden von https://i.discogs.com/WTmSPjrHVH0bUSFnfyUIZhBXErJJ5H_LYv60Jl3lemM/rs:fit/g:sm/q:90/h:528/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWltYWdlcy9SLTE1NzI4NjMzLTE3MzkyMDM4MTktODQ5NS5qcGVn
```
</details>

### 14. `shell` +43s – completed

```
bin/tl-vision "http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg" --context "Japanese CD obi strip for Kenshi Yonezu STRAY SHEEP, SECL-2598. Transcribe any tracklist titles exactly as printed (Japanese/English capitalization)." 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
source-id: image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg
model: gemini-3.8-flash@low, in 1255 / out 605 tokens, 8.7 s
kind: other | readable: True
release_title: STRAY SHEEP
artist: KENSHI YONEZU
label: Sony Music Labels Inc.
catalog_number: SECL 2598
barcode: 4547366457933
01. カムパネルラ | no duration printed
02. Flamingo | no duration printed
03. 感電 | no duration printed
04. PLACEBO + 野田洋次郎 | no duration printed
05. パプリカ | no duration printed
06. 馬と鹿 | no duration printed
07. 優しい人 | no duration printed
08. Lemon | no duration printed
09. まちがいさがし | no duration printed
10. ひまわり | no duration printed
11. 迷える羊 | no duration printed
12. Décolleté | no duration printed
13. TEENAGE RIOT | no duration printed
14. 海の幽霊 | no duration printed
15. カナリヤ | no duration printed
15 tracks read
notes: Obi strip
```
</details>

### 15. `write` +64s – completed

```
{"path": "output/work/fall-6b560853.json", "content": "{\n  \"input\": {\"id\": \"fall-6b560853\", \"title\": \"STRAY SHEEP\", \"artist\": \"Kenshi Yonezu\", \"format\": \"CD\"},\n  \"status\": \"found\",\n  \"release\": {\n    \"title\": \"STRAY SHEEP\",\n    \"artist\": \"米津玄師\",\n    \"format\": \"CD\",\n    \"country\": \"JP\",\n    \"year\": 2020,\n    \"label\": \"Sony Music Labels Inc.\",\n    \"catno\": \"SECL-2598\",\n    \"barcode\": \"4547366457933\",\n    \"edition\": \"通常盤 (standard edition), 1×CD\",\n    \"ids\": {\"musicbrainz\": \"b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs\": \"15728633\"}\n  },\n  \"tracks\": [\n    {\"position\": \"1\", \"disc\": 1, \"title\": \"カムパネルラ\", \"artist\": null, \"duration_s\": 236,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"2\", \"disc\": 1, \"title\": \"Flamingo\", \"artist\": null, \"duration_s\": 196,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"3\", \"disc\": 1, \"title\": \"感電\", \"artist\": null, \"duration_s\": 265,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"4\", \"disc\": 1, \"title\": \"PLACEBO\", \"artist\": \"米津玄師 + 野田洋次郎\", \"duration_s\": 240,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"5\", \"disc\": 1, \"title\": \"パプリカ\", \"artist\": null, \"duration_s\": 203,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"6\", \"disc\": 1, \"title\": \"馬と鹿\", \"artist\": null, \"duration_s\": 265,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"7\", \"disc\": 1, \"title\": \"優しい人\", \"artist\": null, \"duration_s\": 209,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"8\", \"disc\": 1, \"title\": \"Lemon\", \"artist\": null, \"duration_s\": 256,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"9\", \"disc\": 1, \"title\": \"まちがいさがし\", \"artist\": null, \"duration_s\": 267,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"10\", \"disc\": 1, \"title\": \"ひまわり\", \"artist\": null, \"duration_s\": 242,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"11\", \"disc\": 1, \"title\": \"迷える羊\", \"artist\": null, \"duration_s\": 227,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"12\", \"disc\": 1, \"title\": \"Décolleté\", \"artist\": null, \"duration_s\": 210,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"13\", \"disc\": 1, \"title\": \"TEENAGE RIOT\", \"artist\": null, \"duration_s\": 225,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"14\", \"disc\": 1, \"title\": \"海の幽霊\", \"artist\": null, \"duration_s\": 234,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []},\n    {\"position\": \"15\", \"disc\": 1, \"title\": \"カナリヤ\", \"artist\": null, \"duration_s\": 298,\n     \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"],\n     \"duration_sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"itunes:album/1538265733\"], \"flags\": []}\n  ],\n  \"artists\": [\n    {\"name\": \"米津玄師\", \"role\": \"main\", \"tracks\": [], \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\"]},\n    {\"name\": \"野田洋次郎\", \"role\": \"featured\", \"tracks\": [\"4\"], \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\", \"itunes:album/1538265733\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\"]}\n  ],\n  \"total_duration_s\": 3573,\n  \"confidence\": 0.85,\n  \"sources\": [\n    {\"id\": \"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"url\": \"https://musicbrainz.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"kind\": \"database\", \"note\": \"JP CD 通常盤, SECL-2598, barcode 4547366457933, 15 tracks with ms durations and ISRCs\"},\n    {\"id\": \"discogs:release/15728633\", \"url\": \"https://www.discogs.com/release/15728633-Kenshi-Yonezu-Stray-Sheep\", \"kind\": \"database\", \"note\": \"same edition: SECL 2598, barcode 4547366457933, matrix LLDS-8767, 15 tracks (no durations listed)\"},\n    {\"id\": \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\", \"url\": \"http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\", \"kind\": \"image\", \"note\": \"obi strip of SECL 2598, read via tl-vision: printed tracklist 01-15, barcode 4547366457933\"},\n    {\"id\": \"itunes:album/1538265733\", \"url\": \"https://music.apple.com/de/album/stray-sheep/1538265733\", \"kind\": \"streaming\", \"note\": \"digital edition of the same album (Japanese titles, same order); durations agree with MB within milliseconds\"},\n    {\"id\": \"deezer:album/177754422\", \"url\": \"https://www.deezer.com/album/177754422\", \"kind\": \"streaming\", \"note\": \"separate digital edition, UPC 4547366465235, romanized titles; only used as an order cross-check\"}\n  ],\n  \"conflicts\": [\n    {\"field\": \"title track 13\", \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\"], \"resolution\": \"MusicBrainz and the printed obi read 'TEENAGE RIOT' (all caps), Discogs lists 'Teenage Riot'; printed carrier spelling kept.\"}\n  ],\n  \"missing\": [\n    \"Input had no barcode, catalogue number or limited-edition hint; the standard single-CD edition (通常盤, SECL-2598) was chosen over three JP limited editions that also contain a CD (SECL 2590-1 box, SECL 2595-7 CD+DVD, SECL 2592-4 CD+Blu-ray) and a 2025 China CD.\",\n    \"Discogs lists no track durations for this edition, so durations come from MusicBrainz (ms precision) and are corroborated by the Apple digital edition of the same album.\"\n  ],\n  \"alternatives\": [\n    {\"description\": \"CD + DVD + artbook, Japan 2020, SECL 2595-7, barcode 4547366457919, 15 CD tracks + 27 DVD tracks\", \"source\": \"discogs:release/30395246\", \"why_not\": \"input format is plain CD; this edition adds a DVD\"},\n    {\"description\": \"CD + Blu-ray + artbook, Japan 2020, SECL 2592-4, barcode 4547366457926, 15 CD tracks + 27 Blu-ray tracks\", \"source\": \"discogs:release/16115694\", \"why_not\": \"input format is plain CD; this edition adds a Blu-ray\"},\n    {\"description\": \"Box set (おまもり盤), Japan 2020, SECL 2590-1, barcode 4547366457902, 15 CD tracks, includes box and keychain\", \"source\": \"discogs:release/30395297\", \"why_not\": \"limited box edition, input gives no hint of a box set\"},\n    {\"description\": \"China CD, 2025, Starsing Records/Sony Music 19439803992, barcode 9787798443370\", \"source\": \"discogs:release/37170435\", \"why_not\": \"different country, label and barcode; later regional reissue\"}\n  ],\n  \"reasoning\": \"No barcode was supplied, so the edition was fixed by format (CD) plus title/artist. Discogs and MusicBrainz both hold the Japanese standard edition (通常盤, SECL 2598, barcode 4547366457933) with an identical 15-track order; the obi image read via vision confirms catalogue number, barcode and the printed titles (カムパネルラ … カナリヤ, 'TEENAGE RIOT', 'PLACEBO + 野田洋次郎'). The three limited JP editions contain additional DVD/Blu-ray discs or a box, so the plain-CD input points to the standard edition; those editions and the 2025 China CD are listed as alternatives. Durations are taken from the MusicBrainz CD entry (ms precision, identical to the Apple digital master within milliseconds) and total 59:33. Track 4 is the only collaboration: 米津玄師 + 野田洋次郎 (Yojiro Noda), credited as featured artist.\"\n}\n"}
```

<details><summary>Ausgabe</summary>

```
Created file successfully: output/work/fall-6b560853.json
```
</details>

### 16. `shell` +65s – completed

```
bin/tl-validate output/work/fall-6b560853.json 2>&1 | head -40
```

<details><summary>Ausgabe</summary>

```
INVALID:
- conflicts.0.values: Field required
- conflicts.0.sources: Extra inputs are not permitted
```
</details>

### 17. `shell` +67s – completed

```
bin/tl-validate --schema 2>&1 | head -60
```

<details><summary>Ausgabe</summary>

```
{
 "$defs": {
  "Alternative": {
   "additionalProperties": false,
   "properties": {
    "description": {
     "title": "Description",
     "type": "string"
    },
    "source": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Source"
    },
    "why_not": {
     "anyOf": [
      {
       "type": "string"
      },
      {
       "type": "null"
      }
     ],
     "default": null,
     "title": "Why Not"
    }
   },
   "required": [
    "description"
   ],
   "title": "Alternative",
   "type": "object"
  },
  "ArtistCredit": {
   "additionalProperties": false,
   "properties": {
    "name": {
     "description": "one artist or group, as credited (no 'feat.' strings – each featured artist is its own entry)",
     "title": "Name",
     "type": "string"
    },
    "role": {
     "default": "main",
     "enum": [
      "main",
      "featured",
      "remixer",
      "other"
     ],
     "title": "Role",
     "type": "string"
    },
    "tracks": {
```
</details>

### 18. `shell` +69s – completed

```
bin/tl-validate --schema 2>&1 | python3 -c "
import json,sys
s=json.load(sys.stdin)
print(json.dumps(s['\$defs'].get('Conflict'),indent=1,ensure_ascii=False))
print(json.dumps(s['properties'].get('missing'),indent=1,ensure_ascii=False))
"
```

<details><summary>Ausgabe</summary>

```
{
 "additionalProperties": false,
 "properties": {
  "field": {
   "title": "Field",
   "type": "string"
  },
  "values": {
   "additionalProperties": {
    "type": "string"
   },
   "description": "source ID → value",
   "title": "Values",
   "type": "object"
  },
  "resolution": {
   "anyOf": [
    {
     "type": "string"
    },
    {
     "type": "null"
    }
   ],
   "default": null,
   "title": "Resolution"
  }
 },
 "required": [
  "field",
  "values"
 ],
 "title": "Conflict",
 "type": "object"
}
{
 "description": "what is missing, e.g. 'duration track 20'",
 "items": {
  "type": "string"
 },
 "title": "Missing",
 "type": "array"
}
```
</details>

### 19. `edit` +71s – completed

```
{"path": "output/work/fall-6b560853.json", "oldString": "    {\"field\": \"title track 13\", \"sources\": [\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\", \"discogs:release/15728633\"], \"resolution\": \"MusicBrainz and the printed obi read 'TEENAGE RIOT' (all caps), Discogs lists 'Teenage Riot'; printed carrier spelling kept.\"}", "newString": "    {\"field\": \"title track 13\", \"values\": {\"musicbrainz:release/b5562525-a1a4-4eb3-94fd-4bf205c2449f\": \"TEENAGE RIOT\", \"image:http://coverartarchive.org/release/b5562525-a1a4-4eb3-94fd-4bf205c2449f/32271089672-1200.jpg\": \"TEENAGE RIOT\", \"discogs:release/15728633\": \"Teenage Riot\"}, \"resolution\": \"MusicBrainz and the printed obi read 'TEENAGE RIOT' (all caps), Discogs lists 'Teenage Riot'; printed carrier spelling kept.\"}"}
```

<details><summary>Ausgabe</summary>

```
Edited output/work/fall-6b560853.json (1 replacement)
```
</details>

### 20. `shell` +74s – completed

```
bin/tl-validate output/work/fall-6b560853.json 2>&1 | head -20
```

<details><summary>Ausgabe</summary>

```
OK: status=found, 15 tracks (15 with duration), 5 sources, 1 conflicts, confidence=0.85
```
</details>

> **Agent** +75s: FERTIG found 15 Tracks confidence=0.85
