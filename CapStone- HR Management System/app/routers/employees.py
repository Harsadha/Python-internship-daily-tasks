import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.dbconnection import get_db
from ..database import models
from .. import schemas

from ..cache.redis_client import redis_client

from ..tasks.celery_tasks import send_welcome_email

from ..auth.dependencies import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)

@router.get("/")
def get_all_employees(db: Session = Depends(get_db),):
    cache = redis_client.get("employees")
    if cache:
        print("\n** REDIS CACHE HIT **\n")
        return json.loads(cache)
    print("\n** REDIS CACHE MISS **\n")
    employees = db.query(models.Employee).all()
    result = []
    for emp in employees:
        result.append(
            {
                "emp_id": emp.emp_id,
                "name": emp.emp_name,
                "email": emp.email,
                "salary": emp.salary,
                "department": emp.department.dept_name
                if emp.department
                else None,
            }
        )
    redis_client.setex("employees",60,json.dumps(result), )
    return result

@router.get("/{emp_id}")
def get_employee(emp_id: int,db: Session = Depends(get_db),):
    employee = (
        db.query(models.Employee)
        .filter(models.Employee.emp_id == emp_id)
        .first()
    )
    if not employee:
        raise HTTPException(status_code=404,detail="Employee not found",)
    return {
        "emp_id": employee.emp_id,
        "name": employee.emp_name,
        "email": employee.email,
        "salary": employee.salary,
        "department": employee.department.dept_name
        if employee.department
        else None,
    }

@router.post("/")
def create_employee(employee: schemas.EmployeeCreate,db: Session = Depends(get_db),):
    new_employee = models.Employee(
        emp_name=employee.emp_name,
        email=employee.email,
        salary=employee.salary,
        dept_id=employee.dept_id,
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    redis_client.delete("employees")
    print("\n** EMPLOYEE CACHE CLEARED **\n")
    send_welcome_email.delay(
        new_employee.email,
        new_employee.emp_name,
    )
    return new_employee

@router.put("/{emp_id}")
def update_employee(emp_id: int,employee: schemas.EmployeeUpdate,db: Session = Depends(get_db),current_user=Depends(get_current_user),):
    db_employee = (
        db.query(models.Employee)
        .filter(models.Employee.emp_id == emp_id)
        .first()
    )
    if not db_employee:
        raise HTTPException(status_code=404,detail="Employee not found",)
    db_employee.emp_name = employee.emp_name
    db_employee.email = employee.email
    db_employee.salary = employee.salary
    db_employee.dept_id = employee.dept_id
    db.commit()
    db.refresh(db_employee)
    redis_client.delete("employees")
    print("\n** EMPLOYEE CACHE CLEARED **\n")
    return db_employee

@router.delete("/{emp_id}")
def delete_employee(emp_id: int,db: Session = Depends(get_db),current_user=Depends(get_current_user),):
    db_employee = (
        db.query(models.Employee)
        .filter(models.Employee.emp_id == emp_id)
        .first()
    )
    if not db_employee:
        raise HTTPException(status_code=404,detail="Employee not found",)
    db.delete(db_employee)
    db.commit()
    redis_client.delete("employees")
    print("\n** EMPLOYEE CACHE CLEARED **\n")
    return {"message": "Employee deleted successfully"}