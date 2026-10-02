from src.models.product import Product
from src.models.exceptions import InvalidOrderError

class Order:
    def __init__(
        self,
        products,
        order_id=1,
        user=None,
    ):
        if not products:
            raise InvalidOrderError("Заказ невалиден: пустой список товаров")
        self.products = products
        self.order_id = order_id
        self.user = user

    def calculate_total(self):
        return sum(product.get_total_price() for product in self.products)
    
    def __str__(self):
        user_name = self.user.name if self.user is not None else "не указан"
        return f"Заказ пользователя {user_name} на сумму {self.calculate_total()} руб."
    
    def add_product(self, product):  
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект Product")
        self.products.append(product)




