## [Question]()
Table point holds the x coordinate of some points on x-axis in a plane, which are all integers.<br>
Write a query to find the shortest distance between two points in these points.

### Schema
```SQL
DROP TABLE IF EXISTS point;

CREATE TABLE IF NOT ExISTS point (
    x INT NOT NULL, 
    UNIQUE INDEX x_UNIQUE (x ASC)
);

TRUNCATE TABLE point;
INSERT INTO point (x) VALUES ('-1');
INSERT INTO point (x) VALUES ('0');
INSERT INTO point (x) VALUES ('2');
```

### Solution
```SQL
SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM
    point p1, point p2
WHERE
    p1.x <> p2.x;
```