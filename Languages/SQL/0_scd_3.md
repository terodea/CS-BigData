## Type 3 SCDs - Creating a current value field

A Type 3 SCD stores two versions of values for certain selected level attributes. Each record stores the previous value and the current value of the selected attribute. When the value of any of the selected attributes changes, the current value is stored as the old value and the new value becomes the current value.

```SQL
-- This example demonstrates Type 3 Slowly Changing Dimensions in Hive.
-- Be sure to stage data in before starting (load_data.sh)
DROP DATABASE IF EXISTS type3_test cascade;
CREATE DATABASE type3_test;
USE type3_test;

-- CREATE the Hive managed TABLE for our contacts. We track a start and end date.
CREATE TABLE contacts_target(
    id INT, 
    name STRING,
    email STRING, 
    last_email STRING,
    state STRING, 
    last_state STRING
  )
  CLUSTERED BY (id) INTO 2 buckets stored AS ORC tblproperties("transactional"="true");

-- CREATE an EXTERNAL TABLE pointing to our initial data load (1000 records)
CREATE EXTERNAL TABLE contacts_initial_stage(
        id INT, 
        name STRING, 
        email STRING, 
        state STRING
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
    LOCATION '/tmp/merge_data/initial_stage';

-- Copy the initial load into the managed TABLE. We hard code the valid_from dates to the beginning of 2017.
INSERT INTO contacts_target(
        id, name, email, state, last_email, last_state
    )
    SELECT
        *, email, state 
    FROM contacts_initial_stage;

-- CREATE an EXTERNAL TABLE pointing to our refreshed data load (1100 records)
CREATE EXTERNAL TABLE contacts_update_stage(
        id INT, 
        name STRING, 
        email STRING, 
        state STRING
    )
    ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
    LOCATION '/tmp/merge_data/update_stage';

-- SOLUTION
-- Perform the type 3 update.
MERGE INTO
    contacts_target
USING 
    contacts_update_stage AS stage 
    ON stage.id = contacts_target.id
WHEN MATCHED AND
    contacts_target.email <> stage.email OR contacts_target.state <> stage.state -- change detection
    THEN UPDATE SET
        last_email = contacts_target.email, 
        email = stage.email, -- email history
        last_state = contacts_target.state, 
        state = stage.state  -- state history
WHEN NOT MATCHED THEN 
    INSERT VALUE (
        stage.id, 
        stage.name, 
        stage.email, 
        stage.email, 
        stage.state, 
        stage.state
    );

-- Confirm 92 records have been changed.
SELECT COUNT(*) FROM contacts_target WHERE last_email <> email OR last_state <> state;

-- Confirm a total of 1100 records.
SELECT COUNT(*) FROM contacts_target;

-- View a changed record.
SELECT * FROM contacts_target WHERE id = 12;
```