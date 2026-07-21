-- Sales table structure

CREATE TABLE sales (
    invoice_no VARCHAR(20),
    stock_code VARCHAR(20),
    description TEXT,
    quantity INTEGER,
    invoice_date DATETIME,
    unit_price DECIMAL(10,2),
    customer_id INTEGER,
    country VARCHAR(50)
);
