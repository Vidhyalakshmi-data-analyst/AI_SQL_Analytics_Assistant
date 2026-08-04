"""
=================================================
File: prompt_builder.py

Purpose:
Build prompts that are sent to Gemini for different
AI tasks such as SQL generation, business insights,
chart explanations and report summaries.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from ai.database_context import get_database_context


def build_sql_prompt(user_question: str) -> str:
    """
    Build the prompt for SQL generation.
    """

    database_context = get_database_context()

    prompt = f"""

You are an expert PostgreSQL SQL developer and Business Data Analyst.

Your task is to convert business questions into accurate PostgreSQL SQL queries.

Always follow the provided database schema, relationships, business rules and SQL generation rules.


{database_context}

User Question:
{user_question}

Generate only executable PostgreSQL SQL.

Do not include explanations.

Do not include markdown.

Do not include code fences.

Do not include comments.

Return only the SQL query.
"""

    return prompt


def build_chart_prompt():
    """
    Placeholder.

    Will be implemented in Sprint 7.
    """

    raise NotImplementedError(
        "Chart prompt builder will be implemented in Sprint 7."
    )


def build_insight_prompt():
    """
    Placeholder.

    Will be implemented in Sprint 8.
    """

    raise NotImplementedError(
        "Insight prompt builder will be implemented in Sprint 8."
    )


def build_report_prompt():
    """
    Placeholder.

    Will be implemented in Sprint 9.
    """

    raise NotImplementedError(
        "Report prompt builder will be implemented in Sprint 9."
    )