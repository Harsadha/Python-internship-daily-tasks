from sqlalchemy.orm import Session
from .models import Employee

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()