from sqlalchemy.orm import Session
from sqlalchemy import func

from .models import Employee

def get_employee_count(db: Session, department: str):
    return (db.query(Employee).filter(Employee.department.ilike(department)).count())

def get_average_salary(db: Session, department: str):
    return (db.query(func.avg(Employee.salary)).filter(Employee.department.ilike(department)).scalar())