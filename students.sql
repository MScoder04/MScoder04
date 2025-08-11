create table students(
rollNumber integer primary key,
name text,
age integer,
address text
);

insert into students(rollNumber,name,age,address) VALUES
(1,'Kaylie',15,'Atlanta'),
(2,'Gracie',14,'Suwanee'),
(3,'Jackson',16,'Savannah'),
(4,'Brandon',15,'Augusta');

select * from students;
select * from students where age=15 and name='Kaylie';
select * from students where age=15;
select * from students where age=15 or name='Gracie';
select * from students where age=15 and (name='Jackson' or name='Brandon');