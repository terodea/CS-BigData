## PSET: Pivot of students and their marks in each subject

### Schema: DDL
```SQL
CREATE TABLE marks_data(student_id int, subject varchar(50), marks int);
INSERT INTO marks_data VALUES(1001, "English", 88);
INSERT INTO marks_data VALUES(1001, "Science", 90);
INSERT INTO marks_data VALUES(1001, "Maths", 85);
INSERT INTO marks_data VALUES(1002, "English", 70);
INSERT INTO marks_data VALUES(1002, "Science", 80);
INSERT INTO marks_data VALUES(1002, "Maths", 83);
```


### Solution:

1. MySQL
```SQL
SELECT
    student_id,
    SUM(CASE WHEN subject = "English" THEN marks else 0) AS English,
    SUM(CASE WHEN subject = "Science" THEN marks else 0) AS Science,
    SUM(CASE WHEN subject = "Maths" THEN marks else 0) AS Maths,
FROM
    marks_data
GROUP BY student_id
ORDER BY student_id
```