from langchain_core.tools import tool
from sqlalchemy import func

from ..database.dbconnection import SessionLocal
from ..database import models


@tool
def get_employee_count(department: str) -> str:
    """
    Returns the number of employees in a department.
    """
    db = SessionLocal()
    try:
        count = (
            db.query(models.Employee)
            .join(models.Department)
            .filter(func.lower(models.Department.dept_name)== department.lower())
            .count()
        )
        return f"There are {count} employees in the {department} department."
    finally:
        db.close()

@tool
def get_average_salary(department: str) -> str:
    """
    Returns the average salary of a department.
    """
    db = SessionLocal()
    try:
        average = (
            db.query(func.avg(models.Employee.salary))
            .join(models.Department)
            .filter(func.lower(models.Department.dept_name) == department.lower())
            .scalar()
        )
        if average is None:
            return f"No employees found in the {department} department."
        return (
            f"The average salary in the {department} "
            f"department is ₹{average:,.2f}"
        )
    finally:
        db.close()

@tool
def list_departments() -> str:
    """
    Returns all department names.
    """
    db = SessionLocal()
    try:
        departments = (
            db.query(models.Department)
            .order_by(models.Department.dept_name)
            .all()
        )
        if not departments:
            return "No departments found."
        return ", ".join(
            dept.dept_name
            for dept in departments
        )
    finally:
        db.close()