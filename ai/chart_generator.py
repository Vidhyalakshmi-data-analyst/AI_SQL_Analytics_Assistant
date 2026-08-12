"""
=================================================
File: chart_generator.py

Purpose:
Generate appropriate interactive visualizations
from query results.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""


import pandas as pd
import plotly.express as px


def is_chartable(dataframe: pd.DataFrame) -> bool:
    """
    Determine whether a DataFrame is suitable for visualization.

    A DataFrame is considered chartable when it contains:
    - At least 2 columns
    - At least 2 rows
    """

    if dataframe is None:
        return False

    if dataframe.empty:
        return False

    if len(dataframe.columns) < 2:
        return False

    if len(dataframe) < 2:
        return False

    return True


def get_column_types(dataframe: pd.DataFrame) -> dict:
    """
    Identify the type of each DataFrame column.

    Returns:
        Dictionary containing lists of:
        - categorical columns
        - numeric columns
        - datetime columns
    """

    categorical_columns = []
    numeric_columns = []
    datetime_columns = []

    for column in dataframe.columns:

        series = dataframe[column]

        # --------------------------------------------------
        # Datetime
        # --------------------------------------------------

        if pd.api.types.is_datetime64_any_dtype(series):

            datetime_columns.append(column)
            continue

        # --------------------------------------------------
        # Already numeric
        # --------------------------------------------------

        if pd.api.types.is_numeric_dtype(series):

            numeric_columns.append(column)
            continue

        # --------------------------------------------------
        # Try converting object values to numeric
        # --------------------------------------------------

        converted_numeric = pd.to_numeric(
            series,
            errors="coerce"
        )

        if (
            len(series) > 0
            and converted_numeric.notna().all()
        ):

            numeric_columns.append(column)
            continue

        # --------------------------------------------------
        # Try detecting date-like object columns
        # --------------------------------------------------

        converted_datetime = pd.to_datetime(
            series,
            errors="coerce"
        )

        column_name = column.lower()

        date_keywords = (
            "date",
            "month",
            "year",
            "time",
            "timestamp"
        )

        is_date_column_name = any(
            keyword in column_name
            for keyword in date_keywords
        )

        if (
            len(series) > 0
            and converted_datetime.notna().all()
            and is_date_column_name
        ):

            datetime_columns.append(column)
            continue

        # --------------------------------------------------
        # Otherwise categorical
        # --------------------------------------------------

        categorical_columns.append(column)

    return {
        "categorical": categorical_columns,
        "numeric": numeric_columns,
        "datetime": datetime_columns
    }


def choose_chart_type(
    column_types: dict
) -> str | None:
    """
    Determine the basic chart type based
    on detected column types.

    Returns:
        "bar", "line", or None.
    """

    categorical_columns = column_types["categorical"]
    numeric_columns = column_types["numeric"]
    datetime_columns = column_types["datetime"]

    # Time series → line chart
    if datetime_columns and numeric_columns:
        return "line"

    # Category + numeric → bar chart
    if categorical_columns and numeric_columns:
        return "bar"

    # No suitable chart
    return None

def is_distribution_data(
    dataframe: pd.DataFrame,
    categorical_column: str,
    numeric_column: str
) -> bool:
    """
    Determine whether the data represents
    a categorical distribution.

    Responsibility:
    Identify data suitable for a pie chart.

    Returns:
        True if the data is suitable for a
        distribution chart, otherwise False.
    """

    if dataframe.empty:
        return False

    unique_categories = (
        dataframe[categorical_column]
        .nunique()
    )

    if unique_categories < 2:
        return False

    if unique_categories > 6:
        return False

    # Distribution values should be non-negative.
    if (
        dataframe[numeric_column] < 0
    ).any():

        return False

    total = dataframe[numeric_column].sum()

    if total <= 0:
        return False

    # Check whether the numeric column name
    # indicates count/distribution data.
    distribution_keywords = [
        "count",
        "number",
        "num",
        "quantity",
        "orders",
        "customers",
        "users",
        "frequency",
        "total_count"
    ]

    numeric_column_name = (
        numeric_column.lower()
    )

    if any(
        keyword in numeric_column_name
        for keyword in distribution_keywords
    ):
        return True

    return False

def select_chart_columns(
    dataframe: pd.DataFrame,
    column_types: dict
) -> tuple[str | None, str | None]:
    """
    Select the most appropriate columns for visualization.

    Responsibility:
    Choose one category/datetime column and one
    numeric column for chart generation.

    Returns:
        Tuple containing:
        (dimension_column, numeric_column)

        Returns (None, None) when no suitable
        combination exists.
    """

    categorical_columns = column_types["categorical"]
    numeric_columns = column_types["numeric"]
    datetime_columns = column_types["datetime"]

    # Prefer datetime for time-series charts.
    if datetime_columns and numeric_columns:

        return (
            datetime_columns[0],
            numeric_columns[0]
        )

    # Otherwise use the first categorical
    # and numeric columns.
    if categorical_columns and numeric_columns:

        return (
            categorical_columns[0],
            numeric_columns[0]
        )

    return (
        None,
        None
    )

def create_bar_chart(
    dataframe: pd.DataFrame,
    category_column: str,
    numeric_column: str
    ):
    """
    Create an interactive bar chart.

    Responsibility:
    Create a Plotly bar chart from one
    categorical column and one numeric column.
    """

    figure = px.bar(
        dataframe,
        x=category_column,
        y=numeric_column,
        title=f"{numeric_column} by {category_column}",
        labels={
            category_column: category_column.replace(
                "_",
                " "
            ).title(),
            numeric_column: numeric_column.replace(
                "_",
                " "
            ).title()
        }
    )

    return figure

def create_line_chart(
    dataframe: pd.DataFrame,
    datetime_column: str,
    numeric_column: str
):
    """
    Create an interactive line chart.

    Responsibility:
    Create a Plotly line chart from one
    datetime column and one numeric column.
    """

    figure = px.line(
        dataframe,
        x=datetime_column,
        y=numeric_column,
        title=f"{numeric_column} over time",
        markers=True,
        labels={
            datetime_column: datetime_column.replace(
                "_",
                " "
            ).title(),
            numeric_column: numeric_column.replace(
                "_",
                " "
            ).title()
        }
    )

    return figure

def create_pie_chart(
    dataframe: pd.DataFrame,
    category_column: str,
    numeric_column: str
):
    """
    Create an interactive pie chart.

    Responsibility:
    Create a Plotly pie chart from one
    categorical column and one numeric column.
    """

    figure = px.pie(
        dataframe,
        names=category_column,
        values=numeric_column,
        title=f"{numeric_column} distribution by {category_column}"
    )

    return figure


def generate_chart(dataframe: pd.DataFrame):
    """
    Generate the most appropriate Plotly chart
    for the given DataFrame.

    Responsibility:
    Orchestrate the chart-generation pipeline.

    Returns:
        Plotly Figure if a suitable chart can be
        generated, otherwise None.
    """

    # Step 1: Check whether the data is chartable
    if not is_chartable(dataframe):
        return None

    # Step 2: Identify column types
    column_types = get_column_types(
        dataframe
    )

    # Step 3: Select chart columns
    dimension_column, numeric_column = (
        select_chart_columns(
            dataframe,
            column_types
        )
    )

    if (
        dimension_column is None
        or numeric_column is None
    ):
        return None

    # Step 4: Determine basic chart type
    chart_type = choose_chart_type(
        column_types
    )

    # Step 5: Handle time-series data
    if chart_type == "line":

        return create_line_chart(
            dataframe,
            dimension_column,
            numeric_column
        )

    # Step 6: Handle categorical data
    if chart_type == "bar":

        if is_distribution_data(
            dataframe,
            dimension_column,
            numeric_column
        ):

            return create_pie_chart(
                dataframe,
                dimension_column,
                numeric_column
            )

        return create_bar_chart(
            dataframe,
            dimension_column,
            numeric_column
        )

    return None