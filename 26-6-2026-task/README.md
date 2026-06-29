# PostgreSQL with Python - Orders CRUD

## Features

- PostgreSQL connection using psycopg2
- CRUD operations
- Transactions
- JSONB metadata
- SERIAL ID
- TIMESTAMP


## PostgreSQL vs MySQL


| Feature | MySQL | PostgreSQL |
|---|---|---|
| Auto Increment | AUTO_INCREMENT | SERIAL |
| JSON | JSON | JSON + JSONB |
| Driver | mysql connector | psycopg2 |
| Transactions | Supported | ACID focused |
| Timestamp | CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |


## Database

Table:

orders

Columns:

order_id SERIAL PRIMARY KEY
customer_name VARCHAR
product_name VARCHAR
amount DECIMAL
status VARCHAR DEFAULT PENDING
metadata JSONB
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP