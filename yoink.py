import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

def get_first_google_result(query: str) -> dict:
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        raise ValueError("API key not found. Make sure SERPAPI_KEY is set in the .env file.")

    search = GoogleSearch({
        "q": query,
        "api_key": api_key,
        "engine": "google"
    })

    results = search.get_dict()
    organic = results["organic_results"]
    if not organic:
        return {"error": "No results found."}

    return organic[0]