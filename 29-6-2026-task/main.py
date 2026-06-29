# DAILY TASK- WEEK 4- DAY 3
'''
✓ Define Department and Employee ORM models with ForeignKey
✓ Write ORM functions: add, list, update, delete
✓ Query all employees in a department using relationship()
✓ Switch DB URL from MySQL to PostgreSQL — verify no code changes
✓ Push to GitHub'''

from crud import *
from dbconnection import Session, engine
from models import Base

Base.metadata.create_all(engine)
session = Session()

print("""
      MENU
1 ADD DEPARTMENT
2 ADD EMPLOYEE
3 VIEW DEPARTMENTS
4 VIEW EMPLOYEES
5 UPDATE DEPARTMENT
6 UPDATE EMPLOYEE
7 DELETE DEPARTMENT
8 DELETE EMPLOYEE
9 EMPLOYEES BY DEPARTMENT
10 EXIT
""")

while True:
    choice = int(input("\nChoice: "))
    match choice:
        case 1:
            print("Enter the details below to add department..")
            name=input("Department name: ")
            dept=add_department(session,name)
            print("Added:",dept.dept_name)

        case 2:
            print("Enter the details below to add employee..")
            try:
                name=input("Employee name: ")
                dept=int(input("Department id: "))
                emp=add_employee(session,name,dept )
                print("Added:",emp.emp_name)
            except Exception as e:
                print("Error:",e)

        case 3:
            print("Displaying the list of departments...")
            try:
                print(f"{"D_ID":<5} {"D_NAME":<15}")
                for d in list_departments(session):
                    print(f"{d.dept_id:<5} {d.dept_name:<15}")
            except Exception as e:
                print("Error:",e)

        case 4:
            print("Displaying the list of employees...")
            try:
                print(f"{"E_ID":<5} {"E_NAME":<15} {"D_ID":<5}")
                for e in list_employees(session):
                    print(f"{e.emp_id:<5} {e.emp_name:<15} {e.dept_id:<5}")
            except Exception as e:
                print("Error:",e)

        case 5:
            print("Enter the details below to update department info..")
            try:
                id=int(input("Dept id: "))
                name=input("New name: ")
                update_department(session,id,name)
            except Exception as e:
                print("Error:",e)

        case 6:
            print("Enter the details below to update employee info..")
            try:
                id=int(input("Employee id: "))
                dept=int(input("New dept id: "))
                update_employee(session,id,dept)
            except Exception as e:
                print("Error:",e)

        case 7:
            print("Enter the details to delete a department..")
            try:
                id=int(input("Department id: "))
                delete_department(session, id)
            except Exception as e:
                print("Error:",e)

        case 8:
            print("Enter the details to delete a employee..")
            try:
                id=int(input("Employee id: "))
                delete_employee(session, id)
            except Exception as e:
                print("Error:",e)

        case 9:
            try:
                name=input("Department name: ")
                employees=employees_by_department( session, name)
                print(f"{"E_ID":<5} {"E_NAME":<15}")
                for e in employees:
                    print(f"{e.emp_id:<5} {e.emp_name:<15}")
            except Exception as e:
                print("Error:",e)

        case 10:
            print("Exiting..")
            break