# DAILY TASK
'''
✓ Call jsonplaceholder.typicode.com/users — GET,POST, PUT, DELETE
✓ Save results to api_results.json
✓ Store all API keys and URLs in .env (not in code)
✓ Add input validation before making API calls
✓ Log all requests with timestamps'''

import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
session = requests.Session()
results = {}

def log_request(method, url):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-{method} -> {url}")

def validate_user_id(user_id):
    if not user_id.isdigit():
        raise ValueError("User ID must be numeric.")
    return int(user_id)

def get_users():
    url = f"{BASE_URL}/users"
    log_request("GET", url)
    response = session.get(url, timeout=5)
    print(f"Status Code: {response.status_code}")
    results["GET"] = response.json()

def create_user():
    url = f"{BASE_URL}/users"
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    import re
    name_pattern = r'^[A-Za-z]+$'
    email_pattern = r'^[A-Za-z0-9_+#.-]+@[A-Za-z0-9_+#.-]+\.[A-Za-z0-9]{2,}$'
    if not re.fullmatch(name_pattern,name):
        raise ValueError("Name cannot be empty.")
    if not re.fullmatch(email_pattern,email):
        raise ValueError("Invalid email.")
    payload = {
        "name": name,
        "email": email
    }
    log_request("POST", url)
    response = session.post(url,json=payload,timeout=5)
    print(f"Status Code: {response.status_code}")
    results["POST"] = response.json()

def update_user():
    user_id = validate_user_id(input("Enter User ID: ").strip())
    name = input("Enter New Name: ").strip()
    if not name.isalpha():
        raise ValueError("Enter a valid name.")
    url = f"{BASE_URL}/users/{user_id}"
    payload = {
        "name": name
    }
    log_request("PUT", url)
    response = session.put(url,json=payload,timeout=5)
    print(f"Status Code: {response.status_code}")
    results["PUT"] = response.json()

def delete_user():
    user_id = validate_user_id(input("Enter User ID: ").strip())
    url = f"{BASE_URL}/users/{user_id}"
    log_request("DELETE", url)
    response = session.delete(url,timeout=5)
    print(f"Status Code: {response.status_code}")
    results["DELETE"] = {"status_code": response.status_code}

def save_results():
    with open("api_results.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Results saved to api_results.json")

def menu():
    while True:
        print("\nMENU")
        print("1. GET Users")
        print("2. POST User")
        print("3. PUT User")
        print("4. DELETE User")
        print("5. Save Results")
        print("6. Exit")
        choice = input("\nChoose option: ").strip()
        try:
            if choice == "1":
                get_users()
            elif choice == "2":
                create_user()
            elif choice == "3":
                update_user()
            elif choice == "4":
                delete_user()
            elif choice == "5":
                save_results()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()