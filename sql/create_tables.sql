-- Retail Sales Business Intelligence Project
-- Database Table Creation Script


-- Drop existing tables (for re-running script)

DROP TABLE IF EXISTS sales_transactions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;


-- Customers Table

CREATE TABLE customers (

    customer_id INTEGER PRIMARY KEY,

    country VARCHAR(100)

);



-- Products Table

CREATE TABLE products (

    product_id INTEGER PRIMARY KEY,

    stock_code VARCHAR(50),

    description TEXT,

    unit_price DECIMAL(10,2)

);



-- Sales Transactions Table

CREATE TABLE sales_transactions (

    transaction_id INTEGER PRIMARY KEY,

    invoice_number VARCHAR(50),

    customer_id INTEGER,

    product_id INTEGER,

    quantity INTEGER,

    invoice_date DATE,

    revenue DECIMAL(10,2),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)

);
