import pytest

from src.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    return ApiClient()
