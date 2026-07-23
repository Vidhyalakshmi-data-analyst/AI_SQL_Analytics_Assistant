"""
=================================================
File: 06_insert_payments.py

Purpose:
Generate realistic payment data and
insert it into the PostgreSQL Payments table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import random

from database.connection.db_connection import get_connection

import uuid
from datetime import timedelta

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

PAYMENT_STATUSES = {
    "Success": 90,
    "Pending": 5,
    "Failed": 3,
    "Refunded": 2
}

def get_orders():
    """
    Fetch order details required for payment generation.
    """

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            order_id,
            total_amount,
            order_status,
            order_date
        FROM orders;
    """)

    orders = cursor.fetchall()

    cursor.close()
    connection.close()

    return orders    

def generate_payment(order):
    """
    Generate one realistic payment record.
    """

    order_id, total_amount, order_status, order_date = order

    payment_method = random.choice(PAYMENT_METHODS)

    if order_status == "Cancelled":
        payment_status = random.choice([
        "Refunded",
        "Failed"
    ])

    elif order_status == "Processing":
        payment_status = random.choice([
        "Success",
        "Pending"
    ])

    else:
        payment_status = "Success"

    transaction_reference = (
    "TXN" +
    uuid.uuid4().hex[:10].upper()
    )

    payment_date = order_date + timedelta(
    minutes=random.randint(1, 60)
    )

    return (
        order_id,
        payment_method,
        payment_status,
        transaction_reference,
        payment_date,
        total_amount
    )

def generate_payments(orders):
    """
    Generate one payment for every order.
    """

    payments = []

    for order in orders:
        payments.append(
            generate_payment(order)
        )

    return payments

def insert_payments(payments):
    """
    Insert payment records into the Payments table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO payments (
        order_id,
        payment_method,
        payment_status,
        transaction_reference,
        payment_date,
        payment_amount
    )
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, payments)

        connection.commit()

        print(f"✅ {cursor.rowcount} payments inserted successfully!")

    except Exception as e:
        connection.rollback()

        print(f"Error inserting payments: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":

    orders = get_orders()

    if not orders:
        print("No orders found. Please seed the Orders table first.")

    else:

        payments = generate_payments(orders)

        print(f"\nGenerated {len(payments)} payments.\n")

        print("First 5 payments:\n")

        for payment in payments[:5]:
            print(payment)

        print("\nInserting payments into PostgreSQL...\n")

        insert_payments(payments)

