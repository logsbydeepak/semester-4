create database p9;

use p9;

CREATE TABLE student (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    course VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO student VALUES
(1, 'Amit Sharma', 'B.Tech', 'Jaipur'),
(2, 'Neha Verma', 'BCA', 'Delhi'),
(3, 'Rohit Singh', 'MCA', 'Mumbai'),
(4, 'Pooja Mehta', 'B.Tech', 'Jaipur'),
(5, 'Karan Gupta', 'MBA', 'Delhi');


SELECT * FROM student
WHERE city = 'Delhi' AND course = 'BCA';

SELECT * FROM student
WHERE city = 'Jaipur' OR course = 'MBA';

SELECT * FROM student
WHERE NOT city = 'Delhi';

