"""
=================================================
File: kpi_generator.py

Purpose:
Calculate deterministic business KPIs from
query result DataFrames.

This module does not use Gemini or any other AI
service.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd


def generate_kpis(dataframe: pd.DataFrame) -> dict:
    """
    Generate business KPIs from a DataFrame.

    The KPI calculations are deterministic and are
    based only on the values present in the DataFrame.

    Returns:
        Dictionary containing available KPIs.
    """

    # --------------------------------------------------
    # Step 1: Validate DataFrame
    # --------------------------------------------------

    if dataframe is None or dataframe.empty:

        return {
            "status": "no_data",
            "message": (
                "No data is available for KPI calculation."
            ),
            "kpis": {}
        }

    # --------------------------------------------------
    # Step 2: Detect numeric columns
    #
    # Numeric-like object columns are also detected.
    # Datetime columns MUST be excluded before attempting
    # numeric conversion because Pandas can convert
    # datetime values into nanoseconds.
    # --------------------------------------------------

    numeric_columns = []

    for column in dataframe.columns:

        series = dataframe[column]

        # Never treat datetime columns as numeric
        if pd.api.types.is_datetime64_any_dtype(
            series
        ):
            continue

        # Already numeric
        if pd.api.types.is_numeric_dtype(series):

            numeric_columns.append(column)
            continue

        # Try converting non-datetime object values
        # to numeric.
        converted = pd.to_numeric(
            series,
            errors="coerce"
        )

        if (
            len(series) > 0
            and converted.notna().all()
        ):
            numeric_columns.append(column)

    # --------------------------------------------------
    # Step 3: No numeric measure available
    # --------------------------------------------------

    if not numeric_columns:

        return {
            "status": "no_numeric_data",
            "message": (
                "The query result does not contain "
                "numeric measures for KPI calculation."
            ),
            "kpis": {}
        }

    # --------------------------------------------------
    # Step 4: Select primary measure
    # --------------------------------------------------

    measure_column = numeric_columns[0]

    # Convert the selected measure to numeric.
    #
    # This safely handles numeric values stored as
    # strings/object dtype.
    series = pd.to_numeric(
        dataframe[measure_column],
        errors="coerce"
    ).dropna()

    # --------------------------------------------------
    # Step 5: Validate usable numeric values
    # --------------------------------------------------

    if series.empty:

        return {
            "status": "no_numeric_data",
            "message": (
                "The numeric measure does not contain "
                "usable values."
            ),
            "kpis": {}
        }

    # --------------------------------------------------
    # Step 6: Basic KPIs
    # --------------------------------------------------

    kpis = {
        "measure": measure_column,

        "total": float(
            series.sum()
        ),

        "average": float(
            series.mean()
        ),

        "maximum": float(
            series.max()
        ),

        "minimum": float(
            series.min()
        ),

        "count": int(
            series.count()
        )
    }

    # --------------------------------------------------
    # Step 7: Detect categorical + numeric result
    # --------------------------------------------------

    categorical_columns = []

    for column in dataframe.columns:

        # The selected measure cannot be categorical.
        if column == measure_column:
            continue

        series_column = dataframe[column]

        # Datetime columns are handled separately.
        if pd.api.types.is_datetime64_any_dtype(
            series_column
        ):
            continue

        # Genuine numeric columns are not categorical.
        if pd.api.types.is_numeric_dtype(
            series_column
        ):
            continue

        # Check whether an object column is actually
        # numeric-like.
        converted = pd.to_numeric(
            series_column,
            errors="coerce"
        )

        if (
            len(series_column) > 0
            and converted.notna().all()
        ):
            continue

        categorical_columns.append(column)

    # --------------------------------------------------
    # Step 8: Highest and lowest category
    # --------------------------------------------------

    if categorical_columns:

        category_column = categorical_columns[0]

        max_index = series.idxmax()
        min_index = series.idxmin()

        kpis["category_column"] = (
            category_column
        )

        kpis["highest"] = {
            "category": str(
                dataframe.loc[
                    max_index,
                    category_column
                ]
            ),
            "value": float(
                series.loc[max_index]
            )
        }

        kpis["lowest"] = {
            "category": str(
                dataframe.loc[
                    min_index,
                    category_column
                ]
            ),
            "value": float(
                series.loc[min_index]
            )
        }

        kpis["category_count"] = int(
            dataframe[
                category_column
            ].nunique()
        )

    # --------------------------------------------------
    # Step 9: Detect datetime + numeric result
    # --------------------------------------------------

    datetime_columns = []

    for column in dataframe.columns:

        series_column = dataframe[column]

        if pd.api.types.is_datetime64_any_dtype(
            series_column
        ):
            datetime_columns.append(
                column
            )

    if datetime_columns:

        date_column = datetime_columns[0]

        max_index = series.idxmax()
        min_index = series.idxmin()

        kpis["datetime_column"] = (
            date_column
        )

        kpis["highest_period"] = {
            "period": str(
                dataframe.loc[
                    max_index,
                    date_column
                ]
            ),
            "value": float(
                series.loc[max_index]
            )
        }

        kpis["lowest_period"] = {
            "period": str(
                dataframe.loc[
                    min_index,
                    date_column
                ]
            ),
            "value": float(
                series.loc[min_index]
            )
        }

        kpis["period_count"] = int(
            dataframe[
                date_column
            ].nunique()
        )

        # --------------------------------------------------
        # Percentage change only for time-series data
        # --------------------------------------------------

        if len(series) >= 2:

            first_value = float(
                series.iloc[0]
            )

            last_value = float(
                series.iloc[-1]
            )

            if first_value != 0:

                kpis["percentage_change"] = (
                    (
                        last_value - first_value
                    )
                    / abs(first_value)
                ) * 100

    # --------------------------------------------------
    # Step 10: Return successful result
    # --------------------------------------------------

    return {
        "status": "success",
        "message": (
            "KPIs generated successfully."
        ),
        "kpis": kpis
    }