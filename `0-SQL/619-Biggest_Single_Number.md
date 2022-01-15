## [QUESTION]()
Table number contains many numbers in column num including duplicated ones.<br>

Can you write a SQL query to find the biggest number, which only appears once.
### SCHEMA
```SQL
CREATE TABLE IF NOT EXISTS number (num int);
TRUNCATE TABLE number;

INSERT INTO number (num) VALUES ('8');
INSERT INTO number (num) VALUES ('8');
INSERT INTO number (num) VALUES ('3');
INSERT INTO number (num) VALUES ('3');
INSERT INTO number (num) VALUES ('1');
INSERT INTO number (num) VALUES ('4');
INSERT INTO number (num) VALUES ('5');
INSERT INTO number (num) VALUES ('6');
```

### Solution

1. WITH Statement
```SQL
WITH CTE AS(
    SELECT 
        num, 
        count(*) AS cnt
    FROM
        number
    GROUP BY
        num
    HAVING
        cnt = 1;
)
SELECT
    MAX(num) AS num
FROM
    CTE;
```

2. SUB Querry
```SQL
SELECT
    MAX(num) AS num
FROM
    (
        SELECT
            num,
            count(*) AS cnt
        FROM
            number
        GROUP BY
            num
        HAVING
            cnt = 1
    );
```