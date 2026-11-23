import time
from src.models.product import Product
from src.utils.calculations import find_product_in_list, find_product_in_dict

products = []
for i in range(1000):
    product = Product(f"Товар-{i}", 100 + i, i % 10 + 1)
    product.id = i
    products.append(product)
products_dict = {product.id: product for product in products}

start = time.perf_counter()
find_product_in_dict(products_dict, 999)
elapsed_dict = time.perf_counter() - start
print(f"Время выполнения: {elapsed_dict:.4f} секунд")

start = time.perf_counter()
find_product_in_list(products, 999)
elapsed_list = time.perf_counter() - start
print(f"Время выполнения: {elapsed_list:.4f} секунд")

print(f"Ускорение: {elapsed_list / elapsed_dict}")
print(find_product_in_list(products, 999).name == find_product_in_dict(products_dict, 999).name)