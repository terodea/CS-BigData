## [QUESTION](https://leetcode.com/problems/duplicate-emails/)
Write an SQL query to report all the duplicate emails.<br>

Return the result table in any order.
### Schema
```SQL
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (Id, Email) values ('1', 'a@b.com')
insert into Person (Id, Email) values ('2', 'c@d.com')
insert into Person (Id, Email) values ('3', 'a@b.com')
```

### Solution
```SQL
WITH CTE AS (
    SELECT
        Email, count(Id) AS cnt
    FROM
        Peson
    GROUP BY 
        Email;
)

SELECT
    Email
FROM
    CTE
WHERE
    cnt > 1;
```