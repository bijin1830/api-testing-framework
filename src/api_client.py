from __future__ import annotations

import os
from typing import Any

import requests


class ApiClient:
    """Small reusable REST client used by the test suite."""

    def __init__(self, base_url: str | None = None, timeout: int = 10) -> None:
        self.base_url = (base_url or os.getenv("BASE_URL") or "https://jsonplaceholder.typicode.com").rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "bijin1830-api-testing-framework/1.0",
        })

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return self.session.get(self._url(path), timeout=self.timeout, **kwargs)

    def post(self, path: str, json: dict[str, Any] | None = None, **kwargs: Any) -> requests.Response:
        return self.session.post(self._url(path), json=json, timeout=self.timeout, **kwargs)

    def put(self, path: str, json: dict[str, Any] | None = None, **kwargs: Any) -> requests.Response:
        return self.session.put(self._url(path), json=json, timeout=self.timeout, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> requests.Response:
        return self.session.delete(self._url(path), timeout=self.timeout, **kwargs)
