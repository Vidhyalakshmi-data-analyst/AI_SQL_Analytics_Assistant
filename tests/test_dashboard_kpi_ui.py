"""
=================================================
File: test_dashboard_kpi_ui.py

Purpose:
Basic validation for Dashboard KPI UI component.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

from unittest.mock import patch

from ui.components import (
    render_dashboard_kpi_cards
)


class TestDashboardKPIUI(unittest.TestCase):

    @patch(
        "ui.components.st"
    )
    def test_render_dashboard_kpi_cards(
        self,
        mock_streamlit
    ):

        # --------------------------------------------------
        # Mock columns
        # --------------------------------------------------

        mock_columns = [
            mock_streamlit,
            mock_streamlit,
            mock_streamlit,
            mock_streamlit
        ]

        mock_streamlit.columns.return_value = (
            mock_columns
        )

        # --------------------------------------------------
        # KPI result
        # --------------------------------------------------

        kpi_result = {

            "status": "success",

            "kpis": {

                "total_sales": 100000.00,

                "total_orders": 100,

                "total_customers": 75,

                "units_sold": 250,

                "average_order_value": 1000.00
            }
        }

        # --------------------------------------------------
        # Execute
        # --------------------------------------------------

        render_dashboard_kpi_cards(
            kpi_result
        )

        # --------------------------------------------------
        # Verify
        # --------------------------------------------------

        mock_streamlit.subheader.assert_called_once()

        self.assertTrue(
            mock_streamlit.metric.called
        )

        mock_streamlit.caption.assert_called_once()


if __name__ == "__main__":

    unittest.main()