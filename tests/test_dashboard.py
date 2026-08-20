"""
=================================================
File: test_dashboard.py

Purpose:
Unit tests for Dashboard UI orchestration.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest
from unittest.mock import patch

import pandas as pd

from ui.dashboard import (
    render_dashboard
)

from dashboard.filters import (
    FilterContext
)


class TestDashboard(unittest.TestCase):

    @patch(
        "ui.dashboard.get_filter_options"
    )
    @patch(
        "ui.dashboard.render_dashboard_filters"
    )
    @patch(
        "ui.dashboard.load_dashboard_data"
    )
    def test_dashboard_loads_data(
        self,
        mock_load_data,
        mock_render_filters,
        mock_filter_options
    ):

        # --------------------------------------------------
        # Mock filter options
        # --------------------------------------------------

        mock_filter_options.return_value = {
            "categories": [
                "Fashion"
            ],
            "states": [
                "Tamil Nadu"
            ],
            "order_statuses": [
                "Delivered"
            ],
            "min_date": None,
            "max_date": None
        }

        # --------------------------------------------------
        # Mock selected filters
        # --------------------------------------------------

        filter_context = FilterContext(
            category="Fashion"
        )

        mock_render_filters.return_value = (
            filter_context
        )

        # --------------------------------------------------
        # Mock dashboard data
        # --------------------------------------------------

        expected_dataframe = pd.DataFrame({
            "category": [
                "Fashion",
                "Fashion"
            ],
            "total_sales": [
                1000,
                1500
            ]
        })

        mock_load_data.return_value = (
            expected_dataframe
        )

        # --------------------------------------------------
        # Execute
        # --------------------------------------------------

        result = render_dashboard()

        # --------------------------------------------------
        # Assertions
        # --------------------------------------------------

        self.assertIsInstance(
            result,
            pd.DataFrame
        )

        self.assertEqual(
            len(result),
            2
        )

        mock_filter_options.assert_called_once()

        mock_render_filters.assert_called_once()

        mock_load_data.assert_called_once_with(
            filter_context
        )


if __name__ == "__main__":

    unittest.main()