"""
=================================================
File: test_dashboard_service.py

Purpose:
Integration tests for Dashboard Data Service.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import pandas as pd

from dashboard.filters import FilterContext
from dashboard.service import (
    build_dashboard_query,
    get_dashboard_data
)


class TestDashboardService(unittest.TestCase):

    # --------------------------------------------------
    # Test 1: Query construction without filters
    # --------------------------------------------------

    def test_build_query_without_filters(self):

        filter_context = FilterContext()

        sql, parameters = build_dashboard_query(
            filter_context
        )

        self.assertIsInstance(
            sql,
            str
        )

        self.assertIsInstance(
            parameters,
            tuple
        )

        self.assertEqual(
            parameters,
            ()
        )

        self.assertIn(
            "FROM orders",
            sql
        )

        self.assertIn(
            "order_items",
            sql
        )

        print("\nGenerated SQL:")
        print(sql)

    # --------------------------------------------------
    # Test 2: Dashboard data without filters
    # --------------------------------------------------

    def test_get_dashboard_data_without_filters(self):

        filter_context = FilterContext()

        dataframe = get_dashboard_data(
            filter_context
        )

        self.assertIsInstance(
            dataframe,
            pd.DataFrame
        )

        self.assertGreater(
            len(dataframe),
            0
        )

        expected_columns = [
            "order_id",
            "order_date",
            "order_status",
            "customer_id",
            "customer_name",
            "state",
            "city",
            "category",
            "product_name",
            "brand",
            "sub_category",
            "quantity",
            "unit_price",
            "line_total"
        ]

        for column in expected_columns:

            self.assertIn(
                column,
                dataframe.columns
            )

        print("\nDashboard Data:")
        print(dataframe.head())

    # --------------------------------------------------
    # Test 3: Category filter
    # --------------------------------------------------

    def test_category_filter(self):

        unfiltered_context = FilterContext()

        unfiltered_data = get_dashboard_data(
            unfiltered_context
        )

        self.assertGreater(
            len(unfiltered_data),
            0
        )

        category = (
            unfiltered_data[
                "category"
            ].iloc[0]
        )

        filter_context = FilterContext(
            category=category
        )

        filtered_data = get_dashboard_data(
            filter_context
        )

        self.assertGreater(
            len(filtered_data),
            0
        )

        self.assertTrue(
            (
                filtered_data["category"]
                == category
            ).all()
        )

        print(
            f"\nCategory filter tested: {category}"
        )

    # --------------------------------------------------
    # Test 4: State filter
    # --------------------------------------------------

    def test_state_filter(self):

        unfiltered_context = FilterContext()

        unfiltered_data = get_dashboard_data(
            unfiltered_context
        )

        self.assertGreater(
            len(unfiltered_data),
            0
        )

        state = (
            unfiltered_data[
                "state"
            ].iloc[0]
        )

        filter_context = FilterContext(
            state=state
        )

        filtered_data = get_dashboard_data(
            filter_context
        )

        self.assertGreater(
            len(filtered_data),
            0
        )

        self.assertTrue(
            (
                filtered_data["state"]
                == state
            ).all()
        )

        print(
            f"\nState filter tested: {state}"
        )

    # --------------------------------------------------
    # Test 5: Order status filter
    # --------------------------------------------------

    def test_order_status_filter(self):

        unfiltered_context = FilterContext()

        unfiltered_data = get_dashboard_data(
            unfiltered_context
        )

        self.assertGreater(
            len(unfiltered_data),
            0
        )

        order_status = (
            unfiltered_data[
                "order_status"
            ].iloc[0]
        )

        filter_context = FilterContext(
            order_status=order_status
        )

        filtered_data = get_dashboard_data(
            filter_context
        )

        self.assertGreater(
            len(filtered_data),
            0
        )

        self.assertTrue(
            (
                filtered_data["order_status"]
                == order_status
            ).all()
        )

        print(
            f"\nOrder status filter tested: "
            f"{order_status}"
        )

    # --------------------------------------------------
    # Test 6: Multiple filters
    # --------------------------------------------------

    def test_multiple_filters(self):

        unfiltered_data = get_dashboard_data(
            FilterContext()
        )

        self.assertGreater(
            len(unfiltered_data),
            0
        )

        first_row = unfiltered_data.iloc[0]

        filter_context = FilterContext(
            category=first_row["category"],
            state=first_row["state"],
            order_status=first_row["order_status"]
        )

        filtered_data = get_dashboard_data(
            filter_context
        )

        self.assertGreater(
            len(filtered_data),
            0
        )

        self.assertTrue(
            (
                filtered_data["category"]
                == first_row["category"]
            ).all()
        )

        self.assertTrue(
            (
                filtered_data["state"]
                == first_row["state"]
            ).all()
        )

        self.assertTrue(
            (
                filtered_data["order_status"]
                == first_row["order_status"]
            ).all()
        )

        print(
            "\nMultiple filter test passed."
        )


if __name__ == "__main__":

    unittest.main()