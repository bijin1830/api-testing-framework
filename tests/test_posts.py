import pytest
from jsonschema import validate

from src.schemas import POST_SCHEMA


@pytest.mark.smoke
def test_get_single_post(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    payload = response.json()
    validate(instance=payload, schema=POST_SCHEMA)
    assert payload["id"] == 1
    assert payload["userId"] > 0
    assert payload["title"].strip()
    assert payload["body"].strip()


@pytest.mark.regression
def test_get_posts_collection(api_client):
    response = api_client.get("/posts")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 100
    validate(instance=payload[0], schema=POST_SCHEMA)


@pytest.mark.regression
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_filter_posts_by_user_id(api_client, user_id):
    response = api_client.get("/posts", params={"userId": user_id})

    assert response.status_code == 200
    payload = response.json()
    assert payload
    assert all(post["userId"] == user_id for post in payload)


@pytest.mark.smoke
def test_create_post(api_client):
    request_body = {
        "title": "API automation portfolio test",
        "body": "Synthetic test payload created by pytest.",
        "userId": 1,
    }

    response = api_client.post("/posts", json=request_body)

    assert response.status_code == 201
    payload = response.json()
    assert payload["title"] == request_body["title"]
    assert payload["body"] == request_body["body"]
    assert payload["userId"] == request_body["userId"]
    assert isinstance(payload["id"], int)
