import re


def validate_email_regex(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))


def validate_phone_regex(phone):
    pattern = r"^\+?\d[\d\s\-\(\)]*\d$"
    if not re.fullmatch(pattern, phone):
        return False
    digits = re.sub(r"\D", "", phone)
    return len(digits) == 11 and digits.startswith(("7", "8"))


def clean_input(text):
    cleaned = re.sub(r"[^\w\s.]", "", text)
    return cleaned.strip()


def extract_email_from_text(text):
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    if match:
        return match.group(0)
    return ""


email = "ivan@test.ru"
phone = "+7 999 123-45-67"
raw_text = "Заказ 123, Сумма 5000 руб."
source_text = "Контакт: support@example.ru, заказ 123"

print(f"Email валиден: {validate_email_regex(email)}")
print(f"Телефон валиден: {validate_phone_regex(phone)}")
print(f"Очищенный текст: {clean_input(raw_text)}")
print(f"Извлеченный email: {extract_email_from_text(source_text)}")
