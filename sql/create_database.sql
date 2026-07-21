-- Retail Sales Business Intelligence Project
-- Database Schema Creation

-- Create Customers Table

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    country TEXT
);


-- Create Products Table

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    stock_code TEXT,
    description TEXT,
    unit_price DECIMAL(10,2)
);


-- Create Sales Transactions Table

CREATE TABLE sales_transactions (

    transaction_id INTEGER PRIMARY KEY,

    invoice_number TEXT,

    customer_id INTEGER,

    product_id INTEGER,

    quantity INTEGER,

    invoice_date DATE,

    revenue DECIMAL(10,2),

    FOREIGN KEY(customer_id)
    REFERENCES customers(customer_id),

    FOREIGN KEY(product_id)
    REFERENCES products(product_id)

);
