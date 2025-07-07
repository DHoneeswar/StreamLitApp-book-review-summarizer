import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"  # Prevent Streamlit + torch crash

import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import torch

# Patch torch.classes to prevent Streamlit crash during module inspection
try:
    torch.classes.__path__ = []
except Exception:
    pass

from book_utils import search_books
from summary_utils import generate_summary

st.set_page_config(page_title="BookSnap", page_icon="📘")
st.title("📘 BookSnap: AI Book Summary & Explorer")

# Book search input
query = st.text_input("🔍 Search for a book:")

if query:
    st.write("📥 Received query:", query)

    try:
        results = search_books(query)
    except Exception as e:
        st.error(f"❌ Book search failed: {e}")
        results = []

    if results:
        st.write(f"📚 Found {len(results)} book(s)")

        for index, book in enumerate(results):
            st.subheader(book["title"])
            st.write(f"**Author:** {book['author_name']}")
            st.image(book["cover_url"], width=100)

            # Show preview and add a summarization button
            st.write("📖 Description Preview:", book["description"][:500] + "...")
            if st.button(f"Summarize '{book['title']}'", key=f"summarize_{index}_{book['title']}"):
                with st.spinner("Summarizing..."):
                    try:
                        summary = generate_summary(book["description"])
                        st.markdown(f"📖 **Summary:** {summary}")
                    except Exception as e:
                        st.error(f"❌ Summary generation failed: {e}")
    else:
        st.warning("No books found. Try a different title or author.")
else:
    st.info("Enter a book title or author above to get started.")
