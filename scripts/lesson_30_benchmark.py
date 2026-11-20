from src.models.user import User
from src.models.product import Product
from src.models.order import Order
from src.utils.calculations import calculate_total_orders


products = [
    Product("Мышь", 1500, 2),
    Product("Клавиатура", 3500, 1),
    Product("Монитор", 15000, 1),
    Product("Наушники", 2500, 3),
]

print(products)