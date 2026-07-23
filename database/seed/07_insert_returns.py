"""
=================================================
File: 07_insert_returns.py

Purpose:
Generate realistic product return data and
insert it into the PostgreSQL Returns table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import random
from datetime import timedelta

from database.connection.db_connection import get_connection

RETURN_RATE = 0.08

RETURN_REASONS = [
    "Damaged Product",
    "Wrong Item Delivered",
    "Defective Product",
    "Quality Not as Expected",
    "Changed Mind",
    "Size Issue"
]

RETURN_STATUSES = [
    "Requested",
    "Approved",
    "Refunded"
]

def get_order_items():
    """
    Fetch order item details required for return generation.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            order_item_id,
            line_total,
            created_at
        FROM order_items;
    """)

    order_items = cursor.fetchall()

    cursor.close()
    connection.close()

    return order_items

def generate_return(order_item):
    """
    Generate one realistic return record.
    """

    order_item_id, line_total, created_at = order_item

    return_date = (
    created_at +
    timedelta(days=random.randint(3, 30))
    ).date()

    return_reason = random.choice(
    RETURN_REASONS
    )

    return_status = random.choices(
    population=RETURN_STATUSES,
    weights=[10, 20, 70],
    k=1
    )[0]

    refund_amount = line_total

    return (
    order_item_id,
    return_date,
    return_reason,
    refund_amount,
    return_status
    )

def generate_returns(order_items):
    """
    Generate realistic return records based on RETURN_RATE.
    """

    number_of_returns = max(
        1,
        int(len(order_items) * RETURN_RATE)
    )

    selected_order_items = random.sample(
        order_items,
        number_of_returns
    )

    returns = []

    for order_item in selected_order_items:
        returns.append(
            generate_return(order_item)
        )

    return returns

def insert_returns(returns):
    """
    Insert return records into the Returns table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO returns (
        order_item_id,
        return_date,
        return_reason,
        refund_amount,
        return_status
    )
    VALUES (%s, %s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, returns)

        connection.commit()

        print(f"✅ {cursor.rowcount} returns inserted successfully!")

    except Exception as e:
        connection.rollback()

        print(f"Error inserting returns: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":

    order_items = get_order_items()

    if not order_items:
        print("No order items found. Please seed the Order Items table first.")

    else:

        returns = generate_returns(order_items)

        print(f"\nGenerated {len(returns)} returns.\n")

        print("First 5 returns:\n")

        for return_record in returns[:5]:
            print(return_record)

        print("\nInserting returns into PostgreSQL...\n")

        insert_returns(returns)