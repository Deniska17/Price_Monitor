import sqlite3,logging
from scraper import get_price
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("playwright.log"),
        logging.StreamHandler()
    ]
)


def init_db():
    conn = sqlite3.connect("prices.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prices(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   produs TEXT,
                   pret REAL,
                   data_adaugare TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )
""")
    conn.commit()
    conn.close()


def save_price(pret,produs,conn):
    cursor = conn.cursor()    
    cursor.execute("""
INSERT INTO prices(produs,pret)VALUES(?,?)
""",(pret,produs,))
    logging.info(f"Pret salvat: {pret} pentru produs:{produs}")

def get_last_price(produs,conn):
    cursor = conn.cursor()
    cursor.execute("""
SELECT pret FROM prices
WHERE produs = ?
ORDER BY data_adaugare DESC
LIMIT 1                    
""",(produs,))
    rezultat = cursor.fetchone()
    return rezultat[0] if rezultat else None
