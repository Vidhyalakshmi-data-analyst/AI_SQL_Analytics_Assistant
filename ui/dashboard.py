"""
=================================================
File: dashboard.py

Purpose:
Render the interactive dashboard area.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd
import streamlit as st

from dashboard.filter_options import (
    get_filter_options
)

from dashboard.controller import (
    load_dashboard_data
)

from dashboard.filters import (
    FilterContext
)

from ui.dashboard_filters import (
    render_dashboard_filters
)

from dashboard.kpi_service import (
    calculate_dashboard_kpis
)

from ui.components import (
    render_dashboard_kpi_cards
)

from dashboard.chart_service import (
    create_sales_trend_chart,
    create_sales_category_chart,
    create_sales_state_chart,
    create_order_status_chart,
    create_top_products_chart,
    create_top_customers_chart
)

from ui.components import (
    render_dashboard_chart
)

from services.export_service import dashboard_to_excel

def render_dashboard() -> pd.DataFrame | None:
    """
    Render the interactive dashboard.

    Responsibility:
        Coordinate dashboard filter UI and
        dashboard data loading.

    Returns:
        Filtered dashboard DataFrame or None.
    """

    st.divider()

    st.header("📊 Business Dashboard")

    # --------------------------------------------------
    # Load filter options
    # --------------------------------------------------

    filter_options = get_filter_options()

    # --------------------------------------------------
    # Render filters
    # --------------------------------------------------

    filter_context = render_dashboard_filters(
        filter_options
    )

    # --------------------------------------------------
    # No filters applied
    # --------------------------------------------------

    if filter_context is None:

        st.info(
            "Select your dashboard filters and "
            "click 'Apply Filters' to load the dashboard."
        )

        return None

    # --------------------------------------------------
    # Load dashboard data
    # --------------------------------------------------

    dataframe = load_dashboard_data(
        filter_context
    )

    # --------------------------------------------------
    # Handle empty result
    # --------------------------------------------------

    if dataframe.empty:

        st.warning(
            "No data is available for the selected filters."
        )

        return dataframe
    
    # --------------------------------------------------
    # Calculate dashboard KPIs
    # --------------------------------------------------

    kpi_result = calculate_dashboard_kpis(
        dataframe
    )

    # --------------------------------------------------
    # Render dashboard KPI cards
    # --------------------------------------------------

    st.subheader("📊 Dashboard KPIs")


    render_dashboard_kpi_cards(
        kpi_result
    )

    st.divider()

    # --------------------------------------------------
    # Dashboard Visualizations
    # --------------------------------------------------

    st.subheader(
        "📈 Dashboard Visualizations"
    )

    # --------------------------------------------------
    # Sales Trend
    # --------------------------------------------------

    

    st.subheader(
        "📈 Sales Trend"
    )

    sales_trend = create_sales_trend_chart(
        dataframe
    )

    render_dashboard_chart(
        sales_trend
    )

    st.divider()


    # --------------------------------------------------
    # Sales by Category + Sales by State
    # --------------------------------------------------

    category_column, state_column = st.columns(
        2, gap="medium")

    # --------------------------------------------------
    # Sales by Category
    # --------------------------------------------------

    with category_column:

        st.subheader(
            "📊 Sales by Category"
        )

        sales_category = create_sales_category_chart(
            dataframe
        )

        render_dashboard_chart(
            sales_category
        )


    # --------------------------------------------------
    # Sales by State
    # --------------------------------------------------

    with state_column:

        st.subheader(
            "🌎 Sales by State"
        )

        sales_state = create_sales_state_chart(
            dataframe
        )

        render_dashboard_chart(
            sales_state
        )

    st.divider()

    # --------------------------------------------------
    # Order Status + Top Products
    # --------------------------------------------------

    status_column, product_column = st.columns(
        2, gap="medium")

    # --------------------------------------------------
    # Order Status
    # --------------------------------------------------

    with status_column:

        st.subheader(
            "📦 Order Status"
        )

        order_status = create_order_status_chart(
            dataframe
        )

        render_dashboard_chart(
            order_status
        )


    # --------------------------------------------------
    # Top Products
    # --------------------------------------------------

    with product_column:

        st.subheader(
            "🏆 Top Products by Sales"
        )

        top_products = create_top_products_chart(
            dataframe
        )

        render_dashboard_chart(
            top_products
        )


    # --------------------------------------------------
    # Top Customers by Sales
    # --------------------------------------------------

    st.divider()

    st.subheader(
        "👥 Top Customers by Sales"
    )

    top_customers = create_top_customers_chart(
        dataframe
    )

    render_dashboard_chart(
        top_customers
    )


    # --------------------------------------------------
    # Display basic dashboard information
    # --------------------------------------------------

    st.caption(
        f"{len(dataframe):,} records available "
        "for the selected filters."
    )

    

    # --------------------------------------------------
    # Dashboard Export
    # --------------------------------------------------

    st.divider()

    st.subheader(
        "📥 Export Dashboard Data"
    )

    st.caption(
        "Download the currently filtered dashboard data "
        "and analysis as an Excel workbook."
    )

    excel_data = dashboard_to_excel(
        dataframe
    )

    st.download_button(
        label="📊 Download Dashboard Excel",
        data=excel_data,
        file_name="business_dashboard.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
    ),
        use_container_width=True
    )

    # --------------------------------------------------
    # Return filtered dashboard data
    # --------------------------------------------------

    return dataframe