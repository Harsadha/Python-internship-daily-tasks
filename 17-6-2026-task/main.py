import os
import sys

from utils import (
    calculate_age,
    generate_password,
    file_size_checker
)

def main():
    print("Current OS:", os.name)
    print("Python Version:", sys.version)

    name = input("Please enter your name:")
    dob = input("Enter your date of birth in DD-MM-YYYY format:")
    age = calculate_age(dob)
    print(f"{name}'s age for DOB {dob} is: {age}")

    length = int(input("Please enter the length of the password you want to generate:"))
    password = generate_password(length)
    print("Generated Password:", password)

    size = file_size_checker("utils.py")
    print("utils.py size:", size)

if __name__ == "__main__":
    main()