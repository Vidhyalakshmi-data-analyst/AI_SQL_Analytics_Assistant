"""
=================================================
File: test_database_executor.py

Purpose:
Unit tests for Database Executor.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest
import pandas as pd

from database.database_executor import (
    run_query
)


class TestDatabaseExecutor(unittest.TestCase):

    def test_run_query_returns_dataframe(self):

        dataframe = run_query(
            "SELECT * FROM customers;"
        )

        
        self.assertIsInstance(
            dataframe,
            pd.DataFrame
        )

        self.assertGreater(
            len(dataframe),
            0
        )

        print(dataframe.head())


if __name__ == "__main__":

    unittest.main()