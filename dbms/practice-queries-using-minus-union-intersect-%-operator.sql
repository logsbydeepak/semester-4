CREATE DATABASE my_company;

USE my_company;

CREATE TABLE ticket (
    ticket_no INT PRIMARY KEY,
    source VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    journey_dur INT CHECK (journey_dur > 0)
);

CREATE TABLE passenger (
    pnr_no INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0),
    sex CHAR(1) CHECK (sex IN ('m','f')),
    ticket_no INT,
    
    FOREIGN KEY (ticket_no)
    REFERENCES ticket(ticket_no)
    ON DELETE CASCADE
);

INSERT INTO ticket (ticket_no, source, destination, journey_dur) VALUES
(1, 'hyd', 'ban', 12),
(2, 'sec', 'ban', 11),
(3, 'hyd', 'che', 8),
(23, 'hyd', 'mum', 14),
(12, 'del', 'kol', 9),
(4, 'mum', 'goa', 6),
(5, 'del', 'jaipur', 5);

INSERT INTO passenger (pnr_no, name, age, sex, ticket_no) VALUES
(1, 'sachin', 45, 'm', 1),
(2, 'rahul', 38, 'm', 2),
(3, 'swetha', 25, 'f', 3),
(4, 'rafi', 30, 'm', 23),
(5, 'salim', 50, 'm', 12),
(6, 'riyaz', 28, 'm', 4),
(7, 'neha', 22, 'f', 5);


-- Q1
SELECT DISTINCT pnr_no 
FROM passenger;

-- Q2
SELECT name 
FROM passenger 
WHERE sex = 'm';

-- Q3
SELECT ticket_no, name 
FROM passenger;

-- Q4
SELECT source, destination 
FROM ticket 
WHERE journey_dur > 10;

-- Q5
SELECT ticket_no 
FROM passenger 
WHERE name LIKE 's%' AND name LIKE '%n';

-- Q6
SELECT name 
FROM passenger 
WHERE age BETWEEN 20 AND 40;

-- Q7
SELECT name 
FROM passenger 
WHERE name LIKE 'r%';

-- Q8
SELECT name 
FROM passenger 
ORDER BY name;
