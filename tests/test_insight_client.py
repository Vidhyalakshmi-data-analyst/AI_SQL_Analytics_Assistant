"""
=================================================
File: test_insight_client.py

Purpose:
Unit tests for the Gemini insight client.
=================================================
"""

import unittest
from unittest.mock import patch, MagicMock

from ai.insight_client import (
    generate_ai_insight
)


class TestInsightClient(unittest.TestCase):

    @patch(
        "ai.insight_client.get_gemini_client"
    )
    @patch(
        "ai.insight_client.get_model_name"
    )
    def test_generate_ai_insight(
        self,
        mock_get_model_name,
        mock_get_gemini_client
    ):

        mock_get_model_name.return_value = (
            "test-model"
        )

        mock_response = MagicMock()

        mock_response.text = (
            "Sales increased by 20% "
            "during the period."
        )

        mock_client = MagicMock()

        mock_client.models.generate_content.return_value = (
            mock_response
        )

        mock_get_gemini_client.return_value = (
            mock_client
        )

        prompt = (
            "Analyze the sales performance."
        )

        result = generate_ai_insight(
            prompt
        )

        self.assertEqual(
            result,
            "Sales increased by 20% during the period."
        )

        mock_client.models.generate_content.assert_called_once_with(
            model="test-model",
            contents=prompt
        )


    @patch(
        "ai.insight_client.get_gemini_client"
    )
    def test_empty_prompt(
        self,
        mock_get_gemini_client
    ):

        with self.assertRaises(
            ValueError
        ):

            generate_ai_insight(
                ""
            )

        mock_get_gemini_client.assert_not_called()


    @patch(
        "ai.insight_client.get_gemini_client"
    )
    @patch(
        "ai.insight_client.get_model_name"
    )
    def test_empty_gemini_response(
        self,
        mock_get_model_name,
        mock_get_gemini_client
    ):

        mock_get_model_name.return_value = (
            "test-model"
        )

        mock_response = MagicMock()

        mock_response.text = ""

        mock_client = MagicMock()

        mock_client.models.generate_content.return_value = (
            mock_response
        )

        mock_get_gemini_client.return_value = (
            mock_client
        )

        with self.assertRaises(
            ValueError
        ):

            generate_ai_insight(
                "Analyze sales."
            )


if __name__ == "__main__":
    unittest.main()