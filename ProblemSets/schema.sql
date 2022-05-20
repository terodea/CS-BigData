create table if not exists int_orders(order_number int NOT NULL, order_date date NOT NULL, cust_id int NOT NULL, salesperson_id int NOT NULL, amount float NOT NULL);

insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(30, "2015-01-01", 9, 1, 460);
insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(10, "2015-01-02", 4, 2, 540);
insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(40, "2015-01-03", 7, 2, 2400);
insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(50, "2015-01-04", 6, 7, 600);
insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(60, "2015-01-05", 6, 7, 720);
insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(70, "2015-01-06", 9, 7, 150);
insert into int_orders(order_number, order_date, cust_id, salesperson_id, amount) VALUES(20, "2015-01-07", 4, 8, 1800);