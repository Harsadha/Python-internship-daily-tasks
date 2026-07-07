from sqlalchemy import Column, Integer, String, Float
from .dbconnection import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    department = Column(String(100))
    designation = Column(String(100))
    salary = Column(Float)