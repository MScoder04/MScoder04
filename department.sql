create table department(
employee_id text,
name text,
department_id text,
manager_id text,
salary real
);

insert into department(employee_id,name,department_id,manager_id,salary) VALUES
('1','Ella','1','1',17000),
('2','Billy','1','2',15000),
('3','James','2','3',10000),
('4','Lily','3','4',20000);

select * from department;

select department_id as "Department Code",
count(*) as "No. of Employees"
from department
group by department_id;

select department_id as "Department Code", manager_id,
count(*) as "No. of Employees"
from department
group by manager_id;

select department_id as "Department Code",
count(*) as "No. of Employees",
sum(salary) as "Total Salary"
from department
group by department_id;

select department_id as "Department Code",
count(*) as "No. of Employees"
from department
group by department_id
having count(*) > 1;

select * from department
order by salary;

select * from department
order by salary DESC;