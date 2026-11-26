import time
import functools
from typing import Iterator, Optional
from src.models.product import Product

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter()- start
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


def find_product_in_list(products: list, product_id: int)->Product | None:
    for product in products:
        if product.id == product_id:
            return product
    return None


def find_product_in_dict(products_dict: dict, product_id: int)->Product | None:
    return products_dict.get(product_id)


def create_test_products(count: int) -> list[Product]:
  products = [Product(
        name=f"Product{i}",
            id=index,
            price=100 + i, 
            quantity=i % 10 + 1) 
            for index, i in enumerate(range(count))
          ]
  return products
      


def create_products_catalog(products: list[Product]) -> dict[int, Product]:
    pass

print (create_test_products(12))