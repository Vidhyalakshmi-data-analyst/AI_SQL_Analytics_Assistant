"""
=================================================
File: test_sql_validator.py

Purpose:
Unit tests for the SQL Validator module.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import unittest

import ai.sql_validator as sql_validator


class TestSQLValidator(unittest.TestCase):
    """
    Test cases for SQL validation.
    """

    def test_empty_sql(self):

        with self.assertRaises(ValueError):

            sql_validator.validate_sql("")

    def test_valid_select_query(self):

        sql_validator.validate_sql(
            "SELECT * FROM customers;"
        )

    def test_non_select_query(self):

        with self.assertRaises(ValueError):

            sql_validator.validate_sql(
                "DELETE FROM customers;"
            )

    def test_multiple_statements(self):

        with self.assertRaises(ValueError):

            sql_validator.validate_sql(
                "SELECT * FROM customers; DROP TABLE customers;"
            )

    def test_forbidden_keyword(self):

        with self.assertRaises(ValueError):

            sql_validator.validate_sql(
                "UPDATE customers SET city='Chennai';"
            )

    def test_sql_comments(self):

        with self.assertRaises(ValueError):

            sql_validator.validate_sql(
                """
                SELECT *
                FROM customers
                -- Comment
                """
            )


if __name__ == "__main__":

    unittest.main()

