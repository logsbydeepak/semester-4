create database bank_details;

use bank_details;

create table customer_details (
    account_number bigint primary key,
    name varchar(100) not null,
    email varchar(100) unique not null,
    phone_number varchar(15) unique not null,
    address varchar(255)
);

desc customer_details;

drop table customer_details;

alter table customer_details
add balance decimal(12,2) default 0.00;

rename table customer_details to bank_information;

