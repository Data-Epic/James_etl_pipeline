import json
from src.web_scraper import fetch_top_movies

def test_scrape_imdb_data():
    """Test that the scraper fetches data correctly."""
    data = fetch_top_movies()
    
    assert isinstance(data, list), "Scraped data should be a list"
    assert len(data) > 0, "Scraped data should not be empty"
    assert all("id" in item for item in data), "Each item should have an 'id'"
    assert all("fullName" in item for item in data), "Each item should have 'fullName'"
    
    # Optional: Save sample data for debugging
    with open("tests/scraper_sample.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

