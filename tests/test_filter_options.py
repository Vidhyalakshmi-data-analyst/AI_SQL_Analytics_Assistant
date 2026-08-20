"""
=================================================
File: test_filter_options.py

Purpose:
Integration tests for dashboard filter options.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

from dashboard.filter_options import (
    get_filter_options
)


class TestFilterOptions(unittest.TestCase):

    def test_get_filter_options(self):

        result = get_filter_options()

        self.assertIsInstance(
            result,
            dict
        )

        self.assertIn(
            "categories",
            result
        )

        self.assertIn(
            "states",
            result
        )

        self.assertIn(
            "order_statuses",
            result
        )

        self.assertIn(
            "min_date",
            result
        )

        self.assertIn(
            "max_date",
            result
        )

        self.assertIsInstance(
            result["categories"],
            list
        )

        self.assertIsInstance(
            result["states"],
            list
        )

        self.assertIsInstance(
            result["order_statuses"],
            list
        )

        self.assertIsNotNone(
            result["min_date"]
        )

        self.assertIsNotNone(
            result["max_date"]
        )

        self.assertLessEqual(
            result["min_date"],
            result["max_date"]
        )

        print("\nDashboard Filter Options:")
        print(result)


if __name__ == "__main__":

    unittest.main()