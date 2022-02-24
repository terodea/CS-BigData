## PSET: Month over month percentage change 
#### Question: Find the month-over-month percentage change for monthly active users (MAU)

## 1. SQL
```SQL
WITH mau AS(
    SELECT
        MONTH(date) AS month_timestamp, COUNT(DISTINCT user_id) AS mau
    FROM
        logins
    GROUP BY
        MONTH(date)
)

SELECT
    a.month_timestamp AS previoud_month,
    a.mau AS previoud_mau
    b.month_timestamp AS current_month,
    b.mau AS current_mau
    ROUND(100.0 * (b.mau - a.mau) / a.mau, 2) AS percentage_change
FROM
    mau a JOIN mau b
ON
    a.month_timestamp = b.month_timestamp - INTERVAL 1 MONTH;
```
## 2. PySpark

## 3. Pandas