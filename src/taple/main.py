delivery_coordinates = {
    1: (55.7558, 37.6173)
}

order_id = 1
if order_id in delivery_coordinates:
    coordinates = delivery_coordinates[order_id]
    latitude, longitude = coordinates
    print(f"Координаты заказа {order_id}: {coordinates}")
    print("Широта:", latitude)
    print("Долгота:", longitude)
else:
    print(f"Координаты заказа {order_id}: Заказ не найден")

order_id = 3
if order_id in delivery_coordinates:
    coordinates = delivery_coordinates[order_id]
    print(f"Координаты заказа {order_id}: {coordinates}")
else:
    print(f"Координаты заказа {order_id}: Заказ не найден")