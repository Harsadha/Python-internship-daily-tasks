# DAILY TASK- WEEK 4- DAY 5
'''
✓ GET /employees — list all
✓ GET /employees/{id} — get one
✓ POST /employees — add new
✓ All credentials from .env
✓ Test on http://127.0.0.1:8000/docs (Swagger) 
✓ Log every request — push to GitHub'''

from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
import logging

from .models import Base
from .dbconnection import engine, get_db
from . import crud, schemas

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="app.log",      
    filemode="a"             
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming Request: {request.method} {request.url.path}")
    print(f"{request.method} {request.url}")
    response = await call_next(request)
    print(f"Status Code: {response.status_code}")
    logger.info(f"Completed Request: {request.method} {request.url.path} | Status Code: {response.status_code}")
    return response

@app.get("/")
def home():
    return {"message": "Employee API is running!"}

@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employees", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate,db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)