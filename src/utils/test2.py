import time
import functools
from typing import Iterator, Optional

# --- Переиспользуемый декоратор для замера производительности ---


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


# --- Генератор для потоковой обработки заказов ---


def order_products_gen(orders: list) -> Iterator[float]:
    """Генератор: отдаёт стоимость каждого товара по одному"""
    for order in orders:
        for product in order.products:
            yield product.get_total_price()


# --- Оптимизированная функция с аннотациями типов ---

@measure_time
def calculate_total_orders(orders: list) -> float:
    """Оптимизированный подход: генератор + sum + декоратор + type hints"""
    return sum(order_products_gen(orders))