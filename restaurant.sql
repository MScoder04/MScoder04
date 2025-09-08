create table restaurant(
name text,
neighborhood text,
cuisine text,
review real,
price real,
health text
);

insert into restaurant(name,neighborhood,cuisine,review,price,health) VALUES
('Peter', 'Brooklyn', 'Steak', 4.4, 1000, 'A'),
('Jongro', 'Midtown', 'Korean', 3.5, 50, 'A'),
('Pocha', 'Midtown', 'Pizza', 4, 100, 'B'),
('Lighthouse', 'Queens', 'Chinese', 3.9, 9, 'A'),
('Minca', 'Downtown', 'American', 4.6, 100, ''),
('Marea', 'Chinatown', 'Chinese', 3.0, 50, ''),
('Dirty Candy', 'Uptown', 'Italian', 4.9, 1000, 'B'),
('Di Fara Pizza', 'Brooklyn', 'Pizza', 3.8, 100, 'A'),
('Golden Unicorn', 'Uptown', 'Italian', 3.8, 50, 'A');

select * from restaurant;
select name, review from restaurant where review>4;
select name, review, price from restaurant where review>4 and price<1000;
select * from restaurant where neighborhood like '%town';
select * from restaurant where neighborhood in ('Midtown','Downtown','Chinatown');
select * from restaurant order by review DESC;
select * from restaurant order by review DESC limit 5;