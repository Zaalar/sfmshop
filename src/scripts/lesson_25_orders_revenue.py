import sqlite3


def connect_to_db():
    conn = sqlite3.connect(":memory:")
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

    conn.commit()

    cursor.execute("""
        CREATE TABLE orders(
        order_id INTEGER PRIMARY KEY,
        product_id INTEGER NOT NULL,
        quantitu INTEGER NOT NULL
        )
    """)
    conn.commit()



if __name__ == "__main__":
    main()