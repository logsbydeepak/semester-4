create database p10;

use p10;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE enrollments (
    id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO students VALUES
(1, 'Aman', 'Jaipur'),
(2, 'Riya', 'Delhi'),
(3, 'Karan', 'Mumbai'),
(4, 'Neha', 'Pune');

INSERT INTO courses VALUES
(101, 'DBMS'),
(102, 'Python'),
(103, 'AI');

INSERT INTO enrollments VALUES
(1, 1, 101),
(2, 1, 102),
(3, 2, 103),
(4, 3, 101);



-- q1
SELECT s.name, c.name
FROM students s
INNER JOIN enrollments e
ON s.id = e.student_id
INNER JOIN courses c
ON e.course_id = c.id;

-- q2
SELECT s.name, c.name
FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
LEFT JOIN courses c
ON e.course_id = c.id;

-- q3
SELECT s.name, c.name
FROM students s
RIGHT JOIN enrollments e
ON s.id = e.student_id
RIGHT JOIN courses c
ON e.course_id = c.id;

-- q4
SELECT s.name, c.name
FROM students s
CROSS JOIN courses c;

-- q5
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    manager_id INT
);

drop table employees;

-- q6
SELECT s.name
FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
WHERE e.student_id IS NULL;

-- q7
SELECT s.name,
COUNT(e.course_id) AS total_courses
FROM students s
LEFT JOIN enrollments e
ON s.id = e.student_id
GROUP BY s.name;

-- q8
SELECT c.name,
COUNT(e.student_id) AS total_enrollments
FROM courses c
INNER JOIN enrollments e
ON c.id = e.course_id
GROUP BY c.name
ORDER BY total_enrollments DESC
LIMIT 1;

-- q9
SELECT s.name
FROM students s
INNER JOIN enrollments e
ON s.id = e.student_id
INNER JOIN courses c
ON e.course_id = c.id
WHERE c.name = 'DBMS';

-- q10
SELECT s.name,
s.city,
c.name
FROM students s
INNER JOIN enrollments e
ON s.id = e.student_id
INNER JOIN courses c
ON e.course_id = c.id;
