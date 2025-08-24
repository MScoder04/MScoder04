create table customers(
id text primary key,
name text,
city text,
grade integer
);

insert into customers(id,name,city,grade) VALUES
('1','Bill','Atlanta',100),
('2','Emily','New York',200),
('3','Carlos','Austin',500),
('4','Kristy','New York',70);

select * from customers;
select * from customers where city='New York' or grade>100;
select * from customers where city='New York' and grade>100;