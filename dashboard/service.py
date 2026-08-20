"""
=================================================
File: service.py

Purpose:
Retrieve dashboard data based on the current
dashboard filter context.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from datetime import timedelta

import pandas as pd

from dashboard.filters import FilterContext
from database.database_executor import run_query


def build_dashboard_query(
    filter_context: FilterContext
) -> tuple[str, tuple]:
    """
    Build the dashboard SQL query and parameters.

    Responsibility:
        Convert FilterContext into parameterized SQL.

    Returns:
        Tuple containing:
            - SQL query
            - SQL parameters
    """

    sql = """
        SELECT
            o.order_id,
            o.order_date,
            o.order_status,

            o.customer_id,

            CONCAT(
                c.first_name,
                ' ',
                c.last_name
            ) AS customer_name,

            c.state,
            c.city,

            cat.category_name AS category,

            p.product_name,
            p.brand,
            p.sub_category,

            oi.quantity,
            oi.unit_price,
            oi.line_total

        FROM orders o

        INNER JOIN customers c
            ON o.customer_id = c.customer_id

        INNER JOIN order_items oi
            ON o.order_id = oi.order_id

        INNER JOIN products p
            ON oi.product_id = p.product_id

        INNER JOIN categories cat
            ON p.category_id = cat.category_id

        WHERE 1 = 1
    """

    parameters = []

    # --------------------------------------------------
    # Date Filter
    # --------------------------------------------------

    if filter_context.start_date is not None:

        sql += """
            AND o.order_date >= %s
        """

        parameters.append(
            filter_context.start_date
        )

    if filter_context.end_date is not None:

        # Use exclusive upper bound so that the
        # complete end date is included even though
        # order_date is a timestamp.
        end_date_exclusive = (
            filter_context.end_date
            + timedelta(days=1)
        )

        sql += """
            AND o.order_date < %s
        """

        parameters.append(
            end_date_exclusive
        )

    # --------------------------------------------------
    # Category Filter
    # --------------------------------------------------

    if filter_context.category is not None:

        sql += """
            AND cat.category_name = %s
        """

        parameters.append(
            filter_context.category
        )

    # --------------------------------------------------
    # State Filter
    # --------------------------------------------------

    if filter_context.state is not None:

        sql += """
            AND c.state = %s
        """

        parameters.append(
            filter_context.state
        )

    # --------------------------------------------------
    # Order Status Filter
    # --------------------------------------------------

    if filter_context.order_status is not None:

        sql += """
            AND o.order_status = %s
        """

        parameters.append(
            filter_context.order_status
        )

    # --------------------------------------------------
    # Consistent ordering for dashboard data
    # --------------------------------------------------

    sql += """
        ORDER BY
            o.order_date,
            o.order_id,
            oi.order_item_id
    """

    return (
        sql,
        tuple(parameters)
    )


def get_dashboard_data(
    filter_context: FilterContext
) -> pd.DataFrame:
    """
    Retrieve dashboard data using the supplied
    filter context.

    Responsibility:
        Execute the dashboard query and return
        the resulting DataFrame.
    """

    sql, parameters = build_dashboard_query(
        filter_context
    )

    return run_query(
        sql,
        parameters
    )