# features/safe_search_suggestions.py

import streamlit as st

def safe_search_suggestions():
    st.header("🔐 Safe Search Suggestions")
    st.markdown("Here are some privacy-respecting and secure search engines:")

    suggestions = [
        {
            "name": "DuckDuckGo",
            "url": "https://duckduckgo.com/",
            "desc": "A privacy-first search engine that doesn't track your searches or profile you."
        },
        {
            "name": "Startpage",
            "url": "https://www.startpage.com/",
            "desc": "Delivers Google results with complete anonymity. No tracking, no profiling."
        },
        {
            "name": "Swisscows",
            "url": "https://swisscows.com/",
            "desc": "A secure, family-friendly search engine with servers in Switzerland."
        },
        {
            "name": "Brave Search",
            "url": "https://search.brave.com/",
            "desc": "Independent search engine by Brave, with a focus on privacy and speed."
        }
    ]

    for engine in suggestions:
        st.markdown(f"### 🔎 [{engine['name']}]({engine['url']})")
        st.write(engine['desc'])
        st.markdown("---")
