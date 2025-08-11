create table product(
id integer primary key,
name text,
price text,
commission integer);

insert into product(id,name,price,commission) values
(1,'apple','$2.00',0.15),
(2,'banana','$1.00',0.13),
(3,'strawberry','$0.50',0.10),
(4,'pineapple','$5.00',0.18);

select * from product;

select name,price
from product
where price=
(select min(price) from product);

select name,price
from product
where price=
(select max(price) from product);

select * from product
where name like '%e';

select * from product
where name like '%a%';

select * from product
where name like '__n%';

select * from product
where name like '__n';