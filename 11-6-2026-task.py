# DAILY TASK- WEEK 2- DAY 1
'''
✓ Read a CSV of employees (name, department,salary)
✓ Find average salary per department
✓ Write new CSV with "Bonus" column (10% of salary)
✓ Raise custom EmptyFileError if file is empty
✓ Handle all bad rows gracefully with error message'''

import csv
import re
import os
from collections import defaultdict

class EmptyFileError(Exception):
    pass

def read_from_csv(filename):
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if len(rows)==0:
            raise EmptyFileError("The file entered is empty.")
        return rows

def average_salary_per_department(rows):
    list_of_salary_of_departments = defaultdict(list)
    for row in rows:
        try:
            departments = row["Department"].lower()
            salaries = float(row["Salary"])
            list_of_salary_of_departments[departments].append(salaries)
        except (ValueError,KeyError):
            print(f"Skipping bad row: {row}")
    average_salary_of_department = {}
    for department,salary_list in list_of_salary_of_departments.items():
        average_salary_of_department[department] = sum(salary_list)/len(salary_list)

    return average_salary_of_department

def create_hike_file(rows,percentage,output_file):
    fields = ["ID","Name","Department","Salary","Bonus","Bonus_percentage","New_Salary"]
    with open(output_file,"w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        for row in rows:
            try:
                salary = float(row["Salary"])
                row["Bonus"] = round(salary*0.10,2)
                row["Bonus_percentage"] = str(percentage)+"%"
                row["New_Salary"] = round(salary*(1+percentage/100),2)
                writer.writerow(row)
            except (ValueError,KeyError):
                print(f"Skipping bad row: {row}")
    return rows

def write_to_csv(rows,filename):
    fields = ["ID","Name","Department","Salary"]
    with open(filename,"w",newline="") as file:

        writer = csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)

            except (ValueError,KeyError):
                print(f"Skipping bad row: {row}")
    return rows

def add_employee(rows,id,name,department,salary):
    try:
        float(salary)
        rows.append({ "ID":id,"Name":name,"Department":department, "Salary":salary})
        return rows

    except ValueError:
        print("Salary must be numeric.")
        return rows

print("\nWelcome to the Employee Portal.\nMENU:")
print("1. View Employees")
print("2. Add Employee")
print("3. View Average Salary Per Department")
print("4. Create Hike File")
print("5. Save Employees")
print("6. Exit")

filename = "C:/Users/h.ranjeeth.kumar/OneDrive - Accenture/Documents/Project/employee.csv"

try:
    rows = read_from_csv(filename)

except FileNotFoundError:
    print("File not found.")
    rows = []

except EmptyFileError as e:
    print(e)
    rows = []

while True:
    choice = input("\nEnter choice: ")
    if choice =="1":
        if not rows:
            print("No employee records found.")
        else:
            print("\nEmployee Records")
            for row in rows:
                print(row)

    elif choice== "2":
        try:
            emp_id = input("Enter ID (EMPXXX): ")
            name = input("Enter Name: ")
            name_pattern = r"^[A-Za-z]+(\s[A-Za-z]+)*$"
            if not re.fullmatch(name_pattern,name):
                print("Enter a valid name.")
                continue                
            approved_departments = ["sales","hr","marketing","data science","software developement"]
            print("Available departments:",approved_departments)
            department = input("Enter employee's department:")
            if department.strip().lower() not in approved_departments:
                print("Please enter a valid department:")
                continue
            salary = float(input("Enter Salary: "))
            if salary<=0:
                print("Salary cannot be negative or zero")
                continue
            rows = add_employee(rows,emp_id,name,department,salary)
            if rows:
                print("Employee added successfully!")

        except Exception as e:
            print("Error:",e)

    elif choice == "3":
        try:
            averages = average_salary_per_department(rows)
            if not averages:
                print("No valid employee data found.")
            else:
                print("\nAverage Salary Per Department")
                for dept,avg in averages.items():
                    print(f"{dept}: {avg:.2f}")

        except Exception as e:
            print("Error:",e)

    elif choice == "4":
        try:
            percentage = float(input( "Enter hike percentage: "))
            output_file = input("Enter output file name: ")

            create_hike_file(rows,percentage,output_file)
            print("File saved at:")
            print(os.path.abspath(output_file))
            print( f"{output_file} created successfully.")

        except ValueError:
            print("Please enter a valid percentage.")

        except Exception as e:
            print("Error:",e)

    elif choice == "5":
        try:
            write_to_csv(rows,filename)
            print("Employees saved successfully.")

        except Exception as e:
            print("Error:",e)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")

# pdf reading, other readers for csv