create table employees(
id text primary key,
name text,
salary integer
);

insert into employees(id,name,salary) values
('1','Emma',100000),
('2','Sally',80000),
('3','John',70000),
('4','Steven',90000);

select * from employees;
select sum(salary) as totalSalary from employees;
select avg(salary) as averageSalary from employees;
select name,salary from employees where salary=(select min(salary) from employees);
select name,salary from employees where salary=(select max(salary) from employees);