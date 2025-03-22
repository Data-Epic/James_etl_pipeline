import os
import requests
import json
from dotenv import load_dotenv
from typing import Dict, Any

# Load API key from .env file
load_dotenv()
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# Correct API base URL
BASE_URL = "https://imdb236.p.rapidapi.com/imdb/tt7631058/cast"  

# Print API key for debugging
print("API Key Loaded:", bool(RAPIDAPI_KEY))  # Only prints True/False for security

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "imdb236.p.rapidapi.com",  # Ensure the host is correct
}

def fetch_top_movies() -> Dict[str, Any]:
    """Fetch top-rated movies from IMDB via RapidAPI."""
    url = f"{BASE_URL}"  # Use the correct endpoint
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an error for HTTP issues
        
        print("Status Code:", response.status_code)  # Debugging
        print("Response Headers:", response.headers)  # Debugging
        print("Raw Response:", response.text[:500])  # Print part of the response

        # Try parsing JSON
        data = response.json()

        # Save raw data
        os.makedirs("data", exist_ok=True)  # Ensure directory exists
        with open("data/raw_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return data
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

if __name__ == "__main__":
    movies = fetch_top_movies()
    print(json.dumps(movies, indent=2))
