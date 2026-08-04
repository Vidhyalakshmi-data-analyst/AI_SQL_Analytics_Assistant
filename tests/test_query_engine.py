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
    generate_valid_sql,
    execute_valid_sql,
    answer_question
)


class TestQueryEngine(unittest.TestCase):

    def test_generate_valid_sql(self):

        sql = generate_valid_sql(
            "Show all customers"
        )

        self.assertIsInstance(
            sql,
            str
        )

        self.assertTrue(
            sql.upper().startswith("SELECT")
        )

    def test_execute_valid_sql(self):

        dataframe = execute_valid_sql(
            "SELECT * FROM customers;"
        )

        self.assertFalse(
            dataframe.empty
        )


    def test_answer_question(self):

        dataframe = answer_question(
            "Show all customers"
        )

        self.assertFalse(
            dataframe.empty
        )


if __name__ == "__main__":

    unittest.main()

