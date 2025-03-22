import pandas as pd
from src.data_transform import transform_data

def test_transform_data():
    """Test data transformation function."""
    sample_raw_data = [
        {"id": "nm1234567", "fullName": "John Doe", "job": "actor", "characters": ["Character A", "Character B"]},
        {"id": "nm7654321", "fullName": "Jane Smith", "job": "actress", "characters": ["Character X"]},
    ]

    df = transform_data(sample_raw_data)

    assert isinstance(df, pd.DataFrame), "Output should be a DataFrame"
    assert not df.empty, "DataFrame should not be empty"
    assert "imdb_id" in df.columns, "DataFrame should have 'imdb_id' column"
    assert "characters" in df.columns, "DataFrame should have 'characters' column"
    assert df.loc[0, "characters"] == "Character A, Character B", "Characters should be formatted correctly"

