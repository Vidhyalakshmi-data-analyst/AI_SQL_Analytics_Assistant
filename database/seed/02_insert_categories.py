"""
=================================================
File: 02_insert_categories.py

Purpose:
Insert predefined product categories into the
PostgreSQL Categories table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

from datetime import date

from database.connection.db_connection import get_connection


CATEGORIES = [
    (
        "Electronics",
        "Electronic devices and accessories",
        True,
        date.today()
    ),
    (
        "Fashion",
        "Clothing, footwear and fashion accessories",
        True,
        date.today()
    ),
    (
        "Home & Kitchen",
        "Home appliances and kitchen essentials",
        True,
        date.today()
    ),
    (
        "Books",
        "Printed and digital books",
        True,
        date.today()
    ),
    (
        "Beauty",
        "Beauty and personal care products",
        True,
        date.today()
    ),
    (
        "Sports",
        "Sports and fitness equipment",
        True,
        date.today()
    ),
    (
        "Toys",
        "Toys and games for children",
        True,
        date.today()
    ),
    (
        "Grocery",
        "Daily grocery and food products",
        True,
        date.today()
    ),
    (
        "Furniture",
        "Home and office furniture",
        True,
        date.today()
    ),
    (
        "Automotive",
        "Vehicle accessories and maintenance products",
        True,
        date.today()
    )
]


def insert_categories():
    """
    Insert predefined categories into the Categories table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO categories (
        category_name,
        description,
        is_active,
        created_at
    )
    VALUES (%s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, CATEGORIES)

        connection.commit()

        print(f"✅ {cursor.rowcount} categories inserted successfully!")

    except Exception as e:
        connection.rollback()
        print(f"Error inserting categories: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":

    print(f"Total Categories: {len(CATEGORIES)}\n")

    print("Categories:\n")

    for category in CATEGORIES:
        print(category)

    print("\nInserting categories into PostgreSQL...\n")

    insert_categories()
