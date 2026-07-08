from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_employees():
    response = client.get("/employees/")
    assert response.status_code == 200

def test_create_employee():

    response = client.post(
        "/employees/",
        json={
            "emp_name":"test_employee_2",
            "email":"h.ranjeeth.kumar@accenture.com",
            "salary":90000,
            "dept_id":3
        }
    )
    assert response.status_code in [200,201]

def test_update_employee(auth_token):
    headers = {"Authorization":f"Bearer {auth_token}"}
    response = client.put(
        "/employees/17",
        headers=headers,
        json={
            "emp_name":"test_employee_2_updated",
            "email":"h.ranjeeth.kumar@accenture.com",
            "salary":80000,
            "dept_id":5
        }
    )
    assert response.status_code == 200

def test_delete_employee(auth_token):
    headers = {
        "Authorization":f"Bearer {auth_token}"
    }
    response = client.delete(
        "/employees/17",
        headers=headers
    )
    assert response.status_code == 200

