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


def _make_test_product(i: int) -> Product:
    product = Product(
        name=f"Product{i}",
            price=100 + i, 
            quantity=i % 10 + 1) 
    product.id = i
    return product


def create_test_products(count: int) -> list[Product]:
    return [_make_test_product(i) for i in range(count)]


def create_products_catalog(products: list[Product]) -> dict[int, Product]:
    return {product.id: product for product in products}

def benchmark_search(products, product_id):
    """Сравнить время поиска в списке vs словаре"""
    # Поиск в списке
    start_time = time.time()
    result_list = find_product_in_list(products, product_id)
    time_list = time.time() - start_time

    # Поиск в словаре
    products_dict = create_products_catalog(products)
    start_time = time.time()
    result_dict = products_dict.get(product_id)
    time_dict = time.time() - start_time

    speedup = time_list / time_dict if time_dict > 0 else 0
    return {
        "time_list": time_list,
        "time_dict": time_dict,
        "speedup": speedup
        }

def benchmark_optimizations() -> None:
    """Замер: линейный поиск в списке vs поиск в словаре (1000 товаров)."""
    products = create_test_products(1000)
    catalog = create_products_catalog(products)
    product_id = 500
    repeats = 1000

    times_before = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        find_product_in_list(products, product_id)
        t1 = time.perf_counter()
        times_before.append(t1 - t0)

    times_after = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        find_product_in_dict(catalog, product_id)
        t1 = time.perf_counter()
        times_after.append(t1 - t0)

    avg_before = sum(times_before) / len (times_before)
    avg_after = sum(times_after) / len (times_after)
    speedup = avg_before / avg_after 

    print(f"До (список): {avg_before * 1_000_000:.1f} мкс")
    print(f"После (словарь): {avg_after * 1_000_000:.1f} мкс")
    print(f"Ускорение: {speedup:.1f}x")