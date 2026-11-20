def calculate_total_orders(orders):
    """Медленный подход"""
    total = 0
    for order in orders:
        for product in order.products:
            total += product.get_total_price()
    return total

# Нет измерения производительности
# Нет понимания, где происходит задержка
# Нет оптимизации
# Нет аннотаций типов
# Нет генераторов для больших данных