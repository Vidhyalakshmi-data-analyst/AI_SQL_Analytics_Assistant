"""
=================================================
File: sql_generator.py

Purpose:
Generate PostgreSQL SQL queries from natural
language questions using Google's Gemini model.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import re

from ai.gemini_client import (
    get_gemini_client,
    get_model_name
)

from ai.prompt_builder import (
    build_sql_prompt
)

import ai.sql_validator as sql_validator


def send_prompt(prompt: str):
    """
    Send a prompt to Gemini.

    Returns the complete Gemini response object.
    """

    client = get_gemini_client()

    response = client.models.generate_content(
        model=get_model_name(),
        contents=prompt
    )

    return response


def get_response_text(response) -> str:
    """
    Extract text from the Gemini response.
    """

    if hasattr(response, "text") and response.text:
        return response.text

    raise ValueError(
        "Gemini returned an empty response."
    )


def extract_sql(response_text: str) -> str:
    """
    Extract SQL from Gemini's response.

    Removes Markdown code fences if present.
    """

    sql = response_text.strip()

    # Remove opening Markdown SQL fence
    sql = re.sub(
        r"```sql",
        "",
        sql,
        flags=re.IGNORECASE
    )

    # Remove closing Markdown fence
    sql = sql.replace(
        "```",
        ""
    )

    return sql.strip()


def clean_sql(sql: str) -> str:
    """
    Clean the generated SQL.
    """

    # Remove Windows carriage returns
    sql = sql.replace(
        "\r",
        ""
    )

    # Remove leading/trailing whitespace
    sql = sql.strip()

    return sql


def generate_sql(user_question: str) -> str:
    """
    Generate PostgreSQL SQL from
    a natural language question.
    """

    # Step 1: Build the prompt
    prompt = build_sql_prompt(
        user_question
    )

    # Step 2: Send prompt to Gemini
    response = send_prompt(
        prompt
    )

    # Step 3: Extract response text
    response_text = get_response_text(
        response
    )

    # Step 4: Extract SQL
    sql = extract_sql(
        response_text
    )

    # Step 5: Clean SQL
    sql = clean_sql(
        sql
    )

    # Step 6: Validate SQL
    sql_validator.validate_sql(
        sql
    )

    # Step 7: Return validated SQL
    return sql
