# Prüfmodell-Leiter (v2)

Referenz: Opus 5.5 (Lauf A), 17 Ergebnisse. Opus Lauf B zeigt die Rauschgrenze.

| Prüfmodell | Preis in/out pro MTok | Ampel gleich | Stufe gleich | Stufe ± 1 | Fallen rot | Ø Kosten | Ø Dauer |
|---|---|---|---|---|---|---|---|
| opus-a | $4 / $20 | 100% (17/17) | 100% | 100% | 4/4 | $0.1453 | 19 s |
| sonnet | $2 / $10 | 88% (15/17) | 86% | 92% | 4/4 | $0.0744 | 18 s |
| haiku | $0.10 / $0.50 | 88% (15/17) | 78% | 98% | 4/4 | $0.0040 | 14 s |

## Abweichungen der Ampel (gegenüber Opus A)

| Ergebnis | Opus A | sonnet | haiku |
|---|---|---|---|
| examples__kok-mc | 🟢 4/5/4 | 🟡 3/5/4 | 🟢 4/5/4 |
| examples__spatzen-mc-titleonly | 🔴 2/5/5 | 🔴 2/5/5 | 🟢 5/5/5 |
| output__spatzen-mc-titleonly | 🔴 2/5/4 | 🟡 4/5/4 | 🟡 3/4/4 |

Stufen = edition/tracklist/sources (Prüfmodell); durations bewertet immer der Code.
