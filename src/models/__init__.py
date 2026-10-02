try:
	from src.models.order import Order
	from src.models.product import Product
	from src.models.user import User
except ModuleNotFoundError:
	from .order import Order
	from .product import Product
	from .user import User

__all__ = ["Order", "Product", "User"]
