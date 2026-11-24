# Оптимизировать сортировку заказов,
# используя встроенную функцию sorted() с ключом.
# Измерить производительность и сравнить с ручной сортировкой.
# Код с оптимизированной сортировкой через sorted(),
# показывающий значительное ускорение по сравнению с ручной сортировкой.
import time
from datetime import datetime

class Order:
    def __init__(self, id, created_at, total):
        self.id = id
        self.created_at = created_at
        self.total = total
    def __repr__(self):
        return f"Order(id={self.id}, created_at={self.created_at.isoformat()}, total={self.total})"