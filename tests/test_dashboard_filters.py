"""
=================================================
File: test_dashboard_filters.py

Purpose:
Test dashboard filter context.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest
from datetime import date

from dashboard.filters import FilterContext


class TestFilterContext(unittest.TestCase):

    def test_default_filter_context(self):

        filters = FilterContext()

        self.assertIsNone(filters.start_date)
        self.assertIsNone(filters.end_date)
        self.assertIsNone(filters.category)
        self.assertIsNone(filters.state)
        self.assertIsNone(filters.order_status)

    def test_filter_context_with_values(self):

        filters = FilterContext(
            start_date=date(2025, 1, 1),
            end_date=date(2025, 3, 31),
            category="Electronics",
            state="Tamil Nadu",
            order_status="Delivered"
        )

        self.assertEqual(
            filters.start_date,
            date(2025, 1, 1)
        )

        self.assertEqual(
            filters.end_date,
            date(2025, 3, 31)
        )

        self.assertEqual(
            filters.category,
            "Electronics"
        )

        self.assertEqual(
            filters.state,
            "Tamil Nadu"
        )

        self.assertEqual(
            filters.order_status,
            "Delivered"
        )


if __name__ == "__main__":
    unittest.main()