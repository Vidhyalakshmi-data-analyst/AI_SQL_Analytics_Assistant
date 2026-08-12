import unittest

import pandas as pd

from ai.chart_generator import (
    is_chartable,
    get_column_types,
    choose_chart_type,
    is_distribution_data,
    select_chart_columns,
    create_bar_chart,
    create_line_chart,
    create_pie_chart,
    generate_chart
)


class TestChartGenerator(unittest.TestCase):

    def test_chartable_dataframe(self):

        dataframe = pd.DataFrame({
            "category": ["A", "B", "C"],
            "sales": [100, 200, 300]
        })

        self.assertTrue(
            is_chartable(dataframe)
        )


    def test_single_column_dataframe(self):

        dataframe = pd.DataFrame({
            "sales": [100, 200, 300]
        })

        self.assertFalse(
            is_chartable(dataframe)
        )


    def test_empty_dataframe(self):

        dataframe = pd.DataFrame()

        self.assertFalse(
            is_chartable(dataframe)
        )


    def test_single_row_dataframe(self):

        dataframe = pd.DataFrame({
            "category": ["A"],
            "sales": [100]
        })

        self.assertFalse(
            is_chartable(dataframe)
        )


    def test_get_column_types(self):

        dataframe = pd.DataFrame({
            "category": ["A", "B", "C"],
            "sales": [100, 200, 300]
        })

        column_types = get_column_types(
            dataframe
        )

        self.assertEqual(
            column_types["categorical"],
            ["category"]
        )

        self.assertEqual(
            column_types["numeric"],
            ["sales"]
        )

        self.assertEqual(
            column_types["datetime"],
            []
        )


    def test_distribution_data(self):

        dataframe = pd.DataFrame({
            "status": [
            "Delivered",
            "Shipped",
            "Processing",
            "Cancelled"
            ],
            "count": [
                120,
                30,
                20,
                10
            ]
        })

        result = is_distribution_data(
            dataframe,
            "status",
            "count"
        )

        self.assertTrue(
            result
        )

    
    def test_distribution_too_many_categories(self):

        dataframe = pd.DataFrame({
            "category": [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
            ],
            "count": [
            10,
            20,
            30,
            40,
            50,
            60,
            70
            ]
        })

        result = is_distribution_data(
            dataframe,
            "category",
            "count"
        )

        self.assertFalse(
            result
        )

    def test_distribution_negative_values(self):

        dataframe = pd.DataFrame({
            "category": [
            "A",
            "B",
            "C"
            ],
            "count": [
            100,
            -20,
            50
            ]
        })

        result = is_distribution_data(
            dataframe,
            "category",
            "count"
        )

        self.assertFalse(
            result
        )

    def test_business_metric_is_not_distribution(self):

        dataframe = pd.DataFrame({
            "category": [
            "Fashion",
            "Electronics",
            "Home"
            ],
            
            "sales": [
            10000,
            15000,
            8000
            ]
        })

        result = is_distribution_data(
            dataframe,
            "category",
            "sales"
        )

        self.assertFalse(
            result
        )


    def test_select_datetime_and_numeric_columns(self):

        dataframe = pd.DataFrame({
            "month": pd.to_datetime([
            "2026-01-01",
            "2026-02-01",
            "2026-03-01"
            ]),
            "region": [
            "North",
            "South",
            "East"
            ],
            "sales": [
            100,
            200,
            300
            ],
            "profit": [
            20,
            40,
            60
            ]
        })

        column_types = get_column_types(
            dataframe
        )

        dimension_column, numeric_column = (
            select_chart_columns(
                dataframe,
                column_types
            )
        )

        self.assertEqual(
            dimension_column,
            "month"
        )

        self.assertEqual(
            numeric_column,
            "sales"
        )


    def test_select_categorical_and_numeric_columns(self):

        dataframe = pd.DataFrame({
            "category": [
            "Fashion",
            "Electronics",
            "Home"
            ],
            "sales": [
            10000,
            15000,
            8000
            ]
        })

        column_types = get_column_types(
            dataframe
        )

        dimension_column, numeric_column = (
            select_chart_columns(
            dataframe,
            column_types
            )
        )

        self.assertEqual(
            dimension_column,
            "category"
        )

        self.assertEqual(
            numeric_column,
            "sales"
        )

    def test_get_column_types_monthly_sales(self):

        dataframe = pd.DataFrame({
        "sales_month": [
            "2025-07-01",
            "2025-08-01",
            "2025-09-01"
        ],
        "total_sales": [
            "100000",
            "120000",
            "150000"
            ]
        })

        column_types = get_column_types(
            dataframe
        )

        self.assertEqual(
            column_types["datetime"],
            ["sales_month"]
        )

        self.assertEqual(
            column_types["numeric"],
            ["total_sales"]
        )

        self.assertEqual(
            column_types["categorical"],
            []
        )


    def test_select_no_chart_columns(self):

        dataframe = pd.DataFrame({
            "sales": [
            100,
            200,
            300
            ]
        })

        column_types = get_column_types(
            dataframe
        )

        dimension_column, numeric_column = (
            select_chart_columns(
                dataframe,
                column_types
            )
        )

        self.assertIsNone(
            dimension_column
        )

        self.assertIsNone(
            numeric_column
        )


    def test_choose_bar_chart(self):

        column_types = {
            "categorical": ["category"],
            "numeric": ["sales"],
            "datetime": []
        }

        chart_type = choose_chart_type(
            column_types
        )

        self.assertEqual(
            chart_type,
            "bar"
        )


    def test_choose_line_chart(self):

        column_types = {
            "categorical": [],
            "numeric": ["revenue"],
            "datetime": ["month"]
        }

        chart_type = choose_chart_type(
            column_types
        )

        self.assertEqual(
            chart_type,
            "line"
        )


    def test_no_suitable_chart(self):

        column_types = {
            "categorical": [],
            "numeric": ["sales"],
            "datetime": []
        }

        chart_type = choose_chart_type(
            column_types
        )

        self.assertIsNone(
            chart_type
        )


    def test_create_bar_chart(self):

        dataframe = pd.DataFrame({
            "category": [
                "Fashion",
                "Electronics",
                "Home"
            ],
            "sales": [
                10000,
                15000,
                8000
            ]
        })

        figure = create_bar_chart(
            dataframe,
            "category",
            "sales"
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.data[0].type,
            "bar"
        )


    def test_create_line_chart(self):

        dataframe = pd.DataFrame({
            "month": pd.to_datetime([
                "2026-01-01",
                "2026-02-01",
                "2026-03-01"
            ]),
            "revenue": [
                10000,
                12000,
                15000
            ]
        })

        figure = create_line_chart(
            dataframe,
            "month",
            "revenue"
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.data[0].type,
            "scatter"
        )


    def test_create_pie_chart(self):

        dataframe = pd.DataFrame({
            "status": [
                "Delivered",
                "Shipped",
                "Processing",
                "Cancelled"
            ],
            "count": [
                120,
                30,
                20,
                10
            ]
        })

        figure = create_pie_chart(
            dataframe,
            "status",
            "count"
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.data[0].type,
            "pie"
        )


    def test_generate_bar_chart(self):

        dataframe = pd.DataFrame({
            "category": [
            "Fashion",
            "Electronics",
            "Home"
            ],
            "sales": [
            10000,
            15000,
            8000
            ]
        })

        figure = generate_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.data[0].type,
            "bar"
        )

    def test_generate_line_chart(self):

        dataframe = pd.DataFrame({
            "month": pd.to_datetime([
            "2026-01-01",
            "2026-02-01",
            "2026-03-01"
            ]),
            "revenue": [
            10000,
            12000,
            15000
            ]
        })

        figure = generate_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.data[0].type,
            "scatter"
        )

    
    def test_generate_pie_chart(self):

        dataframe = pd.DataFrame({
            "status": [
            "Delivered",
            "Shipped",
            "Processing",
            "Cancelled"
            ],
            "count": [
            120,
            30,
            20,
            10
            ]
        })

        figure = generate_chart(
            dataframe
        )

        self.assertIsNotNone(
            figure
        )

        self.assertEqual(
            figure.data[0].type,
            "pie"
        )   

    def test_generate_no_chart(self):

        dataframe = pd.DataFrame({
            "sales": [
            100,
            200,
            300
            ]
        })

        figure = generate_chart(
            dataframe
        )

        self.assertIsNone(
            figure
        )


if __name__ == "__main__":
    unittest.main()