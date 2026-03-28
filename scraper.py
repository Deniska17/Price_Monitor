from playwright.sync_api import sync_playwright
import time
import logging


def get_price(url, retry=3):
    for attempt in range(retry):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()
                page = context.new_page()

                logging.info(f"Fetching {url} - attempt {attempt + 1}")

                page.goto(url)
                page.wait_for_load_state("load")

                prices = page.locator("span.mms-ui-mBgaT").all_text_contents()
                price = prices[2]

                logging.info(f"Price found: {price}")
                return price

        except Exception as e:
            logging.error(f"Error on attempt {attempt + 1}: {e}")
            time.sleep(2)

    logging.error(f"All attempts failed for {url}")
    return None