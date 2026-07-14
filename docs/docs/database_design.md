# Database Design

## Customers Table

| Column | Description |
|---------|-------------|
| customer_id | Unique customer identifier |
| full_name | Customer full name |
| email | Email address |
| phone | Mobile number |
| date_of_birth | Customer DOB |
| gender | Male/Female/Other |
| city | Customer city |
| state | Customer state |
| registration_date | Account creation date |


---

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
| customer_id | INTEGER | PRIMARY KEY | Unique customer identifier |
| full_name | VARCHAR(100) | NOT NULL | Customer full name |
| email | VARCHAR(255) | UNIQUE, NOT NULL | Customer email |
| phone | VARCHAR(15) | | Mobile number |
| date_of_birth | DATE | | Date of birth |
| gender | VARCHAR(20) | | Gender |
| city | VARCHAR(100) | | Customer city |
| state | VARCHAR(100) | | Customer state |
| registration_date | DATE | NOT NULL | Account creation date |