import os

# Pricing from cost file.py (USD per 1,000,000 tokens for Gemini 3.8 Flash)
DEFAULT_MODEL = os.getenv("GOOGLE_GENAI_MODEL", "gemini-3.8-flash")
INPUT_PRICE_PER_MILLION = 0.75
OUTPUT_PRICE_PER_MILLION = 3.75


def compute_token_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float = INPUT_PRICE_PER_MILLION,
    output_price_per_million: float = OUTPUT_PRICE_PER_MILLION,
) -> float:
    """Compute USD cost for Gemini API token usage matching cost file.py."""
    input_cost = (max(0, input_tokens) / 1_000_000) * input_price_per_million
    output_cost = (max(0, output_tokens) / 1_000_000) * output_price_per_million
    return input_cost + output_cost
