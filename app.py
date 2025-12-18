# app.py
import streamlit as st
from src.graph import app

st.set_page_config(page_title="Research Assistant", layout="wide")
st.title("Multi-Agent Research Assistant")

query = st.text_input("Enter research topic:", placeholder="e.g., transformer efficiency")

if st.button("Research", type="primary"):
    if not query:
        st.warning("Please enter a topic")
    else:
        with st.spinner("Researching..."):
            progress = st.empty()

            initial_state = {
                "query": query,
                "papers": [],
                "insights": [],
                "report": "",
                "errors": [],
                "iteration": 0
            }

            for event in app.stream(initial_state):
                node = list(event.keys())[0]
                progress.text(f"Running: {node}...")

            result = event[node]
            progress.empty()

        # Display results
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Papers Found")
            for p in result["papers"]:
                with st.expander(p["title"][:60] + "..."):
                    st.write(p["summary"])
                    st.link_button("View PDF", p.get("url", "#"))

        with col2:
            st.subheader("Research Report")
            st.markdown(result["report"])

        if result["errors"]:
            st.error(f"Errors: {result['errors']}")
