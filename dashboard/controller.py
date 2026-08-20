"""
=================================================
File: controller.py

Purpose:
Coordinate dashboard data retrieval.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import pandas as pd

from dashboard.filters import FilterContext
from dashboard.service import get_dashboard_data


def load_dashboard_data(
    filter_context: FilterContext
) -> pd.DataFrame:
    """
    Load dashboard data using the supplied
    filter context.

    Responsibility:
        Coordinate dashboard filter state with
        the dashboard data service.

    Parameters:
        filter_context:
            Current dashboard filter selections.

    Returns:
        Dashboard DataFrame.
    """

    return get_dashboard_data(
        filter_context
    )