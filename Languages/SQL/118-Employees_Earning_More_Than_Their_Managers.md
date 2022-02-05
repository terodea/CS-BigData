## [QUESTION](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
Write an SQL query to find the employees who earn more than their managers.<br>

Return the result table in any order.
### Schema
```SQL
CREATE TABLE IF NOT EXISTS Employee (
    Id int, Name varchar(255), Salary int, ManagerId int
)
TRUNCATE TABLE Employee
INSERT INTO Employee (Id, Name, Salary, ManagerId) values ('1', 'Joe', '70000', '3')
INSERT INTO Employee (Id, Name, Salary, ManagerId) values ('2', 'Henry', '80000', '4')
INSERT INTO Employee (Id, Name, Salary, ManagerId) values ('3', 'Sam', '60000', 'None')
INSERT INTO Employee (Id, Name, Salary, ManagerId) values ('4', 'Max', '90000', 'None')
```
### Solution
1.
```SQL
SELECT
    e1.Name AS Name
FROM
    Employee e1, Employee e2
ON
    e1.Id = e2.ManagerId
WHERE
    e1.Salary > e2.Salary;
```