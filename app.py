import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from book_utils import search_books
from summary_utils import generate_summary

st.title("📘 BookSnap: AI Book Summary & Explorer")
query = st.text_input("Search for a book:")

if query:
    results = search_books(query)

    for index, book in enumerate(results):
        st.subheader(book["title"])
        st.write(f"**Author:** {book['author_name']}")
        st.image(book["cover_url"], width=100)
        st.write("📖 Description Preview:", book["description"])
        if st.button(f"Summarize '{book['title']}'", key=f"summarize_{index}_{book['title']}"):
            summary = generate_summary(book["description"])
            st.markdown(f"📖 **Summary:** {summary}")