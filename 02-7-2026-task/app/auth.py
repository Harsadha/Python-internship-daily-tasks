from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from . import crud
from . import schemas
from . import security
from .dbconnection import get_db

router = APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register")
def register(user: schemas.UserRegister,db: Session = Depends(get_db)):
    existing = crud.get_user(db,user.username)
    if existing:
        raise HTTPException(status_code=400,detail="Username already exists")

    crud.create_user( db,user)

    return {"message":"User Registered Successfully"}

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):

    db_user = crud.get_user(db, form_data.username)

    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid Username")

    if not security.verify_password(form_data.password,db_user.hashed_password):
        raise HTTPException(status_code=401,detail="Invalid Password")

    access_token = security.create_access_token({"sub": db_user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }