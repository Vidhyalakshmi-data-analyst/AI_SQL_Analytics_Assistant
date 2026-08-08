"""
=================================================
File: models.py

Purpose:
Data models shared across the AI backend.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""


"""
=================================================
File: models.py

Purpose:
Data models shared across the AI backend.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from dataclasses import dataclass

import pandas as pd


@dataclass
class QueryResult:
    """
    Represents the complete result returned
    by the Query Engine.
    """

    sql: str

    dataframe: pd.DataFrame