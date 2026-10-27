BASE_DISCOUNT = 0.1
BASE_DELIVERY_COST = 100


def calculate_order_price(price, quantity):
	subtotal = price * quantity
	return subtotal - subtotal * BASE_DISCOUNT + BASE_DELIVERY_COST


def update_discount(new_discount):
	global BASE_DISCOUNT
	BASE_DISCOUNT = new_discount


price = 1000
quantity = 2

print(f"Стоимость заказа (скидка 10%): {calculate_order_price(price, quantity)}")
update_discount(0.15)
print(f"Стоимость заказа (скидка 15%): {calculate_order_price(price, quantity)}")
