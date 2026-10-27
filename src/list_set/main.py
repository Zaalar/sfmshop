users = {}

products = {
    "Ноутбук": {
        "price": 50000,
        "category": "Электроника"
    },
    "Мышь": {
        "price": 1500,
        "category": "Аксессуары"
    }
}

visitors = set()

users[1] = {
"name": "Иван",
"email": "ivan@test.ru"
}
search_price = products["Ноутбук"]["price"]
visitor_site = visitors.add("user_123")
visitor_exists = "user_123" in visitors

print(f"Пользователь добавлен: {users[1]}")
print (f"Цена товара 'Ноутбук': {search_price} руб.")
print(f"Посетитель 'user_123' был на сайте: {visitor_exists}")