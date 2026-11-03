import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error


load_dotenv()

def connect_to_db():
    password = os.getenv("DB_PASSWORD")
    conn = psycopg2.connect(
        host="localhost",
        database="sfmshop",
        user="postgres",
        password=password
    )
    return conn

def get_user_order_history(conn, user_id):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
                SELECT orders.id, products.name, order_items.quantity, orders.created_at
                FROM orders
                JOIN order_items ON order_items.order_id = orders.id
                JOIN products ON order_items.product_id = products.id
                WHERE orders.user_id = %s
                ORDER BY orders.created_at DESC""",
            (user_id,)
        )
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        cursor.close()


def get_order_statistics(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT users.id, users.name,
            COUNT(*) AS orders_count,
            SUM(orders.total) AS orders_total
            FROM users
            JOIN orders ON orders.user_id = users.id
            GROUP BY users.id, users.name
            """
        )
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        cursor.close()

def get_top_products(conn, limit=5):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT products.name,
            SUM(order_items.quantity) AS orders_quantity
            FROM order_items
            JOIN products ON order_items.product_id = products.id
            GROUP BY products.id, products.name
            ORDER BY orders_quantity DESC
            LIMIT %s
            """, (limit,)
        )
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        cursor.close()


def get_all_products(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
                SELECT products.id, products.name, products.price
                FROM products 
                """
        )
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        cursor.close()

def main():
    conn = connect_to_db()
    try:
        print(get_user_order_history(conn, user_id=1))
        print(get_order_statistics(conn))
        print(get_top_products(conn))
        print(get_all_products(conn))
    finally:
        conn.close()

if __name__ == "__main__":
    main()
