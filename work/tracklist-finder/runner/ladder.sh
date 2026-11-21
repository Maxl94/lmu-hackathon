#!/usr/bin/env bash
# Modell-Leiter: dieselben Fälle mit mehreren Agent-Modellen (ohne Schnellweg), Ergebnisse in output/ladder/<modell>/
# Aufruf: bash runner/ladder.sh [csv]   – danach: uv run python eval/ladder_report.py
cd "$(dirname "$0")/.."
CSV="${1:-data/ladder.csv}"
MODELS=(
  "kisski/qwen3.5-397b-a17b"
  "openrouter/deepseek/deepseek-v4.1-flash-1017"
  "openrouter/openai/gpt-oss-120b"
  "openrouter/z-ai/glm-5.3-flash"
  "anthropic/claude-haiku-5-5"
)
for m in "${MODELS[@]}"; do
  slug=$(echo "$m" | tr '/' '_')
  mkdir -p "output/ladder/$slug"
  uv run python runner/run.py --csv "$CSV" --parallel 2 --no-fast --timeout 1200 -m "$m" --out-dir "output/ladder/$slug" \
    > "output/ladder/$slug/run.log" 2>&1 &
done
wait
echo "Leiter fertig"; tail -n 2 output/ladder/*/run.log
