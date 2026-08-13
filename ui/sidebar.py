"""
=================================================
File: sidebar.py

Purpose:
Render the application sidebar.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.header("⚙️ Application")

        st.markdown("---")

        st.subheader("Project")

        st.write("AI SQL Analytics Assistant")

        st.caption("Portfolio Project · Developed by Vidhyalakshmi A")

        st.subheader("AI Model")

        st.write("Gemini 3.5 Flash")

        st.subheader("Database")

        st.write("PostgreSQL 17")

        st.subheader("Status")

        st.success("Backend Ready ✅")

        st.markdown("---")

        st.caption("Version 0.5.0")
        