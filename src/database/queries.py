import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

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

def get_user_order_history(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
    """)