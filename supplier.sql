create table supplier (
sno text primary key,
sname text,
status,
city text
);

insert into supplier VALUES
('s1','Ella','1','Paris'),
('s2','Lily','2','Venice'),
('s3','James','3','Atlanta'),
('s4','Jack','4','Suwanee');

select * from supplier;
select sname, city from supplier;