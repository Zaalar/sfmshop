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

def create_user(conn, name, email):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users(name, email) VALUES (%s, %s) RETURNING id;
        """,
        (name, email))
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    try:
        cursor.execute("""
        SELECT id, name, email
        FROM users WHERE id = %s;
       """, (user_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return {"id": row[0], "name": row[1], "email": row[2]} 
    except psycopg2.Error as e:
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def create_order(conn, user_id, total):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO orders(user_id, total) VALUES (%s, %s) RETURNING id;
        """,
        (user_id, total))
        order_id = cursor.fetchone()[0]
        conn.commit()
        return order_id
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def get_user_orders(conn, user_id):
    cursor = conn.cursor()
    try:
        cursor.execute("""
        SELECT id, user_id, total
        FROM orders
        WHERE user_id = %s;
       """, (user_id,))
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def delete_order(conn, order_id):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            DELETE FROM order_items
            WHERE order_id = %s
        """,
        (order_id,))
        cursor.execute("""
            DELETE FROM orders
            WHERE id = %s
        """,
        (order_id,))
        conn.commit()
        deleted_row = cursor.rowcount 
        return deleted_row
    except psycopg2.Error as e:
        conn.rollback()
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def count_products(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM products
            """
        )
        return cursor.fetchone()[0]
    except psycopg2.Error as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        cursor.close()

def get_products_page(conn, limit, offset):
    cursor = conn.cursor()
    try:
        cursor.execute("""
        SELECT id, name, price, quantity
        FROM products
        ORDER BY id LIMIT %s OFFSET %s
       """, (limit, offset))
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def get_product_by_id(conn, product_id):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, name, price, quantity
    FROM products
    WHERE id = %s
    """, (product_id,))
    result = cursor.fetchone()
    if result is None:
        cursor.close()
        return None

    else:
        cursor.close()
        return result


    

    
def main():
    conn = connect_to_db()
    try:
        user_id = create_user(conn, "Тестеинг Тестоав", "test4@example.com")
        if user_id is None:
            print("Пользователь не создан")
            return

        order_id = create_order(conn, user_id, 999.99)
        if order_id is None:
            print("Заказ не создан")
            return

        deleted = delete_order(conn, order_id) 
        print(f"Удалено строк: {deleted}")

        user = get_user_by_id(conn, user_id)
        if user is None:
            print("Пользователь не найден")
            return

        print(f"Пользователь найден: {user}")


        orders = get_user_orders(conn, user_id)
        if orders is None:
            print("Не удалось получить заказы пользователя")
            return

        print(f"Заказы пользователя: {orders}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()