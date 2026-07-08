from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarize():
    response = client.post(
        "/ai/summarize",
        json={
            "employee_id":1,
            "prompt":"Summarize this employee"
        }
    )
    assert response.status_code == 200

def test_ask():
    response = client.post(
        "/ai/ask",
        json={
            "question":"How many employees are in IT?"
        }
    )
    assert response.status_code == 200