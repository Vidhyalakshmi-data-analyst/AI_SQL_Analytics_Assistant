"""
=================================================
File: 01_insert_customers.py

Purpose:
Generate realistic customer data using Faker and
insert it into the PostgreSQL Customers table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""


import random

from faker import Faker

from database.connection.db_connection import get_connection


fake = Faker("en_IN")

NUMBER_OF_CUSTOMERS = 50


GENDERS = [
    "Male",
    "Female",
    "Other"
]


def generate_customer():
    """
    Generate one realistic customer record.
    """

    return (
        fake.first_name(),
        fake.last_name(),
        fake.unique.email(),
        fake.phone_number(),
        fake.date_of_birth(minimum_age=18, maximum_age=75),
        random.choice(GENDERS),
        fake.city(),
        fake.state(),
        "India",
        fake.date_between(start_date="-5y", end_date="today")
    )

def generate_customers(count):
    """
    Generate multiple customer records.
    """

    customers = []

    for _ in range(count):
        customers.append(generate_customer())

    return customers


def insert_customers(customers):
    """
    Insert customer records into the Customers table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO customers (
        first_name,
        last_name,
        email,
        phone,
        date_of_birth,
        gender,
        city,
        state,
        country,
        registration_date
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, customers)

        connection.commit()

        print(f"✅ {cursor.rowcount} customers inserted successfully!")

    except Exception as e:
        connection.rollback()
        print(f"Error inserting customers: {e}")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":

    customers = generate_customers(NUMBER_OF_CUSTOMERS)

    print(f"\nGenerated {len(customers)} customers.\n")

    print("First 5 customers:\n")

    for customer in customers[:5]:
        print(customer)

    print("\nInserting customers into PostgreSQL...\n")

    insert_customers(customers)