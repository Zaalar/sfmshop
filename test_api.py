from fastapi.testclient import TestClient
from src.api.main import app


def test_get_products(client):
    response = client.get("/products")   
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert "total" in data

def test_get_product_by_id(client):
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404

def test_post_orders(client):
    response = client.post("/orders", json={"user_id": 1, "product_id": 2, "quantity": 2})
    assert response.status_code == 201
    data = response.json()
    assert data["total"] == 3000

def test_post_orders_bad_user(client):
    response = client.post("/orders", json={"user_id": 999, "product_id": 2, "quantity": 2})
    assert response.status_code == 404

def test_post_orders_bad_quantity(client):
    response = client.post("/orders", json={"user_id": 1, "product_id": 2, "quantity": -1})
    assert response.status_code == 422


if __name__ == "__main__":
    with TestClient(app) as client:
        test_get_products(client)
        test_get_product_by_id(client)
        test_get_product_not_found(client)
        test_post_orders(client)
        test_post_orders_bad_user(client)
        test_post_orders_bad_quantity(client)
        print("OK")