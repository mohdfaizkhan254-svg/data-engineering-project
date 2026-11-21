-- Calculate total revenue per product

SELECT
    product_id,
    SUM(quantity * unit_price) AS total_revenue
FROM order_items
GROUP BY product_id
ORDER BY total_revenue DESC;