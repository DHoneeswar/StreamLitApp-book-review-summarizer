import requests
import streamlit as st
GOOGLE_API_KEY = st.secrets["api_key"]  # Ensure you have set this in your Streamlit secrets

def search_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={GOOGLE_API_KEY}"
    response = requests.get(url)
    data = response.json()

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
