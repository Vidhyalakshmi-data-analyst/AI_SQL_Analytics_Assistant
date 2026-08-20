import unittest

import pandas as pd

from services.export_service import (
    dashboard_to_excel
)


class TestDashboardExportService(
    unittest.TestCase
):

    def setUp(self):

        self.dataframe = pd.DataFrame({
            "order_status": [
                "Delivered",
                "Delivered",
                "Cancelled"
            ],
            "category": [
                "Electronics",
                "Fashion",
                "Electronics"
            ],
            "state": [
                "Tamil Nadu",
                "Kerala",
                "Tamil Nadu"
            ],
            "product_name": [
                "Laptop",
                "Shirt",
                "Phone"
            ],
            "customer_name": [
                "Customer A",
                "Customer B",
                "Customer A"
            ],
            "line_total": [
                50000,
                10000,
                30000
            ]
        })

    def test_dashboard_to_excel(self):

        excel_data = dashboard_to_excel(
            self.dataframe
        )

        self.assertIsInstance(
            excel_data,
            bytes
        )

        self.assertGreater(
            len(excel_data),
            0
        )


if __name__ == "__main__":

    unittest.main()