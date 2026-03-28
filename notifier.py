import telegram,asyncio,os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API = os.getenv("TELEGRAM_API")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def trimite_mesaj(mesaj):
    bot = telegram.Bot(token = TELEGRAM_API)
    await bot.send_message(chat_id=CHAT_ID,text=mesaj)

def notifica(mesaj):
    asyncio.run(trimite_mesaj(mesaj))

notifica("Price monitor functioneaza!!!")    