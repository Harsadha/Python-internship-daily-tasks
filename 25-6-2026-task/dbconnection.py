import mysql.connector
import os
from dotenv import load_dotenv
from logging_config import logging

load_dotenv()
logging.info("Loading DB Password from the .env file")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password = DB_PASSWORD,
        database="mydb"
    )
    return db