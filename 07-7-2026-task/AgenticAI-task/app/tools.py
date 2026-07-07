from langchain_core.tools import tool

from .dbconnection import SessionLocal
from . import crud

@tool
def get_emp_count(department: str) -> str:
    """
    Returns the number of employees in a department.
    """
    db = SessionLocal()
    try:
        count = crud.get_employee_count(db, department)
        return f"There are {count} employees in the {department} department."
    finally:
        db.close()

@tool
def get_avg_salary(department: str) -> str:
    """
    Returns the average salary of employees in a department.
    """
    db = SessionLocal()
    try:
        avg = crud.get_average_salary(db, department)
        if avg is None:
            return "No employees found."
        return f"The average salary in the {department} department is {avg:.2f}."
    finally:
        db.close()