import time
import functools
from typing import Iterator, Optional
from src.models.product import Product

def measure_time(func):
    """Декоратор: замеряет и выводит время выполнения функции"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} выполнена за {elapsed:.4f} сек")
        return result
    return wrapper

def order_products_gen(orders:list) -> Iterator[float]:
    for order in orders:
        for product in order.products:
            yield product.get_total_price()

@measure_time
def calculate_total_orders_optimized(orders: list) -> float:
    return sum(order_products_gen(orders))


def find_product_in_list(products, product_id):
    for product in products:
        if product.id == product_id:
            return product
    return None


def find_product_in_dict(products_dict, product_id):
    return products_dict.get(product_id)