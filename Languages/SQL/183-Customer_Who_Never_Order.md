## [QUESTION](https://leetcode.com/problems/customers-who-never-order/)
Write an SQL query to report all customers who never order anything.<br>

Return the result table in any order.

### SCHEMA
```SQL
Create table If Not Exists Customers (Id int, Name varchar(255))
Create table If Not Exists Orders (Id int, CustomerId int)
Truncate table Customers
insert into Customers (Id, Name) values ('1', 'Joe')
insert into Customers (Id, Name) values ('2', 'Henry')
insert into Customers (Id, Name) values ('3', 'Sam')
insert into Customers (Id, Name) values ('4', 'Max')
Truncate table Orders
insert into Orders (Id, CustomerId) values ('1', '3')
insert into Orders (Id, CustomerId) values ('2', '1')
```

### Solution
1.
```SQL
SELECT
    Name AS Customer
FROM
    Customers
WHERE
    Id NOT IN (
        SELECT
            CustomerId
        FROM
            Orders
    );
```