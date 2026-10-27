from src.models.order import Order
from src.models.product import Product
from src.models.user import User


products = [
    Product("Ноутбук", 50_000, 10),
	Product("Мышь", 1_500, 20),
	Product("Клавиатура", 3_000, 15),
]
products.sort()

for product in products:
	print(product)

user = User("Иван", "ivan@test.ru")
order = Order(
	[Product("Ноутбук", 50_000, 1)],
	order_id=1,
	user=user.name,
)
print(order)
