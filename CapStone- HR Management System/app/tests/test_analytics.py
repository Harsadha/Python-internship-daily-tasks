from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_dashboard():
    response = client.get("/analytics/dashboard")
    assert response.status_code == 200

def test_employee_count():
    response = client.get("/analytics/employee-count/IT")
    assert response.status_code == 200

def test_average_salary():
    response = client.get("/analytics/average-salary/IT")
    assert response.status_code == 200

def test_salary_chart():
    response = client.get("/analytics/salary-chart")
    assert response.status_code == 200