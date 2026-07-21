-- Top products by quantity sold

SELECT
    description,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY description
ORDER BY total_quantity DESC
LIMIT 10;


-- Revenue by country

SELECT
    country,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY country
ORDER BY revenue DESC;


-- Monthly revenue trend

SELECT
    strftime('%Y-%m', invoice_date) AS month,
    SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY month
ORDER BY month;
