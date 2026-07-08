from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post(
        "/auth/register",
        json={
            "username":"pytestuser6",
            "password":"password123"
        }
    )
    assert response.status_code in [200, 201, 400]

def test_login():
    response = client.post(
        "/auth/login",
        data={
            "username":"pytestuser3",
            "password":"password123"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()