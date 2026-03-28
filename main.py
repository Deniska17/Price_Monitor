from scraper import get_price
from database import init_db, save_price, get_last_price
from notifier import notify
import sqlite3


URL = "https://www.mediaworld.it/it/product/_apple-md4-187609.html"
PRODUCT = "Mac Mini M4 24GB"


def run():
    conn = sqlite3.connect("prices.db")
    init_db()

    current_price = get_price(URL)
    print(f"Current price: {current_price}")

    last_price = get_last_price(PRODUCT, conn)
    print(f"Last recorded price: {last_price}")

    if last_price and current_price < last_price:
        notify(f"🔥 Price drop! {PRODUCT}: {last_price}€ → {current_price}€")
    else:
        notify(f"📊 {PRODUCT}: {current_price}€ — no change")

    save_price(current_price, PRODUCT, conn)
    conn.close()