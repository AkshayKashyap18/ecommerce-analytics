SELECT
    c.name AS customer_name,
    c.city,
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    oi.item_price,
    o.total_amount,
    pay.status AS payment_status,
    pay.method AS payment_method
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
JOIN payments pay ON pay.order_id = o.order_id
ORDER BY o.order_date DESC;