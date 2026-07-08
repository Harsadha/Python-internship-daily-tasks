# CapStone Project- HR Management System PoC

## Overview

The HR Management System is a FastAPI-based backend application that demonstrates modern backend development concepts, including:

* FastAPI REST APIs
* PostgreSQL with SQLAlchemy ORM
* JWT Authentication
* Redis Caching
* Celery Background Tasks
* Gemini AI Integration
* LangChain ReAct Agent
* HR Analytics
* Pytest Unit Testing

The project is designed as a production-style backend following a modular architecture.

---

# Project Structure

```
app/
│
├── auth/
│     security.py
│     dependencies.py
│
├── database/
│     db.py
│     models.py
│     crud.py
│
├── ai/
│     llm.py
│     tools.py
│     agent.py
│
├── tasks/
│     celery_app.py
│     celery_tasks.py
│
├── analytics/
│     analytics.py
│
├── cache/
│     redis_client.py
│
├── routers/
│     auth.py
│     employees.py
│     departments.py
│     ai.py
│
├── tests/
│     conftest.py
│     test_ai.py
│     test_analytics.py
│     test_auth.py
│     test_departments.py
│     test_employees.py
│     test_main.py
│
├── schemas.py
└── main.py
```

---

# Features

* Employee Management (CRUD)
* Department Management
* User Registration & Login
* JWT Authentication
* AI Employee Summary
* AI Agent using LangChain ReAct
* Employee Analytics Dashboard
* Redis Response Caching
* Celery Background Tasks
* Email Notifications
* JSON Backup Generation
* Automated Testing with Pytest

---

# Technologies Used

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Redis
* Celery
* Google Gemini API
* LangChain
* Matplotlib
* JWT
* Pytest

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>

cd "CapStone- HR Management System"
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

PowerShell

```bash
venv\Scripts\Activate.ps1
```

Command Prompt

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create a PostgreSQL database.

Example

```sql
CREATE DATABASE hr_management;
```

---

# Redis Setup

Start Redis server.

Example

```bash
redis-server
```

Verify Redis

```bash
redis-cli ping
```

Expected Output

```
PONG
```

---

# Environment Variables

Create a `.env` file in the project root.

```
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=hr_management

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password

GEMINI_API_KEY=your_gemini_api_key

REDIS_HOST=localhost
REDIS_PORT=6379

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

# Running the FastAPI Server- Terminal 1

```bash
uvicorn app.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Running Celery Worker- Terminal 2

```bash
celery -A app.tasks.celery_app worker -P solo -l info
```

---

# Running Celery Beat- Terminal 3

```bash
celery -A app.tasks.celery_app beat -l info
```

---

# Running Celery Flower- Terminal 4

```bash
celery -A app.tasks.celery_app flower 
```

---

# Running Tests

Run all tests

```bash
python -m pytest
```

Verbose mode

```bash
python -m pytest -v
```

Run a single test file

```bash
python -m pytest app/tests/test_employees.py
```

Run a single test

```bash
python -m pytest app/tests/test_employees.py::test_create_employee
```

---

# API Modules

## Authentication

* Register User
* Login User
* JWT Authentication

---

## Employees

* Create Employee
* Get Employees
* Update Employee
* Delete Employee

---

## Departments

* Create Department
* List Departments

---

## AI

* Employee Summary
* AI Agent
* Tool Calling

---

## Analytics

* Employee Count
* Average Salary
* Salary Distribution Chart

---

## Background Tasks

* Welcome Email
* Employee Backup
* Department Summary
* Analytics Email Report

---

# Testing

The project contains unit tests for:

* Authentication
* Employees
* Departments
* Analytics
* AI
* Main Application

Run

```bash
python -m pytest -v
```

---

# Future Improvements

* Docker Support
* Role-Based Access Control (RBAC)
* File Uploads
* Attendance Management
* Payroll Module
* Leave Management
* CI/CD Pipeline
* Kubernetes Deployment

---

# Author

Ranjeeth Kumar

Capstone Project – HR Management System
