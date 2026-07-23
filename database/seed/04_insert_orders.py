"""
=================================================
File: 04_insert_orders.py

Purpose:
Generate realistic customer order data and
insert it into the PostgreSQL Orders table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import random
from datetime import timedelta

from faker import Faker

from database.connection.db_connection import get_connection

fake = Faker("en_IN")

NUMBER_OF_ORDERS = 200

ORDER_STATUSES = {
    "Delivered": 70,
    "Shipped": 15,
    "Processing": 10,
    "Cancelled": 5
}

def get_customer_ids():
    """
    Fetch all customer IDs.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    cursor.execute("""
        SELECT customer_id
        FROM customers;
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return [row[0] for row in rows]

def generate_order(customer_ids):
    """
    Generate one realistic order record.
    """

    customer_id = random.choice(customer_ids)

    order_date = fake.date_time_between(
        start_date="-1y",
        end_date="now"
    )

    status = random.choices(
        population=list(ORDER_STATUSES.keys()),
        weights=list(ORDER_STATUSES.values()),
        k=1
    )[0]

    subtotal = round(
        random.uniform(500, 50000),
        2
    )

    discount_amount = round(
        subtotal * random.uniform(0, 0.20),
        2
    )

    tax_amount = round(
        (subtotal - discount_amount) * 0.18,
        2
    )

    total_amount = round(
        (subtotal - discount_amount) + tax_amount,
        2
    )

    shipping_address = (
        f"{fake.building_number()}, "
        f"{fake.street_name()}, "
        f"{fake.city()}, "
        f"{fake.state()}"
    )

    if status == "Cancelled":
        expected_delivery_date = None
        delivered_date = None

    else:
        expected_delivery_date = (
            order_date + timedelta(days=random.randint(3, 10))
        ).date()

        if status == "Delivered":
            delivered_date = (
                order_date + timedelta(days=random.randint(2, 10))
            ).date()

        else:
            delivered_date = None
            
    return (
        customer_id,
        order_date,
        status,
        subtotal,
        discount_amount,
        tax_amount,
        total_amount,
        shipping_address,
        expected_delivery_date,
        delivered_date
    )

def generate_orders(customer_ids, count):
    """
    Generate multiple order records.
    """

    orders = []

    for _ in range(count):
        orders.append(generate_order(customer_ids))

    return orders


def insert_orders(orders):
    """
    Insert order records into the Orders table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO orders (
        customer_id,
        order_date,
        order_status,
        subtotal,
        discount_amount,
        tax_amount,
        total_amount,
        shipping_address,
        expected_delivery_date,
        delivered_date
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, orders)

        connection.commit()

        print(f"✅ {cursor.rowcount} orders inserted successfully!")

    except Exception as e:
        connection.rollback()

        print(f"Error inserting orders: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":

    customer_ids = get_customer_ids()

    if not customer_ids:
        print("No customers found. Please seed the Customers table first.")

    else:

        orders = generate_orders(
            customer_ids,
            NUMBER_OF_ORDERS
        )

        print(f"\nGenerated {len(orders)} orders.\n")

        print("First 5 orders:\n")

        for order in orders[:5]:
            print(order)

        print("\nInserting orders into PostgreSQL...\n")

        insert_orders(orders)