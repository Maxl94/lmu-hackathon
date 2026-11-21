# Agent-Modell-Leiter

Gleiche Fälle (`data/ladder.csv`, ohne Schnellweg), gleiches Prüfmodell (Opus 5.5).

| Modell | Preis in/out | gültig | Ausgabe ✓ | Anzahl ✓ | Titel | Dauer ±2 s | Fallen rot | Ampel | Ø Zeit | Ø Tools | Ø Agent-Kosten* | Ø Prüfung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude Haiku 5.5 | $0.1 / $0.5 | 4/4 | 100% | 100% | 100% | 91% | 1/1 | 🟢1 🟡1 🔴1 | 47 s | 6 | $0.007 | $0.073 |
| Qwen3.5-397B (SAIA; Listenpreis OpenRouter) | $0.45 / $3.0 | 4/4 | 100% | 100% | 100% | 97% | 1/1 | 🟢1 🟡2 🔴0 | 356 s | 21 | $0.249 | $0.090 |
| DeepSeek v4.1 Flash | $0.15 / $0.6 | 4/4 | 100% | 100% | 100% | 97% | 1/1 | 🟢1 🟡2 🔴0 | 88 s | 21 | $0.073 | $0.118 |
| gpt-oss-120b | $0.09 / $0.36 | 3/4 | 25% | 100% | 98% | 94% | 0/0 | 🟢0 🟡2 🔴1 ⚪1 | 58 s | 17 | $0.052 | $0.075 |
| GLM-5.3 Flash | $0.04 / $0.078 | 4/4 | 100% | 100% | 100% | 94% | 1/1 | 🟢1 🟡1 🔴1 | 361 s | 26 | $0.031 | $0.140 |

\* Listenpreis × Tokens aus dem Trace (Cache-Lesezugriffe mit Cache-Preis). SAIA selbst ist kostenlos (Kontingent).

## Einzelfälle

| Modell | Fall | Status | Ampel | Tracks | Ausgabe ✓ | Zeit | Tools | Tokens in (+Cache) / out | Agent-Kosten* |
|---|---|---|---|---|---|---|---|---|---|
| Claude Haiku 5.5 | bravo30-ean | found | 🟢 4.65 | 40 | ✅ | 56 s | 6 | 16 (+195,058) / 11,200 | $0.008 |
| Claude Haiku 5.5 | kok-mc | ambiguous | 🟡 3.85 | 16 | ✅ | 42 s | 5 | 14 (+173,568) / 8,639 | $0.006 |
| Claude Haiku 5.5 | spatzen-mc-titleonly | found | 🔴 3.2 | 12 | ✅ | 51 s | 9 | 16 (+203,210) / 10,075 | $0.007 |
| Claude Haiku 5.5 | trap-wrong-ean | ambiguous | 🔴 2.45 | 16 | ✅ | 38 s | 5 | 10 (+103,116) / 8,904 | $0.005 |
| Qwen3.5-397B (SAIA; Listenpreis OpenRouter) | bravo30-ean | found | 🟢 4.75 | 40 | ✅ | 514 s | 18 | 485,279 (+0) / 18,412 | $0.274 |
| Qwen3.5-397B (SAIA; Listenpreis OpenRouter) | kok-mc | found | 🟡 4.1 | 16 | ✅ | 285 s | 21 | 418,301 (+0) / 8,946 | $0.215 |
| Qwen3.5-397B (SAIA; Listenpreis OpenRouter) | spatzen-mc-titleonly | found | 🟡 3.85 | 12 | ✅ | 284 s | 23 | 422,033 (+0) / 8,188 | $0.214 |
| Qwen3.5-397B (SAIA; Listenpreis OpenRouter) | trap-wrong-ean | ambiguous | 🔴 3.4 | 20 | ✅ | 338 s | 22 | 580,050 (+0) / 10,994 | $0.294 |
| DeepSeek v4.1 Flash | bravo30-ean | found | 🟢 5.0 | 40 | ✅ | 132 s | 20 | 30,426 (+532,352) / 12,259 | $0.092 |
| DeepSeek v4.1 Flash | kok-mc | found | 🟡 3.85 | 16 | ✅ | 43 s | 13 | 28,130 (+190,336) / 7,221 | $0.037 |
| DeepSeek v4.1 Flash | spatzen-mc-titleonly | found | 🟡 3.6 | 12 | ✅ | 106 s | 32 | 45,142 (+527,616) / 14,751 | $0.095 |
| DeepSeek v4.1 Flash | trap-wrong-ean | ambiguous | 🔴 2.55 | 16 | ✅ | 72 s | 20 | 33,464 (+358,400) / 14,379 | $0.067 |
| gpt-oss-120b | bravo30-ean | found | 🟡 3.4 | 40 | ❌ | 93 s | 16 | 58,703 (+417,224) / 9,516 | $0.046 |
| gpt-oss-120b | kok-mc | found | 🟡 4.1 | 16 | ✅ | 48 s | 26 | 13,978 (+582,976) / 5,956 | $0.056 |
| gpt-oss-120b | spatzen-mc-titleonly | found | 🔴 2.75 | 12 | ❌ | 65 s | 19 | 444,847 (+548,128) / 4,386 | $0.091 |
| gpt-oss-120b | trap-wrong-ean | ❌ 0 | –  | 0 | – | 27 s | 8 | 7,609 (+143,680) / 2,963 | $0.015 |
| GLM-5.3 Flash | bravo30-ean | found | 🟢 4.75 | 40 | ✅ | 540 s | 19 | 38,351 (+570,368) / 56,535 | $0.029 |
| GLM-5.3 Flash | kok-mc | ambiguous | 🟡 4.2 | 16 | ✅ | 337 s | 29 | 32,312 (+635,392) / 35,682 | $0.029 |
| GLM-5.3 Flash | spatzen-mc-titleonly | ambiguous | 🔴 3.45 | 12 | ✅ | 319 s | 34 | 31,765 (+950,016) / 30,299 | $0.042 |
| GLM-5.3 Flash | trap-wrong-ean | ambiguous | 🔴 3.3 | 16 | ✅ | 247 s | 23 | 29,930 (+533,248) / 28,676 | $0.025 |
