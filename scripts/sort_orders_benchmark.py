import time
import random
from collections.abc import Callable
from datetime import datetime, timedelta


class Order:
    def __init__(self, id, created_at, total):
        self.id = id
        self.created_at = created_at
        self.total = total

def bubble_sort(orders: list)-> list:
    n = len(orders)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if orders[j].created_at > orders[j + 1].created_at:
                orders[j], orders[j + 1] = orders[j + 1], orders[j]
                swapped = True
        if not swapped:
            break
    return orders


def main():
    base_date = datetime(2025, 1, 1)
    orders = [
        Order(
            id=i + 1,
            created_at=base_date + timedelta(hours=i),
            total=500 + (i * 137) % 9500,
        )
        for i in range(1000)
    ]
    random.shuffle(orders)



    def benchmark(sort_func: Callable[[list], list], orders: list, repeats: int) -> float:
        times = []
        for i in range(repeats):
            copy_orders = orders.copy()
            t0 = time.perf_counter()
            sort_func(copy_orders)
            t1 = time.perf_counter()
            times.append(t1 - t0)
        return sum(times) / len(times)



    avg_bubble = benchmark(bubble_sort, orders, 10)
    avg_builtin = benchmark(lambda lst: sorted(lst, key=lambda x: x.created_at), orders, 50)
    speedup = avg_bubble / avg_builtin

    bubble_sorted = bubble_sort(orders.copy())
    builtin_sorted = sorted(orders.copy(), key=lambda order: order.created_at)
    bubble_ids = [order.id for order in bubble_sorted]
    builtin_ids = [order.id for order in builtin_sorted]


    print(f"Пузырьковая сортировка: {avg_bubble * 1000:.3f} мс")
    print(f"Встроенная сортировка: {avg_builtin * 1000:.3f} мс")
    print(f"Ускорение: {speedup:.2f}x")
    print(f"ID результатов совпадают: {bubble_ids == builtin_ids}")


if __name__ == "__main__":
    main()