CREATE DATABASE CollegeDB;
USE CollegeDB;
CREATE TABLE Student(
   RollNo INT PRIMARY KEY,
   Name VARCHAR(50),
   Course VARCHAR(50),
   City VARCHAR(50)
);
INSERT INTO Student VALUES
(1, 'Amit Sharma', 'B.Tech', 'Jaipur'),
(2, 'Neha Verma', 'BCA', 'Delhi'),
(3, 'Rohit Singh', 'MCA', 'Mumbai'),
(4, 'Priya Mehta', 'B.Tech', 'Jaipur'),
(5, 'Karan Gupta', 'MBA', 'Delhi');

SELECT UPPER(Name) AS Name_Upper FROM Student

SELECT LOWER(Name) AS Name_Lower FROM Student;

SELECT Name, LENGTH(Name) AS Name_Length FROM Student;

SELECT SUBSTRING(Name, 1, 4) AS Short_Name FROM Student;

SELECT CONCAT(Name, ' - ', City) AS Student_Details FROM Student;

SELECT Name, REPLACE(City, 'Delhi', 'New Delhi') AS City FROM Student;

SELECT TRIM(Name) AS Clean_Name FROM Student;