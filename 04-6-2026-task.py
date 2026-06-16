# DAILY TASK- WEEK 1- DAY 1
'''
Take a list of 10 employee names and salaries as a dictionary. Print:
✓ Top 3 highest earners
✓ Average salary
✓ Count of employees above/below average
✓ All names sorted alphabetically in uppercase '''

# imports
from datetime import datetime
import re

# functionalities
# 1. Finding top 3 highest earning employees
def top_3_highest_earners(**employees):
    employees_sorted_by_salary = dict(sorted(employees.items(),key=lambda x:x[1],reverse=True))
    top_3_highest_earners_list = []
    i=0
    for k,v in employees_sorted_by_salary.items():
        top_3_highest_earners_list.append(k)
        i+=1
        if i==3:
            return top_3_highest_earners_list
    return top_3_highest_earners_list

# 2. Finding employees' average salary
def employees_average_salary(**employees):
    total_salary = sum(employees.values())
    number_of_employees = len(employees.items())
    if number_of_employees==0:
        return 0
    return total_salary/number_of_employees

# 3. Counting the number of employees earning more/less than the average salary
def employees_salary_above_average(**employees):
    employees_salary_above_average_count=0
    employees_average_salary_amount = employees_average_salary(**employees)
    for employee, salary in employees.items():
        if salary>=employees_average_salary_amount:
            employees_salary_above_average_count+=1
    return employees_salary_above_average_count

# 4. Sort the employees by name in alphabetical order
def employees_sorted_by_name(**employees):
    employees_sorted_by_name_dict = dict(sorted(employees.items()))
    return employees_sorted_by_name_dict

# Storing the employees data into a dictionary
employees={}

current_hour = datetime.now().hour
if 5 <= current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 16:
    greeting = "Good Afternoon"
elif 16 <= current_hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"
print(greeting,"O-O!")

print("Welcome to the employee portal :)\n" \
"Menu:\n0-> exit\n1-> Enter employee details\n2-> View top 3 earning employees\n3-> Find average salary\n" \
"4-> Find number of employees earning above/below the average salary\n5-> sort the employees in alphabetic order\n")
while(1):
    choice = int(input("Enter choice:"))    
    if choice==1:
        name = input("Enter name(e.g: Anne Hathaway):") 
        pattern = r"^[A-Za-z]+ ([A-Za-z])*$"
        if not re.match(pattern, name):
            print("Please enter a valid name")
            continue
        salary = input("Enter salary:")
        try:
            salary = float(salary)
        except ValueError:
            print("Please enter a valid salary, do not include alphabets or special characters.")
            continue
        if salary<=0:
            print("Salary cannot be negative or 0. Please enter a valid salary.")
            continue
        employees[name] = salary
        print(name,"'s record added!")
    elif choice==2:
        top_3_highest_earners_result=top_3_highest_earners(**employees)
        print("The top 3 earning employees are:",top_3_highest_earners_result)
    elif choice==3:
        employees_average_salary_result = employees_average_salary(**employees)
        print("The average salary of the employees are:",employees_average_salary_result)
    elif choice==4:
        employees_salary_above_average_result = employees_salary_above_average(**employees)
        employees_salary_below_average_result = len(employees.items())-employees_salary_above_average_result
        print("Number of employees earning more than average are:",employees_salary_above_average_result,"\nNumber of employees earning less than average are:",employees_salary_below_average_result)
    elif choice==5:
        employees_sorted_by_name_result = employees_sorted_by_name(**employees)
        print("Employees sorted by name:",employees_sorted_by_name_result)
    elif choice==0:
        print("Exiting..")
        break
    else:
        print("Please enter a valid choice.")
        continue