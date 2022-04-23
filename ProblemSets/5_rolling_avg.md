## PSET: Rolling Averages.
#### Question: Write a query to get 7-day rolling (preceding) average of daily sign ups. Such that we end up with a table in the form below.

### Schema:
```SQL
CREATE TABLE IF NOT EXISTS transactions(
    date datetime,
    sign_ups int,
)
TRUNCATE TABLE transactions
INSERT INTO transactions(date, sign_ups) VALUES ("2018-01-01", 10);
INSERT INTO transactions(date, sign_ups) VALUES ("2018-01-02", 20);
INSERT INTO transactions(date, sign_ups) VALUES ("2018-01-03", 50);
INSERT INTO transactions(date, sign_ups) VALUES ("2018-01-04", 30);
INSERT INTO transactions(date, sign_ups) VALUES ("2018-01-05", 40);
```

### DATA:
| date        | sing_ups    |
| :---        |    :----:   |
| 2018-01-01  | 10          |
| 2018-01-02  | 20          |
| 2018-01-03  | 50          |
| 2018-01-04  | 30          |
| 2018-01-05  | 40          |

## Solutions:

### 1: SQL
```SQL
SELECT
    date, SUM(b.cashflow) as cumu_cashflow
FROM
    transactions a
INNER JOIN
    transactions b
ON
    a.date >= b.date
GROUP BY
    a.date
ORDER BY
    date ASC
```

```SQL
SELECT
    date, SUM(cashflow) OVER(ORDER BY date ASC) as cumu_cashflow
FROM
    transactions
ORDER BY date ASC
```

### SQL Output:
| date        | cashflow    |
| :---        |    :----:   |
| 2018-01-01  | -1000       |
| 2018-01-02  | -1100       |
| 2018-01-03  | -1050       |
| 2018-01-04  | -950        |
| 2018-01-05  | 4050        |


### 2: PySpark
### 3: Pandas

*Note: There are different ways to compute rolling/moving averages. Here we'll use a preceding average which means that the metric for the 7th day of the month would be the average of the preceding 6 days and that day itself.*