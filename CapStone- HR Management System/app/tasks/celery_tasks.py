import json
import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from dotenv import load_dotenv

from .celery_app import celery_app

from ..database.dbconnection import SessionLocal
from ..database import models

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

@celery_app.task
def send_welcome_email(email: str, name: str):
    subject = "Welcome to HR Management System"
    body = f"""
    Hi {name},
    Welcome to the HR Management System.
    Your employee account has been created successfully.

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
        server.login(SMTP_EMAIL,SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Welcome Email Sent")
    except Exception as e:
        print(e)

@celery_app.task
def export_employees():
    db = SessionLocal()
    try:
        employees = db.query(models.Employee).all()
        data = []
        for emp in employees:
            data.append({
                "emp_id": emp.emp_id,
                "name": emp.emp_name,
                "email": emp.email,
                "salary": emp.salary,
                "department": emp.department.dept_name if emp.department else None
            })
        os.makedirs("backups", exist_ok=True)
        with open("backups/employees_backup.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Employee Backup Created")
    finally:
        db.close()

@celery_app.task
def generate_department_summary():
    db = SessionLocal()
    try:
        employees = db.query(models.Employee).all()
        summary = {}
        for emp in employees:
            dept = emp.department.dept_name if emp.department else "Unknown"
            summary[dept] = summary.get(dept, 0) + 1
        os.makedirs("reports", exist_ok=True)
        with open("reports/department_summary.json", "w") as file:
            json.dump(summary, file, indent=4)
        print("Department Summary Generated")
    finally:
        db.close()

@celery_app.task
def send_report_email(receiver_email):
    message = MIMEMultipart()
    message["Subject"] = "HR Analytics Report"
    message["From"] = SMTP_EMAIL
    message["To"] = receiver_email
    message.attach(MIMEText( "Attached is today's HR Dashboard.", "plain"))
    chart_path = "reports/dashboard.png"
    if os.path.exists(chart_path):
        with open(chart_path, "rb") as file:
            attachment = MIMEApplication(file.read())
            attachment.add_header("Content-Disposition","attachment",filename="dashboard.png")
            message.attach(attachment)
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL,SMTP_PASSWORD)
        server.send_message(message)
        server.quit()
        print("Analytics Report Sent")
    except Exception as e:
        print(e)