"""
=================================================
File: test_dashboard_controller.py

Purpose:
Tests for Dashboard Controller.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import pandas as pd

from dashboard.controller import (
    load_dashboard_data
)

from dashboard.filters import (
    FilterContext
)


class TestDashboardController(unittest.TestCase):

    # --------------------------------------------------
    # Test 1: Load dashboard data without filters
    # --------------------------------------------------

    def test_load_dashboard_data(self):

        filter_context = FilterContext()

        dataframe = load_dashboard_data(
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

    # --------------------------------------------------
    # Test 2: Load filtered dashboard data
    # --------------------------------------------------

    def test_load_filtered_dashboard_data(self):

        filter_context = FilterContext(
            category="Fashion"
        )

        dataframe = load_dashboard_data(
            filter_context
        )

        self.assertIsInstance(
            dataframe,
            pd.DataFrame
        )

        if not dataframe.empty:

            self.assertTrue(
                (
                    dataframe["category"]
                    == "Fashion"
                ).all()
            )


if __name__ == "__main__":

    unittest.main()