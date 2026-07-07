from celery import Celery
from celery.schedules import crontab
from dotenv import load_dotenv
import os

load_dotenv()

celery_app = Celery(
    "tasks",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)

celery_app.conf.timezone = "Asia/Bengaluru"

celery_app.conf.beat_schedule = {
    "department-summary": {
        "task": "app.tasks.generate_department_summary",
        "schedule": 120.0    
    },

    "employee-backup": {
        "task": "app.tasks.export_employees",
        "schedule": 60.0 #crontab(hour=0, minute=0)   
    }
}

celery_app.conf.imports = ("app.tasks",)

celery_app.autodiscover_tasks(["app"])