import json
import os
import smtplib

from email.mime.text import MIMEText
from dotenv import load_dotenv

from app.celery_app import celery_app
from app.dbconnection import SessionLocal
from app import crud

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

@celery_app.task
def send_welcome_email(email, name):
    subject = "Welcome"
    body = f"""
Hi {name},
Welcome to our Employee Management System.
Regards,
HR Team
"""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_EMAIL
    msg["To"] = email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Welcome email sent to {name}")
    except Exception as e:
        print(e)

@celery_app.task
def generate_department_summary():
    db = SessionLocal()
    try:
        employees = crud.get_all_employees(db)
        summary = {}
        for emp in employees:
            summary[emp.department] = summary.get(emp.department, 0) + 1
        with open("department_summary.txt", "a") as file:
            file.write(json.dumps(summary))
            file.write("\n")
        print("Department summary generated")
    finally:
        db.close()

@celery_app.task
def export_employees():
    db = SessionLocal()
    try:
        employees = crud.get_all_employees(db)
        result = []
        for emp in employees:
            result.append({
                "id": emp.id,
                "name": emp.name,
                "department": emp.department,
                "designation": emp.designation,
                "salary": emp.salary
            })
        with open("employees_backup.json", "w") as file:
            json.dump(result, file, indent=4)
        print("Employee backup created")
    finally:
        db.close()