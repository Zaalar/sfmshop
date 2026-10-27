from src.models.order import Order
from src.models.product import Product
from src.models.user import User


try:
    Product("Некорректный товар", -100, 1)
except ValueError as error:
    print(f"Ошибка при создании товара: {error}")

try:
    available_product = Product("Ноутбук", 50_000, 1)
    missing_product = Product("Мышь", 1_500, 1)
    order = Order([available_product])
    order.add_product(missing_product)
except KeyError as error:
    print(f"Ошибка при создании заказа: {error.args[0]}")

try:
    User("Иван Иванов", "ivan.test.ru")
except ValueError as error:
    print(f"Ошибка при создании пользователя: {error}")
