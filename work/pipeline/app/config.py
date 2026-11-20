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


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
