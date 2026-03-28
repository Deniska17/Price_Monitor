import telegram
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


async def send_message(text):
    bot = telegram.Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)


def notify(text):
    asyncio.run(send_message(text))