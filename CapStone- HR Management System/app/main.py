from fastapi import FastAPI
import logging
from logging.handlers import RotatingFileHandler
import os

from .database.dbconnection import engine
from .database import models

from .routers import auth
from .routers import employees
from .routers import ai
from .routers import departments
from .analytics import analytics

os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("backups", exist_ok=True)

logger = logging.getLogger()

logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=5 * 1024 * 1024,
    backupCount=5
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)
logging.info("Application Starting...")

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HR Management System",
    description="Production Proof of Concept",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(departments.router)
app.include_router(ai.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    logging.info("Root endpoint accessed")
    return {
        "message": "HR Management System API Running Successfully"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }