# DAILY TASK- WEEK 5- DAY 4
'''
✓ LLMs, tokens, prompts, completions
✓ OpenAI API from Python — api_key in .env 
✓ System / user / assistant message roles 
✓ Structured JSON output from LLM'''

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from google import genai

from dotenv import load_dotenv
from datetime import datetime
import json
import os

from .dbconnection import get_db
from . import crud
from .schemas import PromptRequest

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

@app.post("/ai/summarize")
async def summarize(data: PromptRequest,db: Session = Depends(get_db)):
    employee = crud.get_employee(db, data.employee_id)
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    timestamp = datetime.now().isoformat()
    prompt = f"""You are an HR assistant.
    User Request:
    {data.prompt}
    Employee Details:
    Name: {employee.name}
    Department: {employee.department}
    Designation: {employee.designation}
    Salary: {employee.salary}
    Return ONLY valid JSON.
    Format:
    {{
        "timestamp": "{timestamp}",
        "employee": {{
            "name": "{employee.name}",
            "department": "{employee.department}"
        }},
        "response": "<answer to the user's prompt>"
    }}
    Return only the JSON.
    Do not use markdown.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )
    result = json.loads(response.text)
    with open("employee_summary.json", "w") as file:
        json.dump(result, file, indent=4)
    return result