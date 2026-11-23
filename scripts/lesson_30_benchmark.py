import sys
from pathlib import Path
from src.models.user import User
from src.models.product import Product
from src.models.order import Order
from src.utils.calculations import measure_time, order_products_gen
import time
import functools
from typing import Iterator, Optional


products = [
    Product("Мышь", 1500, 2),
    Product("Клавиатура", 3500, 1),
    Product("Монитор", 15000, 1),
    Product("Наушники", 2500, 3),
]
orders = [Order(products)]

@measure_time
def calculate_total_orders_optimized(orders: list) -> Iterator[float]:
    return sum(order_products_gen(orders))


start_time = time.time()
result = calculate_total_orders_optimized(orders)
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.4f} секунд")