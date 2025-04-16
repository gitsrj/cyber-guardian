# features/domain_age_checker.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("IPQS_API_KEY")

def domain_age_checker():
    st.header("⏳ Domain Age Checker")
    st.markdown("Check how old a domain is — new domains are often suspicious.")

    domain = st.text_input("🌐 Enter a domain to check:", key="domain_age_input")

    if st.button("Check Domain Age", key="domain_age_button"):
        if domain:
            with st.spinner("Checking domain age..."):
                try:
                    api_url = "https://ipqualityscore.com/api/json/url"
                    params = {
                        "key": API_KEY,
                        "url": domain,
                        "strictness": 0,
                        "fast": "true"
                    }
                    response = requests.get(api_url, params=params)
                    result = response.json()

                    age_info = result.get("domain_age", {}).get("human", "Unknown")
                    st.success(f"📅 Domain Age: {age_info}")

                    with st.expander("More Details"):
                        st.json(result)

                except Exception as e:
                    st.error(f"❌ Something went wrong: {e}")
        else:
            st.warning("Please enter a domain.")
