## [QUESTION](https://leetcode.com/problems/combine-two-tables/)
Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a PersonId is not present in the Address table, report null instead.<br>

Return the result table in any order.

### Schema

```SQL
CREATE TABLE IF NOT EXISTS Person (
    PersonId int, 
    FirstName varchar(255), 
    LastName varchar(255)
)
CREATE TABLE IF NOT EXISTS Address (
    AddressId int, 
    PersonId int, 
    City varchar(255), 
    State varchar(255)
)
TRUNCATE TABLE Person
INSERT INTO Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')
INSERT INTO Person (PersonId, LastName, FirstName) values ('2', 'Alice', 'Bob')
TRUNCATE TABLE Address
INSERT INTO Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')
INSERT INTO Address (AddressId, PersonId, City, State) values ('2', '3', 'Leetcode', 'California')
```

### Solution
1.
```SQL
SELECT
    p.FirstName AS FirstName,
    p.LastName AS LastName,
    a.City AS City,
    a.State AS State
FROM
    Person p LEFT OUTER JOIN Address a
ON
    p.PersonId = a.PersonId;
```