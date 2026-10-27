from datetime import datetime, timedelta


def calculate_delivery_date(order_date, delivery_days):
    return order_date + timedelta(days=delivery_days)


def log_order_creation(order_id, order_time):
    return f"Заказ #{order_id} создан: {order_time.strftime('%Y-%m-%d %H:%M:%S')}"


order_creation_time = datetime(2024, 1, 15, 14, 30, 0)
order_date = datetime(2024, 1, 15, 10, 0, 0)
delivery_days = 3

delivery_date = calculate_delivery_date(order_date, delivery_days)

print(f"Дата доставки: {delivery_date.strftime('%Y-%m-%d %H:%M:%S')}")
print(log_order_creation(123, order_creation_time))