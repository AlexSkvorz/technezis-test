import asyncio

from aiogram import Bot, Dispatcher

from app.handlers import handle_doc, ping
from settings.loader import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(ping.router)
    dp.include_router(handle_doc.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
