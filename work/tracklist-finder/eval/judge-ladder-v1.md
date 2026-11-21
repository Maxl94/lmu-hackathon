# Prüfmodell-Leiter (v1)

Referenz: Opus 5.5 (Lauf A), 17 Ergebnisse. Opus Lauf B zeigt die Rauschgrenze.

| Prüfmodell | Preis in/out pro MTok | Ampel gleich | Stufe gleich | Stufe ± 1 | Fallen rot | Ø Kosten | Ø Dauer |
|---|---|---|---|---|---|---|---|
| opus-a | $4 / $20 | 100% (17/17) | 100% | 100% | 4/4 | $0.1336 | 17 s |
| opus-b | $4 / $20 | 100% (17/17) | 94% | 100% | 4/4 | $0.1321 | 16 s |
| sonnet | $2 / $10 | 88% (15/17) | 80% | 98% | 4/4 | $0.0609 | 8 s |
| haiku | $0.10 / $0.50 | 82% (14/17) | 71% | 90% | 4/4 | $0.0033 | 8 s |

## Abweichungen der Ampel (gegenüber Opus A)

| Ergebnis | Opus A | opus-b | sonnet | haiku |
|---|---|---|---|---|
| examples__kok-mc | 🟢 4/5/4 | 🟢 4/5/4 | 🟡 3/5/4 | 🟢 4/5/4 |
| examples__kok-noartist-r1 | 🔴 2/5/4 | 🔴 2/5/4 | 🔴 2/4/4 | 🟡 3/4/4 |
| examples__ram-vinyl-r3 | 🟡 3/5/4 | 🟡 3/5/4 | 🟡 3/5/4 | 🟢 4/5/4 |
| examples__spatzen-mc-titleonly | 🟡 3/5/5 | 🟡 3/5/5 | 🟢 4/5/5 | 🟢 5/5/5 |

Stufen = edition/tracklist/sources (Prüfmodell); durations bewertet immer der Code.
