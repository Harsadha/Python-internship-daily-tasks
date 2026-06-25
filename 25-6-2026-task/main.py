# DAILY TASK- WEEK 4- DAY 1
'''
✓ Connect Python to MySQL — create employees table
✓ Write: add employee, get by dept, update salary, delete by ID
✓ Use ONLY parameterized queries
✓ Store credentials in .env
✓ Log all DB operations to db.log'''

from dbconnection import get_connection
from validation import *
from logging_config import logging

logging.basicConfig(
    level=logging.INFO, 
    filename="db.log",
    format="%(asctime)s- %(levelname)s- %(message)s")

def db_connection():
    db = get_connection()
    cursor = db.cursor()
    return db,cursor
    
def proper_display(employees):
    if not employees:
        print("No employees found.")
        return
    print()

    for emp in employees:
        for value in emp:
            print(f"{str(value):<20}", end="")
        print()

def get_employees_by_department(input_dept):
    try:
        db,cursor = db_connection()
        validate_department(input_dept)
        query = "SELECT ID,NAME,SALARY FROM EMPLOYEES WHERE DEPARTMENT=%s"
        cursor.execute(query,(input_dept,))
        logging.info(f"Showing all employees in {input_dept}")
        employees_by_department = cursor.fetchall()
            
    except Exception as e:
        print("Error:",e)
        logging.error(str(e))
        
    finally:
        cursor.close()
        db.close()
        
    return employees_by_department

def add_employee(input_name,input_department,input_salary):
    try:
        db,cursor = db_connection()
        validate_name(input_name)
        validate_department(input_department)
        validate_salary(input_salary)

        query = "INSERT INTO EMPLOYEES(NAME,DEPARTMENT,SALARY) VALUES(%s,%s,%s)"
        cursor.execute(query,(input_name,input_department,input_salary))
        logging.info(f"Employee added:{input_name}")
        print(f"Employee:{input_name} is added!")
        db.commit()
            
    except Exception as e:
        logging.error(str(e))
        print("Error:",e)
    
    finally:
        cursor.close()
        db.close()
    
def update_salary(input_id,updated_salary):
    try:
        db,cursor = db_connection()
        valid_id = validate_id(input_id)
        if valid_id:
            query = "UPDATE EMPLOYEES SET SALARY=%s WHERE ID=%s"
            cursor.execute(query,(updated_salary,input_id))
            db.commit()
            if cursor.rowcount == 0:
                raise ValueError("Employee ID not found")
            logging.info(f"Salary updated for ID {input_id}")
        
    except Exception as e:
        print("Error:",e)
        logging.error(str(e))
    
    finally:
        cursor.close()
        db.close()

def delete_employee(input_id):
    try:
        db,cursor = db_connection()
        validate_id(input_id)
        query = "DELETE FROM employees WHERE id=%s"
        cursor.execute(query,(input_id,))
        db.commit()
        if cursor.rowcount == 0:
            raise ValueError("Employee not found")
        logging.info(f"Deleted employee {input_id}")
        print("Employee Deleted")

    except Exception as e:
        logging.error(str(e))
        print("Error:", e)

    finally:
        cursor.close()
        db.close()

def display_employees():
    try:
        db,cursor = db_connection()
        query = "SELECT * FROM EMPLOYEES"
        cursor.execute(query)
        employees = cursor.fetchall()
        logging.info("Displaying all employees..")
        print(f"\n{'ID':<20}{'NAME':<20}{'DEPARTMENT':<20}{'SALARY':<20}")
        proper_display(employees)

    except Exception as e:
        logging.error(str(e))
        print("Error:",e)

    finally:
        cursor.close()
        db.close()

def search_employee(search_value):
    try:
        db, cursor = db_connection()
        if search_value.isdigit():
            query = "SELECT ID, NAME, DEPARTMENT, SALARY FROM EMPLOYEES WHERE ID=%s"
            cursor.execute(query,(int(search_value),))
        else:
            query = "SELECT ID, NAME, DEPARTMENT, SALARY FROM EMPLOYEES WHERE NAME LIKE %s"
            cursor.execute(query,(f"%{search_value}%",) )
        result = cursor.fetchall()
        logging.info(f"Search performed: {search_value}")
        return result
    except Exception as e:
        logging.error(str(e))
        print("Error:", e)
    finally:
        cursor.close()
        db.close()

print("\nEMPLOYEE PORTAL")
print("\n1.Add Employee")
print("2.Get Employees By Department")
print("3.Update Salary")
print("4.Delete Employee")
print("5.Display all employees")
print("6.Search for employee")
print("7.Exit\n")
while True:
    print()
    choice = int(input("Enter Choice: "))
    
    match(choice):
        case 1:
            print("Insertion portal..")
            name = input("Enter Employee's Name: ")
            dept = input(f"Enter {name}'s Department: ")
            salary = float(input(f"Enter {name}'s Salary: "))
            add_employee(name,dept,salary)

        case 2:
            print("Department wise display employee portal..")
            dept = input("Enter the Department to get the employee's in: ")
            result = get_employees_by_department(dept)
            print(f"\n{'ID':<20}{'NAME':<20}{'SALARY':<20}")
            proper_display(result)

        case 3:
            print("Updation portal..")
            emp_id = int(input("Enter the Employee ID to change the salary for: "))
            salary = float(input(f"Enter the New Salary for EMP_ID:{emp_id}: "))
            update_salary(emp_id,salary)

        case 4:
            print("Deletion portal..")
            emp_id = int( input("Employee ID to be deleted: "))
            delete_employee(emp_id)

        case 5:
            print("Displaying all the employees..")
            display_employees()

        case 6:
            print("Employee searching portal...")
            search_value = input("Enter your search value:")
            employees = search_employee(search_value)
            print("\nYour search results are..")
            print(f"\n{'ID':<20}{'NAME':<20}{'DEPARTMENT':<20}{'SALARY':<20}")
            proper_display(employees)

        case 7:
            logging.info("Exiting the application..")
            print("Exiting...")
            break
        
        case _:
            print("Invalid Choice")