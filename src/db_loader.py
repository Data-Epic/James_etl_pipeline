import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Load environment variables
load_dotenv()

# Database connection settings
DB_NAME = os.getenv("DB_NAME", "etl_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# PostgreSQL Connection String
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DEFAULT_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"

# Create the database if it doesn't exist
def create_database():
    try:
        conn = psycopg2.connect(DEFAULT_DATABASE_URL)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE {DB_NAME};")
        cur.close()
        conn.close()
        print(f"Database '{DB_NAME}' created successfully.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database '{DB_NAME}' already exists.")
    except OperationalError as e:
        print(f"Error creating database: {e}")

# Create database engine
engine = create_engine(DATABASE_URL)

def load_data_to_postgres(csv_file: str, table_name: str):
    """Load cleaned data from CSV into PostgreSQL table."""
    try:
        # Read CSV
        df = pd.read_csv(csv_file)

        # Load to PostgreSQL
        df.to_sql(table_name, engine, if_exists="replace", index=False)

        print(f"Data successfully loaded into {table_name} table")
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    create_database()  # Ensure database exists before loading data

    csv_path = "data/cleaned_data.csv"
    table_name = "imdb_cast"

    load_data_to_postgres(csv_path, table_name)
