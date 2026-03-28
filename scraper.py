# facem scrape la website pentru a extrage datele de interes.
from playwright.sync_api import sync_playwright
import time, logging, os

def get_price(url,retry=3):
    for incercare in range(retry):
        try:
         with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            logging.info(f"Accesam {url} - incercare: {incercare +1}")

            page.goto(url)
            page.wait_for_load_state("load")
            price = page.locator("span.mms-ui-mBgaT").all_text_contents()
            pret_principal = price[2]
            logging.info(f"Extras pret : {price} -euro")

            return pret_principal
        
        except Exception as e:
           logging.error(f"Eroare: {e}")
           page.screenshot(path=(f"Eroare_{incercare}.png"))
           time.sleep(2)
       
    logging.error(f"Toate incercarile au esuat pentru {url}")
    return []
date = get_price("https://www.mediaworld.it/it/product/_apple-md4-187609.html")
print(f"pretul la moment este de : {date}")       


