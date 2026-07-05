from sqlalchemy.orm import Session
from app import models, schemas

def get_all_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id: int):
    return (db.query(models.Employee).filter(models.Employee.id == employee_id).first())

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    new_employee = models.Employee(
        name=employee.name,
        department=employee.department,
        designation=employee.designation,
        salary=employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee(db: Session,employee_id: int,employee: schemas.EmployeeUpdate):
    emp = (db.query(models.Employee).filter(models.Employee.id == employee_id).first())
    if not emp:
        return None
    emp.name = employee.name
    emp.department = employee.department
    emp.designation = employee.designation
    emp.salary = employee.salary
    db.commit()
    db.refresh(emp)
    return emp

def delete_employee(db: Session, employee_id: int):
    emp = (db.query(models.Employee).filter(models.Employee.id == employee_id).first())
    if not emp:
        return None
    db.delete(emp)
    db.commit()
    return emp

def get_user(db: Session, username: str):
    return (db.query(models.User).filter(models.User.username == username).first())

def create_user(db: Session,username: str,hashed_password: str):
    user = models.User(username=username,password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user