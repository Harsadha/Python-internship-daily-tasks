from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_departments():
    response = client.get("/departments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_department():
    response = client.post(
        "/departments/",
        json={
            "dept_name":"PYTEST2"
        }
    )
    assert response.status_code in [200,201]