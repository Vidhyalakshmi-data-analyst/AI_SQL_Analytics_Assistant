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

from ai.query_engine import answer_question
from ai.chart_generator import generate_chart

from ui.layout import (
    render_header,
    render_sql_section,
    render_results_section,
    render_chart_section,
    render_insight_section
)

from ui.sidebar import render_sidebar

from ui.components import (
    render_question_input,
    render_generate_button,
    render_success_message,
    render_dataframe,
    render_sql,
    render_result_summary,
    render_download_button,
    render_chart,
    render_insight_placeholder,
    render_error_message,
    render_warning_message
)


# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI SQL Analytics Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "query_result" not in st.session_state:
    st.session_state.query_result = None


# --------------------------------------------------
# Render Static UI
# --------------------------------------------------

render_sidebar()

render_header()

question = render_question_input()

generate_clicked = render_generate_button()


# --------------------------------------------------
# Handle User Request
# --------------------------------------------------

if generate_clicked:

    if not question.strip():

        render_warning_message(
            "Please enter a business question."
        )

    else:

        try:

            with st.spinner(
                "Generating SQL and retrieving data..."
            ):

                st.session_state.query_result = (
                    answer_question(question)
                )

        except Exception as e:

            st.session_state.query_result = None

            render_error_message(
                str(e)
            )

# --------------------------------------------------
# Render Query Result
# --------------------------------------------------

result = st.session_state.query_result

if result is not None:

    render_success_message()

    render_sql_section()

    render_sql(
        result.sql
    )

    st.divider()

    render_results_section()

    render_result_summary(
        result.dataframe
    )

    render_dataframe(
        result.dataframe
    )

    render_download_button(
        result.dataframe
    )

    st.divider()

    render_chart_section()

    figure = generate_chart(result.dataframe)

    render_chart(figure)
    
    st.divider()

    render_insight_section()

    render_insight_placeholder()