products = [
    {"name": "Ноутбук", "price": 50000},
    {"name": "Мышь", "price": 1500},
    {"name": "Монитор", "price": 25000},
    {"name": "Клавиатура", "price": 3000},
    {"name": "Наушники", "price": 8000}
    ]


def expensive_products(products: list, min_price: int):
    for product in products:
        if product["price"] > min_price:
            yield product

count = 0
for p in expensive_products(products, 10000):
    print(p["name"], p["price"])
    count += 1
total = sum(p["price"] for p in expensive_products(products, 10000))
print(total)