from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.dbconnection import get_db
from ..database import models

from .. import schemas

from ..ai.llm import summarize_employee
from ..ai.agent import ask_hr_agent

router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"],
)


@router.post("/summarize")
def summarize(data: schemas.SummaryRequest,db: Session = Depends(get_db),):
    employee = (
        db.query(models.Employee)
        .filter(models.Employee.emp_id == data.employee_id)
        .first()
    )
    if not employee:
        raise HTTPException(status_code=404,detail="Employee not found",)

    return summarize_employee(employee,data.prompt,)

@router.post("/ask")
def ask(question: schemas.AskRequest,):
    answer = ask_hr_agent(question.question)
    return {"question": question.question,"answer": answer,}