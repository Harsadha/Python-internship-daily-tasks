from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import declarative_base

# Existing Employee Table
Base = declarative_base()

class Employee(Base):
    __tablename__="employee"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    dept=Column(String)
    salary=Column(Float)
    experience=Column(Integer)

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    hashed_password=Column(String)