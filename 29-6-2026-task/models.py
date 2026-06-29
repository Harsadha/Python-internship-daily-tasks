from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    dept_id = Column(Integer,primary_key=True)
    dept_name = Column(String(100),nullable=False)
    # 1(dept) to many(employees) relationship
    employees = relationship("Employee", back_populates="department", cascade="all, delete")

class Employee(Base):
    __tablename__ = "employees"
    emp_id = Column( Integer, primary_key=True)
    emp_name = Column( String(100), nullable=False)
    dept_id = Column(Integer,ForeignKey("departments.dept_id"))
    # many(employees) to 1(department) relationship
    department = relationship("Department",back_populates="employees")