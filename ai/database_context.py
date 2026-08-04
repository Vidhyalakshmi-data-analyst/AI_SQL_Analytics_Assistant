"""
Database schema information for the AI assistant.

This module provides the complete PostgreSQL schema so that
Gemini can generate accurate SQL queries.
"""


def get_database_context():
    """
    Return the complete database context.
    """

    return f"""
{get_database_information()}

{get_tables_information()}

{get_relationship_information()}

{get_business_rules()}

{get_sql_rules()}
"""


def get_database_information():
    """
    Basic information about the database.
    """

    return """
Database Name:
AI SQL Analytics Assistant

Business Domain:
Retail Sales Analytics
"""


def get_tables_information():
    """
    Information about all database tables.
    """

    return """
Tables:

1. customers
Purpose: Stores customer information.

- customer_id (Primary Key)
- first_name
- last_name
- email
- phone
- date_of_birth
- gender
- city
- state
- country
- registration_date

2. categories
Purpose: Stores product categories.

- category_id (Primary Key)
- category_name
- description
- is_active

3. products
Purpose: Stores products available for sale.

- product_id (Primary Key)
- category_id (Foreign Key -> categories.category_id)
- product_name
- brand
- sub_category
- unit_price
- stock_quantity
- is_active

4. orders
Purpose: Stores customer orders.

- order_id (Primary Key)
- customer_id (Foreign Key -> customers.customer_id)
- order_date
- order_status
- subtotal
- discount_amount
- tax_amount
- total_amount
- shipping_address
- expected_delivery_date
- delivered_date

5. order_items
Purpose: Stores products included in each order.

- order_item_id (Primary Key)
- order_id (Foreign Key -> orders.order_id)
- product_id (Foreign Key -> products.product_id)
- quantity
- unit_price
- line_total

6. payments
Purpose: Stores payment information for orders.

- payment_id (Primary Key)
- order_id (Foreign Key -> orders.order_id)
- payment_method
- payment_status
- transaction_reference
- payment_date
- payment_amount

7. returns
Purpose: Stores returned order items.

- return_id (Primary Key)
- order_item_id (Foreign Key -> order_items.order_item_id)
- return_date
- return_reason
- refund_amount
- return_status
"""

def get_relationship_information():
    """
    Information about relationships between tables.
    """

    return """
Relationships:

1. customers.customer_id = orders.customer_id
One customer can place many orders.

2. categories.category_id = products.category_id
One category contains many products.

3. orders.order_id = order_items.order_id
One order contains many order items.

4. products.product_id = order_items.product_id
One product can appear in many order items.

5. orders.order_id = payments.order_id
Each order has one payment.

6. order_items.order_item_id = returns.order_item_id
One order item may have one return.
"""


def get_business_rules():
    """
    Business rules for SQL generation.
    """

    return """
Business Rules:

1. Revenue is calculated using orders.total_amount.

2. Cancelled orders should not be included when calculating revenue or sales.

3. Refunds are stored in returns.refund_amount.

4. One customer can place multiple orders.

5. One order can contain multiple products through the order_items table.

6. Products belong to one category.

7. Payments are associated with orders.

8. Returns are associated with individual order items, not entire orders.

9. Total sales should normally be calculated from completed (non-cancelled) orders.

10. Unless the user specifically requests otherwise, analytical queries should use active products and active categories.
"""


def get_sql_rules():
    """
    SQL generation rules.
    """

    return """
SQL Generation Rules:

1. Generate only PostgreSQL-compatible SQL.

2. Generate only SELECT queries.

3. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE or CREATE statements.

4. Use explicit JOIN clauses whenever data from multiple tables is required.

5. Always use meaningful table aliases.

6. Avoid SELECT * unless the user explicitly requests all columns.

7. Return only the SQL query without explanations, markdown or code fences.

8. Use aggregate functions such as SUM(), COUNT(), AVG(), MIN() and MAX() whenever appropriate.

9. Use ORDER BY when ranking or sorting results.

10. Apply LIMIT when the user requests top or bottom records.

11. Use GROUP BY whenever aggregate functions are used with non-aggregated columns.

12. Use the relationships provided in the database context for JOIN conditions.

13. Generate readable and properly formatted SQL.
"""