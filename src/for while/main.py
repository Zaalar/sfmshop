prices = [500, 1500, 800, 2000, 1200]

for i, price in enumerate(prices):
    if price > 1000:
        print("Товар", i + 1, "цена", price)
# ///////////////////////////////////

price_1 = 500
price_2 = 1500
price_3 = 800
price_4 = 2000
price_5 = 1200

prices = [price_1, price_2, price_3, price_4, price_5]
filtered_prices = []
max_price = 0
max_product = 0

for i, price in enumerate(prices):
    if price > 1000:
        filtered_prices.append(price)
        if price > max_price:
            max_price = price
            max_product = i + 1

if filtered_prices:
    print("Товары с ценой больше 1000:")
    for i, price in enumerate(prices):
        if price > 1000:
            print(f"Товар {i + 1}: {price} руб.")

    print()
    print(f"Количество товаров с ценой больше 1000: {len(filtered_prices)}")
    print()
    print(f"Товар с максимальной ценой: Товар {max_product}, цена {max_price} руб.")
else:
    print("Товаров с ценой больше 1000 не найдено.")