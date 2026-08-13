"""
=================================================
File: test_insight_prompt.py

Purpose:
Unit tests for the insight prompt builder.
=================================================
"""

import unittest

from ai.insight_prompt import (
    build_insight_prompt
)


class TestInsightPrompt(unittest.TestCase):

    def test_build_insight_prompt(self):

        findings = {
            "status": "success",
            "numeric_column": "sales",
            "summary": {
                "total": 1000,
                "average": 333.33,
                "minimum": 200,
                "maximum": 500
            }
        }

        question = (
            "What is the overall sales performance?"
        )

        prompt = build_insight_prompt(
            question,
            findings
        )

        self.assertIsInstance(
            prompt,
            str
        )

        self.assertIn(
            question,
            prompt
        )

        self.assertIn(
            "sales",
            prompt
        )

        self.assertIn(
            "verified",
            prompt.lower()
        )


    def test_prompt_contains_business_instructions(self):

        findings = {
            "status": "success",
            "numeric_column": "sales",
            "summary": {
                "total": 1000
            }
        }

        prompt = build_insight_prompt(
            "Analyze sales.",
            findings
        )

        self.assertIn(
            "Do not invent",
            prompt
        )

        self.assertIn(
            "business",
            prompt.lower()
        )


    def test_empty_question(self):

        findings = {
            "status": "success"
        }

        with self.assertRaises(
            ValueError
        ):

            build_insight_prompt(
                "",
                findings
            )


    def test_whitespace_question(self):

        findings = {
            "status": "success"
        }

        with self.assertRaises(
            ValueError
        ):

            build_insight_prompt(
                "   ",
                findings
            )


    def test_empty_findings(self):

        with self.assertRaises(
            ValueError
        ):

            build_insight_prompt(
                "Analyze sales.",
                {}
            )


if __name__ == "__main__":
    unittest.main()