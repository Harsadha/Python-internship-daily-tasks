from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    action = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)

class Department(Base):
    __tablename__ = "departments"
    dept_id = Column(Integer,primary_key=True)
    dept_name = Column(String(100),nullable=False)
    employees = relationship("Employee", back_populates="department", cascade="all, delete")

class Employee(Base):
    __tablename__ = "employees"
    emp_id = Column( Integer, primary_key=True)
    emp_name = Column( String(100), nullable=False)
    email = Column(String, unique=True, nullable=False)
    salary = Column(Integer, nullable=False)
    dept_id = Column(Integer,ForeignKey("departments.dept_id"))
    department = relationship("Department",back_populates="employees")

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    hashed_password=Column(String)