"""
=================================================
File: test_dashboard_kpi_service.py

Purpose:
Unit tests for Dashboard KPI Service.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import pandas as pd

from dashboard.kpi_service import (
    calculate_dashboard_kpis
)


class TestDashboardKPIService(unittest.TestCase):

    def test_dashboard_kpis(self):

        dataframe = pd.DataFrame({

            "order_id": [
                1,
                1,
                2,
                3
            ],

            "customer_id": [
                101,
                101,
                102,
                103
            ],

            "quantity": [
                2,
                1,
                3,
                2
            ],

            "line_total": [
                200.00,
                100.00,
                300.00,
                400.00
            ]
        })

        result = calculate_dashboard_kpis(
            dataframe
        )

        # --------------------------------------------------
        # Status
        # --------------------------------------------------

        self.assertEqual(
            result["status"],
            "success"
        )

        kpis = result["kpis"]

        # --------------------------------------------------
        # Total Sales
        # --------------------------------------------------

        self.assertEqual(
            kpis["total_sales"],
            1000.00
        )

        # --------------------------------------------------
        # Total Orders
        #
        # Order 1 has two rows because it has
        # multiple order items.
        # --------------------------------------------------

        self.assertEqual(
            kpis["total_orders"],
            3
        )

        # --------------------------------------------------
        # Total Customers
        # --------------------------------------------------

        self.assertEqual(
            kpis["total_customers"],
            3
        )

        # --------------------------------------------------
        # Units Sold
        # --------------------------------------------------

        self.assertEqual(
            kpis["units_sold"],
            8
        )

        # --------------------------------------------------
        # Average Order Value
        # --------------------------------------------------

        self.assertAlmostEqual(
            kpis["average_order_value"],
            333.333333,
            places=4
        )


if __name__ == "__main__":

    unittest.main()