"""
=================================================
File: test_kpi_generator.py

Purpose:
Unit tests for KPI generation.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import pandas as pd

from ai.kpi_generator import generate_kpis


class TestKPIGenerator(unittest.TestCase):

    def test_category_sales_kpis(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Automotive",
                "Fashion"
            ],
            "sales": [
                5000,
                2000,
                3000
            ]
        })

        result = generate_kpis(dataframe)

        self.assertEqual(
            result["status"],
            "success"
        )

        kpis = result["kpis"]

        self.assertEqual(
            kpis["measure"],
            "sales"
        )

        self.assertEqual(
            kpis["total"],
            10000
        )

        self.assertEqual(
            kpis["average"],
            10000 / 3
        )

        self.assertEqual(
            kpis["maximum"],
            5000
        )

        self.assertEqual(
            kpis["minimum"],
            2000
        )

        self.assertEqual(
            kpis["count"],
            3
        )

        self.assertEqual(
            kpis["highest"]["category"],
            "Electronics"
        )

        self.assertEqual(
            kpis["lowest"]["category"],
            "Automotive"
        )

        self.assertEqual(
            kpis["category_count"],
            3
        )

    def test_numeric_only_dataframe(self):

        dataframe = pd.DataFrame({
            "sales": [
                100,
                200,
                300
            ]
        })

        result = generate_kpis(dataframe)

        self.assertEqual(
            result["status"],
            "success"
        )

        self.assertEqual(
            result["kpis"]["total"],
            600
        )

        self.assertEqual(
            result["kpis"]["average"],
            200
        )

        self.assertEqual(
            result["kpis"]["maximum"],
            300
        )

        self.assertEqual(
            result["kpis"]["minimum"],
            100
        )

        self.assertEqual(
            result["kpis"]["count"],
            3
        )

    def test_empty_dataframe(self):

        dataframe = pd.DataFrame()

        result = generate_kpis(dataframe)

        self.assertEqual(
            result["status"],
            "no_data"
        )

        self.assertEqual(
            result["kpis"],
            {}
        )

    def test_no_numeric_columns(self):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Automotive",
                "Fashion"
            ]
        })

        result = generate_kpis(dataframe)

        self.assertEqual(
            result["status"],
            "no_numeric_data"
        )

        self.assertEqual(
            result["kpis"],
            {}
        )

    def test_time_series_kpis(self):

        dataframe = pd.DataFrame({
            "month": pd.to_datetime([
                "2026-01-01",
                "2026-02-01",
                "2026-03-01"
            ]),
            "sales": [
                100,
                150,
                200
            ]
        })

        result = generate_kpis(dataframe)

        self.assertEqual(
            result["status"],
            "success"
        )

        kpis = result["kpis"]

        self.assertEqual(
            kpis["period_count"],
            3
        )

        self.assertEqual(
            kpis["highest_period"]["value"],
            200
        )

        self.assertEqual(
            kpis["lowest_period"]["value"],
            100
        )

        self.assertEqual(
            kpis["percentage_change"],
            100
        )


if __name__ == "__main__":
    unittest.main()