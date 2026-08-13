"""
=================================================
File: test_insight_generator.py

Purpose:
Unit tests for the insight generator module.
=================================================
"""

import unittest

import pandas as pd

from decimal import Decimal

from ai.insight_generator import (
    calculate_summary,
    find_highest_value,
    find_lowest_value,
    calculate_percentage_change,
    analyze_time_series,
    generate_basic_insights,
    generate_insights
)


class TestInsightGenerator(unittest.TestCase):

    # --------------------------------------------------
    # calculate_summary
    # --------------------------------------------------

    def test_calculate_summary(self):

        dataframe = pd.DataFrame({
            "sales": [
                100,
                200,
                300
            ]
        })

        result = calculate_summary(
            dataframe,
            "sales"
        )

        self.assertEqual(
            result["total"],
            600
        )

        self.assertEqual(
            result["average"],
            200
        )

        self.assertEqual(
            result["minimum"],
            100
        )

        self.assertEqual(
            result["maximum"],
            300
        )


    # --------------------------------------------------
    # find_highest_value
    # --------------------------------------------------

    def test_find_highest_value(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture",
                "Fashion"
            ],
            "sales": [
                500,
                800,
                600
            ]
        })

        result = find_highest_value(
            dataframe,
            "category",
            "sales"
        )

        self.assertEqual(
            result["category"],
            "Furniture"
        )

        self.assertEqual(
            result["value"],
            800
        )


    # --------------------------------------------------
    # find_lowest_value
    # --------------------------------------------------

    def test_find_lowest_value(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture",
                "Fashion"
            ],
            "sales": [
                500,
                800,
                600
            ]
        })

        result = find_lowest_value(
            dataframe,
            "category",
            "sales"
        )

        self.assertEqual(
            result["category"],
            "Electronics"
        )

        self.assertEqual(
            result["value"],
            500
        )


    # --------------------------------------------------
    # calculate_percentage_change
    # --------------------------------------------------

    def test_calculate_percentage_change(self):

        dataframe = pd.DataFrame({
            "sales": [
                100,
                120
            ]
        })

        result = calculate_percentage_change(
            dataframe,
            "sales"
        )

        self.assertEqual(
            result,
            20.0
        )


    # --------------------------------------------------
    # analyze_time_series
    # --------------------------------------------------

    def test_analyze_time_series(self):

        dataframe = pd.DataFrame({
            "sales_month": [
                "2026-01-01",
                "2026-02-01",
                "2026-03-01",
                "2026-04-01"
            ],
            "total_sales": [
                100,
                120,
                90,
                150
            ]
        })

        result = analyze_time_series(
            dataframe,
            "sales_month",
            "total_sales"
        )

        self.assertEqual(
            result["first_value"],
            100
        )

        self.assertEqual(
            result["last_value"],
            150
        )

        self.assertEqual(
            result["percentage_change"],
            50.0
        )

        self.assertEqual(
            result["highest_value"],
            150
        )

        self.assertEqual(
            result["lowest_value"],
            90
        )

        self.assertEqual(
            result["highest_period"],
            pd.Timestamp("2026-04-01")
        )

        self.assertEqual(
            result["lowest_period"],
            pd.Timestamp("2026-03-01")
        )


    def test_analyze_time_series_sorts_dates(self):

        dataframe = pd.DataFrame({
            "sales_month": [
                "2026-03-01",
                "2026-01-01",
                "2026-02-01"
            ],
            "total_sales": [
                150,
                100,
                120
            ]
        })

        result = analyze_time_series(
            dataframe,
            "sales_month",
            "total_sales"
        )

        self.assertEqual(
            result["first_period"],
            pd.Timestamp("2026-01-01")
        )

        self.assertEqual(
            result["last_period"],
            pd.Timestamp("2026-03-01")
        )

        self.assertEqual(
            result["first_value"],
            100
        )

        self.assertEqual(
            result["last_value"],
            150
        )


    def test_analyze_time_series_largest_changes(self):

        dataframe = pd.DataFrame({
            "sales_month": [
                "2026-01-01",
                "2026-02-01",
                "2026-03-01",
                "2026-04-01"
            ],
            "total_sales": [
                100,
                160,
                120,
                200
            ]
        })

        result = analyze_time_series(
            dataframe,
            "sales_month",
            "total_sales"
        )

        self.assertEqual(
            result["largest_increase"]["change"],
            80
        )

        self.assertEqual(
            result["largest_increase"]["from_period"],
            pd.Timestamp("2026-03-01")
        )

        self.assertEqual(
            result["largest_increase"]["to_period"],
            pd.Timestamp("2026-04-01")
        )

        self.assertEqual(
            result["largest_decrease"]["change"],
            -40
        )

        self.assertEqual(
            result["largest_decrease"]["from_period"],
            pd.Timestamp("2026-02-01")
        )

        self.assertEqual(
            result["largest_decrease"]["to_period"],
            pd.Timestamp("2026-03-01")
        )


    def test_analyze_time_series_empty_dataframe(self):

        dataframe = pd.DataFrame()

        result = analyze_time_series(
            dataframe,
            "sales_month",
            "total_sales"
        )

        self.assertEqual(
            result,
            {}
        )


    def test_analyze_time_series_invalid_columns(self):

        dataframe = pd.DataFrame({
            "month": [
                "2026-01-01",
                "2026-02-01"
            ],
            "sales": [
                100,
                200
            ]
        })

        result = analyze_time_series(
            dataframe,
            "sales_month",
            "total_sales"
        )

        self.assertEqual(
            result,
            {}
        )


    # --------------------------------------------------
    # generate_basic_insights
    # --------------------------------------------------

    def test_generate_basic_insights(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture",
                "Fashion"
            ],
            "sales": [
                500,
                800,
                600
            ]
        })

        result = generate_basic_insights(
            dataframe
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["numeric_column"],
            "sales"
        )

        self.assertEqual(
            result["highest"]["category"],
            "Furniture"
        )

        self.assertEqual(
            result["lowest"]["category"],
            "Electronics"
        )


    def test_generate_basic_insights_empty_dataframe(self):

        dataframe = pd.DataFrame()

        result = generate_basic_insights(
            dataframe
        )

        self.assertEqual(
            result["status"],
            "no_data"
        )

        self.assertEqual(
            result["message"],
            "No data is available for analysis."
        )


    def test_generate_basic_insights_with_decimal_values(self):

        dataframe = pd.DataFrame({
            "category": [
            "Fashion",
            "Electronics",
            "Home"
            ],
            "total_sales": [
            Decimal("80000.00"),
            Decimal("50000.00"),
            Decimal("30000.00")
            ]
        })

        result = generate_basic_insights(
            dataframe
        )

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["numeric_column"],
            "total_sales"
        )

        self.assertEqual(
            result["summary"]["total"],
            160000
        )

        self.assertEqual(
            result["highest"]["category"],
            "Fashion"
        )

        self.assertEqual(
            result["lowest"]["category"],
            "Home"
        )

    def test_generate_basic_insights_no_numeric_data(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture",
                "Fashion"
            ]
        })

        result = generate_basic_insights(
            dataframe
        )

        self.assertEqual(
            result["status"],
            "no_numeric_data"
        )


    # --------------------------------------------------
    # generate_insights
    # --------------------------------------------------

    def test_generate_insights(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture",
                "Fashion"
            ],
            "sales": [
                500,
                800,
                600
            ]
        })

        result = generate_insights(
            dataframe
        )

        self.assertIsInstance(
            result,
            str
        )

        self.assertIn(
            "sales",
            result
        )


    def test_generate_insights_empty_dataframe(self):

        dataframe = pd.DataFrame()

        result = generate_insights(
            dataframe
        )

        self.assertEqual(
            result,
            "No data is available for analysis."
        )


    def test_generate_insights_none_dataframe(self):

        result = generate_insights(
            None
        )

        self.assertEqual(
            result,
            "No data is available for analysis."
        )


if __name__ == "__main__":
    unittest.main()