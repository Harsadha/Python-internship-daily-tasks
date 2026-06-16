# DAILY TASK- WEEK 2- DAY 2
'''
✓ Read students.json with nested subject marks
✓ Calculate total, average, pass/fail per student
✓ Add "result" key to each record
✓ Write updated data to output.json with clean formatting
✓ Log every step (reads, writes, errors) to app.log + console'''

import json
import logging
from logging.handlers import RotatingFileHandler

INPUT_FILE = "C:/Users/h.ranjeeth.kumar/OneDrive - Accenture/Documents/Project/student.json"
OUTPUT_FILE = "output.json"
PASS_MARK = 50

logger = logging.getLogger("StudentApp")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# console Logs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# file Logs
file_handler = RotatingFileHandler(
    "app.log",
    maxBytes=5000,
    backupCount=3
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_students():
    try:
        logger.info("Loading student data")

        with open(INPUT_FILE, "r") as file:
            students = json.load(file)

        logger.info(f"{len(students)} student records loaded")
        logger.debug(f"Loaded Data: {students}")
        return students

    except FileNotFoundError:
        logger.error("student.json not found")
        return []

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {e}")
        return []

    except Exception as e:
        logger.critical(f"Unexpected Error: {e}")
        return []

def view_students(students):
    if not students:
        print("\nNo student records found.")
        return

    for student in students:
        print(f"\nID: {student.get('id')}")
        print(f"Name: {student.get('name')}")
        print(f"Subjects: {student.get('subjects')}")

    logger.info("Viewed all students")

def add_student(students):
    try:
        student_id = int(input("Enter Student ID: "))

        # duplicate ID check
        for student in students:
            if student.get("id") == student_id:
                logger.warning("Duplicate student ID")
                print("Student ID already exists.")
                return

        name = input("Enter Student Name: ").strip()

        if not name:
            logger.error("Empty name entered")
            print("Name cannot be empty.")
            return

        subjects = {}
        for subject in ["Math", "Science", "English"]:
            while True:
                try:
                    mark = int(input(f"Enter {subject} marks: "))
                    if 0 <= mark <= 100:
                        subjects[subject] = mark
                        break
                    print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

        new_student = {
            "id": student_id,
            "name": name,
            "subjects": subjects
        }

        students.append(new_student)
        # savr to student.json
        with open(INPUT_FILE, "w") as file:
            json.dump(students, file, indent=4)
        logger.info(f"Student {name} added successfully")

    except Exception as e:
        logger.error(f"Error adding student: {e}")

def search_student(students):
    try:
        search_id = int(input("Enter Student ID: "))
        logger.info(f"Searching for student ID {search_id}")

        for student in students:
            if student.get("id") == search_id:
                print(f"ID :{student.get('id')}")
                print(f"Name : {student.get('name')}")
                print(f"Subjects: {student.get('subjects')}")

                if "total" in student:
                    print(f"Total : {student.get('total')}")
                    print(f"Average: {student.get('average')}")
                    print(f"Result  : {student.get('result')}")
                return

        logger.warning("Student not found")
        print("Student not found.")

    except ValueError:
        logger.error("Invalid ID entered")

def calculate_results(students):
    if not students:
        logger.warning("No students available")
        return
    logger.info("Calculating student results")

    for student in students:
        try:
            name = student.get("name", "Unknown")
            subjects = student.get("subjects", {})
            logger.debug(f"{name} Subjects: {subjects}")
            marks = list(subjects.values())
            logger.debug(f"{name} Marks: {marks}")
            total = sum(marks)
            average = (total / len(marks) if marks else 0)

            result = ("Pass" if all(mark >= PASS_MARK for mark in marks) else "Fail")
            
            student["total"] = total
            student["average"] = round(average, 2)
            student["result"] = result

            logger.debug( f"{name}: Total={total}, Average={average}, Result={result}")
            logger.info(f"{name} processed successfully")

        except Exception as e:
            logger.error(
                f"Error processing student: {e}"
            )

    for student in students:
        print(f"\nID      : {student.get('id')}")
        print(f"Name    : {student.get('name')}")
        print(f"Total   : {student.get('total')}")
        print(f"Average : {student.get('average')}")
        print(f"Result  : {student.get('result')}")

    save_results(students)

def save_results(students):
    try:
        logger.info("Writing results to output.json")
        with open(OUTPUT_FILE, "w") as file:
            json.dump(students,file, indent=3)
        logger.info("output.json created successfully")

    except Exception as e:

        logger.error(
            f"Error writing output file: {e}"
        )

logger.info("Program Started")

students = load_students()
print(" WELCOME TO STUDENT MANAGEMENT SYSTEM :)")
print("1. View Students")
print("2. Add Student")
print("3. Generate Results")
print("4. Search Student by ID")
print("0. Exit")

while True:
    print()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_students(students)

    elif choice == 2:
        add_student(students)

    elif choice == 3:
        calculate_results(students)

    elif choice == 4:
        search_student(students)

    elif choice==0:
        logger.info("Exiting the program..")
        break

    else:
        logger.warning("Invalid menu option selected")
        print("Invalid choice. Please try again.")