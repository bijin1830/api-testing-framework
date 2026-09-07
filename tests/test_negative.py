import pytest


@pytest.mark.negative
def test_missing_post_returns_404(api_client):
    response = api_client.get("/posts/999999")

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.negative
def test_missing_user_returns_404(api_client):
    response = api_client.get("/users/999999")

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.negative
def test_filter_with_unknown_user_returns_empty_list(api_client):
    response = api_client.get("/posts", params={"userId": 999999})

    assert response.status_code == 200
    assert response.json() == []
