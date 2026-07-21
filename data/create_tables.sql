
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    country TEXT,
    segment TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    description TEXT,
    category TEXT,
    unit_price REAL NOT NULL CHECK(unit_price >= 0)
);

CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    invoice_date TEXT NOT NULL,
    revenue REAL NOT NULL CHECK(revenue >= 0),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);

CREATE INDEX idx_transactions_customer_id ON transactions(customer_id);
CREATE INDEX idx_transactions_product_id ON transactions(product_id);
CREATE INDEX idx_transactions_invoice_date ON transactions(invoice_date);
