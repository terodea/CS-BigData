## PSET: Finding "out-of-sequence" records.
#### Question: Items identiﬁed by ID values must move from STATUS 'ONE' to 'TWO' to 'THREE' in sequence, without skipping statuses. The problem is to ﬁnd users ( STATUS_BY ) values who violate the rule and move from 'ONE' immediately to 'THREE'.

### Schema:
```SQL
CREATE TABLE IF NOT EXISTS users_status(
    id int,
    status varchar(25),
    status_time datetime,
    status_by varchar(25)
)
TRUNCATE TABLE user_status
INSERT INTO user_status(id, status, status_time, status_by) VALUES (1, 'ONE', '2016-08-28-19.47.52.501398', 'USER_1');
INSERT INTO user_status(id, status, status_time, status_by) VALUES (3, 'ONE', '2016-08-28-19.47.52.501511', 'USER_2');
INSERT INTO user_status(id, status, status_time, status_by) VALUES (1, 'THREE', '2016-08-28-19.47.52.501517', 'USER_3');
INSERT INTO user_status(id, status, status_time, status_by) VALUES (3, 'TWO', '2016-08-28-19.47.52.501521', 'USER_2');
INSERT INTO user_status(id, status, status_time, status_by) VALUES (3, 'THREE', '2016-08-28-19.47.52.501524', 'USER_4');
```

### DATA:
| id          | status      | status_time                  | status_by     |
| :---        | :---        |    :----:                    |          ---: |
| 1           | ONE         |  2016-08-28-19.47.52.501398  | USER_1        |
| 3           | ONE         |  2016-08-28-19.47.52.501511  | USER_2        |
| 1           | THREE       |  2016-08-28-19.47.52.501517  | USER_3        |
| 3           | TWO         |  2016-08-28-19.47.52.501521  | USER_2        |
| 3           | THREE       |  2016-08-28-19.47.52.501524  | USER_4        |

## Solutions:

### 1: SQL
```SQL
SELECT
    id, status, status_time, status_by
FROM
    (
        SELECT
            s.*, LAG(status) OVER (PARTITION BY id ORDER BY status_time) AS prev_status
        FROM
            status t
    ) status_with_lag
WHERE
    status = "THREE" AND prev_status != "TWO"
```
So your db doesn't support LAG() an analytical support, here's the alternative.

```SQL
SELECT
    s1.id, s1.status, s2.status AS prev_status, s1.status_time, s1.status_time AS prev_status_time
FROM
    status s1, status s2
WHERE
    s1.id = s2.id AND s2.status_time = (
        SELECT
            MAX(status_time)
        FROM
            status
        WHERE
            status_time < s1.status_time AND id = s1.id
    )
    AND s1.status = "THREE" AND NOT s2.status = "TWO"

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
```Python3
import os
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql.functions import to_timestamp, lag
from pyspark.sql.window import Window
from pyspark.sql.types import StructType,StructField, StringType, IntegerType


class OutOfSequenceRecords:
    def compute(self):
        """
        Objective: Get of out sequence records
        """
        try:
            raw_data = [
                (1, 'ONE', '2016-08-28 19:47:52:501398', 'USER_1'),
                (1, 'ONE', '2016-08-28 19:47:52:501511', 'USER_2'),
                (1, 'THREE', '2016-08-28 19:47:52:501517', 'USER_3'),
                (1, 'TWO', '2016-08-28 19:47:52:501521', 'USER_2'),
                (1, 'THREE', '2016-08-28 19:47:52:501524', 'USER_4')
            ]
            rd_schema = StructType(
                [
                    StructField("id", IntegerType(), True),
                    StructField("status", StringType(), True),
                    StructField("status_tms" ,StringType(), True),
                    StructField("status_by", StringType(), True)
                ]
            )
            df = spark.createDataFrame(data=raw_data, schema=rd_schema)
            df1 = df.withColumn("status_time", df["status_tms"].cast(DateType()))
            windowSpec = Window.partitionBy("id").orderBy("status_time")
            status_with_lag = df1.withColumn("prev_status", lag(status).over(windowSpec)
            status_with_lag.where(status_with_lag.status == "THREE" AND status_with_lag.prev_status != "TWO").show()

        except Exception as err:
            raise err
if __name__ == "__main__":
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week10Practical10")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    OutOfSequenceRecords().compute()
```
### 3: Pandas