## PSET: Tree Structure Labelling
### Problem: Say you've a table tree with a column of nodes and a column correspoding parent nodes. Write SQL/ PySpark/ Pandas code such that we label each node as a "leaf", "inner" or "Root" node


## 1. SQL
- Solution for only two levels of tree.
```SQL
WITH join_table AS(
    SELECT
        a.node AS a_node, 
        a.parent AS a_parent,
        b.node AS b_node,
        b.parent AS b_parent
    FROM
        tree a LEFT JOIN tree b
    ON
        a.parent = b.tree
);

SELECT
    a_node AS node,
    CASE 
        WHEN b_node IS NULL AND b_parent IS NULL THEN "Root"
        WHEN b_node IS NOT NULL AND b_parent IS NOT NULL THEN "Leaf"
        ELSE "Inner"
        END AS label
FROM
    join_table;
```
- Without Explicit Joins
```SQL
WITH join_table AS(
    SELECT
        cur.node AS node,
        cur.parent AS parent,
        COUNT(next.node) AS num_children
    FROM
        tree cur LEFT JOIN tree next ON (next.parent = cur.node)
    GROUP BY
        cur.node, cur.parent
);

SELECT
    node,
    CASE
        WHEN parent IS NULL THEN "Root"
        WHEN num_children = 0 THEN "Leaf"
        ELSE "Inner"
    END AS label
FROM
    join_table;
```
- Sub Querries (Generic Approach)
```SQL
SELECT
    node,
    CASE
        WHEN parent IS NULL THEN "Root"
        WHEN node NOT IN (
            SELECT
                parent
            FROM
                tree
            WHERE
                parent IS NOT NULL
        ) THEN "Leaf"
        WHEN node IN (
            SELECT
                parent
            FROM
                tree
        ) AND parent IS NOT NULL THEN "Inner"
    END AS label
FROM
    tree
```