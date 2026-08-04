"""
=================================================
File: query_engine.py

Purpose:
Coordinate the complete AI query pipeline.

Convert a natural language question into a
validated SQL query, execute it against
PostgreSQL, and return the results as a
Pandas DataFrame.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd

from ai.sql_generator import (
    generate_sql
)

import ai.sql_validator as sql_validator

from database.database_executor import (
    run_query
)


def generate_valid_sql(user_question: str) -> str:
    """
    Generate SQL from a natural language question
    and validate it.
    """

    sql = generate_sql(
        user_question
    )

    sql_validator.validate_sql(
        sql
    )

    return sql


def execute_valid_sql(sql: str) -> pd.DataFrame:
    """
    Execute validated SQL and return
    the query results as a DataFrame.
    """

    dataframe = run_query(
        sql
    )

    return dataframe


def answer_question(user_question: str) -> pd.DataFrame:
    """
    Complete AI query pipeline.

    Natural Language
            ↓
    SQL Generation
            ↓
    SQL Validation
            ↓
    Database Execution
            ↓
    Pandas DataFrame
    """

    try:

        sql = generate_valid_sql(
            user_question
        )

        dataframe = execute_valid_sql(
            sql
        )

        return dataframe

    except Exception as e:

        raise RuntimeError(
            f"Failed to process question: {e}"
        ) from e