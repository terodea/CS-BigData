## PSET: Flag Duplicates in a column.
#### Question: Set ﬂag column as True if other rows have a common property in tag column or Find Duplicate Records in a Tag column and mark them as True in flag column.

### Schema:
```SQL
CREATE TABLE IF NOT EXISTS items(
    id int,
    name varchar(25),
    tag varchar(25)
)
TRUNCATE TABLE items
INSERT INTO items(id, name, tag) VALUES (1, 'example', 'unique_tag');
INSERT INTO items(id, name, tag) VALUES (2, 'foo', 'simple');
INSERT INTO items(id, name, tag) VALUES (42, 'bar', 'simple');
INSERT INTO items(id, name, tag) VALUES (3, 'baz', 'hello');
INSERT INTO items(id, name, tag) VALUES (51, 'quux', 'world');
```
### DATA:
| id          | name        | tag           |
| :---        |    :----:   |          ---: |
| 1           | example     | unique_tag    |
| 2           | foo         | simple        |
| 42          | bar         | simple        |
| 3           | baz         | hello         |
| 51          | quux        | world         |

## Solutions:

### 1: SQL
```SQL
SELECT
    id, name, tag, COUNT(*) OVER (PARTITION BY tage) > 1 AS flag
GFROM
    items
```

```SQL
SELECT
    id, name, tag, COUNT(1) OVER (PARTITION BY tage) > 1 AS flag
FROM
    items
```
So your db doesn't support OVER and PARTITION, here's the alternative.

```SQL
SELECT
    id, name, tag, (
                        SELECT
                            COUNT(tag)
                        FROM
                            items B
                        WHERE
                            B.tag = A.tag
                    ) > 1 AS flag
FROM
    items A
```

### SQL Output:
| id          | name        | tag           | flag           |
| :---        |    :----:   | :---          |     :----:     |
| 1           | example     | unique_tag    |false           |
| 2           | foo         | simple        |true            |
| 42          | bar         | simple        |true            |
| 3           | baz         | hello         |false           |
| 51          | quux        | world         |false           |


### 2: PySpark
### 3: Pandas