# DAILY TASK- WEEK 5- DAY 3
''''
✓ Async task: send welcome email when new employee added via POST
✓ Scheduled task (celery beat): every 2 mins generate dept summary → log
✓ Daily midnight task: export all employees to JSON backup
✓ Monitor tasks on Flower at http://localhost:5555''''

from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from .tasks import send_welcome_email
import logging
import time

from .dbconnection import engine, Base, get_db
from app import models, schemas, crud
from .redis_client import redis_client
from app.utils import (
    hash_password,
    verify_password,
    create_access_token,
    serialize,
    deserialize,
)
from app.auth import get_current_user

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="a"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API with Redis")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request Started | {request.method} {request.url.path}")
    response = await call_next(request)
    process_time = round((time.time() - start_time) * 1000, 2)

    logger.info(
        f"Request Completed | "
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Time: {process_time} ms"
    )
    return response

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400,detail="Username already exists")

    hashed_password = hash_password(user.password)
    crud.create_user(db,username=user.username,hashed_password=hashed_password)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    db_user = crud.get_user(db, form_data.username)
    if db_user is None:
        raise HTTPException(status_code=401,detail="Invalid username or password")
    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token({"sub": db_user.username})
    redis_client.setex( f"session:{db_user.username}", 3600, access_token)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/employees")
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_employee = crud.create_employee(db, employee)
    redis_client.delete("employees")
    send_welcome_email.delay(
        new_employee.email,
        new_employee.name
    )
    return new_employee

@app.get("/employees")
def get_all_employees(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    cache_key = "employees"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("CACHE HIT")
        return deserialize(cached_data)
    print("CACHE MISS")
    employees = crud.get_all_employees(db)
    result = jsonable_encoder(employees)
    redis_client.setex(cache_key,60,serialize(result))
    return result

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    cache_key = f"employee:{employee_id}"
    cached = redis_client.get(cache_key)
    if cached:
        print("CACHE HIT")
        return deserialize(cached)
    print("CACHE MISS")
    employee = crud.get_employee(db,employee_id)
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    result = jsonable_encoder(employee)
    redis_client.setex(cache_key,60,serialize(result))
    return result

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int,employee: schemas.EmployeeUpdate,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    updated_employee = crud.update_employee( db, employee_id, employee)
    if updated_employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    # Cache Invalidation
    redis_client.delete("employees")
    redis_client.delete(f"employee:{employee_id}")
    return updated_employee

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int,db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    employee = crud.delete_employee( db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    # Cache Invalidation
    redis_client.delete("employees")
    redis_client.delete(f"employee:{employee_id}")
    return {"message": "Employee deleted successfully" }

@app.get("/")
def home():
    return {"message": "Employee Management API is running!"}