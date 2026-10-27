from src.models.payment import Payment, CardPayment, PayPalPayment


class Delivery:
    def get_description(self):
        return "Общее описание доставки"
class StandardDelivery(Delivery):
    def get_description(self):
        return "Стандартная доставка: 3-5 дней"

class ExpressDelivery(Delivery):
    def get_description(self):
        return "Экспресс-доставка: 1 день"

standard = StandardDelivery()
express = ExpressDelivery()


# print(standard.get_description())
# print(express.get_description())


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    def final_price(self):
        return self._price


class DiscountProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount
    def final_price(self):
        discount_amount = self._price * self.__discount
        return self._price - discount_amount


class GiftProduct(Product):
    def final_price(self):
        price = 0
        return price


products = [
    Product("Кружка", 500),
    DiscountProduct("Футболка", 1000, 0.2),
    GiftProduct("Открытка", 100),
]

for product in products:
    print(f"{product.name}: {product.final_price()} руб.")


# /////////////////////////////////////////////////////////////////////////////////////////////////////
card_payment = CardPayment(1000, "1234756728903456")
paypal_payment = PayPalPayment(2000, "user@paypal.com")
payments = [card_payment, paypal_payment]
for payment in payments:
    print(payment.process_payment())


