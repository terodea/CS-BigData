## [Question]()
Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest Id.


### SCHEMA
```SQL
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (Id, Email) values ('1', 'john@example.com')
insert into Person (Id, Email) values ('2', 'bob@example.com')
insert into Person (Id, Email) values ('3', 'john@example.com')
```

### Solution
1.
```SQL
WITH CTE AS(
    SELECT
        Id, Email,
        ROW_NUMBER() OVER(PARTITION BY Email ORDER BY Id) as rw_rk
    FROM
        Person
)

DELETE
FROM
    Person
WHERE
    Id IN(
        SELECT
            Id
        FROM
            CTE
        WHERE rw_rk > 1
    );
```