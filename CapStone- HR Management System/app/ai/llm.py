import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_employee(employee, prompt: str):
    """
    Generates an AI summary for an employee.
    """
    full_prompt = f"""
    You are an HR Assistant.
    Employee Details
    Name: {employee.emp_name}
    Email: {employee.email}
    Department: {employee.department.dept_name if employee.department else "N/A"}
    Salary: {employee.salary}

    User Request:
    {prompt}
    Return ONLY valid JSON.

    Format:
    {{
        "employee":"{employee.emp_name}",
        "department":"{employee.department.dept_name if employee.department else 'N/A'}",
        "summary":"..."
    }}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
        config={
            "response_mime_type": "application/json"
        }
    )
    result = json.loads(response.text)
    os.makedirs("reports", exist_ok=True)
    with open("reports/employee_summary.json", "w") as file:
        json.dump(result, file, indent=4)
    return result