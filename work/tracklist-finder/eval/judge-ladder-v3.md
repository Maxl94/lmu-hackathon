# Prüfmodell-Leiter (v3)

Referenz: Opus 5.5 (Lauf A), 17 Ergebnisse. Opus Lauf B zeigt die Rauschgrenze.

| Prüfmodell | Preis in/out pro MTok | Ampel gleich | Stufe gleich | Stufe ± 1 | Fallen rot | Ø Kosten | Ø Dauer |
|---|---|---|---|---|---|---|---|
| opus-a | $4 / $20 | 100% (17/17) | 100% | 100% | 4/4 | $0.1419 | 19 s |
| haiku | $0.10 / $0.50 | 94% (16/17) | 76% | 98% | 4/4 | $0.0040 | 13 s |
| gemini-2.5-flash-lite | ? | 100% (2/2) | 100% | 100% | 2/2 | $0.0000 | 0 s |
| gemini-3.1-flash-lite | ? | 82% (14/17) | 73% | 86% | 4/4 | $0.0061 | 3 s |
| gemini-3.1-pro-preview | $2 / $12 (GEMA) | 94% (16/17) | 84% | 92% | 4/4 | $0.0764 | 21 s |
| gemini-3.5-flash-lite | ? | 82% (14/17) | 76% | 86% | 4/4 | $0.0072 | 2 s |
| gemini-3.8-flash | $0.83 / $4.13 (GEMA) | 94% (16/17) | 92% | 100% | 4/4 | $0.0282 | 27 s |
| gemini-4-argon | $2 / $10 (GEMA) | 100% (17/17) | 94% | 100% | 4/4 | $0.0555 | 21 s |
| gemini-4-carbon | $2 / $10 (GEMA) | 94% (16/17) | 94% | 100% | 4/4 | $0.0798 | 44 s |
| gemini-4-hydrogen | $1.50 / $7.50? (GEMA) | 94% (16/17) | 94% | 100% | 4/4 | $0.0706 | 28 s |
| gemini-4-neon | ? (GEMA) | 94% (16/17) | 94% | 100% | 4/4 | $0.0000 | 75 s |

## Abweichungen der Ampel (gegenüber Opus A)

| Ergebnis | Opus A | haiku | gemini-2.5-flash-lite | gemini-3.1-flash-lite | gemini-3.1-pro-preview | gemini-3.5-flash-lite | gemini-3.8-flash | gemini-4-argon | gemini-4-carbon | gemini-4-hydrogen | gemini-4-neon |
|---|---|---|---|---|---|---|---|---|---|---|---|
| examples__kok-mc | 🟢 4/5/4 | 🟡 3/5/4 | –  | 🟢 4/5/4 | 🟡 3/5/4 | 🟢 4/5/4 | 🟡 3/5/4 | 🟢 4/5/4 | 🟡 3/5/4 | 🟡 3/5/4 | 🟡 3/5/4 |
| examples__ram-vinyl-r3 | 🔴 2/5/4 | 🔴 2/5/4 | –  | 🟢 4/5/4 | 🔴 2/5/4 | 🟢 4/5/4 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/5/4 |
| examples__spatzen-mc-titleonly | 🔴 2/5/5 | 🔴 2/4/4 | –  | 🟢 4/5/5 | 🔴 2/5/5 | 🟢 4/5/5 | 🔴 2/5/5 | 🔴 2/5/5 | 🔴 2/5/5 | 🔴 2/5/5 | 🔴 2/5/5 |
| output__spatzen-mc-titleonly | 🔴 2/5/4 | 🔴 2/5/4 | –  | 🟡 4/5/5 | 🔴 2/5/4 | 🟡 4/5/4 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/5/4 |

Stufen = edition/tracklist/sources (Prüfmodell); durations bewertet immer der Code.
