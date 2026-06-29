from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# mysql connection
# engine= create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")

# postgresql connection
engine= create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")

Session = sessionmaker(bind=engine)