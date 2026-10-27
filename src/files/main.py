def load_orders_from_file(filename): 
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            orders = [line.strip() for line in lines]
            return orders
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []


# 2////////////////////////////////////////////////////////////////////////////

def calculate_order_total(price, discount_rate):
    return round(price * (1 - discount_rate), 2)


def get_discount_by_total(total):
    if total <= 0:
        return 0
    elif total > 10000:
        return 0.15
    elif total > 5000:
        return 0.10
    else:
        return 0.05

# print(get_discount_by_total(-100))
# print(get_discount_by_total(0))
# print(get_discount_by_total(5000))
# print(get_discount_by_total(5001))
# print(get_discount_by_total(10000))
# print(get_discount_by_total(10001))


# 3////////////////////////////////////////////////////////////////////////

def process_orders(orders):
    processed_orders = []

    for order in orders:
        try:
            result = order.split(":")
            if len(result) != 4:
                raise ValueError

            price = int(result[1])
            discount_rate = get_discount_by_total(price)
            final_total = calculate_order_total(price, discount_rate)
            order_data = {
                "order_id": int(result[0]),
                "total": final_total,
                "status": result[2],
                "user": result[3]
            }
            processed_orders.append(order_data)
        except ValueError:
            print(f"Ошибка в строке: {order}")

    return processed_orders

test=(process_orders(load_orders_from_file("data/orders.txt")))
# print(test)
# t = 0
# for i in test:
#     t += 1
# print (t)

# 4///////////////////////////////////////////////////////////////////////
def analyze_orders(processed_orders):
    list_orders = processed_orders
    stats = {
   "total_orders": 0,
   "total_sum": 0,
   "by_status": {},
   "unique_users": set()
   }
    for i in list_orders:
        stats["total_orders"] += 1
        stats["total_sum"] += i["total"]
        status = i["status"]
        if status in stats["by_status"]:
            stats["by_status"][status] += 1
        else:
            stats["by_status"][status] = 1
        user = i["user"]
        stats["unique_users"].add(user)
    stats["unique_users"] = list(stats["unique_users"])
    return stats
        
# print(analyze_orders(test))


def process_order_file(input_file, output_file):
    orders = load_orders_from_file(input_file)
    process = process_orders(orders)
    stats = analyze_orders(process)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Обработано заказов: {stats['total_orders']}\n")
        file.write(f"Общая сумма: {stats['total_sum']} руб.\n")
        file.write(f"По статусам: {', '.join(f'{status}: {count}' for status, count in stats['by_status'].items())}\n")
        file.write(f"Уникальных пользователей: {len(stats['unique_users'])}\n")

process_order_file("data/orders.txt", "data/report.txt")