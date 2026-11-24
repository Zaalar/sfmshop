# Файл scripts/lesson_31_binary_search.py
# Реализуй бинарный поиск товара по ID в каталоге SFMShop. 
# Сначала отсортируй список товаров по ID 
# (бинарный поиск работает только на отсортированных данных), выведи отсортированный каталог,
# а затем найди товары по нескольким ID, сообщая для каждого, найден товар или нет.
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


def binary_search_by_id(sorted_products, target_id):
    """Бинарный поиск товара по ID (O(log n)). Верни товар или None."""
    left = 0
    right = len(sorted_products) - 1

    while left <= right:
        mid = (left + right) // 2
        product = sorted_products[mid]

        if product.id == target_id:
            return product
        elif product.id < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return None


def main():
    products = [
        Product(105, "Мышь", 1500),
        Product(101, "Ноутбук", 50000),
        Product(110, "Монитор", 18000),
        Product(103, "Клавиатура", 3000),
        Product(108, "Наушники", 7000),
    ]
    key_products = lambda product: product.id
    sorted_products = sorted(products, key=key_products)
    search_id = [108, 110, 104]
    for i in search_id:
        product = binary_search_by_id(sorted_products, i)
        if product is not None:
            print(f"Товар с ID {i} найден: {product.name}")
        else:
            print(f"Товар с ID {i} не найден")


if __name__ == "__main__":
    main()