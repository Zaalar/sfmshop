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
            INSERT INTO orders(user_id, total) VALUES (%s, %s) RETURNING order_id;
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
        SELECT order_id, user_id, total
        FROM orders
        WHERE user_id = %s;
       """, (user_id,))
        return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Ошибка БД {e}")
        return None
    finally:
        cursor.close()

def main():
    conn = connect_to_db()
    try:
        user_id = create_user(conn, "Иван", "ivan@test.ru")
        if user_id is None:
            print("Не удалось создать пользователя")
            return

        print(f"Пользователь создан: Иван, ivan@test.ru")

        user = get_user_by_id(conn, user_id)
        if user is None:
            print("Пользователь не найден")
            return

        print(f"Пользователь найден: {user}")

        order_id = create_order(conn, user_id, 5000.00)
        if order_id is None:
            print("Не удалось создать заказ")
            return

        print(f"Заказ создан: user_id={user_id}, total=5000.0")

        orders = get_user_orders(conn, user_id)
        if orders is None:
            print("Не удалось получить заказы пользователя")
            return

        print(f"Заказы пользователя: {orders}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()