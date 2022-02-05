## [QUESTION] (https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)

### SCHEMA
```SQL
DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS orders (
    order_number int,
    customer_number int,
    order_date date,
    required_date date,
    shipped_date date,
    status char(15),
    comment char(200),
    key(order_number)
);

TRUNCATE TABLE orders;
INSERT INTO orders (order_number, customer_number) VALUES ('1', '1');
INSERT INTO orders (order_number, customer_number) VALUES ('2', '2');
INSERT INTO orders (order_number, customer_number) VALUES ('3', '3');
INSERT INTO orders (order_number, customer_number) VALUES ('4', '3');
```

### SOLUTIONS

1. BASIC
```SQL
WITH orderCount AS(
    SELECT
        customer_number, COUNT(DISTINCT(order_number)) AS cnt
    FROM
        orders
    GROUP BY
        customer_number
    ORDER BY
        cnt DESC
)
SELECT
    customer_number
FROM
    CTE
LIMIT 1;
```
What if multiple customers have same count of orders ?
2. Follow Up
```SQL
SELECT
    customer_number
FROM
    orders
GROUP BY customer_number
HAVING COUNT(order_number) = (
    SELECT 
        MAX(order_count)
    FROM
        (
            SELECT
                COUNT(order_number) order_count
            FROM
                orders
            GROUP BY customer_number
        ) a
)
```