from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database.dbconnection import get_db
from ..database import crud
from .. import schemas

from ..auth.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/register")
def register(user: schemas.UserCreate,db: Session = Depends(get_db),):
    existing = crud.get_user(db, user.username)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )
    hashed = hash_password(user.password)
    crud.create_user(db,user.username,hashed,)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db),):
    user = crud.get_user( db, form_data.username,)
    if not user:
        raise HTTPException(status_code=401,detail="Invalid credentials",)
        
    if not verify_password(form_data.password,user.hashed_password,):
        raise HTTPException(status_code=401,detail="Invalid credentials", )

    token = create_access_token({ "sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }