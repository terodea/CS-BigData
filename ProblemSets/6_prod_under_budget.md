## PSET: Budget shopping.
#### Question: Write a query to find how manny products falls into customer budget along with list of products.

### DDL:
```SQL
CREATE TABLE IF NOT EXISTS products(
    product_id VARCHAR(20) ,
    cost INT
);
INSERT INTO products VALUES ('P1',200),('P2',300),('P3',500),('P4',800);

CREATE TABLE IF NOT EXISTS customer_budget(
    customer_id INT,
    budget INT
);

INSERT INTO customer_budget VALUES (100,400),(200,800),(300,1500);
```

### DATA:
1. products

| product_id  | cost        |
| :---        |    :----:   |
| P1          | 200         |
| P2          | 300         |
| P3          | 500         |
| P4          | 800         |
2. customer_budget

| customer_id  | budget      |
| :---         |    :----:   |
| 100          | 400         |
| 200          | 800         |
| 300          | 1500        |

## Solution:

### 1. SQL:
```SQL
WITH running_cost AS (
    SELECT 
        *,
        SUM(cost) OVER(ORDER BY cost ASC) AS r_cost
    FROM
        products
)
SELECT
    customer_id,
    budget,
    COUNT(1) AS no_of_products,
    STRING_AGG(product_id, ',') AS list_of_products
FROM
    customer_budget cb
LEFT JOIN
    running_cost rc
ON
    rc.r_cost < cb.budget
GROUP BY
    customer_id, budget;
```
| customer_id  | budget      | no_of_products  | list_of_products  |
| :---         |    :----:   |    :----:       |       ---:        |
| 100          | 400         |       1         |        P1         |
| 200          | 800         |       2         |       P1,P2       |
| 300          | 1500        |       3         |      P1,P2,P3     |

### 2. PySpark
### 3. Pandas