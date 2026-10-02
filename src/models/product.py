from src.models.exceptions import NegativePriceError, InsufficientStockError, ValidationError

class Product:

    def __init__(self, name, price, quantity):
        if price < 0:
            raise NegativePriceError("Цена не может быть отрицательной")

        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}"

    def reduce_stock(self, requested_quantity):
        if requested_quantity < 0:
            raise ValidationError("Запрошенное количество не может быть отрицательным")
        if requested_quantity > self.quantity:
            raise InsufficientStockError(
                f"Товара недостаточно. На складе: {self.quantity}, требуется: {requested_quantity}"
            )
        self.quantity -= requested_quantity

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"
    
    def set_price(self, price):
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        else:
            self.price = price
