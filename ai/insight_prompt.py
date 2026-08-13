"""
=================================================
File: insight_prompt.py

Purpose:
Build a controlled prompt for generating AI-powered
business insights from verified analytical findings.

This module does NOT call the AI model.

Responsibility:
Verified findings + user question
        ↓
Structured Gemini prompt
=================================================
"""

def build_insight_prompt(
    user_question: str,
    findings: dict
) -> str:
    """
    Build a prompt for Gemini using verified
    analytical findings.

    Parameters:
        user_question:
            Original business question asked by
            the user.

        findings:
            Verified analytical results generated
            by insight_generator.py.

    Returns:
        A structured prompt string.
    """

    if not user_question or not user_question.strip():

        raise ValueError(
            "User question cannot be empty."
        )

    if not findings:

        raise ValueError(
            "Analytical findings cannot be empty."
        )

    prompt = f"""
You are a business data analyst.

Analyze the verified findings provided below and
answer the user's business question.

IMPORTANT ANALYTICAL RULES:

- Do not describe differences between categories as
  increases or decreases unless the data represents
  a time sequence.

- For category comparisons, use phrases such as:
  "higher than", "lower than", "greater than",
  or "less than".

- Use "increased" or "decreased" only when there is
  a valid time/order dimension supporting a trend.

- Do not invent causes, explanations, or business
  reasons that are not supported by the provided data.

USER QUESTION:
{user_question.strip()}

VERIFIED ANALYTICAL FINDINGS:
{findings}

INSTRUCTIONS:

1. Base your response only on the verified findings.
2. Do not invent numbers, categories, trends, or causes.
3. Clearly identify important trends or comparisons.
4. Mention the most significant observation first.
5. Use concise and professional business language.
6. Explain the result in a way that is useful to a
   business decision-maker.
7. If the findings are insufficient to answer the
   question confidently, clearly state that.
8. Do not mention that you are an AI.
9. Do not repeat the entire dataset.
10. Keep the response concise, preferably 2–4 bullet points.

Return only the business insights.
"""

    return prompt.strip()