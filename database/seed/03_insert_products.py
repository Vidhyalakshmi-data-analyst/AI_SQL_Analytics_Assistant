"""
=================================================
File: 03_insert_products.py

Purpose:
    Generate realistic product data using predefined product
    catalogs and insert the records into the PostgreSQL
    Products table.

Author: Vidhyalakshmi
Project: AI SQL Analytics Assistant
=================================================
"""

import random

from database.connection.db_connection import get_connection

NUMBER_OF_PRODUCTS = 50

PRODUCT_CATALOG = {
    "Electronics": [
        ("Laptop", "Dell", "Computers"),
        ("Smartphone", "Samsung", "Mobiles"),
        ("Headphones", "Sony", "Audio"),
        ("Smart Watch", "Apple", "Wearables"),
        ("Bluetooth Speaker", "JBL", "Audio")
    ],

    "Fashion": [
        ("T-Shirt", "Nike", "Men"),
        ("Jeans", "Levi's", "Men"),
        ("Kurti", "Biba", "Women"),
        ("Jacket", "Puma", "Winter"),
        ("Hoodie", "Adidas", "Casual")
    ],

    "Furniture": [
        ("Office Chair", "Godrej", "Office"),
        ("Dining Table", "IKEA", "Dining"),
        ("Study Table", "Nilkamal", "Study"),
        ("Sofa", "Home Centre", "Living Room"),
        ("Bookshelf", "Durian", "Storage")
    ],

    "Books": [
        ("Python Programming", "O'Reilly", "Programming"),
        ("SQL Cookbook", "O'Reilly", "Database"),
        ("Atomic Habits", "Penguin", "Self Help"),
        ("Clean Code", "Pearson", "Programming"),
        ("The Psychology of Money", "Jaico", "Finance")
    ],

    "Sports": [
        ("Cricket Bat", "SG", "Cricket"),
        ("Football", "Nivia", "Football"),
        ("Badminton Racquet", "Yonex", "Badminton"),
        ("Yoga Mat", "Boldfit", "Fitness"),
        ("Dumbbells", "Kore", "Gym")
    ],

    "Beauty": [
        ("Face Wash", "Himalaya", "Skincare"),
        ("Shampoo", "Dove", "Hair Care"),
        ("Lipstick", "Lakme", "Cosmetics"),
        ("Perfume", "Fogg", "Fragrance"),
        ("Moisturizer", "Nivea", "Skincare")
    ],

    "Grocery": [
        ("Basmati Rice", "India Gate", "Rice"),
        ("Sunflower Oil", "Fortune", "Cooking Oil"),
        ("Sugar", "Madhur", "Essentials"),
        ("Tea Powder", "Tata Tea", "Beverages"),
        ("Coffee", "Bru", "Beverages")
    ],

    "Automotive": [
        ("Engine Oil", "Castrol", "Lubricants"),
        ("Car Shampoo", "3M", "Cleaning"),
        ("Helmet", "Steelbird", "Safety"),
        ("Car Cover", "AutoHub", "Accessories"),
        ("Tyre Inflator", "Michelin", "Tools")
    ]
}


def get_categories():
    """
    Fetch all categories from PostgreSQL.
    """

    connection = get_connection()

    if connection is None:
        return {}

    cursor = connection.cursor()

    cursor.execute("""
        SELECT category_id, category_name
        FROM categories;
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return {name: category_id for category_id, name in rows}

def generate_product(categories):
    """
    Generate one realistic product.
    """

    category_name = random.choice(list(PRODUCT_CATALOG.keys()))

    product_name, brand, sub_category = random.choice(
        PRODUCT_CATALOG[category_name]
    )

    return (
        categories[category_name],
        product_name,
        brand,
        sub_category,
        round(random.uniform(100, 50000), 2),
        random.randint(10, 500),
        True
    )


def generate_products(categories, count):
    """
    Generate multiple product records.
    """

    products = []

    for _ in range(count):
        products.append(generate_product(categories))

    return products

def insert_products(products):
    """
    Insert product records into the Products table.
    """

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO products (
        category_id,
        product_name,
        brand,
        sub_category,
        unit_price,
        stock_quantity,
        is_active
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    try:
        cursor.executemany(insert_query, products)

        connection.commit()

        print(f"✅ {cursor.rowcount} products inserted successfully!")

    except Exception as e:
        connection.rollback()

        print(f"Error inserting products: {e}")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":

    categories = get_categories()

    if not categories:
        print("No categories found. Please seed the Categories table first.")
    else:

        products = generate_products(
            categories,
            NUMBER_OF_PRODUCTS
        )

        print(f"\nGenerated {len(products)} products.\n")

        print("First 5 products:\n")

        for product in products[:5]:
            print(product)

        print("\nInserting products into PostgreSQL...\n")

        insert_products(products)

