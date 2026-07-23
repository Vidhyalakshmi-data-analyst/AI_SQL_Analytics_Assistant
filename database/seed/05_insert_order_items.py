"""
=================================================
File: 05_insert_order_items.py

Purpose:
Generate realistic order item data and
insert it into the PostgreSQL Order_Items table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import random

from database.connection.db_connection import get_connection

NUMBER_OF_ORDER_ITEMS = 500

def get_order_ids():
    """
    Fetch all order IDs.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    cursor.execute("""
        SELECT order_id
        FROM orders;
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [row[0] for row in rows]


def get_products():
    """
    Fetch product details.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            product_id,
            unit_price,
            stock_quantity
        FROM products;
    """)

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products


def generate_order_item(order_ids, products):
    """
    Generate one realistic order item record.
    """

    order_id = random.choice(order_ids)

    product = random.choice(products)

    product_id, unit_price, stock_quantity = product

    quantity = random.randint(
        1,
        min(5, stock_quantity)
    )

    line_total = round(
        quantity * unit_price,
        2
    )

    return (
        order_id,
        product_id,
        quantity,
        unit_price,
        line_total
    )


def generate_order_items(order_ids, products, count):
    """
    Generate multiple unique order item records.
    """

    order_items = []

    used_pairs = set()

    while len(order_items) < count:

        order_item = generate_order_item(order_ids, products)

        order_id = order_item[0]
        product_id = order_item[1]

        pair = (order_id, product_id)

        if pair not in used_pairs:

            used_pairs.add(pair)

            order_items.append(order_item)

    return order_items

def insert_order_items(order_items):
    """
    Insert order item records into the Order_Items table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO order_items (
        order_id,
        product_id,
        quantity,
        unit_price,
        line_total
    )
    VALUES (%s, %s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, order_items)

        connection.commit()

        print(f"✅ {cursor.rowcount} order items inserted successfully!")

    except Exception as e:
        connection.rollback()

        print(f"Error inserting order items: {e}")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":

    order_ids = get_order_ids()

    products = get_products()

    if not order_ids:
        print("No orders found. Please seed the Orders table first.")

    elif not products:
        print("No products found. Please seed the Products table first.")

    else:

        order_items = generate_order_items(
            order_ids,
            products,
            NUMBER_OF_ORDER_ITEMS
        )

        print(f"\nGenerated {len(order_items)} order items.\n")

        print("First 5 order items:\n")

        for order_item in order_items[:5]:
            print(order_item)

        print("\nInserting order items into PostgreSQL...\n")

        insert_order_items(order_items)

        
