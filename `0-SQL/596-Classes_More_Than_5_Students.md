## [QUESTION](https://leetcode.com/problems/classes-more-than-5-students/)
List out all classes which have more than or equal to 5 students.

### SCHEMA
```SQL
Create table If Not Exists courses (student varchar(255), class varchar(255));
Truncate table courses;
insert into courses (student, class) values ('A', 'Math');
insert into courses (student, class) values ('B', 'English');
insert into courses (student, class) values ('C', 'Math');
insert into courses (student, class) values ('D', 'Biology');
insert into courses (student, class) values ('E', 'Math');
insert into courses (student, class) values ('F', 'Computer');
insert into courses (student, class) values ('G', 'Math');
insert into courses (student, class) values ('H', 'Math');
insert into courses (student, class) values ('I', 'Math');
```

### SOLUTION
1.
```SQL
WITH CTE AS(
    SELECT
        class,
        student,
        DESNSE_RANK() OVER(PARTITION BY class ORDER BY student) AS rnk
    FROM
        courses
)
SELECT
    class
FROM
    CTE
WHERE
    rnk >= 5;
```

2.
```SQL
SELECT
    distinct class
FROM
    courses
GROUP BY
    class
HAVING COUNT(DISTINCT student) >= 5;
```

3. SQL Template to get max rank from each partition. First + Last - 1. All rows will have max rank for each partition
```SQL
WITH CTE AS(
    SELECT
        class,
        student,
        DENSE_RANK() OVER(PARTITION BY class ORDER BY student ASC) + DENSE_RANK() OVER(PARTITION BY class ORDER BY student DESC) -1 AS rnk
    FROM
        courses
)
SELECT
    distinct class
FROM
    CTE
WHERE
    rnk >= 5;
```