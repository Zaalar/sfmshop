from database.connection import connect_to_db, create_user, get_user_by_id
from database.queries import (
    get_all_products,
    get_order_statistics,
    get_top_products,
    get_user_order_history,
)


def main():
    conn = connect_to_db()
    try:
        user_id = create_user(conn, "Тестовый пользователь", "test5@example.com")
        if user_id is None:
            print("Пользователь не создан")
            return
        print(f"Пользователь создан: id={user_id}")

        print(f"Все товары: {get_all_products(conn)}")
        print(f"Статистика заказов: {get_order_statistics(conn)}")
        print(f"Топ товаров: {get_top_products(conn)}")

        user = get_user_by_id(conn, user_id)
        print(f"Пользователь: {user}")
        print(f"История заказов: {get_user_order_history(conn, user_id)}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
