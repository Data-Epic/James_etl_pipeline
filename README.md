ETL Pipeline with FastAPI, Polars, and PostgreSQL

    Project Overview
This project is an API-based ETL pipeline that fetches movie cast data from the IMDb API via RapidAPI, transforms it, and loads it into a PostgreSQL database. The API is built using FastAPI and follows best practices for data extraction, transformation, and loading (ETL).

    Features
 Extract movie cast data from the IMDb API
Transform raw JSON data into a structured format using Pandas/Polars
 Load transformed data into a PostgreSQL database
 Expose API endpoints for querying movie cast details
 Unit & Integration Tests using pytest
Code Formatting & Type Hints for maintainability


Project Structure

etl_pipeline/
│── src/
│   ├── web_scraper.py        # Extract data from IMDb API
│   ├── data_transform.py     # Transform JSON data
│   ├── db_loader.py          # Load data into PostgreSQL
│   ├── api.py                # FastAPI endpoints
│── tests/
│   ├── test_scraper.py       # Tests for web scraper
│   ├── test_transform.py     # Tests for data transformation
│   ├── test_db_loader.py     # Tests for database operations
│── .env                      # Environment variables
│── pyproject.toml            # Dependencies (Poetry)
│── README.md                 # Project documentation

