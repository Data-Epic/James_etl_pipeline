from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Load database credentials from environment variables
DB_NAME = os.getenv("DB_NAME", "etl_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create FastAPI app
app = FastAPI(title="IMDB Cast API", version="1.0")

# Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to the IMDB Cast API!"}

@app.get("/cast/")
def get_all_cast():
    """Retrieve all cast members from the database."""
    try:
        query = "SELECT * FROM imdb_cast;"
        df = pd.read_sql(query, con=engine)
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

@app.get("/cast/{imdb_id}")
def get_cast_by_id(imdb_id: str):
    """Retrieve cast details by IMDb ID."""
    try:
        query = f"SELECT * FROM imdb_cast WHERE imdb_id = '{imdb_id}';"
        df = pd.read_sql(query, con=engine)

        if df.empty:
            raise HTTPException(status_code=404, detail="Cast member not found")

        return df.to_dict(orient="records")[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
