"""
=================================================
File: test_sales_category_chart.py

Purpose:
Unit tests for Sales by Category chart.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import pandas as pd

from dashboard.chart_service import (
    create_sales_category_chart
)


class TestSalesCategoryChart(unittest.TestCase):

    def test_sales_category_chart(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Electronics",
                "Fashion",
                "Office"
            ],
            "line_total": [
                1000,
                2000,
                1500,
                500
            ]
        })

        figure = create_sales_category_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.layout.title.text,
            "Sales by Category"
        )

        self.assertEqual(
            len(figure.data[0].x),
            3
        )

    def test_empty_dataframe(self):

        dataframe = pd.DataFrame()

        figure = create_sales_category_chart(
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
            ]
        })

        figure = create_sales_category_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )


if __name__ == "__main__":

    unittest.main()