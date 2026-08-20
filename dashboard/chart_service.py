"""
=================================================
File: chart_service.py

Purpose:
Generate dashboard-specific Plotly visualizations.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd
import plotly.express as px

def format_chart_currency(value: float) -> str:
    """
    Format sales values for dashboard chart labels.
    """

    value = float(value)

    if abs(value) >= 10_000_000:
        return f"₹{value / 10_000_000:.2f} Cr"

    if abs(value) >= 100_000:
        return f"₹{value / 100_000:.2f} L"

    if abs(value) >= 1_000:
        return f"₹{value / 1_000:.2f} K"

    return f"₹{value:,.2f}"


def create_sales_trend_chart(
    dataframe: pd.DataFrame
):
    """
    Create a sales trend chart.

    Responsibility:
        Aggregate sales by order date and create
        a Plotly line chart.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate AI insights

    Returns:
        Plotly Figure or None.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return None

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "order_date",
        "line_total"
    }

    if not required_columns.issubset(
        dataframe.columns
    ):

        return None

    # --------------------------------------------------
    # Step 3: Create working DataFrame
    # --------------------------------------------------

    trend_data = dataframe[
        [
            "order_date",
            "line_total"
        ]
    ].copy()

    # --------------------------------------------------
    # Step 4: Convert values
    # --------------------------------------------------

    trend_data["order_date"] = pd.to_datetime(
        trend_data["order_date"],
        errors="coerce"
    )

    trend_data["line_total"] = pd.to_numeric(
        trend_data["line_total"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Step 5: Remove invalid records
    # --------------------------------------------------

    trend_data = trend_data.dropna(
        subset=[
            "order_date",
            "line_total"
        ]
    )

    if trend_data.empty:

        return None

    # --------------------------------------------------
    # Step 6: Aggregate daily sales
    # --------------------------------------------------

    trend_data = (
        trend_data
        .groupby("order_date", as_index=False)
        ["line_total"]
        .sum()
    )

    # --------------------------------------------------
    # Step 7: Sort chronologically
    # --------------------------------------------------

    trend_data = trend_data.sort_values(
        "order_date"
    )

    # --------------------------------------------------
    # Step 8: Generate Plotly chart
    # --------------------------------------------------

    figure = px.line(
        trend_data,
        x="order_date",
        y="line_total",
        markers=True,
        title="Sales Trend"
    )

    # --------------------------------------------------
    # Step 9: Configure chart
    # --------------------------------------------------

    figure.update_layout(
        xaxis_title="Order Date",
        yaxis_title="Sales",
        hovermode="x unified"
    )

    return figure


def create_sales_category_chart(
    dataframe: pd.DataFrame
):
    """
    Create a sales by category chart.

    Responsibility:
        Aggregate sales by category and create
        a Plotly bar chart.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate AI insights

    Returns:
        Plotly Figure or None.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return None

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "category",
        "line_total"
    }

    if not required_columns.issubset(
        dataframe.columns
    ):

        return None

    # --------------------------------------------------
    # Step 3: Create working DataFrame
    # --------------------------------------------------

    category_data = dataframe[
        [
            "category",
            "line_total"
        ]
    ].copy()

    # --------------------------------------------------
    # Step 4: Convert sales values
    # --------------------------------------------------

    category_data["line_total"] = pd.to_numeric(
        category_data["line_total"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Step 5: Remove invalid records
    # --------------------------------------------------

    category_data = category_data.dropna(
        subset=[
            "category",
            "line_total"
        ]
    )

    if category_data.empty:

        return None

    # --------------------------------------------------
    # Step 6: Aggregate sales by category
    # --------------------------------------------------

    category_data = (
        category_data
        .groupby("category", as_index=False)
        ["line_total"]
        .sum()
    )

    # --------------------------------------------------
    # Step 7: Sort by sales
    # --------------------------------------------------

    category_data = category_data.sort_values(
        "line_total",
        ascending=False
    )

    # --------------------------------------------------
    # Step 8: Generate Plotly chart
    # --------------------------------------------------

    figure = px.bar(
        category_data,
        x="category",
        y="line_total",
        title="Sales by Category",
        text=category_data["line_total"].apply(format_chart_currency)
    )

    # --------------------------------------------------
    # Step 9: Configure chart
    # --------------------------------------------------

    figure.update_traces(
        textposition="outside",
        hovertemplate=(
        "<b>%{x}</b><br>"
        "Sales: ₹%{y:,.2f}"
        "<extra></extra>"
        )
    )

    figure.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales",
        hovermode="x unified",
        uniformtext_minsize=10,
        uniformtext_mode="hide"
    )
    
    return figure


def create_sales_state_chart(
    dataframe: pd.DataFrame):
    """
    Create a sales by state chart.

    Responsibility:
        Aggregate sales by state and create
        a Plotly bar chart.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate AI insights

    Returns:
        Plotly Figure or None.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return None

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "state",
        "line_total"
    }

    if not required_columns.issubset(
        dataframe.columns
    ):

        return None

    # --------------------------------------------------
    # Step 3: Create working DataFrame
    # --------------------------------------------------

    state_data = dataframe[
        [
            "state",
            "line_total"
        ]
    ].copy()

    # --------------------------------------------------
    # Step 4: Convert sales to numeric
    # --------------------------------------------------

    state_data["line_total"] = pd.to_numeric(
        state_data["line_total"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Step 5: Remove invalid records
    # --------------------------------------------------

    state_data = state_data.dropna(
        subset=[
            "state",
            "line_total"
        ]
    )

    if state_data.empty:

        return None

    # --------------------------------------------------
    # Step 6: Aggregate sales by state
    # --------------------------------------------------

    state_data = (
        state_data
        .groupby("state", as_index=False)
        ["line_total"]
        .sum()
    )

    # --------------------------------------------------
    # Step 7: Sort descending
    # --------------------------------------------------

    state_data = state_data.sort_values(
        "line_total",
        ascending=False
    )

    # --------------------------------------------------
    # Step 8: Generate chart
    # --------------------------------------------------

    figure = px.bar(
        state_data,
        x="state",
        y="line_total",
        title="Sales by State",
        text_auto=".2s"
    )

    # --------------------------------------------------
    # Step 9: Configure chart
    # --------------------------------------------------

    figure.update_traces(
        texttemplate="%{text}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Sales: ₹%{y:,.2f}"
            "<extra></extra>"
        )
    )

    figure.update_layout(
        xaxis_title="State",
        yaxis_title="Sales",
        hovermode="x unified"
    )

    return figure

def create_order_status_chart(
    dataframe: pd.DataFrame
):
    """
    Create an order status distribution chart.

    Responsibility:
        Count orders by status and create
        a Plotly bar chart.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate AI insights

    Returns:
        Plotly Figure or None.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return None

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "order_status"
    }

    if not required_columns.issubset(
        dataframe.columns
    ):

        return None

    # --------------------------------------------------
    # Step 3: Create working DataFrame
    # --------------------------------------------------

    status_data = dataframe[
        ["order_status"]
    ].copy()

    # --------------------------------------------------
    # Step 4: Remove missing status values
    # --------------------------------------------------

    status_data = status_data.dropna(
        subset=["order_status"]
    )

    if status_data.empty:

        return None

    # --------------------------------------------------
    # Step 5: Count orders by status
    # --------------------------------------------------

    status_data = (
        status_data
        .groupby(
            "order_status",
            as_index=False
        )
        .size()
    )

    # --------------------------------------------------
    # Step 6: Rename count column
    # --------------------------------------------------

    status_data = status_data.rename(
        columns={
            "size": "order_count"
        }
    )

    # --------------------------------------------------
    # Step 7: Sort descending
    # --------------------------------------------------

    status_data = status_data.sort_values(
        "order_count",
        ascending=False
    )

    # --------------------------------------------------
    # Step 8: Generate chart
    # --------------------------------------------------

    figure = px.bar(
        status_data,
        x="order_status",
        y="order_count",
        title="Order Status Distribution",
        text="order_count"
    )

    # --------------------------------------------------
    # Step 9: Configure chart
    # --------------------------------------------------

    figure.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Orders: %{y:,}"
            "<extra></extra>"
        )
    )

    figure.update_layout(
        xaxis_title="Order Status",
        yaxis_title="Number of Orders",
        hovermode="x unified"
    )

    return figure

def create_top_products_chart(
    dataframe: pd.DataFrame,
    top_n: int = 10
):
    """
    Create a Top Products by Sales chart.

    Responsibility:
        Aggregate sales by product and display
        the top N products.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate AI insights

    Parameters:
        dataframe:
            Dashboard DataFrame.

        top_n:
            Number of top products to display.

    Returns:
        Plotly Figure or None.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return None

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "product_name",
        "line_total"
    }

    if not required_columns.issubset(
        dataframe.columns
    ):

        return None

    # --------------------------------------------------
    # Step 3: Create working DataFrame
    # --------------------------------------------------

    product_data = dataframe[
        [
            "product_name",
            "line_total"
        ]
    ].copy()

    # --------------------------------------------------
    # Step 4: Convert sales to numeric
    # --------------------------------------------------

    product_data["line_total"] = pd.to_numeric(
        product_data["line_total"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Step 5: Remove invalid records
    # --------------------------------------------------

    product_data = product_data.dropna(
        subset=[
            "product_name",
            "line_total"
        ]
    )

    if product_data.empty:

        return None

    # --------------------------------------------------
    # Step 6: Aggregate sales by product
    # --------------------------------------------------

    product_data = (
        product_data
        .groupby(
            "product_name",
            as_index=False
        )["line_total"]
        .sum()
    )

    # --------------------------------------------------
    # Step 7: Sort by sales
    # --------------------------------------------------

    product_data = product_data.sort_values(
        "line_total",
        ascending=False
    )

    # --------------------------------------------------
    # Step 8: Select Top N
    # --------------------------------------------------

    product_data = product_data.head(
        top_n
    )

    if product_data.empty:

        return None

    # --------------------------------------------------
    # Step 9: Generate chart
    # --------------------------------------------------

    figure = px.bar(
        product_data,
        x="line_total",
        y="product_name",
        orientation="h",
        title=f"Top {top_n} Products by Sales",
        text=product_data["line_total"].apply(
            format_chart_currency
        )
    )

    # --------------------------------------------------
    # Step 10: Configure chart
    # --------------------------------------------------

    figure.update_traces(
        textposition="outside",
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Sales: ₹%{x:,.2f}"
            "<extra></extra>"
        )
    )

    figure.update_layout(
        xaxis_title="Sales",
        yaxis_title="Product",
        hovermode="y unified"
    )

    return figure

def create_top_customers_chart(
    dataframe: pd.DataFrame,
    top_n: int = 10
):
    """
    Create a Top Customers by Sales chart.

    Responsibility:
        Aggregate sales by customer and create
        a Plotly bar chart for the top customers.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate AI insights

    Parameters:
        dataframe:
            Dashboard DataFrame.

        top_n:
            Number of top customers to display.

    Returns:
        Plotly Figure or None.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return None

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "customer_name",
        "line_total"
    }

    if not required_columns.issubset(
        dataframe.columns
    ):

        return None

    # --------------------------------------------------
    # Step 3: Validate top_n
    # --------------------------------------------------

    if top_n <= 0:

        return None

    # --------------------------------------------------
    # Step 4: Create working DataFrame
    # --------------------------------------------------

    customer_data = dataframe[
        [
            "customer_name",
            "line_total"
        ]
    ].copy()

    # --------------------------------------------------
    # Step 5: Convert sales to numeric
    # --------------------------------------------------

    customer_data["line_total"] = pd.to_numeric(
        customer_data["line_total"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Step 6: Remove invalid records
    # --------------------------------------------------

    customer_data = customer_data.dropna(
        subset=[
            "customer_name",
            "line_total"
        ]
    )

    if customer_data.empty:

        return None

    # --------------------------------------------------
    # Step 7: Aggregate sales by customer
    # --------------------------------------------------

    customer_data = (
        customer_data
        .groupby(
            "customer_name",
            as_index=False
        )["line_total"]
        .sum()
    )

    # --------------------------------------------------
    # Step 8: Sort by sales
    # --------------------------------------------------

    customer_data = customer_data.sort_values(
        "line_total",
        ascending=False
    )

    # --------------------------------------------------
    # Step 9: Select top customers
    # --------------------------------------------------

    customer_data = customer_data.head(
        top_n
    )

    if customer_data.empty:

        return None

    # --------------------------------------------------
    # Step 10: Generate Plotly chart
    # --------------------------------------------------

    figure = px.bar(
        customer_data,
        x="customer_name",
        y="line_total",
        title=f"Top {top_n} Customers by Sales",
        text="line_total"
    )

    # --------------------------------------------------
    # Step 11: Configure chart
    # --------------------------------------------------

    figure.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Sales: ₹%{y:,.2f}"
            "<extra></extra>"
        )
    )

    figure.update_layout(
        xaxis_title="Customer",
        yaxis_title="Sales",
        hovermode="x unified"
    )

    return figure