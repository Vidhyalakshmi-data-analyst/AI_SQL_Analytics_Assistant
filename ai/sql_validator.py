"""
=================================================
File: sql_validator.py

Purpose:
Validate AI-generated SQL before execution.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import re

FORBIDDEN_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
    "GRANT",
    "REVOKE"
]

def check_empty_sql(sql: str) -> None:
    """
    Ensure SQL is not empty.
    """

    if not sql.strip():

        raise ValueError(
            "Generated SQL is empty."
        )
    
    
def check_select_query(sql: str) -> None:
    """
    Ensure only SELECT queries are allowed.
    """

    sql = sql.strip().upper()

    if not sql.startswith("SELECT"):

        raise ValueError(
            "Only SELECT queries are allowed."
        )
    

def check_multiple_statements(sql: str) -> None:
    """
    Prevent execution of multiple SQL statements.
    """

    sql = sql.strip()

    # Remove one optional trailing semicolon
    if sql.endswith(";"):
        sql = sql[:-1].strip()

    # Reject any remaining semicolon
    if ";" in sql:

        raise ValueError(
            "Multiple SQL statements are not allowed."
        )



def check_forbidden_keywords(sql: str) -> None:
    """
    Prevent dangerous SQL keywords.
    """

    sql_upper = sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:

        pattern = rf"\b{keyword}\b"

        if re.search(pattern, sql_upper):

            raise ValueError(
                f"Forbidden SQL keyword detected: {keyword}"
            )        



def check_sql_comments(sql: str) -> None:
    """
    Prevent SQL comments.
    """

    if "--" in sql:

        raise ValueError(
            "Single-line SQL comments are not allowed."
        )

    if "/*" in sql or "*/" in sql:

        raise ValueError(
            "Multi-line SQL comments are not allowed."
        )
    

def validate_sql(sql: str) -> None:
    """
    Validate SQL before execution.
    """
    check_empty_sql(sql)

    check_select_query(sql)

    check_multiple_statements(sql)

    check_forbidden_keywords(sql)

    check_sql_comments(sql)