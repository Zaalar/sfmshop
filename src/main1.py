price_per_item = 1500.0
quantity = 3
discount = 0.1
result = price_per_item * quantity * (1 - discount)
print(result)

paid = 5000
cost = 3750

calculation = paid - cost
result2 = calculation // 500
remainder = calculation % 500
print (f"Сдача: {calculation}; купюр по 500: {result2}, остаток: {remainder}")

# ////////////////////////////////////////////////////////

order_1_price = 2000.0
order_1_quantity = 2
order_1_discount = 0.15

order_2_price = 3000.0
order_2_quantity = 1
order_2_discount = 0.0

order_3_price = 5000.0
order_3_quantity = 3
order_3_discount = 0.2

order_1_initial_price = order_1_price * order_1_quantity
order_1_discount_amount = order_1_initial_price * order_1_discount
order_1_total = round(order_1_initial_price - order_1_discount_amount, 2)

order_2_initial_price = order_2_price * order_2_quantity
order_2_discount_amount = order_2_initial_price * order_2_discount
order_2_total = round(order_2_initial_price - order_2_discount_amount, 2)

order_3_initial_price = order_3_price * order_3_quantity
order_3_discount_amount = order_3_initial_price * order_3_discount
order_3_total = round(order_3_initial_price - order_3_discount_amount, 2)

print("Заказ 1:")
print(f"Исходная цена: {order_1_initial_price} руб.")
print(f"Размер скидки: {order_1_discount_amount} руб.")
print(f"Итоговая стоимость: {order_1_total} руб.")
print()

print("Заказ 2:")
print(f"Исходная цена: {order_2_initial_price} руб.")
print(f"Размер скидки: {order_2_discount_amount} руб.")
print(f"Итоговая стоимость: {order_2_total} руб.")
print()

print("Заказ 3:")
print(f"Исходная цена: {order_3_initial_price} руб.")
print(f"Размер скидки: {order_3_discount_amount} руб.")
print(f"Итоговая стоимость: {order_3_total} руб.")