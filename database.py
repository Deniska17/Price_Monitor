import sqlite3
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("price_monitor.log"),
        logging.StreamHandler()
    ]
)


def init_db():
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            price REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_price(price, product, conn):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO prices (product, price) VALUES (?, ?)
    """, (product, price))
    conn.commit()
    logging.info(f"Price saved: {price} for {product}")


def get_last_price(product, conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT price FROM prices
        WHERE product = ?
        ORDER BY created_at DESC
        LIMIT 1
    """, (product,))
    result = cursor.fetchone()
    return result[0] if result else None