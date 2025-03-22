import os
import polars as pl
import pandas as pd
import json

def load_raw_data(file_path: str) -> list:
    """Load raw JSON data from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return []

def transform_data(raw_data: list) -> pd.DataFrame:
    """Transform raw JSON data into a structured Pandas DataFrame."""
    if not raw_data:
        print("No data to transform")
        return pd.DataFrame()

    # Convert to Pandas DataFrame for easy processing
    df = pd.DataFrame(raw_data)

    # Select relevant columns (adjust based on actual data structure)
    df = df[["id", "fullName", "job", "characters"]]

    # Standardize column names
    df.columns = ["imdb_id", "name", "role", "characters"]

    # Convert 'characters' list to comma-separated string
    df["characters"] = df["characters"].apply(lambda x: ", ".join(x) if isinstance(x, list) else "")

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Ensure the 'data' directory exists
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    # Save cleaned data inside the 'data' directory
    output_file = os.path.join(data_dir, "cleaned_data.csv")
    df.to_csv(output_file, index=False)
    print(f"Data transformation complete. Saved to '{output_file}'")

    return df

if __name__ == "__main__":
    raw_data = load_raw_data("data/raw_data.json") 
    transformed_df = transform_data(raw_data)
    print(transformed_df.head()) 
