from sqlalchemy import Column, Integer, String
from .dbconnection import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    department = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    salary = Column(Integer, nullable=False)
    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)