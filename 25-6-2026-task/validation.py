import re
from logging_config import logging

def validate_name(name):
    if not re.fullmatch(r"[A-Za-z ]+", name):
        logging.info(f"Name:{name} is invalid")
        raise ValueError("Name should contain only letters")
    logging.info(f"Name:{name} is validated")
    return True

def validate_department(dept):
    valid_departments = ["it","aip","mern","hr","sap"]
    if dept.lower() not in valid_departments:
        logging.info(f"Department:{dept} is invalid")
        raise ValueError("Invalid Department")
    logging.info(f"Department:{dept} is validated")
    return True

def validate_salary(salary):
    if salary <= 0:
        logging.error(f"Salary:{salary} is invalid")
        raise ValueError("Salary must be greater than 0")
    logging.info(f"Salary:{salary} is validated")
    return True

def validate_id(emp_id):
    if emp_id <= 0:
        logging.error(f"ID:{emp_id} is invalid")
        raise ValueError( "Invalid Employee ID")
    logging.info(f"ID:{emp_id} is validated")
    return True