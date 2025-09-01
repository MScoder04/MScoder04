create table salesman(
salesman_id text primary key,
name text,
city text,
comission real
);

insert into salesman(salesman_id,name,city,comission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);

create table customer(
customer_id text primary key,
name text,
city text,
grade text,
salesman_id text
);

insert into customer(customer_id,name,city,grade,salesman_id) VALUES
('3002', 'nick rimando', 'new york', 100, '5001'),
('3007', 'brad davis', 'new york', 200, '5001'),
('3005', 'graham zusi', 'california', 200, '5002'),
('3008', 'julian green', 'london', 300, '5002'),
('3004', 'fabian johnson', 'paris', 300, '5006'),
('3009', 'geoff cameron', 'berlin', 100, '5003'),
('3003', 'jozy altidor', 'moscow', 200, '5007'),
('3001', 'brad guzan', 'london', NULL, '5005');

create table orders(
order_id text primary key,
purch_amt text,
ord_date text,
salesman_id,
customer_id
);

insert into orders(order_id,purch_amt,ord_date,salesman_id,customer_id) VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),
('70009', 270.65, '2012-09-10', '3001', '5001'),
('70002', 65.26, '2012-10-05', '3002', '5003'),
('70004', 110.5, '2012-08-17', '3009', '5007'),
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70005', 2400.6, '2012-07-27', '3007', '5006');

alter table orders rename column salesman_id to cust_id;
alter table orders rename column customer_id to s_id;

select * from salesman;
select * from customer;
select * from orders;

select *
from customer
join orders on orders.cust_id=customer.customer_id
where ord_date='2012-09-10';

select customer.name as "Customer Name",
customer.city as "Customer City",
salesman.name as "Salesman Name",
salesman.comission as "Salesman Comission"
from customer join salesman on salesman.salesman_id=customer.salesman_id
where salesman.comission between 0.12 and 0.14;