from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "hr_management",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.timezone = "Asia/Kolkata"

celery_app.conf.beat_schedule = {
    # Daily employee backup
    "employee-backup": {
        "task": "app.tasks.celery_tasks.export_employees",
        "schedule": 120.0 #crontab(hour=0, minute=0)
    },
    # Daily analytics report
    "department-summary": {
        "task": "app.tasks.celery_tasks.generate_department_summary",
        "schedule": 60.0 #crontab(hour=9, minute=0)
    }
}

celery_app.conf.imports = (
    "app.tasks.celery_tasks",
)