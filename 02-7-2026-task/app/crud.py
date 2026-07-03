from sqlalchemy.orm import Session
from . import models
from . import schemas
from . import security

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()

def create_employee(db: Session,employee: schemas.EmployeeCreate):
    emp = models.Employee(
        name=employee.name,
        dept=employee.dept,
        salary=employee.salary,
        experience=employee.experience
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

def update_employee(db: Session,emp_id: int,employee: schemas.EmployeeUpdate):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if emp is None:
        return None
    emp.name = employee.name
    emp.dept = employee.dept
    emp.salary = employee.salary
    emp.experience = employee.experience
    db.commit()
    db.refresh(emp)
    return emp

def delete_employee(db: Session,emp_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if emp is None:
        return None
    db.delete(emp)
    db.commit()
    return emp

def get_user(db: Session,username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session,user: schemas.UserRegister):
    hashed = security.hash_password(user.password)
    new_user = models.User(username=user.username,hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
