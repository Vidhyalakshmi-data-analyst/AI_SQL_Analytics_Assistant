"""
=================================================
File: test_dashboard_chart_ui.py

Purpose:
Unit tests for Dashboard Chart UI.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

from unittest.mock import patch

from ui.components import (
    render_dashboard_chart
)


class TestDashboardChartUI(
    unittest.TestCase
):

    @patch(
        "ui.components.st"
    )
    def test_render_dashboard_chart(
        self,
        mock_streamlit
    ):

        figure = object()

        render_dashboard_chart(
            figure
        )

        mock_streamlit.plotly_chart.assert_called_once_with(
            figure,
            use_container_width=True
        )


if __name__ == "__main__":

    unittest.main()