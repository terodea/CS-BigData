### Complex Schema DDL
```SQL
CREATE TABLE IF NOT EXISTS mobile(
    title           STRING,
    cost            FLOAT,
    colors          ARRAY<STRING>,
    screen_size     ARRAY<FLOAT>,
    features        MAP<STRING, BOOLEAN>,
    information     STRUCT<battery: STRING, camera:STRING>
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATAED BY '#'
MAP KEYS TERMINATED BY ':';
```
### Partition
```bash
SET hive.exec.dynamic.partition=TRUE
SET hive.exec.dynamic.partition.mode='nonstrict'
CREATE TABLE IS NOT EXISTS products(
    id INT,
    name STRING,
    cost DOUBLE
)
PARTITION BY (category STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```
### Bucketing:
```bash
SET hive.enforce.bucketing=TRUE;

hive> CREATE TABLE IF NOT EXISITS products(
    id INT,
    name STRING,
    cost DOUBLE,
    category STRING
)
CLUSTURED BY (id) INTO 4 BUCKETS;

hive> SELECT * FROM products TABLESAMPLE(bucket 1 OUT OF 4);
hive> SELECT * FROM products TABLESAMPLE(bucket 2 OUT OF 4);
hive> SELECT * FROM products TABLESAMPLE(bucket 3 OUT OF 4);
hive> SELECT * FROM products TABLESAMPLE(bucket 4 OUT OF 4);
```

### Partitioning with bucketing
```SQL
CREATE TABLE IF NOT EXISTS products_no_buckets(id INT, name STRING, cost DOUBLE, category STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
LOAD DATA LOCAL INPATH '/home/cloudera/newProducts.csv' INTO TABLE products_no_buckets;

CREATE TABLE IF NOT EXISTS products_part_buck(id INT, name STRING, cost DOUBLE) PARTITIONED BY (category STRING) CLUSTERED BY (id) INTO 4 BUCKETS ROW FORMAT DELIMITED ROW TERMINATED BY ',';

INSERT INTO product_part_buck PARTITION (category) SELECT id, name, cost, category FROM products_no_buckets;
```

## JOIN Optimization:
1. One Join == One MR job. Try reducing joins.
2. LEFT TABLE is small (use inner and right outer join)
3. RIGHT TABLE is small (user inner and left outer join)

- **Map Side Join**: </br>
1. A local task of creating hash map from small table.
2. Hashtable is passed on to the hdfs.
3. That hashtable is broadcasted to all the nodes.
4. That hastable will reside on local hdfs of each node (mimicing distributed caceh.)
5. Then that hashtable is loaded in to the memory and map reduce jobs are launched.

- **Bucket Map Join**:</br>
0. 
```SQL
SET hive.optimize.bucketmapjoin=true
```
1. Unlike Map side join it can be done on 2 big tables also.
2. Both the tables should be bucketed on join column.
3. Number of buckets in one table should be integral multiple of othertable.
4. Only the required buckets are loaded in memory that’s the advantageover map side join.

- **Sort Merge Bucket Map Join (SMB)**</br>
0. 
```SQL
hive> set hive.auto.convert.sortmerge.join=true;
hive> set hive.auto.convert.sortmerge.join.noconditionaltask=true;
hive> set hive.optimize.bucketmapjoin=true;
hive> set hive.optimize.bucketmapjoin.sortedmerge=true;
hive> set hive.enforce.bucketing=true;
hive> set hive.enforce.sorting=true;
hive> set hive.auto.convert.join=true;
```
1. Unlike Map side join it can be done on 2 big tables also.
2. Both the tables should be sorted on join column
3. Both the tables should be bucketed on join column.
4. Number of buckets in both tables should be exactly equal
5. There will be a one to one mapping between buckets in both tables.And a quick joining can be performed as both the buckets have sorteddata.

```SQL
SET hive.auto.convert.join=true
```
Set it to false to check out the join optimization is missing and a reducer job is lau
launched.
