def safe_order_total(items):
    total = 0
    processed_count = 0
    for item in items:
        try:
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            result = price * quantity
            total += result
            processed_count += 1
        except KeyError as error:
            print(f' Ошибка в товаре {item.get("name", "Неизвестный товар")}: отсутствует обязательное поле')
        except TypeError as error:
            print(f'Ошибка в товаре {item.get("name", "Неизвестный товар")}: неверный тип данных для расчета')
    print(f'обработано товаров {processed_count}')
    return total


test_items = [
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Мышь", "price": 1500, "quantity": 2},
    {"name": "Клавиатура"},
    {"name": "Монитор", "price": None, "quantity": 1},
    {"name": "Наушники", "price": 3000, "quantity": 3}
    ]

result = safe_order_total(test_items)
print("Общая стоимость: " + str(result))