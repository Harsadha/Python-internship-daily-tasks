from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database.dbconnection import get_db
from ..database import models

import os
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/employee-count/{department}")
def employee_count(department: str, db: Session = Depends(get_db)):
    count = (
        db.query(models.Employee)
        .join(models.Department)
        .filter(models.Department.dept_name == department)
        .count()
    )
    return {
        "department": department,
        "employee_count": count
    }

@router.get("/average-salary/{department}")
def average_salary(department: str, db: Session = Depends(get_db)):
    avg = (
        db.query(func.avg(models.Employee.salary))
        .join(models.Department)
        .filter(models.Department.dept_name == department)
        .scalar()
    )
    return {
        "department": department,
        "average_salary": avg
    }

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    total_employees = db.query(models.Employee).count()
    total_departments = db.query(models.Department).count()
    average_salary = db.query(func.avg(models.Employee.salary)).scalar()
    return {
        "total_employees": total_employees,
        "total_departments": total_departments,
        "average_salary": average_salary
    }

@router.get("/salary-chart")
def salary_chart(db: Session = Depends(get_db)):
    data = (
        db.query(models.Department.dept_name, func.avg(models.Employee.salary))
        .join(models.Employee)
        .group_by(models.Department.dept_name)
        .all()
    )
    departments = [row[0] for row in data]
    salaries = [float(row[1]) for row in data]
    plt.figure(figsize=(8,5))
    plt.bar(departments, salaries)
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    os.makedirs("reports", exist_ok=True)
    path = "reports/salary_chart.png"
    plt.savefig(path)
    plt.close()
    return {
        "message": "Chart created successfully",
        "file": path
    }