order_total = 6000
discount = 0

if order_total > 10000:
    discount = 15
elif order_total > 5000 and order_total < 10000:
    discount = 10
else:
    discount = 5

print(f"Размер скидки: {discount:.1f}%")

# ////////////////////////////////////////////////////////////////

initial_price = order_total
discount_amount = initial_price * discount / 100
final_price = initial_price - discount_amount

print(f"Исходная сумма: {initial_price} руб.")
print(f"Размер скидки: {discount:.1f}%")
print(f"Размер скидки: {discount_amount:.1f} руб.")
print(f"Итоговая стоимость: {final_price:.1f} руб.")


# //////////////////////////////////////////////////////////////
user_age = 17
user_balance = 500
order_total = 1000
requested_qty = 3
in_stock = 5


if user_age < 18:
    print("Отказ: пользователь несовершеннолетний")
elif user_balance < order_total:
    print("Отказ: недостаточно средств")
elif requested_qty > in_stock:
    print("Отказ: недостаточно товара на складе")
else:
    print("Заказ можно оформить")

# ///////////////////////////////////////////////////////////////////
order_total = 3500
city = "Казань"


if order_total > 5000:
    delivery_cost = 0
elif city == "Москва" or city == "Санкт-Петербург":
    delivery_cost = 300
else:
    delivery_cost = 500

print(f"Стоимость доставки: {delivery_cost} руб.")

