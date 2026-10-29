import sqlite3


def connect_to_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON") # так мы делаем проверку. только так заказ с несуществующим ид выдаст ошибку
    return conn



def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price DECIMAL NOT NULL,
        count INTEGER NOT NULL)
    """)

    cursor.execute("""
        CREATE TABLE orders(
        order_id INTEGER PRIMARY KEY,
        product_id INTEGER NOT NULL REFERENCES products(product_id),
        quantity INTEGER NOT NULL
        )
    """)
    conn.commit()

    cursor.executemany(
        "INSERT INTO products (name, price, count) VALUES (?, ?, ?)",
        [
            ("Ноутбук", 50000.00, 10),
            ("Мышь", 1500.00, 10),
        ],
    )

    cursor.executemany(
        "INSERT INTO orders (product_id, quantity) VALUES (?, ?)",
        [
            (1, 2),  # 2 ноутбука
            (2, 1),  # 1 мышь
            (2, 3),  # 3 мыши
        ],
    )
    conn.commit()

    cursor.execute("""
        SELECT orders.order_id,
        SUM(products.price * orders.quantity) AS total
        FROM orders 
        JOIN products
        ON orders.product_id = products.product_id
        GROUP BY orders.order_id
    """)

    total = cursor.fetchall()

    for i in total:
        print(f"Сумма заказа {i[0]}: {i[1]}")

    cursor.execute("""
        SELECT
        SUM(products.price * orders.quantity) AS total
        FROM orders 
        JOIN products
        ON orders.product_id = products.product_id
    """)
    
    revenue = cursor.fetchall()
    print(f"Общая выручка: {revenue[0][0]}")


    conn.close()


if __name__ == "__main__":
    main()