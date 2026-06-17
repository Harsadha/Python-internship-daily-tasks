# main.py

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

    dob = "2002-05-15"
    age = calculate_age(dob)

    print(f"Age for DOB {dob}: {age}")

    password = generate_password(12)
    print("Generated Password:", password)

    size = file_size_checker("utils.py")
    print("utils.py size:", size)


if __name__ == "__main__":
    main()