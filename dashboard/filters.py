"""
=================================================
File: filters.py

Purpose:
Define the dashboard filter context.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class FilterContext:
    """
    Store the filter selections applied to the dashboard.

    This class contains filter state only.

    Responsibility:
        Represent the current dashboard filter selections.
    """

    start_date: Optional[date] = None

    end_date: Optional[date] = None

    category: Optional[str] = None

    state: Optional[str] = None

    order_status: Optional[str] = None