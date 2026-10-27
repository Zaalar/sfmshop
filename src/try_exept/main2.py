# Практика: Задание 2 - Валидация данных пользователя

def validate_user_data(user_data):
    is_valid = True
    name = user_data.get("name", "")
    age = user_data.get("age")
    email = user_data.get("email", "")
    phone = user_data.get("phone", "")
    if not name.strip():
        print("Имя: ошибка - имя не может быть пустым")
        is_valid = False
    else:
        print("Имя: OK")
    if age is None or str(age).strip() == "":
        print("Возраст не должен быть пустым")
        is_valid = False
    else:
        try:
            age = int(age)
            print (f"Возраст: OK ({age})")
        except (TypeError, ValueError):
            print("Возраст: ошибка - невозможно преобразовать в число")
            is_valid = False
    if "@" in email:
        print ("Email: OK")
    else:
        print ("Email: ошибка - email должен содержать символ @")
        is_valid = False
    if isinstance(phone, str) and phone.isdigit():
        print("Телефон: OK")
    else:
        print("Телефон: ошибка - телефон должен содержать только цифры")
        is_valid = False
    if is_valid:
        print("Результат: все поля корректны")
    else:
        print("Результат: найдены ошибки")
    return is_valid
    

# Тестовые данные
user_1 = {"name": "Иван Петров", "age": "25", "email": "ivan@sfmshop.ru", "phone": "89001234567"}
user_2 = {"name": "", "age": "молодой", "email": "неверный_email", "phone": "89oo1234567"}

print("Проверка пользователя 1:")
result_1 = validate_user_data(user_1)

print("Проверка пользователя 2:")
result_2 = validate_user_data(user_2)