import requests
import streamlit as st
GOOGLE_API_KEY = st.secrets["api_key"]  # Ensure you have set this in your Streamlit secrets

def search_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={GOOGLE_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
    except Exception as e:
        st.error(f"❌ Google Books API request failed: {e}")
        return []

    results = []
    for item in data.get("items", [])[:5]:
        volume = item["volumeInfo"]
        results.append({
            "title": volume.get("title", "No Title"),
            "author_name": ", ".join(volume.get("authors", ["Unknown Author"])),
            "cover_url": volume.get("imageLinks", {}).get("thumbnail", ""),
            "description": volume.get("description", "No description available.")
        })
    return results
