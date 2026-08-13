"""
=================================================
File: test_insight_integration.py

Purpose:
Perform one real end-to-end test of the AI insight
pipeline using Gemini.

This test makes a real Gemini API call and should
NOT be included in the regular unit-test suite.
=================================================
"""

import pandas as pd

from ai.insight_engine import generate_insight


def main():

    dataframe = pd.DataFrame({
        "category": [
            "Electronics",
            "Furniture",
            "Fashion"
        ],
        "sales": [
            50000,
            80000,
            60000
        ]
    })

    question = (
        "Which category has the highest sales "
        "and what is the overall sales performance?"
    )

    insight = generate_insight(
        dataframe,
        question
    )

    print("\n")
    print("=" * 60)
    print("AI GENERATED BUSINESS INSIGHT")
    print("=" * 60)
    print(insight)
    print("=" * 60)


if __name__ == "__main__":
    main()