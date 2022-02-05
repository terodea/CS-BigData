## [Question](https://leetcode.com/problems/trips-and-users/)
### SCHEMA

```SQL
CREATE TABLE IF NOT EXISTS Trips (Id int, Client_Id int, Driver_Id int, City_Id int, Status ENUM('completed', 'cancelled_by_driver', 'cancelled_by_client'), Request_at varchar(50));
CREATE TABLE IF NOT EXISTS Users (Users_Id int, Banned varchar(50), Role ENUM('client', 'driver', 'partner'));
TRUNCATE TABLE Trips;
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('1', '1', '10', '1', 'completed', '2013-10-01');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('3', '3', '12', '6', 'completed', '2013-10-01');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('5', '1', '10', '1', 'completed', '2013-10-02');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('6', '2', '11', '6', 'completed', '2013-10-02');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('7', '3', '12', '6', 'completed', '2013-10-02');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('8', '2', '12', '12', 'completed', '2013-10-03');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('9', '3', '10', '12', 'completed', '2013-10-03');
INSERT INTO Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03');
TRUNCATE TABLE Users;
INSERT INTO Users (Users_Id, Banned, Role) values ('1', 'No', 'client');
INSERT INTO Users (Users_Id, Banned, Role) values ('2', 'Yes', 'client');
INSERT INTO Users (Users_Id, Banned, Role) values ('3', 'No', 'client');
INSERT INTO Users (Users_Id, Banned, Role) values ('4', 'No', 'client');
INSERT INTO Users (Users_Id, Banned, Role) values ('10', 'No', 'driver');
INSERT INTO Users (Users_Id, Banned, Role) values ('11', 'No', 'driver');
INSERT INTO Users (Users_Id, Banned, Role) values ('12', 'No', 'driver');
INSERT INTO Users (Users_Id, Banned, Role) values ('13', 'No', 'driver');
```

### SOLUTION
```SQL
SELECT
    t.Request_at AS Day,
    ROUND(COUNT(IF(t.Status != "completed", TRUE, null))/COUNT(1),2) AS `Cancellation Rate`
FROM
    Trips t
WHERE
    t.Client_Id IN (
        SELECT 
            Users_Id
        FROM
            Users
        WHERE
            Banned = "No" 
    )
    AND
    t.Driver_Id IN (
        SELECT
            Users_Id
        FROM
            Users
        WHERE
            Banned = "No"
    )
    AND
    t.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY
    t.Request_at;
```
