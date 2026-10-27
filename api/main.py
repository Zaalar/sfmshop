from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

app = FastAPI()

products =  [
    {"id": 1, "name": "Ноутбук", "price": 50000},
    {"id": 2, "name": "Мышь", "price": 1500},
{   "id": 3, "name": "Монитор", "price": 7500}]

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product
    else:
        raise HTTPException(status_code=404, detail="Товар не найден")
