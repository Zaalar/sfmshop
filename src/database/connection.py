import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    password = os.getenv("DB_PASSWORD")
    conn = psycopg2.connect(
        host="localhost",
        database="sfmshop",
        user="postgres",
        password=password
    )
    return conn
conn = connect_to_db()
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
    ('Ноутбук',  50000.00, 10)
)
conn.commit()
print("Товар добавлен: Ноутбук, 50000.00, 10")

cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

print('Все товары:')
for product in products:
    print(product)

cursor.execute(
    "UPDATE products SET price = %s WHERE id = %s",
    (45000.00, 1)
)

conn.commit()

print ("Цена обновлена: 45000.00")
cursor.close()
conn.close()