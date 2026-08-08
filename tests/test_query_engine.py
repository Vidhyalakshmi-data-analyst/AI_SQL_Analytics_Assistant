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

from ai.query_engine import (
    answer_question
)

from ai.models import QueryResult


class TestQueryEngine(unittest.TestCase):

    def test_answer_question_returns_query_result(self):

        result = answer_question(
            "Show all customers"
        )

        self.assertIsInstance(
            result,
            QueryResult
        )

        self.assertIsInstance(
            result.sql,
            str
        )

        self.assertFalse(
            result.dataframe.empty
        )


if __name__ == "__main__":
    unittest.main()