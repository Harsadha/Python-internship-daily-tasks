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