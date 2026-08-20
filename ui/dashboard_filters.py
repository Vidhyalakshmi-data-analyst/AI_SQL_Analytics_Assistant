"""
=================================================
File: dashboard_filters.py

Purpose:
Render interactive dashboard filters and create
a FilterContext from the user's selections.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from datetime import date
from typing import Optional

import streamlit as st

from dashboard.filters import FilterContext

def create_filter_context(
    selected_category: str,
    selected_state: str,
    selected_status: str,
    selected_dates
) -> FilterContext:
    """
    Convert UI selections into FilterContext.

    Responsibility:
        Convert raw UI selections into the dashboard
        filter model.
    """

     # --------------------------------------------------
    # Initialize dashboard filter state
    # --------------------------------------------------

    if "dashboard_filters_applied" not in st.session_state:

        st.session_state.dashboard_filters_applied = False

    if "dashboard_filter_context" not in st.session_state:

        st.session_state.dashboard_filter_context = None

    category = None

    if selected_category != "All Categories":

        category = selected_category

    state = None

    if selected_state != "All States":

        state = selected_state

    order_status = None

    if selected_status != "All Statuses":

        order_status = selected_status

    start_date = None
    end_date = None

    if selected_dates:

        if len(selected_dates) == 2:

            start_date = selected_dates[0]
            end_date = selected_dates[1]

        else:

            start_date = selected_dates[0]
            end_date = selected_dates[0]

    return FilterContext(
        start_date=start_date,
        end_date=end_date,
        category=category,
        state=state,
        order_status=order_status
    )



def render_dashboard_filters(
    filter_options: dict
) -> Optional[FilterContext]:
    """
    Render dashboard filter controls.

    Responsibility:
        Display filter controls and return the
        selected FilterContext.

    Parameters:
        filter_options:
            Available filter values retrieved from
            PostgreSQL.

    Returns:
        FilterContext when filters are applied.

        None when the user has not applied filters.
    """

    st.subheader("🎛️ Dashboard Filters")

    # --------------------------------------------------
    # Available options
    # --------------------------------------------------

    categories = filter_options.get(
        "categories",
        []
    )

    states = filter_options.get(
        "states",
        []
    )

    order_statuses = filter_options.get(
        "order_statuses",
        []
    )

    min_date = filter_options.get(
        "min_date"
    )

    max_date = filter_options.get(
        "max_date"
    )

    # --------------------------------------------------
    # Filter controls
    # --------------------------------------------------

    columns = st.columns(4)

    # --------------------------------------------------
    # Category
    # --------------------------------------------------

    with columns[0]:

        selected_category = st.selectbox(
            "Category",
            options=["All Categories"] + categories
        )

    # --------------------------------------------------
    # State
    # --------------------------------------------------

    with columns[1]:

        selected_state = st.selectbox(
            "State",
            options=["All States"] + states
        )

    # --------------------------------------------------
    # Order Status
    # --------------------------------------------------

    with columns[2]:

        selected_status = st.selectbox(
            "Order Status",
            options=["All Statuses"] + order_statuses
        )

    # --------------------------------------------------
    # Date Range
    # --------------------------------------------------

    with columns[3]:

        if (
            min_date is not None
            and max_date is not None
        ):

            selected_dates = st.date_input(
                "Order Date",
                value=(
                    min_date,
                    max_date
                ),
                min_value=min_date,
                max_value=max_date
            )

        else:

            selected_dates = None

    # --------------------------------------------------
    # Apply / Reset
    # --------------------------------------------------

    apply_column, reset_column = st.columns(2)

    with apply_column:

        apply_clicked = st.button(
            "🔍 Apply Filters",
            use_container_width=True
        )

    with reset_column:

        reset_clicked = st.button(
            "🔄 Reset Filters",
            use_container_width=True
        )

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    if reset_clicked:

        st.session_state.dashboard_filters_applied = False
        st.session_state.dashboard_filter_context = None

        st.rerun()

    # --------------------------------------------------
    # No Apply
    # --------------------------------------------------

    if not apply_clicked:

        if st.session_state.get(
            "dashboard_filters_applied",
            False):

            return st.session_state.get(
                "dashboard_filter_context"
            )

        return None

    # --------------------------------------------------
    # Create FilterContext
    # --------------------------------------------------

    filter_context = create_filter_context(
        selected_category,
        selected_state,
        selected_status,
        selected_dates
    )


    st.session_state.dashboard_filters_applied = True
    st.session_state.dashboard_filter_context = (
    filter_context
    )

    return filter_context