def calculate_order_total(price, quantity, discount):
	return (price * quantity) * (1 - discount)


def check_stock_availability(stock, requested_quantity):
	return stock >= requested_quantity


def format_order_info(order_id, total):
    return f'Заказ #{order_id}, Сумма: {total} руб.'


is_available = check_stock_availability(10, 3)
print(f"Товар доступен: {is_available}")

if is_available:
	total = calculate_order_total  (1000, 3, 0.1)
	result = format_order_info (1, total)
	print(result)