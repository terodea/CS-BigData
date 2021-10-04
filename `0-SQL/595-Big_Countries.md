## [QUESTION](https://leetcode.com/problems/big-countries/)
A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.<br>

Write a SQL solution to output big countries' name, population and area.

### SCHEMA
```SQL
Create table If Not Exists World (name varchar(255), continent varchar(255), area int, population bigint, gdp bigint);
Truncate table World;
insert into World (name, continent, area, population, gdp) values ('Afghanistan', 'Asia', 652230, 25500100, 20343000000);
insert into World (name, continent, area, population, gdp) values ('Albania', 'Europe', 28748, 2831741, 12960000000);
insert into World (name, continent, area, population, gdp) values ('Algeria', 'Africa', 2381741, 37100000, 188681000000);
insert into World (name, continent, area, population, gdp) values ('Andorra', 'Europe', 468, 78115, 3712000000);
insert into World (name, continent, area, population, gdp) values ('Angola', 'Africa', 1246700, 20609294, 100990000000);
```

### SOLUTION
1.
```SQL
SELECT
    name, population, area
FROM
    World
WHERE
    area > 3000000 OR population > 25000000;
```

2.
```SQL
SELECT
    name, population, area
FROM
    World
WHERE
    area > 3000000
UNION
SELECT
    name, population, area
FROM
    World
WHERE
    population > 25000000;
```