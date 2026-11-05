from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
from src.database.connection import connect_to_db, count_products, get_products_page, get_product_by_id

class Product(BaseModel):
    name: str
    price: float

class UserCreate(BaseModel):
    name: str
    email: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    global conn
    conn = connect_to_db()
    yield
    if conn:
        conn.close()

app = FastAPI(lifespan=lifespan)

products =  [
    {"id": 1, "name": "Ноутбук", "price": 50000},
    {"id": 2, "name": "Мышь", "price": 1500},
{   "id": 3, "name": "Монитор", "price": 7500}]

users = [
    {"id": 1, "name": "Анна Иванова", "email": "anna@example.com"},
    {"id": 2, "name": "Иван Петров", "email": "ivan@example.com"},
    {"id": 3, "name": "Мария Смирнова", "email": "maria@example.com"},
]

@app.get("/products", status_code=200)
def get_products(limit: int = 10, offset: int = 0):
    try:
        total = count_products(conn)
        rows = get_products_page(conn, limit, offset)
        return {
            "total": total,
            "limit": limit,
            "offset": offset,
            "products": rows
            }
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")

@app.get("/products/{id}", status_code=200)
def get_products_id(id: int):
    try:
        product_by_id = get_product_by_id(conn, id)
        if product_by_id is None:
            raise HTTPException(status_code=404, detail="Товар не найден")
        return product_by_id
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")

@app.get("/users", status_code=200)
def get_user():
    try:
        return users
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")

@app.get("/users/{id}", status_code=200)
def get_user_by_id(id: int):
    try:
        for user in users:
            if user["id"] == id:
                return user
        raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")        

@app.post("/users", status_code=201)
def post_user(user: UserCreate):
    try:
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
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")

@app.post("/products", status_code=201)
def post_products(product: Product):
    try:
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
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")