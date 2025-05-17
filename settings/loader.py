import os

from dotenv import load_dotenv

load_dotenv()

# SQLite
SQL_LITE_URL = os.getenv("SQL_LITE_URL")

# Aiogram
BOT_TOKEN = os.getenv("BOT_TOKEN")

os.makedirs("uploads", exist_ok=True)
