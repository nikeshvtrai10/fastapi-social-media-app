import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import schemas


@pytest.fixture
def client():
    #run our code before we run our test
    yield TestClient(app)


def test_root(client):
    res = client.get("/")
    print(res.json()['message'])
    assert res.json()['message'] == "Hello World"
    assert res.status_code == 200


def test_create_user():
    res = client.post("/users/", json={"email": "hi@gmail.com", "password": "pass"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hi@gmail.com"
    assert res.status_code == 201