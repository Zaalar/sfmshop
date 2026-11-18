from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager
from src.database.connection import (
    connect_to_db,
    count_products, 
    get_products_page, 
    get_product_by_id, 
    update_product,
    delete_product,
    get_user_by_id,
    create_order
    )
from src.models.product import Product
from src.models.order import Order
class ProductCreate(BaseModel):
    name: str
    price: float

class UserCreate(BaseModel):
    name: str
    email: str

class ProductUpdate(BaseModel):
    name: str
    price: float

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int = Field(gt=0)

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
        result_products = []
        for row in rows:
            product = row_to_product(row)
            result_products.append(product.__dict__)

        return {
            "total": total,
            "limit": limit,
            "offset": offset,
            "products": result_products
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
        return row_to_product(product_by_id).__dict__
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
def get_user(id: int):
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
def post_products(product: ProductCreate):
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


@app.put("/products/{id}", status_code=200)
def put_poducts_by_id(id: int, product_data: ProductUpdate):
    try:
        product_row = get_product_by_id(conn, id)
        if product_row is None:
            raise HTTPException(status_code=404, detail="Товар с таким id не найден")

        update_product(conn, id, product_data.name, product_data.price)
        updated_row = get_product_by_id(conn, id)
        return row_to_product(updated_row).__dict__

    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")


@app.delete("/products/{id}", status_code=200)
def delete_products_by_id(id: int):
    try:
        deleted = delete_product(conn, id)
        if deleted is None: 
            raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Товар с таким id не найден")
        else:
            return {"message": "Товар удален"}
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")

@app.post("/orders", status_code=201)
def post_oders(order: OrderCreate):
    try:
        user = get_user_by_id(conn, order.user_id)
        product = get_product_by_id(conn, order.product_id)
        if user is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        if product is None:
            raise HTTPException(status_code=404, detail="Товар не найден")
        product_obj = Product(product[1], product[2], order.quantity)
        total = Order([product_obj]).calculate_total()
        new_order_id = create_order(conn, order.user_id, total)
        if new_order_id is None:
            raise HTTPException(status_code=500, detail="Не удалось создать заказ")
        return {"order_id": new_order_id, "total": total}
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {str(e)}")

def row_to_product(row):
    product = Product(row[1], row[2], row[3])
    product.id = row[0]
    return product


