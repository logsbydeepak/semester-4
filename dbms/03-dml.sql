create database my_company;

use my_company;

drop table employee;

create table employee (
    id bigint primary key,
    name varchar(100) not null,
    phone_no varchar(15),
    email varchar(100) unique,
    department_no varchar(15),
    department_name varchar(100),
    job_id varchar(50),
    salary decimal(10,2),
    address varchar(255)
);

insert into employee(id, name, phone_no, email, department_no, department_name, job_id, salary, address) values
(1, 'arun kumar', '9876543210', null, 'd4', 'cse', 'dev01', 55000.00, 'chennai'),
(2, 'priya sharma', '9123456780', null, 'd1', 'sales', 'sal01', 45000.00, 'mumbai'),
(3, 'rahul verma', '9988776655', null, 'd5', 'marketing', 'dev02', 60000.00, 'bangalore'),
(4, 'sneha reddy', '9090909090', 'sneha.reddy@email.com', 'd3', 'it', 'sal02', 50000.00, 'hyderabad'),
(5, 'karan mehta', '9345678901', null, 'd4', 'cse', 'dev03', 52000.00, 'pune'),
(6, 'anjali singh', '9765432109', null, 'd2', 'hr', 'sal03', 47000.00, 'delhi'),
(7, 'vikram das', '9012345678', null, 'd2', 'hr', 'dev04', 58000.00, 'kolkata');

select * from employee;

select * from employee where department_no = 'd5';

update employee
set address = 'mumbai'
where id = 5;

select * from employee where department_name = 'cse';

update employee
set email = null
where id = 4;

select * from employee where department_name = 'sales';
