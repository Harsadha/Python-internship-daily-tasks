# DAILY TASK- WEEK 1- DAY 4
'''
✓ Base class Employee → inherit Manager and Intern
✓ Each overrides get_details() with different output
✓ Store all in a list, call get_details() polymorphically
✓ Use filter + lambda to get employees with salary > 40000
✓ Use sorted(key=) to rank by salary and print leaderboard'''

class Employee:
    employee_id=1000
    def __init__(self,name,salary):
        self.id = Employee.employee_id
        Employee.employee_id+=1
        self.name = name
        self.salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if value<=0:
            raise ValueError("Salary cannot be negative or 0.")
        else:
            self._salary = value
    
    def get_details(self):
        return f"Employee:{self.id}\tName:{self.name}\tSalary:{self.salary}"
    
    def __str__(self):
        return self.get_details()
    
class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def get_details(self):
        return f"Manager:{self.id}\tName:{self.name}\tSalary:{self.salary}"
    
    def __str__(self):
        return self.get_details()
    
class Intern(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def get_details(self):
        return f"Intern:{self.id}\tName:{self.name}\tSalary:{self.salary}"
    
    def __str__(self):
        return self.get_details()

Employees = []

print("\nWelcome to the Employee Management System")
print("1. Add Employee")
print("2. Filter Employees (Salary > 40000)")
print("3. Sort Employees by Salary")
print("4. Display All Employees")
print("0. Exit")
while True:
    print()
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            try:
                name = input("Enter employee name:")
                import re
                pattern = r"^[A-Za-z]+ ([A-Za-z])*$"
                if not re.match(pattern, name):
                    print("Please enter a valid name")
                    continue
                salary = float(input("Enter salary:"))
                designation = input("Enter designation (Employee/Manager/Intern):").lower()
                match designation:
                    case "employee":
                        employee = Employee(name, salary)
                    case "manager":
                        employee = Manager(name, salary)
                    case "intern":
                        employee = Intern(name, salary)
                    case _:
                        print("Invalid designation!")
                        continue
                Employees.append(employee)
                print("Employee added successfully!")
            except Exception as e:
                print("Error:",e)
            # employee = Employee("Harsadha R",90000)
            # Employees.append(employee)
            # employee = Intern("Sruthi",15000)
            # Employees.append(employee)
            # employee = Manager("Ranjeeth K",100000)
            # Employees.append(employee)

        case 2:
            print("\nEmployees with Salary more than Rs.40,000")
            filtered_employees = list(filter(lambda employee: employee.salary > 40000,Employees))
            if not filtered_employees:
                print("No employees found.")
            else:
                for employee in filtered_employees:
                    print(employee)

        case 3:
            print("\nEmployees Sorted by Salary (Descending)\n**Leaderboard**")
            sorted_employees = sorted(Employees,key=lambda employee: employee.salary,reverse=True)
            if not sorted_employees:
                print("No employees available.")
            else:
                rank=0
                for employee in sorted_employees:
                    print("Rank:",rank+1,"\t",employee)
                    rank+=1

        case 4:
            print("\nAll Employees")
            if not Employees:
                print("No employees available.")
            else:
                for employee in Employees:
                    print(employee)

        case 0:
            print("Exiting...")
            break

        case _:
            print("Invalid choice!:/")
