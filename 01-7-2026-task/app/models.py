from sqlalchemy import Integer, String, Numeric, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    dept = Column(String(50),nullable=False)
    salary = Column(Numeric(10,2),nullable=False)
    experience = Column(Integer,nullable=False)