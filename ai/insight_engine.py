"""
=================================================
File: insight_engine.py

Purpose:
Coordinate the complete AI business insight
pipeline.

Pipeline:

DataFrame + User Question
        ↓
Verified Analysis
        ↓
Prompt Construction
        ↓
Gemini
        ↓
Business Insight

This module orchestrates the insight process.
=================================================
"""

import pandas as pd

from ai.insight_generator import (
    generate_basic_insights
)

from ai.insight_prompt import (
    build_insight_prompt
)

from ai.insight_client import (
    generate_ai_insight
)


def generate_insight(
    dataframe: pd.DataFrame,
    user_question: str
) -> str:
    """
    Generate an AI-powered business insight
    from query results.

    Parameters:
        dataframe:
            Query result DataFrame.

        user_question:
            Original business question.

    Returns:
        AI-generated business insight or a
        controlled fallback message.
    """

    # --------------------------------------------------
    # Step 1:
    # Generate verified analytical findings
    # --------------------------------------------------

    findings = generate_basic_insights(
        dataframe
    )

    # --------------------------------------------------
    # Step 2:
    # Stop if there is no usable data
    # --------------------------------------------------

    if findings.get("status") != "success":

        return findings.get(
            "message",
            "No insights could be generated."
        )

    # --------------------------------------------------
    # Step 3:
    # Build controlled Gemini prompt
    # --------------------------------------------------

    try:

        prompt = build_insight_prompt(
            user_question,
            findings
        )

    except Exception:

        return (
            "Unable to prepare AI insights "
            "for this result."
        )

    # --------------------------------------------------
    # Step 4:
    # Send prompt to Gemini
    # --------------------------------------------------

    try:

        insight = generate_ai_insight(
            prompt
        )

    except Exception:

        return (
            "AI insights are temporarily "
            "unavailable. The query results "
            "and visualizations are still available."
        )

    # --------------------------------------------------
    # Step 5:
    # Return final AI insight
    # --------------------------------------------------

    return insight