"""
=================================================
File: test_dashboard_filter_ui.py

Purpose:
Unit tests for Dashboard Filter UI conversion.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest
from datetime import date

from ui.dashboard_filters import (
    create_filter_context
)


class TestDashboardFilterUI(unittest.TestCase):

    # --------------------------------------------------
    # Test 1: All filters selected as "All"
    # --------------------------------------------------

    def test_no_category_state_status_filter(self):

        context = create_filter_context(
            "All Categories",
            "All States",
            "All Statuses",
            (
                date(2025, 1, 1),
                date(2025, 12, 31)
            )
        )

        self.assertIsNone(
            context.category
        )

        self.assertIsNone(
            context.state
        )

        self.assertIsNone(
            context.order_status
        )

        self.assertEqual(
            context.start_date,
            date(2025, 1, 1)
        )

        self.assertEqual(
            context.end_date,
            date(2025, 12, 31)
        )

    # --------------------------------------------------
    # Test 2: Category filter
    # --------------------------------------------------

    def test_category_filter(self):

        context = create_filter_context(
            "Fashion",
            "All States",
            "All Statuses",
            None
        )

        self.assertEqual(
            context.category,
            "Fashion"
        )

        self.assertIsNone(
            context.state
        )

        self.assertIsNone(
            context.order_status
        )

    # --------------------------------------------------
    # Test 3: State filter
    # --------------------------------------------------

    def test_state_filter(self):

        context = create_filter_context(
            "All Categories",
            "Tamil Nadu",
            "All Statuses",
            None
        )

        self.assertEqual(
            context.state,
            "Tamil Nadu"
        )

        self.assertIsNone(
            context.category
        )

        self.assertIsNone(
            context.order_status
        )

    # --------------------------------------------------
    # Test 4: Order status filter
    # --------------------------------------------------

    def test_order_status_filter(self):

        context = create_filter_context(
            "All Categories",
            "All States",
            "Delivered",
            None
        )

        self.assertEqual(
            context.order_status,
            "Delivered"
        )

        self.assertIsNone(
            context.category
        )

        self.assertIsNone(
            context.state
        )

    # --------------------------------------------------
    # Test 5: Multiple filters
    # --------------------------------------------------

    def test_multiple_filters(self):

        context = create_filter_context(
            "Fashion",
            "Tamil Nadu",
            "Delivered",
            (
                date(2025, 2, 1),
                date(2025, 5, 31)
            )
        )

        self.assertEqual(
            context.category,
            "Fashion"
        )

        self.assertEqual(
            context.state,
            "Tamil Nadu"
        )

        self.assertEqual(
            context.order_status,
            "Delivered"
        )

        self.assertEqual(
            context.start_date,
            date(2025, 2, 1)
        )

        self.assertEqual(
            context.end_date,
            date(2025, 5, 31)
        )

    # --------------------------------------------------
    # Test 6: Single date selection
    # --------------------------------------------------

    def test_single_date_selection(self):

        selected_date = date(
            2025,
            6,
            15
        )

        context = create_filter_context(
            "All Categories",
            "All States",
            "All Statuses",
            (selected_date,)
        )

        self.assertEqual(
            context.start_date,
            selected_date
        )

        self.assertEqual(
            context.end_date,
            selected_date
        )


if __name__ == "__main__":

    unittest.main()