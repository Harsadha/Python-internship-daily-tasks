import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="mydb",
            user="postgres",
            password=os.getenv("DB_PASSWORD"),
            port=5432
        )
        return connection

    except Exception as e:
        print("Database connection failed:", e)
        return None