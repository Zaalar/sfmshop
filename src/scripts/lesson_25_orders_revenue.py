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


if __name__ == "__main__":
    main()