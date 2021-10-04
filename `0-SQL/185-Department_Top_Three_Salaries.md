## [Question](https://leetcode.com/problems/department-top-three-salaries/)
### SQL Schema
```SQL
CREATE TABLE IF NOT EXISTS Employee (Id int, Name varchar(255), Salary int, DepartmentId int);
CREATE TABLE IF NOT EXISTS Department (Id int, Name varchar(255));
TRUNCATE TABLE Employee;
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('1', 'Joe', '85000', '1');
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('2', 'Henry', '80000', '2';)
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('3', 'Sam', '60000', '2');
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('4', 'Max', '90000', '1');
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('5', 'Janet', '69000', '1');
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('6', 'Randy', '85000', '1');
INSERT INTO Employee (Id, Name, Salary, DepartmentId) values ('7', 'Will', '70000', '1');
TRUNCATE TABLE Department;
INSERT INTO Department (Id, Name) values ('1', 'IT');
INSERT INTO Department (Id, Name) values ('2', 'Sales');
```

### SOLUTION
1. Common Table Expression With Window Functions

```SQL
WITH topThreeSalary AS
    (
        SELECT
            d.Name AS Department,
            e.Name AS Employee,
            e.Salary AS Salary,
            DENSE_RANK() OVER (PARTITION BY d.Name ORDER BY e.Salary DESC) as Ranking,
        FROM
            Employee e JOIN Department d
        ON
            e.DepartmentId = d.Id
    )
SELECT
    Department, Employee, Salary
FROM
    topThreeSalary
WHERE Ranking <= 3;
```

2. WINDOW Function With Sub-Query

```SQL
SELECT
    res.Department AS Department,
    res.Employee AS Employee,
    res.Salary AS Salary
FROM
    (
        SELECT
            d.Name AS Department,
            e.Name AS Employee,
            e.Salary AS Salary,
            DENSE_RANK() OVER (PARTITION BY d.Name ORDER BY e.Salary DESC) as Ranking,
        FROM
            Employee e JOIN Department d
        ON
            e.DepartmentId = d.Id
    ) res
WHERE Ranking <= 3;
```
