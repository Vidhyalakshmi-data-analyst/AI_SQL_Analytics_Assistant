"""
=================================================
File: insight_client.py

Purpose:
Send a prepared business-insight prompt to
Google Gemini and return the generated insight.

This module is responsible only for communicating
with the Gemini model.

It does NOT:
- analyze DataFrames
- calculate statistics
- build prompts
- generate SQL
- handle Streamlit UI
=================================================
"""

from ai.gemini_client import (
    get_gemini_client,
    get_model_name
)


def generate_ai_insight(
    prompt: str
) -> str:
    """
    Send a prepared insight prompt to Gemini
    and return the generated text.

    Parameters:
        prompt:
            Fully prepared insight-generation prompt.

    Returns:
        Generated business insight as a string.
    """

    if not prompt or not prompt.strip():

        raise ValueError(
            "Insight prompt cannot be empty."
        )

    client = get_gemini_client()

    response = client.models.generate_content(
        model=get_model_name(),
        contents=prompt
    )

    if hasattr(response, "text") and response.text:

        return response.text.strip()

    raise ValueError(
        "Gemini returned an empty insight response."
    )