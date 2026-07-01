from sqlalchemy.orm import Session
from . import models, schemas

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    new_employee = models.Employee(
        name=employee.name,
        dept=employee.dept,
        salary=employee.salary,
        experience=employee.experience
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee