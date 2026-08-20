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
from ai.insight_engine import (generate_insight)
from ai.chart_generator import generate_chart
from ai.kpi_generator import generate_kpis

from ui.layout import (
    render_header,
    render_sql_section,
    render_results_section,
    render_chart_section,
    render_insight_section
)

from ui.sidebar import render_sidebar

from ui.dashboard import render_dashboard

from ui.components import (
    render_question_input,
    render_generate_button,
    render_success_message,
    render_dataframe,
    render_sql,
    render_result_summary,
    render_download_button,
    render_chart,
    render_insight,
    render_error_message,
    render_warning_message,
    render_footer,
    render_kpi_cards
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

if "insight" not in st.session_state:
    st.session_state.insight = None

if "question" not in st.session_state:
    st.session_state.question = ""

# --------------------------------------------------
# Render Static UI
# --------------------------------------------------

render_sidebar()

render_header()

# --------------------------------------------------
# AI-Powered Query Analysis
# --------------------------------------------------

st.subheader("🤖 AI-Powered Query Analysis")


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

                # Store the question
                st.session_state.question = question

                # Generate SQL and execute query
                st.session_state.query_result = (
                    answer_question(question)
                )

            # --------------------------------------------------
            # Generate AI Insight ONLY ONCE
            # --------------------------------------------------

            with st.spinner(
                "Generating business insight..."
            ):

                st.session_state.insight = (
                    generate_insight(
                        st.session_state.query_result.dataframe,
                        question
                    )
                )

        except Exception as e:

            st.session_state.query_result = None

            st.session_state.insight = None

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

    render_sql(result.sql)

    st.download_button(
    label="⬇️ Download SQL",
    data=result.sql,
    file_name="generated_query.sql",
    mime="text/plain"
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

    # --------------------------------------------------
    # Render KPI Cards
    # --------------------------------------------------

    kpi_result = generate_kpis(result.dataframe)

    render_kpi_cards(kpi_result)

    st.divider()

    render_chart_section()

    figure = generate_chart(result.dataframe)

    render_chart(figure)
    
    st.divider()

    render_insight_section()

    render_insight(st.session_state.insight)

    st.divider()

    # --------------------------------------------------
    # Interactive Business Dashboard
    # --------------------------------------------------

    render_dashboard()

    render_footer()
    