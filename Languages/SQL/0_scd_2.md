## Type 2 SCDs - Creating another dimension record

A Type 2 SCD retains the full history of values. When the value of a chosen attribute changes, the current record is closed. A new record is created with the changed data values and this new record becomes the current record. Each record contains the effective time and expiration time to identify the time period between which the record was active.
```SQL
-- This example demonstrates Type 2 Slowly Changing Dimensions in Hive.
-- Be sure to stage data in before starting (load_data.sh)
DROP DATABASE IF EXISTS type2_test cascade;
CREATE DATABASE type2_test;
USE type2_test;

-- CREATE the Hive managed TABLE for our contacts. We track a start AND end date.
CREATE TABLE contacts_target(
        id INT, 
        name STRING, 
        email STRING, 
        state STRING, 
        valid_from DATE, 
        valid_to DATE
    )
    CLUSTERED BY (id) INTO 2 BUCKETS STORED AS ORC tblproperties("transactional"="true");

-- CREATE an EXTERNAL TABLE pointing to our initial data load (1000 records)
CREATE EXTERNAL TABLE contacts_initial_stage(
        id INT, 
        name STRING, 
        email STRING, 
        state string
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' stored AS textfile
    LOCATION '/tmp/merge_data/initial_stage';

-- Copy the initial load INTO the managed TABLE. We hard code the valid_from dates to the beginning of 2017.
INSERT INTO contacts_target SELECT *, cast('2017-01-01' AS date), cast(NULL AS date) FROM contacts_initial_stage;

-- CREATE an EXTERNAL TABLE pointing to our refreshed data load (1100 records)
CREATE EXTERNAL TABLE contacts_update_stage(
        id INT, 
        name STRING, 
        email STRING, 
        state string
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
    LOCATION '/tmp/merge_data/update_stage';

-- Perform the Type 2 SCD.
MERGE INTO contacts_target
USING (
    -- The base staging data.
    SELECT
        contacts_update_stage.id AS join_key,
        contacts_update_stage.* 
    FROM contacts_update_stage
    
    UNION ALL

    -- Generate an extra row for changed records.
    -- The null join_key means it will be inserted.
    SELECT
        NULL, contacts_update_stage.*
    FROM
        contacts_update_stage 
        JOIN contacts_target 
        ON contacts_update_stage.id = contacts_target.id
    WHERE
        (
            contacts_update_stage.email <> contacts_target.email OR contacts_update_stage.state <> contacts_target.state 
        )
        AND contacts_target.valid_to IS NULL 
    ) sub
ON sub.join_key = contacts_target.id
WHEN MATCHED
  AND sub.email <> contacts_target.email OR sub.state <> contacts_target.state
  THEN UPDATE SET valid_to = current_date()
WHEN NOT MATCHED
  THEN INSERT VALUES (sub.id, sub.name, sub.email, sub.state, current_date(), NULL);

-- Confirm 92 records are expired.
SELECT COUNT(*) FROM contacts_target WHERE valid_to IS NOT NULL ;

-- Confirm we now have 1192 records.
SELECT COUNT(*) FROM contacts_target;

-- View one of the changed records.
SELECT * FROM contacts_target WHERE id = 12;
```