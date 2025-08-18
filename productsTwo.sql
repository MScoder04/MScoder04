create table products(
id text primary key,
name text,
supplierId text,
unit text,
price real
);

insert into products(id,name,supplierId,unit,price) values
('1', 'pencil', '1', '5', 2.00),
('2', 'eraser', '2', '2', 1.50),
('3', 'pen', '3', '3', 2.50),
('4', 'highlighter', '4', '4', 3.00),
('5', 'highlighter', '5', '4', 4.00);

select * from products;
select count (name) as productCount from products;
select count (distinct(name)) as productcount from products;
select distinct name from products;
select sum (price) as totalPrice from products;
select avg (price) as averagePrice from products;