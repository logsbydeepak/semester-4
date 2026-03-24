CREATE DATABASE my_company;

USE my_company;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    age INT
);

INSERT INTO employees VALUES
(1, 'Amit', 'IT', 50000, 25),
(2, 'Neha', 'HR', 40000, 28),
(3, 'Raj', 'IT', 60000, 30),
(4, 'Simran', 'Finance', 45000, 27),
(5, 'Karan', 'IT', 55000, 26),
(6, 'Riya', 'HR', 52000, 29),
(7, 'Arjun', 'Finance', 70000, 32),
(8, 'Priya', 'HR', 48000, 26),
(9, 'Vikas', 'Finance', 30000, 24),
(10, 'Sneha', 'IT', 65000, 31),
(11, 'Rahul', 'Finance', 55000, 28),
(12, 'Ankit', 'HR', 60000, 27);

-- Q1
SELECT COUNT(*) AS total_employees
FROM employees;

-- Q2
SELECT COUNT(*) AS it_employees
FROM employees
WHERE department = 'IT';

-- Q3
SELECT SUM(salary) AS total_salary
FROM employees;

-- Q4
SELECT AVG(salary) AS avg_salary
FROM employees;

-- Q5
SELECT MAX(salary) AS highest_salary
FROM employees;

-- Q6
SELECT MIN(salary) AS lowest_salary
FROM employees;

-- Q7
SELECT SUM(salary) AS it_total_salary
FROM employees
WHERE department = 'IT';

-- Q8
SELECT COUNT(*) AS employees_above_40000
FROM employees
WHERE salary > 40000;

-- Q9
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- Q10
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Q11
SELECT department, MAX(salary) AS max_salary
FROM employees
GROUP BY department;

-- Q12
SELECT department, MIN(age) AS min_age
FROM employees
GROUP BY department;

-- Q13
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;

-- Q14
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

-- Q15
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 100000;

-- Q16
SELECT department, COUNT(*) AS total_employees, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- Q17
SELECT department, COUNT(*) AS total_employees
FROM employees
WHERE salary > 40000
GROUP BY department
HAVING COUNT(*) >= 2;


