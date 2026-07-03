# DAILY TASK- WEEK 5- DAY 2
'''
✓ PUT /employees/{id} — update (JWT protected)
✓ DELETE /employees/{id} — delete (JWT protected)
✓ POST /auth/register — hash password with bcrypt
✓ POST /auth/login — returns JWT access token
✓ Return 401 for invalid/missing token'''

from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
import logging

from .models import Base
from .dbconnection import engine, get_db
from . import crud, schemas
from .auth import router as auth_router
from .dependencies import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")

app.include_router(auth_router)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="a"
)

logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming Request : {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Completed Request : {request.method} {request.url.path} | Status : {response.status_code}")
    return response

@app.get("/")
def home():
    return {"message":"Employee API is Running!"}

@app.get("/employees",response_model=list[schemas.EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{emp_id}",response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int,db: Session = Depends(get_db)):
    employee = crud.get_employee(db,emp_id)
    if employee is None:
        raise HTTPException( status_code=404, detail="Employee not found")
    return employee

@app.post("/employees",response_model=schemas.EmployeeResponse)
def add_employee(employee: schemas.EmployeeCreate,db: Session = Depends(get_db)):
    return crud.create_employee(db,employee)

@app.put("/employees/{emp_id}",response_model=schemas.EmployeeResponse)
def update_employee(emp_id: int,employee: schemas.EmployeeUpdate,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    updated = crud.update_employee(db, emp_id, employee)
    if updated is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    return updated

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    deleted = crud.delete_employee(db,emp_id)
    if deleted is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    return {"message":"Employee Deleted Successfully"}