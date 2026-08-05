"""
=================================================
File: main.py

Purpose:
Entry point for the AI SQL Analytics Assistant
Streamlit application.

Author: Vidhyalakshmi
=================================================
"""

import streamlit as st

st.set_page_config(
    page_title="AI SQL Analytics Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 AI SQL Analytics Assistant")

st.markdown(
    """
Ask business questions in plain English and receive
AI-generated SQL, query results, visualizations,
and business insights.
"""
)

