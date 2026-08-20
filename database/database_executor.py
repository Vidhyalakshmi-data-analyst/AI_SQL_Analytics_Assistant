"""
=================================================
File: database_executor.py

Purpose:
Execute validated SQL queries against the
PostgreSQL database and return the results.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd

from database.connection.db_connection import (
    get_connection
)

def execute_query(
    connection,
    sql: str,
    parameters=None
):
    """
    Execute a validated SQL query.

    Parameters:
        connection:
            PostgreSQL database connection.

        sql:
            SQL query to execute.

        parameters:
            Optional parameters for parameterized SQL.

    Returns:
        Database cursor.
    """

    cursor = connection.cursor()

    if parameters:

        cursor.execute(
            sql,
            parameters
        )

    else:

        cursor.execute(sql)

    return cursor


def fetch_dataframe(cursor):
    """
    Convert query results into a Pandas DataFrame.

    Returns:
        Pandas DataFrame.
    """

    columns = [
        description[0]
        for description in cursor.description
    ]

    rows = cursor.fetchall()

    return pd.DataFrame(
        rows,
        columns=columns
    )


def close_connection(connection, cursor):
    """
    Close the database cursor and connection.
    """

    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()


def run_query(
    sql: str,
    parameters=None
) -> pd.DataFrame:
    """
    Execute a validated SQL query and
    return the results as a DataFrame.

    Parameters:
        sql:
            SQL query to execute.

        parameters:
            Optional parameters for parameterized SQL.
    """

    connection = None
    cursor = None

    try:

        connection = get_connection()

        cursor = execute_query(
            connection,
            sql,
            parameters
        )

        dataframe = fetch_dataframe(
            cursor
        )

        return dataframe

    finally:

        close_connection(
            connection,
            cursor
        )