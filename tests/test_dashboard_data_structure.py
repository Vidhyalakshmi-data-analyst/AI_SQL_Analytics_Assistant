"""
=================================================
File: test_dashboard_data_structure.py

Purpose:
Inspect the structure of the dashboard DataFrame.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

from dashboard.controller import (
    load_dashboard_data
)

from dashboard.filters import (
    FilterContext
)


class TestDashboardDataStructure(unittest.TestCase):

    def test_dashboard_data_structure(self):

        dataframe = load_dashboard_data(
            FilterContext()
        )

        print("\nDashboard columns:")
        print(
            dataframe.columns.tolist()
        )

        print("\nDashboard data types:")
        print(
            dataframe.dtypes
        )

        print("\nFirst 5 rows:")
        print(
            dataframe.head()
        )

        self.assertIsNotNone(
            dataframe
        )


if __name__ == "__main__":

    unittest.main()