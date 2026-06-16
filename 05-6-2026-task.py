# DAILY TASK- WEEK 1- DAY 2
'''
✓ Use Counter to find top 3 frequent words in a paragraph
✓ Use defaultdict to group employees by department
✓ List comprehension — filter salaries above 50000 and square them
✓ Write a generator that yields fibonacci numbers — print first 10'''

# logging.info -> status, .error
# finding top 3 frequent words
def top_3_frequent_words(paragraph):
    from collections import Counter
    words = paragraph.lower().split()
    counter = Counter(words)
    top_3_frequent_words = counter.most_common(3)
    return top_3_frequent_words

paragraph = "Betty bought a bit of butter and the butter was bitter so betty bought a better butter to make the bitter butter better"
# paragraph = input("Enter the paragraph:")
print("The top 3 most frequent words are:",top_3_frequent_words(paragraph))

#getting records from db
def read_from_db():
    query = """SELECT id,name,department,salary FROM EMPLOYEES"""
    cursor.execute(query)

    columns = [col[0] for col in cursor.description]
    employees = [ dict(zip(columns, row)) for row in cursor.fetchall()]
    return employees

# defaultdict to group employees by department
def grouping_employees(employees):
    from collections import defaultdict
    department_with_employees = defaultdict(list)
    for employee in employees:
        department_with_employees[employee["department"]].append(employee)
    return department_with_employees

# filter salaries abover 50000 and square them using list comprehension
def filter_salary_above_5000(employees):
    employees_earning_above_5000 = [employee for employee in employees if employee["salary"]>50000]
    return employees_earning_above_5000

# # key:  value: square
# {name: marks}
# list=> 
# result = {student[":  if student["marks"]>=90}

# update employee records
def update_employee_salary_hike(employee_id, hike_percentage):
    query = """ UPDATE employees SET salary = salary + (salary * %s / 100) 
                WHERE id = %s"""
    cursor.execute(query, (hike_percentage, employee_id))
    conn.commit()
    return cursor.rowcount> 0

def update_employee_salary(employee_id, new_salary):
    query = """ UPDATE employees SET salary = %s
                WHERE id = %s"""
    cursor.execute(query, (new_salary, employee_id))
    conn.commit()
    return cursor.rowcount> 0

def update_employee_department(employee_id,new_department):
    query = """ UPDATE employees SET department = %s
                WHERE id = %s"""
    cursor.execute(query, (new_department, employee_id))
    conn.commit()
    return cursor.rowcount> 0

def delete_employee_record(id):
    query = """ DELETE FROM EMPLOYEES WHERE ID=%s"""
    cursor.execute(query,(id,))
    conn.commit()
    return cursor.rowcount> 0

# db connection
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TjI0AVxe",
    database="mydb"
)
cursor = conn.cursor()

# main function
print("Welcome to the employee portal :)\nMenu\n1-> Enter employee details\n2-> group employees based on department\n" \
"3-> filtering salaries above 50000 and squaring them\n4-> Display the records of the employees\n5-> Update a record of an employee" \
"\n6-> delete an employee record\n0-> exit")

while(1):
    choice = int(input("\nEnter your choice:"))

    if choice==1:
        # getting input values from the user
        name = input("\nEnter employee's name(eg: Harsadha Ranjeeth):")
        # name validation with pattern
        import re
        pattern = r"^[A-Za-z]+ ([A-Za-z])*$"
        if not re.match(pattern, name):
            print("Please enter a valid name")
            continue

        approved_departments = ["aip","sap","mern","it"]
        print("Available departments:",approved_departments)
        department = input("Enter employee's department:")
        # department validation with the existing departments
        if department.strip().lower() not in approved_departments:
            print("Please enter a valid department:")
            continue

        salary = input("Entern employee's salary:")
        # salary validation with float and negative
        try:
            salary = float(salary)
        except ValueError:
            print("Please enter a valid salary, do not include alphabets or special characters.")
            continue
        if salary<=0:
            print("Salary cannot be negative or 0. Please enter a valid salary.")
            continue

        # inserting records into the db
        query = """INSERT INTO EMPLOYEES(name,department,salary) VALUES(%s,%s,%s)"""
        values = (name,department,salary)
        cursor.execute(query,values)
        conn.commit()
        print("\n",name,"'s record added successfully!")
        # employee id is auto incremented in the db, so getting the last rowid for the employee id
        print("Generated Employee ID:", cursor.lastrowid)

    elif choice==2:
        employees = read_from_db()

        grouping_employees_result = grouping_employees(employees)
        print("Displaying employees name department-wise")
        for department, employees_list in grouping_employees_result.items():
            print("\nDepartment:",department.upper())
            for employee in employees_list:
                print("+",employee["name"].upper())

    elif choice==3:
        employees = read_from_db()
        employee_earning_above_5000_result = filter_salary_above_5000(employees)

        print("\nEmployees earning above 50000 with their salaries squared are:")
        for employee in employee_earning_above_5000_result:
            print("+",employee["name"].upper(),"-",employee["salary"]**2)

    elif choice==4:
        # display all the records
        employees = read_from_db()
        print("\nDisplaying the employee records:")
        for employee in employees:
            print("ID:",employee["id"],"Name:",employee["name"],"Department:",employee["department"],"Salary:",employee["salary"])

    elif choice==5:
        # updating salary or department
        print("\nEnter 0 if you want to update salary or 1 to update department")
        update_choice = int(input("Please enter your choice:"))
        if update_choice==0:
            print("\nPlease enter 0 if you want to give a hike or 1 if you want to change the salary")
            salary_choice = int(input("Enter your salary updation choice:"))
            if salary_choice==0:
                id = int(input("Enter the employee's id:"))
                hike = int(input("\nPlease enter the hike percentage as a number(if 5% just enter 5):"))
                if update_employee_salary_hike(id,hike):
                    print("Updation was successful!")
                else:
                    print("Updation failed.Please retry.")
                    continue
            elif salary_choice==1:
                id = int(input("Enter the employee's id:"))
                new_salary = float(input("Enter the new salary for the employee:"))
                if update_employee_salary(id,new_salary):
                    print("Updation of the salary was successful!")
                else:
                    print("Updation failed.Please retry.")
                    continue
            else:
                print("Please enter a valid choice")
                continue

        elif update_choice==1:
            # updation of department
            id = int(input("Enter the employee's id:"))
            new_department = input("Enter the department name to be updated:")
            if update_employee_department(id,new_department):
                print("Updation was sucessful")
            else:
                print("Updation failed. Please retry.")
                continue
        else:
            print("Please enter a valid choice for the updation")

    elif choice==6:
        # deletion of the employee records
        id = int(input("Enter the employee's id to be deleted:"))
        if delete_employee_record(id):
            print("Deletion was successful!")
        else:
            print("Deletion failed.")

    elif choice==0: 
        print("Exiting...")
        conn.close()
        break

    else:
        print("Enter a valid choice.")
        continue

# Write a generator that yields fibonacci numbers — print first 10
def fibonacci():
    a,b=0,1
    while(1):
        yield a
        a,b = b,a+b

fib = fibonacci()
for i in range(10):
    print(next(fib))

