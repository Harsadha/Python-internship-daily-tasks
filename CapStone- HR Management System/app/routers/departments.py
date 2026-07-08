import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.dbconnection import get_db
from ..database import models
from .. import schemas

from ..cache.redis_client import redis_client

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)

@router.get("/")
def get_departments(db: Session = Depends(get_db)):
    cache = redis_client.get("departments")
    if cache:
        print("\n** REDIS CACHE HIT **\n")
        return json.loads(cache)
    print("\n** REDIS CACHE MISS **\n")
    departments = db.query(models.Department).all()
    result = []
    for dept in departments:
        result.append({ "dept_id": dept.dept_id,"dept_name": dept.dept_name})
    redis_client.setex("departments", 60,json.dumps(result))
    return result

@router.get("/{dept_id}")
def get_department(dept_id: int,db: Session = Depends(get_db),):
    department = (
        db.query(models.Department)
        .filter(models.Department.dept_id == dept_id)
        .first()
    )
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@router.post("/")
def create_department(department: schemas.DepartmentCreate,db: Session = Depends(get_db),):
    db_department = models.Department(dept_name=department.dept_name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    redis_client.delete("departments")
    print("\n**DEPARTMENT CACHE CLEARED**\n")
    return db_department