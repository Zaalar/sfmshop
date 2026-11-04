from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float

class UserCreate(BaseModel):
    name: str
    email: str

app = FastAPI()

products = [
    {"id": 1, "name": "Ноутбук", "price": 50000},
    {"id": 2, "name": "Мышь", "price": 1500},
{   "id": 3, "name": "Монитор", "price": 7500}]

users = [
    {"id": 1, "name": "Анна Иванова", "email": "anna@example.com"},
    {"id": 2, "name": "Иван Петров", "email": "ivan@example.com"},
    {"id": 3, "name": "Мария Смирнова", "email": "maria@example.com"},
]

@app.get("/products")
def get_products(limit: int = 10, offset: int = 0):
    result_products = products[offset: offset + limit]
    return {"products": result_products, "limit": limit, "offset": offset}
@app.get("/products/{id}")
def get_products_id(id: int):
    for product in products:
        if product["id"] == id:
            return product
    raise HTTPException(status_code=404, detail="Товар не найден")

@app.get("/users")
def get_user():
    return users

@app.get("/users/{id}")
def get_user_by_id(id: int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")

@app.post("/users", status_code=201)
def post_user(user: UserCreate):
    id = 0
    for existing_user in users:
        if existing_user["id"] > id:
            id = existing_user["id"]
    new_user =  {
        "id": id + 1,
        "name": user.name,
        "email": user.email
        }
    users.append(new_user)
    return new_user

@app.post("/products", status_code=201)
def post_products(product: Product):
    id = 0
    for existing_product in products:
        if existing_product["id"] > id:
            id = existing_product["id"]
    new_product =  {
        "id": id + 1,
        "name": product.name,
        "price": product.price
        }
    products.append(new_product)
    return new_product