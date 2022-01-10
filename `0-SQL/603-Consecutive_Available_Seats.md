## [QUESTION](https://leetcode.com/problems/consecutive-available-seats/)

### SCHEMA
```SQL
DROP TABLE IF EXISTS cinema;
CREATE TABLE IF NOT EXISTS cinema (
    seat_id int primary key AUTO_INCREMENT, 
    free bool);
TRUNCATE TABLE cinema;

INSERT INTO cinema (seat_id, free) VALUES ('1', '1');
INSERT INTO cinema (seat_id, free) VALUES ('2', '0');
INSERT INTO cinema (seat_id, free) VALUES ('3', '1');
INSERT INTO cinema (seat_id, free) VALUES ('4', '1');
INSERT INTO cinema (seat_id, free) VALUES ('5', '1');
```
### SOLUTION
1.
```SQL
SELECT
    DISTINCT c1.seat_id
FROM
    cinema c1 CROSS JOIN cinema c2
WHERE
    (c1.seat_id = c2.seat_id +1 OR c1.seat_id = c2.seat_id - 1) AND (c1.free = 1 AND c2.free = 1)
ORDER BY
    c1.seat_id;
```