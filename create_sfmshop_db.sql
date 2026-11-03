CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER DEFAULT 0
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO users (id, name, email) VALUES
    (1, 'Анна Иванова', 'anna@example.com'),
    (2, 'Иван Петров', 'ivan@example.com'),
    (3, 'Мария Смирнова', 'maria@example.com');

INSERT INTO products (id, name, price, quantity) VALUES
    (1, 'Ноутбук', 75000.00, 10),
    (2, 'Мышь', 1500.00, 50),
    (3, 'Клавиатура', 3500.00, 30),
    (4, 'Монитор', 22000.00, 15),
    (5, 'Наушники', 6000.00, 25);

INSERT INTO orders (id, user_id, total, created_at) VALUES
    (1, 1, 78000.00, '2026-10-30 10:00:00'),
    (2, 2, 10000.00, '2026-11-01 14:30:00');

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
    (1, 1, 1, 75000.00),
    (1, 2, 2, 1500.00),
    (2, 3, 1, 3500.00),
    (2, 5, 1, 6000.00),
    (2, 2, 1, 1500.00);

SELECT setval(pg_get_serial_sequence('users', 'id'), (SELECT MAX(id) FROM users));
SELECT setval(pg_get_serial_sequence('products', 'id'), (SELECT MAX(id) FROM products));
SELECT setval(pg_get_serial_sequence('orders', 'id'), (SELECT MAX(id) FROM orders));
SELECT setval(pg_get_serial_sequence('order_items', 'id'), (SELECT MAX(id) FROM order_items));
