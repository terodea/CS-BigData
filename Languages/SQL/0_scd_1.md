# About: What is Slowly changing dimension ?
A Slowly Changing Dimension (SCD) is a dimension that stores and manages both current and historical data over time in a data warehouse. It is considered and implemented as one of the most critical ETL tasks in tracking the history of dimension records.


## Type 1 SCDs - Overwriting/ Upsert(If new_record THEN Insert ELSE UPDATE)
In a Type 1 SCD the new data overwrites the existing data. Thus the existing data is lost as it is not stored anywhere else. This is the default type of dimension you create. You do not need to specify any additional information to create a Type 1 SCD.

```SQL
-- This example demonstrates Type 1 Slowly Changing Dimensions in Hive.
-- Be sure to stage data in before starting (load_data.sh)
DROP DATABASE IF EXISTS type1_test cascade;
CREATE DATABASE type1_test;
USE type1_test;

-- Create the Hive managed table for our contacts.
CREATE TABLE contacts_target(
        id INT, 
        name STRING, 
        email STRING, 
        state STRING
    )
    CLUSTERED BY (id) INTO 2 BUCKETS STORED AS ORC TBLPROPERTIES("transactional"="true");

-- Create an external table pointing to our initial data load (1000 records)
CREATE EXTERNAL TABLE contacts_initial_stage(
        id int, 
        name string, 
        email string, 
        state string
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
    LOCATION '/tmp/merge_data/initial_stage';

-- Copy the initial load into the managed table.
INSERT INTO contacts_target SELECT * FROM contacts_initial_stage;

-- Create an external table pointing to our refreshed data load (1100 records)
CREATE EXTERNAL TABLE contacts_update_stage(
        id INT, 
        name STRING, 
        email STRING, 
        state STRING
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
    LOCATION '/tmp/merge_data/update_stage';

-- Perform the Type 1 Update (full table upsert)
MERGE INTO
  contacts_target
USING
  contacts_update_stage AS stage
ON
  stage.id = contacts_target.id
WHEN MATCHED THEN
  UPDATE SET 
    name = stage.name, 
    email = stage.email, 
    state = stage.state
WHEN NOT MATCHED THEN
  INSERT VALUES (
      stage.id, 
      stage.name, 
      stage.email, 
      stage.state
);

-- Confirm we now have 1100 records.
SELECT COUNT(1) FROM contacts_target;
```


**Credits : [LINK](https://github.com/cartershanklin/hive-scd-examples)**
