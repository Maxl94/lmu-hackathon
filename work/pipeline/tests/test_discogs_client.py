import json
from typing import Any

import httpx
import pytest

from app.config import Settings
from app.discogs_client import (
    DiscogsAuthError,
    DiscogsClient,
    DiscogsRateLimitError,
    DiscogsUpstreamError,
)


class InMemoryCacheStore:
    def __init__(self) -> None:
        self.rows: dict[str, dict[str, Any]] = {}

    def get_api_cache(self, cache_key: str) -> dict[str, Any] | None:
        return self.rows.get(cache_key)

    def set_api_cache(
        self, cache_key: str, endpoint: str, status_code: int, payload: dict[str, Any]
    ) -> None:
        self.rows[cache_key] = {
            "cache_key": cache_key,
            "endpoint": endpoint,
            "status_code": status_code,
            "payload_json": payload,
        }


def test_discogs_client_requires_valid_token() -> None:
    for bad_token in ("", "PASTE_YOUR_DISCOGS_PERSONAL_ACCESS_TOKEN"):
        client = DiscogsClient(Settings(discogs_token=bad_token))
        try:
            with pytest.raises(DiscogsAuthError):
                client.search_releases({"barcode": "123456"})
        finally:
            client.close()


def test_discogs_client_headers_cache_hit_and_bypass(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.discogs_client.time.sleep", lambda _: None)
    seen_headers: list[dict[str, str]] = []
    call_count = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal call_count
        call_count += 1
        seen_headers.append(dict(request.headers))
        return httpx.Response(
            200,
            json={"results": [{"id": call_count}]},
            headers={"X-Discogs-Ratelimit-Remaining": "59"},
        )

    cache = InMemoryCacheStore()
    http = httpx.Client(base_url="https://api.discogs.com", transport=httpx.MockTransport(handler))
    client = DiscogsClient(
        Settings(discogs_token="test-token-123", discogs_user_agent="TestUA/1.0"),
        cache_store=cache,
        http_client=http,
    )

    payload1, cached1 = client.search_releases({"barcode": "4065629733131"})
    assert cached1 is False
    assert payload1["results"][0]["id"] == 1
    assert seen_headers[0]["user-agent"] == "TestUA/1.0"
    assert seen_headers[0]["authorization"] == "Discogs token=test-token-123"

    # Second call uses cache (0 HTTP calls)
    payload2, cached2 = client.search_releases({"barcode": "4065629733131"})
    assert cached2 is True
    assert payload2["results"][0]["id"] == 1
    assert call_count == 1

    # bypass_cache=True forces live HTTP request & updates cache
    payload3, cached3 = client.search_releases(
        {"barcode": "4065629733131"}, bypass_cache=True
    )
    assert cached3 is False
    assert payload3["results"][0]["id"] == 2
    assert call_count == 2
    http.close()


def test_discogs_client_retries_429_5xx_and_handles_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("app.discogs_client.time.sleep", lambda _: None)

    # 1. Transient 429 -> 200
    seq = iter([429, 200])

    def handler_429_recover(request: httpx.Request) -> httpx.Response:
        code = next(seq)
        if code == 429:
            return httpx.Response(429, headers={"Retry-After": "1"})
        return httpx.Response(200, json={"id": 42})

    http1 = httpx.Client(
        base_url="https://api.discogs.com",
        transport=httpx.MockTransport(handler_429_recover),
    )
    c1 = DiscogsClient(Settings(discogs_token="tok"), http_client=http1)
    rel, _ = c1.get_release(42)
    assert rel["id"] == 42
    http1.close()

    # 2. Persistent 429 -> DiscogsRateLimitError
    http2 = httpx.Client(
        base_url="https://api.discogs.com",
        transport=httpx.MockTransport(lambda req: httpx.Response(429)),
    )
    c2 = DiscogsClient(Settings(discogs_token="tok"), http_client=http2)
    with pytest.raises(DiscogsRateLimitError):
        c2.get_release(42)
    http2.close()

    # 3. 401 -> DiscogsAuthError; 404 -> ({}, False); invalid JSON -> DiscogsUpstreamError
    def handler_status(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/1"):
            return httpx.Response(401)
        if request.url.path.endswith("/2"):
            return httpx.Response(404)
        if request.url.path.endswith("/3"):
            return httpx.Response(200, content=b"{not-json")
        return httpx.Response(503)

    http3 = httpx.Client(
        base_url="https://api.discogs.com",
        transport=httpx.MockTransport(handler_status),
    )
    c3 = DiscogsClient(Settings(discogs_token="tok"), http_client=http3)
    with pytest.raises(DiscogsAuthError):
        c3.get_release(1)
    assert c3.get_release(2) == ({}, False)
    with pytest.raises(DiscogsUpstreamError):
        c3.get_release(3)
    with pytest.raises(DiscogsUpstreamError):
        c3.get_release(4)
    http3.close()

    # 4. Network ConnectError -> DiscogsUpstreamError
    def handler_net(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused", request=request)

    http4 = httpx.Client(
        base_url="https://api.discogs.com",
        transport=httpx.MockTransport(handler_net),
    )
    c4 = DiscogsClient(Settings(discogs_token="tok"), http_client=http4)
    with pytest.raises(DiscogsUpstreamError):
        c4.search_releases({"q": "anything"})
    http4.close()
