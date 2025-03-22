import pytest
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from src.db_loader import load_data_to_postgres

# Create a test database in memory
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the IMDbCast model (since you don't have a models.py)
class IMDbCast(Base):
    __tablename__ = "imdb_cast"
    imdb_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    characters = Column(String, nullable=False)

# Create the table in the test database
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    """Fixture to provide a test database session."""
    session = SessionLocal()
    yield session
    session.close()

def test_load_data_to_db(db_session: Session):
    """Test loading data into the database."""
    sample_data = [
        {"imdb_id": "nm1234567", "name": "John Doe", "role": "actor", "characters": "Character A, Character B"},
        {"imdb_id": "nm7654321", "name": "Jane Smith", "role": "actress", "characters": "Character X"},
    ]

    # Load sample data
    load_data_to_postgres(sample_data, db_session)

    # Query database to check if data was inserted
    results = db_session.query(IMDbCast).all()

    assert len(results) == 2, "Database should contain 2 records"
    assert results[0].name == "John Doe", "First record should be John Doe"
    assert results[1].characters == "Character X", "Second record should have correct character data"
