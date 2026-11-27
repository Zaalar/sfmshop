# import time
# import random
# from datetime import datetime
# import functools
# from typing import Iterator
# from src.models.product import Product

# class Order:
#     def __init__(self, id, created_at, total):
#         self.id = id
#         self.created_at = created_at
#         self.total = total
#     def __repr__(self):
#         return f"Order(id={self.id}, created_at={self.created_at.isoformat()}, total={self.total})"    

# from datetime import datetime, timedelta


# base_date = datetime(2025, 1, 1)
# orders = [
#     Order(
#         id=i + 1,
#         created_at=base_date + timedelta(hours=i),
#         total=500 + (i * 137) % 9500,
#     )
#     for i in range(1000)
# ]
# print (orders["created_at"])


prices = [500, 1500, 3000, 25000, 50000]

def binary_search(items: list, target) -> int | None:
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = - 1
    return mid

print(binary_search(prices, 3000))





