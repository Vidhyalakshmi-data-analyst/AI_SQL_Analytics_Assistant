"""
=================================================
File: test_insight_engine.py

Purpose:
Unit tests for the insight engine.
=================================================
"""

import unittest
from unittest.mock import patch

import pandas as pd

from ai.insight_engine import (
    generate_insight
)


class TestInsightEngine(unittest.TestCase):

    @patch(
        "ai.insight_engine.generate_ai_insight"
    )
    @patch(
        "ai.insight_engine.build_insight_prompt"
    )
    @patch(
        "ai.insight_engine.generate_basic_insights"
    )
    def test_generate_insight(
        self,
        mock_generate_basic_insights,
        mock_build_insight_prompt,
        mock_generate_ai_insight
    ):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture"
            ],
            "sales": [
                500,
                800
            ]
        })

        question = (
            "Which category has the highest sales?"
        )

        findings = {
            "status": "success",
            "numeric_column": "sales",
            "highest": {
                "category": "Furniture",
                "value": 800
            }
        }

        mock_generate_basic_insights.return_value = (
            findings
        )

        mock_build_insight_prompt.return_value = (
            "Analyze these verified findings."
        )

        mock_generate_ai_insight.return_value = (
            "Furniture has the highest sales."
        )

        result = generate_insight(
            dataframe,
            question
        )

        self.assertEqual(
            result,
            "Furniture has the highest sales."
        )

        mock_generate_basic_insights.assert_called_once_with(
            dataframe
        )

        mock_build_insight_prompt.assert_called_once_with(
            question,
            findings
        )

        mock_generate_ai_insight.assert_called_once_with(
            "Analyze these verified findings."
        )


    @patch(
        "ai.insight_engine.generate_ai_insight"
    )
    @patch(
        "ai.insight_engine.build_insight_prompt"
    )
    @patch(
        "ai.insight_engine.generate_basic_insights"
    )
    def test_no_data(
        self,
        mock_generate_basic_insights,
        mock_build_insight_prompt,
        mock_generate_ai_insight
    ):

        dataframe = pd.DataFrame()

        mock_generate_basic_insights.return_value = {
            "status": "no_data",
            "message": (
                "No data is available for analysis."
            )
        }

        result = generate_insight(
            dataframe,
            "Analyze sales."
        )

        self.assertEqual(
            result,
            "No data is available for analysis."
        )

        mock_build_insight_prompt.assert_not_called()

        mock_generate_ai_insight.assert_not_called()


    @patch(
        "ai.insight_engine.generate_ai_insight"
    )
    @patch(
        "ai.insight_engine.build_insight_prompt"
    )
    @patch(
        "ai.insight_engine.generate_basic_insights"
    )
    def test_gemini_failure(
        self,
        mock_generate_basic_insights,
        mock_build_insight_prompt,
        mock_generate_ai_insight
    ):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture"
            ],
            "sales": [
                500,
                800
            ]
        })

        findings = {
            "status": "success",
            "numeric_column": "sales",
            "highest": {
                "category": "Furniture",
                "value": 800
            }
        }

        mock_generate_basic_insights.return_value = (
            findings
        )

        mock_build_insight_prompt.return_value = (
            "Analyze these verified findings."
        )

        mock_generate_ai_insight.side_effect = (
            Exception("Gemini API unavailable")
        )

        result = generate_insight(
            dataframe,
            "Analyze sales."
        )

        self.assertEqual(
            result,
            (
                "AI insights are temporarily "
                "unavailable. The query results "
                "and visualizations are still available."
            )
        )


    @patch(
        "ai.insight_engine.generate_ai_insight"
    )
    @patch(
        "ai.insight_engine.build_insight_prompt"
    )
    @patch(
        "ai.insight_engine.generate_basic_insights"
    )
    def test_prompt_failure(
        self,
        mock_generate_basic_insights,
        mock_build_insight_prompt,
        mock_generate_ai_insight
    ):

        dataframe = pd.DataFrame({
            "category": [
                "Electronics",
                "Furniture"
            ],
            "sales": [
                500,
                800
            ]
        })

        findings = {
            "status": "success",
            "numeric_column": "sales"
        }

        mock_generate_basic_insights.return_value = (
            findings
        )

        mock_build_insight_prompt.side_effect = (
            Exception("Prompt construction failed")
        )

        result = generate_insight(
            dataframe,
            "Analyze sales."
        )

        self.assertEqual(
            result,
            (
                "Unable to prepare AI insights "
                "for this result."
            )
        )

        mock_generate_ai_insight.assert_not_called()


if __name__ == "__main__":
    unittest.main()