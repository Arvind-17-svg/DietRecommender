import streamlit as st
import requests
import json

# Page setup
st.set_page_config(page_title="Diet Recommender", page_icon="🥗", layout="centered")
st.title("🥦 Diet & Nutrition Assistant")

# API endpoint
FAST_API_URL = "http://127.0.0.1:8000"

# User input box
query = st.chat_input("Ask a question about diet, nutrients, or food recommendations...")

if query:
    with st.chat_message("user"):
        st.markdown(f"**You:** {query}")

    with st.spinner("🤖 Thinking..."):
        try:
            response = requests.post(
                f"{FAST_API_URL}/query",
                headers={"Content-Type": "application/json"},
                data=json.dumps({"query": query}),
            )
            response.raise_for_status()
            result = response.json()

            # Show AI response
            with st.chat_message("assistant"):
                st.markdown(f"**Answer:**\n\n{result['answer']}")

                # Show metadata (sources)
                if "sources" in result and result["sources"]:
                    with st.expander("📄 Source Metadata"):
                        for i, meta in enumerate(result["sources"], 1):
                            st.markdown(f"**Source {i}:** `{json.dumps(meta, indent=2)}`")

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Error communicating with backend: {e}")
