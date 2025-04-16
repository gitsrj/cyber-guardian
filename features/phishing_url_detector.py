# features/phishing_url_detector.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("IPQS_API_KEY")

def phishing_url_detector():
    st.header("🛡️ Phishing URL Detector")
    st.markdown("Check if a URL is safe or potentially malicious using real-time scanning.")

    user_url = st.text_input("🔗 Enter a URL to scan:", key="phishing_url")

    if st.button("Scan URL", key="scan_button"):
        if user_url:
            with st.spinner("Scanning..."):
                try:
                    api_url = "https://ipqualityscore.com/api/json/url"
                    params = {
                        "key": API_KEY,
                        "url": user_url,
                        "strictness": 1,
                        "fast": "true"
                    }
                    response = requests.get(api_url, params=params)
                    result = response.json()

                    st.subheader("🔍 Scan Result")
                    risk_score = result.get("risk_score", 0)

                    if result.get("unsafe") or risk_score >= 75:
                        st.error("⚠️ This URL is considered *malicious*.")
                    else:
                        st.success("✅ This URL is *safe* to visit.")

                    with st.expander("More Details"):
                        st.json(result)

                except Exception as e:
                    st.error(f"❌ Something went wrong: {e}")
        else:
            st.warning("Please enter a URL.")
