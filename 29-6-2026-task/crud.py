from models import Employee, Department
import re

def add_department(session, name):
    dept = Department(dept_name=name)
    session.add(dept)
    session.commit()
    return dept

def add_employee(session, name,dept_id):
    if not re.fullmatch("^[A-Za-z]+$",name):
        raise ValueError("Enter a valid name.")
    # checking if the department exists already
    department = session.query(Department).filter(Department.dept_id==dept_id).first()
    if not department:
        raise ValueError(f"Department with ID {dept_id} does not exist.")
    employee = Employee(emp_name=name,dept_id = dept_id)
    session.add(employee)
    session.commit()
    return employee

def list_departments(session):
    depts = session.query(Department).all()
    if not depts:
        raise ValueError(f"Department list is empty")
    return depts

def list_employees(session):
    employees = session.query(Employee).all()
    if not employees:
        raise ValueError(f"Employee list is empty")
    return employees

def update_department(session,id,name):
    dept = session.query(Department).filter(Department.dept_id==id).first()
    if dept:
        dept.dept_name = name
        session.commit()
        return dept
    raise ValueError(f"Department_ID:{id} doesnt exist.")

def update_employee(session,employee_id,dept_id):
    employee = session.query(Employee).filter(Employee.emp_id==employee_id).first()
    if employee:
        employee.dept_id = dept_id
        session.commit()
        return employee
    raise ValueError(f"Employee_ID:{employee_id} doesnt exist.")  

def delete_department(session,id):
    dept = session.query(Department).filter(Department.dept_id==id).first()
    if dept:
        session.delete(dept)
        session.commit()
        return dept
    raise ValueError(f"Department_ID:{id} doesn't exist.")    

def delete_employee(session,id):
    employee = session.query(Employee).filter(Employee.emp_id==id).first()
    if employee:
        session.delete(employee)
        session.commit()
        return employee
    raise ValueError(f"Employee_ID:{id} doesnt exist.")  

def employees_by_department(session,dept_name):
    dept = session.query(Department).filter(Department.dept_name == dept_name).first()
    if dept:
        return dept.employees
    raise ValueError(f"Employees do not exist in DEPT_ID:{dept_name}.")