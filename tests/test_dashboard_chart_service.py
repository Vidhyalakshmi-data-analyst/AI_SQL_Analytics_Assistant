"""
=================================================
File: test_dashboard_chart_service.py

Purpose:
Unit tests for Dashboard Chart Service.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import pandas as pd

from dashboard.chart_service import (
    create_sales_trend_chart,
    create_sales_category_chart,
    create_sales_state_chart,
    create_order_status_chart,
    create_top_products_chart,
    create_top_customers_chart
)



class TestDashboardChartService(
    unittest.TestCase
):

    def test_sales_trend_chart(self):

        dataframe = pd.DataFrame({

            "order_date": pd.to_datetime([
                "2025-07-01",
                "2025-07-01",
                "2025-07-02",
                "2025-07-03"
            ]),

            "line_total": [
                100,
                200,
                300,
                400
            ]
        })

        figure = create_sales_trend_chart(
            dataframe
        )

        # --------------------------------------------------
        # Figure should be created
        # --------------------------------------------------

        self.assertIsNotNone(
            figure
        )

        # --------------------------------------------------
        # Three unique dates should exist
        # --------------------------------------------------

        self.assertEqual(
            len(figure.data[0].x),
            3
        )

        # --------------------------------------------------
        # Daily sales:
        #
        # July 1 = 300
        # July 2 = 300
        # July 3 = 400
        # --------------------------------------------------

        self.assertEqual(
            list(figure.data[0].y),
            [
                300,
                300,
                400
            ]
        )


    def test_create_order_status_chart(self):

        dataframe = pd.DataFrame({
            "order_status": [
                "Delivered",
                "Delivered",
                "Delivered",
                "Shipped",
                "Shipped",
                "Processing",
                "Cancelled"
            ]
        })

        figure = create_order_status_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            len(figure.data),
            1
        )

    def test_empty_dataframe(self):

        dataframe = pd.DataFrame()

        figure = create_order_status_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )

    def test_missing_status_column(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Fashion"
            ]
        })

        figure = create_order_status_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )

    def test_missing_status_values(self):

        dataframe = pd.DataFrame({
            "status": [
                None,
                None
            ]
        })

        figure = create_order_status_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )


    def test_create_top_products_chart(self):

        dataframe = pd.DataFrame({
            "product_name": [
                "Laptop",
                "Laptop",
                "Phone",
                "Phone",
                "Chair",
                "Book"
            ],
            "line_total": [
                50000,
                25000,
                30000,
                20000,
                15000,
                5000
            ]
        })

        figure = create_top_products_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            len(figure.data),
            1
        )

    def test_top_n_limit(self):

        dataframe = pd.DataFrame({
            "product_name": [
                "Product A",
                "Product B",
                "Product C",
                "Product D",
                "Product E"
            ],
            "line_total": [
                50000,
                40000,
                30000,
                20000,
                10000
            ]
        })

        figure = create_top_products_chart(
            dataframe,
            top_n=3
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            len(
                figure.data[0].x
            ),
            3
        )

    def test_empty_dataframe(self):

        dataframe = pd.DataFrame()

        figure = create_top_products_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )

    def test_missing_required_columns(self):

        dataframe = pd.DataFrame({
            "category": [
                "Fashion",
                "Books"
            ],
            "line_total": [
                10000,
                5000
            ]
        })

        figure = create_top_products_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )

    def test_invalid_sales_values(self):

        dataframe = pd.DataFrame({
            "product_name": [
                "Laptop",
                "Phone"
            ],
            "line_total": [
                "invalid",
                None
            ]
        })

        figure = create_top_products_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )


    def test_create_sales_state_chart(self):

        dataframe = pd.DataFrame({
            "state": [
                "Tamil Nadu",
                "Tamil Nadu",
                "Kerala",
                "Karnataka"
            ],
            "line_total": [
                10000,
                15000,
                8000,
                12000
            ]
        })

        figure = create_sales_state_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            len(figure.data),
            1
        )


    def test_empty_dataframe(self):

        dataframe = pd.DataFrame()

        figure = create_sales_state_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )


    def test_missing_columns(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Fashion"
            ],
            "line_total": [
                1000,
                2000
            ]
        })

        figure = create_sales_state_chart(
                dataframe
            )

        self.assertIsNone(
                figure
            )

    def test_create_top_customers_chart(self):

        dataframe = pd.DataFrame({
            "customer_name": [
                "Customer A",
                "Customer B",
                "Customer C",
                "Customer A",
                "Customer B"
            ],
            "line_total": [
                10000,
                5000,
                2000,
                3000,
                4000
            ]
        })

        figure = create_top_customers_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.layout.title.text,
            "Top 10 Customers by Sales"
        )


    def test_create_top_customers_chart_ranking(self):

        dataframe = pd.DataFrame({
            "customer_name": [
                "Customer A",
                "Customer B",
                "Customer C",
                "Customer A",
                "Customer B"
            ],
            "line_total": [
                10000,
                5000,
                2000,
                3000,
                4000
            ]
        })

        figure = create_top_customers_chart(
            dataframe,
            top_n=2
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            len(figure.data[0].x),
            2
        )

        self.assertEqual(
            figure.data[0].x[0],
            "Customer A"
        )

        self.assertEqual(
            figure.data[0].x[1],
            "Customer B"
        )


if __name__ == "__main__":

    unittest.main()