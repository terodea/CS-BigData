## [QUESTION](https://leetcode.com/problems/employee-bonus/)
Select all employee’s name and bonus whose bonus is < 1000.

### SCHEMA
```SQL
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Bonus;

CREATE TABLE IF NOT EXISTS Employee (
    EmpId int, 
    Name varchar(255), 
    Supervisor int, 
    Salary int);
CREATE TABLE IF NOT EXISTS Bonus (
    EmpId int, 
    Bonus int);

TRUNCATE TABLE Employee;
INSERT INTO Employee (EmpId, Name, Supervisor, Salary) VALUES ('3', 'Brad', null, '4000');
INSERT INTO Employee (EmpId, Name, Supervisor, Salary) VALUES ('1', 'John', '3', '1000');
INSERT INTO Employee (EmpId, Name, Supervisor, Salary) VALUES ('2', 'Dan', '3', '2000');
INSERT INTO Employee (EmpId, Name, Supervisor, Salary) VALUES ('4', 'Thomas', '3', '4000');

TRUNCATE TABLE Bonus;
INSERT INTO Bonus (EmpId, Bonus) VALUES ('2', '500');
INSERT INTO Bonus (EmpId, Bonus) VALUES ('4', '2000');
```

### Solutions
1. 
```SQL
SELECT 
    e.Name AS name, b.Bonus AS bonus
FROM
    Employee e LEFT JOIN Bonus b 
ON
    b.EmpId = e.EmpId
WHERE
    b.Bonus < 1000 OR b.Bonus IS NULL;
```

2. 
```SQL
SELECT
    e.Name AS name, b.Bonus AS bonus
FROM
    Employee e LEFT OUTER JOIN Bonus b
ON 
    e.EmpId = b.EmpId
WHERE
    IFNULL(b.Bonus, -1) < 1000;
```