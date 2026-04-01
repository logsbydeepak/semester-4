CREATE DATABASE collage_db;

USE collage_db;

CREATE TABLE student(
   roll_no INT PRIMARY KEY,
   name VARCHAR(50),
   course VARCHAR(50),
   city VARCHAR(50)
);

INSERT INTO student VALUES
(1, 'Amit Sharma', 'B.Tech', 'Jaipur'),
(2, 'Neha Verma', 'BCA', 'Delhi'),
(3, 'Rohit Singh', 'MCA', 'Mumbai'),
(4, 'Priya Mehta', 'B.Tech', 'Jaipur'),
(5, 'Karan Gupta', 'MBA', 'Delhi');

-- 1
SELECT UPPER(name) AS name_upper
FROM student;

-- 2
SELECT LOWER(name) AS name_lower
FROM student;

-- 3
SELECT name, LENGTH(name) AS name_length
FROM student;

-- 4
SELECT SUBSTRING(name, 1, 4) AS short_name
FROM student;

-- 5
SELECT CONCAT(name, ' - ', city) AS student_details
FROM student;

-- 6
SELECT name, REPLACE(city, 'Delhi', 'New Delhi') AS city
FROM student;

-- 7
SELECT TRIM(name) AS clean_name
FROM student;
