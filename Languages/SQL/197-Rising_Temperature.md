## [QUESTION]()
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).<br>

### SCHEMA
```SQL
Create table If Not Exists Weather (Id int, RecordDate date, Temperature int)
Truncate table Weather
insert into Weather (Id, RecordDate, Temperature) values ('1', '2015-01-01', '10')
insert into Weather (Id, RecordDate, Temperature) values ('2', '2015-01-02', '25')
insert into Weather (Id, RecordDate, Temperature) values ('3', '2015-01-03', '20')
insert into Weather (Id, RecordDate, Temperature) values ('4', '2015-01-04', '30')
```

### Solution:
```SQL
SELECT
    w2.Id AS id
FROM
    Weather w1, Weather w2
WHERE
    w2.RecordDate = DATE_ADD(w1.RecordDate, INTERVAL 1 DAY) AND w2.Temperature > w1.Temperature;
```