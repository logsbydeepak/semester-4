create database my;
use my;

drop table student;

create table student(
	id int primary key,
    name varchar(50),
    city varchar(50),
    age int,
    marks int
);

insert into student values
(1, 'Amit', 'Jaipur', 18, 47),
(2, 'Neha', 'Delhi', 16, 87),
(3, 'Rohit', 'Jodhpur', 18, 78),
(4, 'Sneha', 'Jaipur', 17, 38),
(5, 'Arjun', 'Ajmer', 18, 78),
(6, 'Ankit', 'Delhi', 16, 75),
(7, 'Nisha', 'Jaipur', 19, 38)
;

-- 1
select name from student
where name like 'N%';

-- 2
select name from student
where name like '%t';

-- 3
select name from student
where name like '%ha%';

-- 4
select name from student
where city like '%r';

-- 5
select name,city from student
where name like '_r%';

-- 6
select name from student
where name like 'a%' and name like '%t';

-- 7
select name from student
where name like '%i%';

-- 8
select name from student
where name like '%am%';
