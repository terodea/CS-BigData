## PSET: Deduplicate the records and sort on the basis of c1 column (i.e comparative sort) element inserted first should come first. TLDR; Sort by initial entry but get latest record.

### Data: my_table
| id          | c1        | c2      |
| :---        |  :----:   |  ---:   |
| 1           |     v1    | 100     |
|2            |     v2    | 150     |
|3            |     v1    | 50      |
|4            |     v3    | 10      |
|5            |     v2    | 200     |
|6            |     v2    | 100     |

### Output:
| id          | c1        | c2      |
| :---        |  :----:   |  ---:   |
|      3      |     v1    |    50   |
|      6      |     v2    |   100   |
|      4      |     v3    |    10   |


### Solution:
1. MySQL
```SQL
WITH cte_rank AS (
    SELECT
        id, c1, c2, ROW_NUMBER() over(PARTITION BY c1 ORDER BY id DESC) as duplicate_rank
    FROM my_table
)
cte_distinct_order AS (
    SELECT
        DISTINCT(c1) AS c1 FROM my_table
)

SELECT 
	id, cdo.c1, c2
FROM
	cte_rank cr
    INNER JOIN cte_distinct_order cdo
        ON cr.c1 = cdo.c1 
WHERE
	cr.duplicate_rank = 1;
```

