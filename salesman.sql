create table salesman (
id text primary key,
name text,
city text,
commission REAL
);

insert into salesman (id,name,city,commission) VALUES
('1','Emma','Paris',0.18),
('2','Lily','Venice',0.15),
('3','Jack','Milan',0.16),
('4','Ethan','Madrid',0.13);

select * from salesman;
