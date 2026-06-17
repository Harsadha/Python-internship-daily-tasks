# DAILY TASK- WEEK 2- DAY 5
'''
✓ Create utils.py with helper functions (age from DOB, random password generator, file size checker)
✓ Import and use all in main.py
✓ Set up a clean virtual environment for the project
✓ Generate requirements.txt with pip freeze
✓ Commit utils.py and requirements.txt to GitHub'''

from datetime import datetime
import random
import string
import os

def calculate_age(dob):
    birth_date = datetime.strptime(dob, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )
    return password

def file_size_checker(file_path):
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        return f"{size} bytes"
    else:
        return "File not found"