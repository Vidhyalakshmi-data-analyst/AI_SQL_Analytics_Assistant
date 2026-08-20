"""
=================================================
File: kpi_service.py

Purpose:
Calculate dashboard-level business KPIs from
the filtered dashboard DataFrame.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd


def calculate_dashboard_kpis(
    dataframe: pd.DataFrame
) -> dict:
    """
    Calculate business KPIs for the dashboard.

    Responsibility:
        Calculate deterministic KPIs from the
        dashboard DataFrame.

    This function does not:
        - Query the database
        - Render UI
        - Generate charts
        - Use Gemini

    Returns:
        Dictionary containing dashboard KPIs.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return {
            "status": "no_data",
            "message": (
                "No data is available for "
                "dashboard KPI calculation."
            ),
            "kpis": {}
        }

    # --------------------------------------------------
    # Step 2: Validate required columns
    # --------------------------------------------------

    required_columns = {
        "order_id",
        "customer_id",
        "quantity",
        "line_total"
    }

    missing_columns = (
        required_columns
        - set(dataframe.columns)
    )

    if missing_columns:

        return {
            "status": "missing_columns",
            "message": (
                "Required dashboard columns are missing."
            ),
            "missing_columns": list(
                missing_columns
            ),
            "kpis": {}
        }

    # --------------------------------------------------
    # Step 3: Convert numeric columns
    # --------------------------------------------------

    quantity = pd.to_numeric(
        dataframe["quantity"],
        errors="coerce"
    )

    line_total = pd.to_numeric(
        dataframe["line_total"],
        errors="coerce"
    )

    # --------------------------------------------------
    # Step 4: Validate numeric values
    # --------------------------------------------------

    if line_total.dropna().empty:

        return {
            "status": "no_numeric_data",
            "message": (
                "Line total does not contain "
                "usable numeric values."
            ),
            "kpis": {}
        }

    # --------------------------------------------------
    # Step 5: Calculate core KPIs
    # --------------------------------------------------

    total_sales = float(
        line_total.sum()
    )

    total_orders = int(
        dataframe["order_id"].nunique()
    )

    total_customers = int(
        dataframe["customer_id"].nunique()
    )

    units_sold = int(
        quantity.sum()
    )

    # --------------------------------------------------
    # Step 6: Average Order Value
    # --------------------------------------------------

    if total_orders > 0:

        average_order_value = (
            total_sales
            / total_orders
        )

    else:

        average_order_value = 0.0

    # --------------------------------------------------
    # Step 7: Return KPI result
    # --------------------------------------------------

    return {
        "status": "success",

        "message": (
            "Dashboard KPIs calculated successfully."
        ),

        "kpis": {

            "total_sales": total_sales,

            "total_orders": total_orders,

            "total_customers": total_customers,

            "units_sold": units_sold,

            "average_order_value": (
                average_order_value
            )
        }
    }