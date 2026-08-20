"""
=================================================
File: export_service.py

Purpose:
Generate downloadable files for query results
and dashboard exports.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from io import BytesIO

import pandas as pd


def dataframe_to_excel(
    dataframe: pd.DataFrame,
    sheet_name: str = "Query Results"
) -> bytes:
    """
    Convert a DataFrame into an Excel workbook.

    Responsibility:
        Generate Excel output from a DataFrame.

    This function does not:
        - Query PostgreSQL
        - Render Streamlit UI
        - Apply filters
        - Generate AI insights
    """

    if dataframe is None or dataframe.empty:

        return b""

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        dataframe.to_excel(
            writer,
            index=False,
            sheet_name=sheet_name
        )

    output.seek(0)

    return output.getvalue()



def dashboard_to_excel(
    dataframe: pd.DataFrame
) -> bytes:
    """
    Generate an Excel workbook for the
    filtered business dashboard.

    Responsibility:
        Create a multi-sheet Excel report
        from the filtered dashboard data.

    This function does not:
        - Query PostgreSQL
        - Apply dashboard filters
        - Render Streamlit UI
        - Generate charts
        - Generate AI insights
    """

    if dataframe is None or dataframe.empty:

        return b""

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        # ------------------------------------------
        # Filtered Dashboard Data
        # ------------------------------------------

        dataframe.to_excel(
            writer,
            index=False,
            sheet_name="Filtered Data"
        )

        # ------------------------------------------
        # Sales by Category
        # ------------------------------------------

        if {
            "category",
            "line_total"
        }.issubset(dataframe.columns):

            category_data = (
                dataframe
                .assign(
                    line_total=pd.to_numeric(
                        dataframe["line_total"],
                        errors="coerce"
                    )
                )
                .groupby(
                    "category",
                    as_index=False
                )["line_total"]
                .sum()
                .sort_values(
                    "line_total",
                    ascending=False
                )
            )

            category_data.to_excel(
                writer,
                index=False,
                sheet_name="Sales by Category"
            )

        # ------------------------------------------
        # Sales by State
        # ------------------------------------------

        if {
            "state",
            "line_total"
        }.issubset(dataframe.columns):

            state_data = (
                dataframe
                .assign(
                    line_total=pd.to_numeric(
                        dataframe["line_total"],
                        errors="coerce"
                    )
                )
                .groupby(
                    "state",
                    as_index=False
                )["line_total"]
                .sum()
                .sort_values(
                    "line_total",
                    ascending=False
                )
            )

            state_data.to_excel(
                writer,
                index=False,
                sheet_name="Sales by State"
            )

        # ------------------------------------------
        # Order Status
        # ------------------------------------------

        if "order_status" in dataframe.columns:

            status_data = (
                dataframe
                .groupby(
                    "order_status"
                )
                .size()
                .reset_index(
                    name="order_count"
                )
                .sort_values(
                    "order_count",
                    ascending=False
                )
            )

            status_data.to_excel(
                writer,
                index=False,
                sheet_name="Order Status"
            )

        # ------------------------------------------
        # Top Products
        # ------------------------------------------

        if {
            "product_name",
            "line_total"
        }.issubset(dataframe.columns):

            product_data = (
                dataframe
                .assign(
                    line_total=pd.to_numeric(
                        dataframe["line_total"],
                        errors="coerce"
                    )
                )
                .groupby(
                    "product_name",
                    as_index=False
                )["line_total"]
                .sum()
                .sort_values(
                    "line_total",
                    ascending=False
                )
                .head(10)
            )

            product_data.to_excel(
                writer,
                index=False,
                sheet_name="Top Products"
            )

        # ------------------------------------------
        # Top Customers
        # ------------------------------------------

        if {
            "customer_name",
            "line_total"
        }.issubset(dataframe.columns):

            customer_data = (
                dataframe
                .assign(
                    line_total=pd.to_numeric(
                        dataframe["line_total"],
                        errors="coerce"
                    )
                )
                .groupby(
                    "customer_name",
                    as_index=False
                )["line_total"]
                .sum()
                .sort_values(
                    "line_total",
                    ascending=False
                )
                .head(10)
            )

            customer_data.to_excel(
                writer,
                index=False,
                sheet_name="Top Customers"
            )

    output.seek(0)

    return output.getvalue()