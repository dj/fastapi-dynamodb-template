import pytest
from .client import test_client


@pytest.fixture(scope="session")
def user():
    return {
        "email": "test@test.com",
        "username": "testname",
        "password": "hunter2",
    }


@pytest.fixture(scope="session")
def post_user(user):
    response = test_client.post("/users", json=user)
    return response


def test_get_users_me_unauthorized():
    response = test_client.get("/users/me")
    assert response.status_code == 401
    assert response.json()


def test_post_user(post_user):
    assert post_user.status_code == 201


def test_post_user_already_exists(post_user, user):
    same_username = test_client.post(
        "/users",
        json={
            **user,
            "email": "different_email@test.com",
        },
    )
    assert same_username.json()["error"] == "username or email already exists"
    assert same_username.status_code == 422

    same_email = test_client.post(
        "/users",
        json={
            **user,
            "username": "different_username",
        },
    )
    assert same_email.json()["error"] == "username or email already exists"
    assert same_email.status_code == 422


def test_post_token(post_user, user):
    response = test_client.post(
        "/token",
        data={
            "username": user["username"],
            "password": user["password"],
            "grant_type": "password",
        },
    )
    assert response.json() == ""
    assert response.status_code == 200
