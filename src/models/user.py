from src.models.exceptions import ValidationError

class User:

    def __init__(self, name, email):
        if "@" not in email:
            raise ValidationError("Неверный формат email")

        self.name = name
        self._email = email

    def get_info(self) -> str:
        return f"Пользователь: {self.name}, Email: {self._email}"

    def set_email(self, email):
        if "@" not in email:
            raise ValidationError("Неверный формат email")
        else:
            self._email = email