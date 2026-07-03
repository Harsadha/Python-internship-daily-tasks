from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    dept: str
    salary: float
    experience: int

class EmployeeResponse(EmployeeCreate):
    id: int
    class Config:
        from_attributes = True

class EmployeeUpdate(BaseModel):
    name: str
    dept: str
    salary: float
    experience: int

class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str