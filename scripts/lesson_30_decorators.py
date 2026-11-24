import functools
# Написать декоратор log_call, 
# который при каждом вызове функции выводит её имя и переданные аргументы. 
# Применить декоратор к функции расчёта стоимости заказа. 
# Файл: scripts/lesson_30_decorators.py
def log_cal(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(x)for x in args)
        print(f"Вызов: {func.__name__}({args_str})")
        return func(*args, **kwargs)
    return wrapper

@log_cal
def calculate_order(price, quantity, discount):
    return price * quantity * (1 - discount)

print(f"Заказ 1: {calculate_order(1000, 3, 0.1)} руб.")
print(f"Заказ 2: {calculate_order(2000, 1, 0.2)} руб.")