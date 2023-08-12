DROP TABLE IF EXISTS items CASCADE;
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    unit_price FLOAT,
    quantity INT
);

DROP TABLE IF EXISTS items_orders CASCADE;
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fl_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
);

DROP TABLE IF EXISTS orders CASCADE;
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer TEXT,
    date DATE
);

INSERT INTO items (name, unit_price, quantity) VALUES
('Maton Acoustic', 2345.99, 3),
('Tanglewood Acoustic', 679.49, 6),
('Eastman Mandolin', 659.00, 4),
('Kala Baritone Ukulele', 519.49, 5),
('Elixir Strings', 11.99, 20),
('Strap', 14.99, 15),
('Snark Tuner', 19.99, 15),
('Dusty Bread Roll', 1.19, 1);

INSERT INTO orders (customer, date) VALUES
('Benedict', '2023-05-30'),
('Will', '2022-07-04'),
('Ian', '2023-03-27'),
('Simeon', '2022-10-16'),
('Megan', '2023-06-21');

INSERT INTO items_orders (item_id, order_id) VALUES
(1, 1),
(4, 1),
(5, 1),
(7, 1),
(3, 2),
(6, 2),
(1, 3),
(2, 3),
(5, 3),
(4, 4),
(6, 4),
(8, 5);

-- ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("order_id") REFERENCES "public"."orders"("id");
-- ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("item_id") REFERENCES "public"."items"("id");
