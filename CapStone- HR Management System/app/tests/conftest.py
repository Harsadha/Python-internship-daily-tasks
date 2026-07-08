import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def auth_token():
    response = client.post(
        "/auth/login",
        data={
            "username": "pytestuser3",
            "password": "password123"
        }
    )
    assert response.status_code == 200, response.text
    return response.json()["access_token"]