## [QUESTION](https://leetcode.com/problems/find-customer-referee)
Given a table customer holding customers information and the referee. **Write a query to return the list of customers NOT referred by the person with id ‘2’.**

### SCHEMA
```SQL
CREATE TABLE IF NOT EXISTS customer (
    id INT,
    name VARCHAR(25),
    referee_id INT);

TRUNCATE TABLE customer;
INSERT INTO customer (id, name, referee_id) VALUES ('1', 'Will', null);
INSERT INTO customer (id, name, referee_id) VALUES ('2', 'Jane', null);
INSERT INTO customer (id, name, referee_id) VALUES ('3', 'Alex', '2');
INSERT INTO customer (id, name, referee_id) VALUES ('4', 'Bill', null);
INSERT INTO customer (id, name, referee_id) VALUES ('5', 'Zack', '1');
INSERT INTO customer (id, name, referee_id) VALUES ('6', 'Mark', '2');
```
### SOLUTION
1.
```SQL
SELECT
    name
FROM
    customer
WHERE 
    referee_id <> 2 OR referee_id IS NULL;
```
2.
```SQL
SELECT
    name
FROM
    customer
WHERE
    IFNULL(referee_id,-1) <> 2;
```