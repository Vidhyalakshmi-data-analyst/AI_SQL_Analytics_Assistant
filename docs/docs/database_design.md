# Database Design

## Primary Keys

| Table | Primary Key |
|---------|-------------|
| Customers | customer_id |
| Products | product_id |
| Categories | category_id |
| Orders | order_id |
| Order Items | order_item_id |
| Payments | payment_id |
| Shipments | shipment_id |
| Returns | return_id |
| Employees | employee_id |
| Stores | store_id |


---

# Foreign Keys

| Table | Foreign Key | References |
|---------|------------|------------|
| Orders | customer_id | Customers |
| Products | category_id | Categories |
| Order Items | order_id | Orders |
| Order Items | product_id | Products |
| Payments | order_id | Orders |
| Shipments | order_id | Orders |
| Returns | order_item_id | Order Items |
| Employees | store_id | Stores |

---

# Relationships

| Relationship | Type |
|--------------|------|
| Customers → Orders | One-to-Many |
| Categories → Products | One-to-Many |
| Orders → Order Items | One-to-Many |
| Products → Order Items | One-to-Many |
| Orders → Payments | One-to-One |
| Orders → Shipments | One-to-One |
| Stores → Employees | One-to-Many |

---

## Many-to-Many Relationship

Customers and Products have a Many-to-Many relationship.

This is implemented using:

Customers
→ Orders
→ Order Items
→ Products

# Customers Table

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| customer_id | SERIAL | PRIMARY KEY | Unique customer identifier |
| first_name | VARCHAR(50) | NOT NULL | Customer first name |
| last_name | VARCHAR(50) | NOT NULL | Customer last name |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Customer email |
| phone | VARCHAR(15) | | Mobile number |
| date_of_birth | DATE | | Date of birth |
| gender | VARCHAR(20) | | Gender |
| city | VARCHAR(100) | | Customer city |
| state | VARCHAR(100) | | Customer state |
| country | VARCHAR(100) | | Customer country |
| registration_date | DATE | NOT NULL | Account creation date |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation timestamp |
---

# Categories Table

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| category_id | INTEGER | PRIMARY KEY | Unique category identifier |
| category_name | VARCHAR(100) | UNIQUE, NOT NULL | Category name |
| description | VARCHAR(255) | | Brief description of the category |
| is_active | BOOLEAN | NOT NULL | Indicates whether the category is active or inactive |
| created_at | DATE | NOT NULL | Date the category was created |

---

# Products Table

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| product_id | SERIAL | PRIMARY KEY | Unique product identifier |
| category_id | INT | NOT NULL, FOREIGN KEY | References Categories(category_id) |
| product_name | VARCHAR(150) | NOT NULL | Name of the product |
| brand | VARCHAR(100) | NOT NULL | Product brand |
| sub_category | VARCHAR(100) | NOT NULL | Product sub-category |
| unit_price | DECIMAL(10,2) | NOT NULL | Selling price |
| stock_quantity | INT | NOT NULL | Current stock available |
| is_active | BOOLEAN | DEFAULT TRUE | Product availability |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation date |


# Orders Table

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| order_id | INTEGER | PRIMARY KEY | Unique order identifier |
| customer_id | INTEGER | FOREIGN KEY REFERENCES Customers(customer_id), NOT NULL | Customer who placed the order |
| order_date | TIMESTAMP | NOT NULL | Date and time the order was placed |
| order_status | VARCHAR(30) | NOT NULL | Current order status (Pending, Shipped, Delivered, Cancelled) |
| subtotal | DECIMAL(10,2) | NOT NULL | Total before tax and discount |
| discount_amount | DECIMAL(10,2) | DEFAULT 0 | Discount applied to the order |
| tax_amount | DECIMAL(10,2) | DEFAULT 0 | Tax charged |
| total_amount | DECIMAL(10,2) | NOT NULL | Final amount paid |
| shipping_address | VARCHAR(255) | NOT NULL | Delivery address |
| expected_delivery_date | DATE | | Estimated delivery date |
| delivered_date | DATE | | Actual delivery date |
| created_at | TIMESTAMP | NOT NULL | Record creation timestamp |

---

# Order Items Table

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| order_item_id | INTEGER | PRIMARY KEY | Unique order item identifier |
| order_id | INTEGER | FOREIGN KEY REFERENCES Orders(order_id), NOT NULL | Associated order |
| product_id | INTEGER | FOREIGN KEY REFERENCES Products(product_id), NOT NULL | Purchased product |
| quantity | INTEGER | NOT NULL | Quantity purchased |
| unit_price | DECIMAL(10,2) | NOT NULL | Product price at the time of purchase |
| line_total | DECIMAL(10,2) | NOT NULL | Quantity × Unit Price |
| created_at | TIMESTAMP | NOT NULL | Record creation timestamp |


---

# Payments Table

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| payment_id | INTEGER | PRIMARY KEY | Unique payment identifier |
| order_id | INTEGER | FOREIGN KEY REFERENCES Orders(order_id), UNIQUE, NOT NULL | Associated order |
| payment_method | VARCHAR(30) | NOT NULL | UPI, Credit Card, Debit Card, Net Banking, COD |
| payment_status | VARCHAR(20) | NOT NULL | Success, Failed, Pending, Refunded |
| transaction_reference | VARCHAR(100) | UNIQUE | Payment gateway transaction reference |
| payment_date | TIMESTAMP | NOT NULL | Date and time of payment |
| payment_amount | DECIMAL(10,2) | NOT NULL | Amount paid |
| created_at | TIMESTAMP | NOT NULL | Record creation timestamp |


---

# Returns Table

| Column | Data Type | Constraints | Description |
|----------|-----------|-------------|-------------|
| return_id | INTEGER | PRIMARY KEY | Unique return identifier |
| order_item_id | INTEGER | FOREIGN KEY REFERENCES Order_Items(order_item_id), NOT NULL | Returned order item |
| return_date | DATE | NOT NULL | Date the item was returned |
| return_reason | VARCHAR(255) | NOT NULL | Reason for the return |
| refund_amount | DECIMAL(10,2) | NOT NULL | Amount refunded |
| return_status | VARCHAR(20) | NOT NULL | Requested, Approved, Rejected, Refunded |
| created_at | TIMESTAMP | NOT NULL | Record creation timestamp |

