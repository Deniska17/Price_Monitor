from scraper import get_price
from database import init_db, save_price, get_last_price
import sqlite3
from notifier import notifica
# Config
URL_MAC_MINI = "https://www.mediaworld.it/it/product/_apple-md4-187609.html"
PRODUS = "Mac Mini M4"
def ruleaza():
# Init DB
 conn = sqlite3.connect("prices.db")
 init_db()

# Scrape preț
 pret_curent = get_price(URL_MAC_MINI)
 print(f"Preț curent: {pret_curent}")

# Ultimul preț din DB
 pret_anterior = get_last_price(PRODUS, conn)

 if pret_anterior and pret_curent < pret_anterior:
    notifica(f"🔥 Preț scăzut! {PRODUS}: {pret_anterior}€ → {pret_curent}€")
 else:
    notifica(f"📊 Preț actual {PRODUS}: {pret_curent}€ — fără modificări")

 print(f"Preț anterior: {pret_anterior}")

# Salvează prețul curent
 save_price(pret_curent, PRODUS, conn)

 conn.close()