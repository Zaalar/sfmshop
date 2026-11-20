# Оптимизировать функцию обработки большого списка данных в src/utils/calculations.py,
# измерить время выполнения до и после через простой замер времени (time.time()). 
# Функции — в src/utils/calculations.py, 
# сборка списка заказов и запуск замера — в scripts/lesson_30_benchmark.py. 
# Работать нужно с настоящими Order, Product и User из src/models/.
import time
import functools
from typing import Iterator, Optional

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
        order

def calculate_total_orders(orders):
    """Рассчитать общую сумму всех заказов"""
    total = 0
    for order in orders:
        for product in order.products:
            total += product.get_total_price()
    return total

# Измерение производительности
start_time = time.time()
result = calculate_total_orders(orders)
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.4f} секунд")