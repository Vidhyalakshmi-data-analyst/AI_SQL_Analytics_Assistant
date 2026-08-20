"""
=================================================
File: filter_options.py

Purpose:
Retrieve available values for dashboard filters.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from datetime import date
from typing import Any

from database.database_executor import run_query


def get_filter_options() -> dict[str, Any]:
    """
    Retrieve the available dashboard filter options.

    Responsibility:
        Retrieve valid filter values from PostgreSQL.

    Returns:
        Dictionary containing:
            - categories
            - states
            - order_statuses
            - min_date
            - max_date
    """

    sql = """
        SELECT
            (
                SELECT
                    ARRAY_AGG(
                        DISTINCT category_name
                        ORDER BY category_name
                    )
                FROM categories
                WHERE is_active = TRUE
            ) AS categories,

            (
                SELECT
                    ARRAY_AGG(
                        DISTINCT state
                        ORDER BY state
                    )
                FROM customers
                WHERE state IS NOT NULL
            ) AS states,

            (
                SELECT
                    ARRAY_AGG(
                        DISTINCT order_status
                        ORDER BY order_status
                    )
                FROM orders
                WHERE order_status IS NOT NULL
            ) AS order_statuses,

            (
                SELECT
                    MIN(order_date)::date
                FROM orders
            ) AS min_date,

            (
                SELECT
                    MAX(order_date)::date
                FROM orders
            ) AS max_date;
    """

    dataframe = run_query(sql)

    if dataframe.empty:

        return {
            "categories": [],
            "states": [],
            "order_statuses": [],
            "min_date": None,
            "max_date": None
        }

    row = dataframe.iloc[0]

    return {
        "categories": (
            row["categories"]
            if row["categories"] is not None
            else []
        ),

        "states": (
            row["states"]
            if row["states"] is not None
            else []
        ),

        "order_statuses": (
            row["order_statuses"]
            if row["order_statuses"] is not None
            else []
        ),

        "min_date": row["min_date"],

        "max_date": row["max_date"]
    }