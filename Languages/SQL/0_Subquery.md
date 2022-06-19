# Subquery
A conceptual understanding of SQL subquery and their practice question.

### Topics:
1. Correlated subquery
2. Linear subquery


**NOTE :**
1. If the set being evaluated by **SQL NOT IN** contains any **NULL** then outer query will return and empty set.
```PYTHON3
>>> from pyspark.sql.types import *
>>> _data = [(1, "John Doe"), (2, "Jane Doe"), (3, "Alice Jones"), (4, "Bobby Louis"), (5, "Lisa Romero")]
>>> runner_df = spark.createDataFrame(_data, schema=["id", "name"])

>>> race_data = [(1, "100 meter dash", 2), (2, "500 meter dash", 3), (3, "cross-country", 2), (4, "triathlon", None)]

>>> race_df = spark.createDataFrame(race_data, schema=["id","event", "winner_id"])
>>> race_df.createOrReplaceTempView("race_df")
>>> runner_df.createOrReplaceTempView("runner_df")

>>> spark.sql("SELECT * FROM runner_df WHERE id NOT IN (SELECT winner_id FROM race_df);").show()
+---+----+
| id|name|
+---+----+
+---+----+

>>> spark.sql("SELECT * FROM runner_df WHERE id NOT IN (SELECT winner_id FROM race_df WHERE winner_id IS NOT NULL);").show()
+---+-----------+
| id|       name|
+---+-----------+
|  1|   John Doe|
|  4|Bobby Louis|
|  5|Lisa Romero|
+---+-----------+

```