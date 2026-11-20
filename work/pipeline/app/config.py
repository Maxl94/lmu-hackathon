from functools import lru_cache
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(extra="ignore")

    database_url: str = "postgresql://tracklist:tracklist@db:5432/tracklist"
    discogs_token: str = ""
    discogs_user_agent: str = "LMUTracklistHackathon/1.0"
    not_found_ttl_hours: int = 24
    max_candidates_to_fetch: int = 4
    discogs_timeout_sec: float = 15.0
    discogs_min_remaining: int = 5
    discogs_base_url: str = "https://api.discogs.com"
    gemini_api_key: str = ""
    google_genai_model: str = "gemini-3.8-flash"
    enable_agent_fallback: bool = True
    agent_max_attempts: int = 3
    enable_queue_workers: bool = True
    discogs_queue_concurrency: int = 1
    agent_queue_concurrency: int = 2
    queue_poll_interval_sec: float = 0.5

    def is_agent_configured(self) -> bool:
        """Return True when Gemini agent fallback is enabled with a non-placeholder API key."""
        key = (self.gemini_api_key or "").strip()
        return self.enable_agent_fallback and bool(
            key and key not in {"PASTE_YOUR_GEMINI_API_KEY", "AQ.Ab8RN6LZCw-"}
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
