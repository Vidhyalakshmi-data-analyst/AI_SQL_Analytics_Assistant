"""
=================================================
File: insight_generator.py

Purpose:
Analyze query results and generate verified
business insights.

Python performs the numerical analysis.
AI can later convert these verified findings
into natural-language business explanations.
=================================================
"""

import pandas as pd


def calculate_summary(
    dataframe: pd.DataFrame,
    numeric_column: str
) -> dict:
    """
    Calculate basic statistics for a numeric column.

    Returns:
        Dictionary containing total, average,
        minimum, and maximum values.
    """

    series = dataframe[numeric_column].dropna()

    if series.empty:
        return {}

    return {
        "total": series.sum(),
        "average": series.mean(),
        "minimum": series.min(),
        "maximum": series.max()
    }


def find_highest_value(
    dataframe: pd.DataFrame,
    category_column: str,
    numeric_column: str
) -> dict:
    """
    Find the category with the highest numeric value.
    """

    if dataframe.empty:
        return {}

    row = dataframe.loc[
        dataframe[numeric_column].idxmax()
    ]

    return {
        "category": row[category_column],
        "value": row[numeric_column]
    }


def find_lowest_value(
    dataframe: pd.DataFrame,
    category_column: str,
    numeric_column: str
) -> dict:
    """
    Find the category with the lowest numeric value.
    """

    if dataframe.empty:
        return {}

    row = dataframe.loc[
        dataframe[numeric_column].idxmin()
    ]

    return {
        "category": row[category_column],
        "value": row[numeric_column]
    }


def calculate_percentage_change(
    dataframe: pd.DataFrame,
    numeric_column: str
) -> float | None:
    """
    Calculate percentage change between the first
    and last values in a numeric series.

    Returns:
        Percentage change or None when it cannot
        be calculated.
    """

    series = dataframe[numeric_column].dropna()

    if len(series) < 2:
        return None

    first_value = series.iloc[0]
    last_value = series.iloc[-1]

    if first_value == 0:
        return None

    return (
        (last_value - first_value)
        / abs(first_value)
    ) * 100


def analyze_time_series(
    dataframe: pd.DataFrame,
    datetime_column: str,
    numeric_column: str
) -> dict:
    """
    Analyze a time-series DataFrame.

    Determines:
    - first period and value
    - last period and value
    - overall percentage change
    - highest period and value
    - lowest period and value
    - largest increase between consecutive periods
    - largest decrease between consecutive periods

    Returns:
        Dictionary containing verified time-series findings.
    """

    if dataframe is None or dataframe.empty:
        return {}

    required_columns = [
        datetime_column,
        numeric_column
    ]

    if not all(
        column in dataframe.columns
        for column in required_columns
    ):
        return {}

    working_dataframe = dataframe[
        required_columns
    ].copy()

    # Convert values safely
    working_dataframe[datetime_column] = pd.to_datetime(
        working_dataframe[datetime_column],
        errors="coerce"
    )

    working_dataframe[numeric_column] = pd.to_numeric(
        working_dataframe[numeric_column],
        errors="coerce"
    )

    # Remove invalid rows
    working_dataframe = working_dataframe.dropna(
        subset=[
            datetime_column,
            numeric_column
        ]
    )

    if len(working_dataframe) < 2:
        return {}

    # Sort chronologically
    working_dataframe = working_dataframe.sort_values(
        by=datetime_column
    ).reset_index(drop=True)

    dates = working_dataframe[datetime_column]
    values = working_dataframe[numeric_column]

    first_period = dates.iloc[0]
    last_period = dates.iloc[-1]

    first_value = values.iloc[0]
    last_value = values.iloc[-1]

    # Overall percentage change
    if first_value != 0:

        percentage_change = (
            (last_value - first_value)
            / abs(first_value)
        ) * 100

    else:

        percentage_change = None

    # Highest and lowest
    highest_index = values.idxmax()
    lowest_index = values.idxmin()

    highest_period = dates.loc[
        highest_index
    ]

    highest_value = values.loc[
        highest_index
    ]

    lowest_period = dates.loc[
        lowest_index
    ]

    lowest_value = values.loc[
        lowest_index
    ]

    # Period-to-period changes
    changes = values.diff()

    # Ignore first NaN
    valid_changes = changes.dropna()

    largest_increase = None
    largest_decrease = None

    if not valid_changes.empty:

        increase_index = valid_changes.idxmax()
        decrease_index = valid_changes.idxmin()

        increase_value = valid_changes.loc[
            increase_index
        ]

        decrease_value = valid_changes.loc[
            decrease_index
        ]

        if increase_value > 0:

            largest_increase = {
                "from_period": dates.iloc[
                    increase_index - 1
                ],
                "to_period": dates.iloc[
                    increase_index
                ],
                "change": increase_value
            }

        if decrease_value < 0:

            largest_decrease = {
                "from_period": dates.iloc[
                    decrease_index - 1
                ],
                "to_period": dates.iloc[
                    decrease_index
                ],
                "change": decrease_value
            }

    return {
        "first_period": first_period,
        "first_value": first_value,
        "last_period": last_period,
        "last_value": last_value,
        "percentage_change": percentage_change,
        "highest_period": highest_period,
        "highest_value": highest_value,
        "lowest_period": lowest_period,
        "lowest_value": lowest_value,
        "largest_increase": largest_increase,
        "largest_decrease": largest_decrease
    }


def generate_basic_insights(
    dataframe: pd.DataFrame
) -> dict:
    """
    Generate structured analytical findings from
    query results.

    The returned information contains verified
    numerical observations that can later be
    passed to Gemini for natural-language explanation.
    """

    if dataframe is None or dataframe.empty:

        return {
            "status": "no_data",
            "message": (
                "No data is available for analysis."
            )
        }

    # --------------------------------------------------
    # Detect numeric columns
    # --------------------------------------------------
    #
    # PostgreSQL results may sometimes arrive as
    # object/Decimal columns even when they contain
    # valid numeric values.
    #
    # Therefore:
    # 1. Detect normal numeric columns.
    # 2. Try safely converting other columns to numeric.
    # 3. Treat a column as numeric only when all
    #    non-null values can be converted.
    # --------------------------------------------------

    numeric_columns = []

    working_dataframe = dataframe.copy()

    for column in working_dataframe.columns:

        series = working_dataframe[column]

        # Already numeric
        if pd.api.types.is_numeric_dtype(series):

            numeric_columns.append(column)

            continue

        # Try converting object/Decimal values
        converted = pd.to_numeric(
            series,
            errors="coerce"
        )

        # Do not classify an empty column as numeric
        if (
            len(series) > 0
            and converted.notna().all()
        ):

            working_dataframe[column] = converted

            numeric_columns.append(column)

    # --------------------------------------------------
    # No numeric measure
    # --------------------------------------------------

    if not numeric_columns:

        return {
            "status": "no_numeric_data",
            "message": (
                "The query result does not contain "
                "numeric measures for analysis."
            )
        }

    # --------------------------------------------------
    # Select first numeric measure
    # --------------------------------------------------

    numeric_column = numeric_columns[0]

    # --------------------------------------------------
    # Calculate summary
    # --------------------------------------------------

    summary = calculate_summary(
        working_dataframe,
        numeric_column
    )

    insights = {
        "status": "success",
        "numeric_column": numeric_column,
        "summary": summary
    }

    # --------------------------------------------------
    # Find categorical columns
    # --------------------------------------------------

    categorical_columns = working_dataframe.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if categorical_columns:

        category_column = categorical_columns[0]

        insights["highest"] = find_highest_value(
            working_dataframe,
            category_column,
            numeric_column
        )

        insights["lowest"] = find_lowest_value(
            working_dataframe,
            category_column,
            numeric_column
        )

    # --------------------------------------------------
    # Calculate percentage change
    # --------------------------------------------------

    percentage_change = calculate_percentage_change(
        working_dataframe,
        numeric_column
    )

    if percentage_change is not None:

        insights["percentage_change"] = (
            percentage_change
        )

    return insights


def generate_insights(
    dataframe: pd.DataFrame
) -> str:
    """
    Generate a basic human-readable insight summary.
    """

    result = generate_basic_insights(
        dataframe
    )

    if result["status"] != "success":

        return result["message"]

    numeric_column = result["numeric_column"]

    summary = result["summary"]

    messages = [
        (
            f"{numeric_column} has a total of "
            f"{summary['total']:,.2f} and an average of "
            f"{summary['average']:,.2f}."
        )
    ]

    if "highest" in result:

        highest = result["highest"]

        messages.append(
            f"The highest value is "
            f"{highest['value']:,.2f}, recorded for "
            f"{highest['category']}."
        )

    if "lowest" in result:

        lowest = result["lowest"]

        messages.append(
            f"The lowest value is "
            f"{lowest['value']:,.2f}, recorded for "
            f"{lowest['category']}."
        )

    if "percentage_change" in result:

        change = result["percentage_change"]

        if change > 0:

            direction = "increased"

        elif change < 0:

            direction = "decreased"

        else:

            direction = "remained unchanged"

        if change == 0:

            messages.append(
                "The value remained unchanged "
                "from the first to the last observation."
            )

        else:

            messages.append(
                f"The value {direction} by "
                f"{abs(change):.2f}% from the first "
                f"to the last observation."
            )

    return "\n\n".join(messages)