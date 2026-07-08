from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    dept_name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    dept_id: int
    class Config:
        from_attributes = True

class EmployeeBase(BaseModel):
    emp_name: str
    email: str
    salary: int
    dept_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    emp_id: int
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class AuditLogCreate(BaseModel):
    username: str
    action: str
    timestamp: str

class AuditLogResponse(AuditLogCreate):
    id: int

    class Config:
        from_attributes = True

class SummaryRequest(BaseModel):
    employee_id: int
    prompt: str

class AskRequest(BaseModel):
    question: str