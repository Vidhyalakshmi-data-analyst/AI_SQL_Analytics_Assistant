"""
=================================================
File: test_query_engine.py

Purpose:
Integration tests for Query Engine.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest
from unittest.mock import patch

from ai.query_engine import (
    answer_question
)

from ai.models import QueryResult


class TestQueryEngine(unittest.TestCase):

    @patch(
        "ai.query_engine.generate_valid_sql"
    )
    def test_answer_question_returns_query_result(
        self,
        mock_generate_valid_sql
    ):

        # --------------------------------------------------
        # Mock Gemini-generated SQL
        # --------------------------------------------------
        #
        # This prevents the test from making a real
        # Gemini API request and consuming API quota.
        #
        mock_generate_valid_sql.return_value = (
            "SELECT * FROM customers LIMIT 5;"
        )

        # --------------------------------------------------
        # Execute query engine
        # --------------------------------------------------

        result = answer_question(
            "Show all customers"
        )

        # --------------------------------------------------
        # Verify result type
        # --------------------------------------------------

        self.assertIsInstance(
            result,
            QueryResult
        )

        # --------------------------------------------------
        # Verify SQL
        # --------------------------------------------------

        self.assertIsInstance(
            result.sql,
            str
        )

        self.assertEqual(
            result.sql,
            "SELECT * FROM customers LIMIT 5;"
        )

        # --------------------------------------------------
        # Verify query result DataFrame
        # --------------------------------------------------

        self.assertFalse(
            result.dataframe.empty
        )

        # --------------------------------------------------
        # Verify Gemini was NOT called
        # --------------------------------------------------

        mock_generate_valid_sql.assert_called_once_with(
            "Show all customers"
        )


if __name__ == "__main__":
    unittest.main()