from src.utils.calculations import (
    calculate_delivery,
    calculate_discount,
    calculate_final_price,
)
from src.utils.validators import validate_age, validate_email


price = 1000
discount_rate = 0.1
weight = 5
age = 20
email = "ivan@test.ru"

age_valid = validate_age(age)
email_valid = validate_email(email)

print(f"Возраст валиден: {age_valid}")
print(f"Email валиден: {email_valid}")

if age_valid and email_valid:
    discount = calculate_discount(price, discount_rate)
    delivery = calculate_delivery(weight)
    final_price = calculate_final_price(price, discount, delivery)
    print(f"Итоговая стоимость заказа: {final_price} руб.")
