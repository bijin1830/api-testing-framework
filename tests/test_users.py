import pytest
from jsonschema import validate

from src.schemas import USER_SCHEMA


@pytest.mark.smoke
def test_get_single_user(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200
    payload = response.json()
    validate(instance=payload, schema=USER_SCHEMA)
    assert payload["id"] == 1
    assert "@" in payload["email"]


@pytest.mark.regression
def test_get_users_collection(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 10
    for user in payload:
        validate(instance=user, schema=USER_SCHEMA)


@pytest.mark.regression
def test_user_has_nested_address_and_company(api_client):
    response = api_client.get("/users/1")
    payload = response.json()

    assert response.status_code == 200
    assert "city" in payload["address"]
    assert "geo" in payload["address"]
    assert "lat" in payload["address"]["geo"]
    assert "lng" in payload["address"]["geo"]
    assert "name" in payload["company"]
