## PSET: Cummulative Sum for a column.
#### Question: Write a query to get cumulative cash flow for each day such that we end up with a table in the form below.
| date        | cashflow    |
| :---        |    :----:   |
| 2018-01-01  | -1000       |
| 2018-01-02  | -100        |
| 2018-01-03  | 50          |
| 2018-01-04  | 100         |
| 2018-01-05  | 5000        |

### Schema:
```SQL
CREATE TABLE IF NOT EXISTS transactions(
    date datetime,
    id int,
)
TRUNCATE TABLE transactions
INSERT INTO transactions(date, cashflow) VALUES ("2018-01-01", -1000);
INSERT INTO transactions(date, cashflow) VALUES ("2018-01-02", -100);
INSERT INTO transactions(date, cashflow) VALUES ("2018-01-03", 50);
INSERT INTO transactions(date, cashflow) VALUES ("2018-01-04", 100);
INSERT INTO transactions(date, cashflow) VALUES ("2018-01-05", 5000);
```
### DATA:
| date        | cashflow    |
| :---        |    :----:   |
| 2018-01-01  | -1000       |
| 2018-01-02  | -100        |
| 2018-01-03  | 50          |
| 2018-01-04  | 100         |
| 2018-01-05  | 5000        |

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