from aiogram import Bot, F, Router
from aiogram.types import Document, Message

from app.services.excel_service import parse_excel
from database.core import async_session
from database.crud import create_source

router = Router()


@router.message(F.document)
async def handle_document(msg: Message, bot: Bot):
    document: Document = msg.document

    if not document.file_name.endswith(".xlsx"):
        await msg.reply("Некорректный формат. Пришлите Excel-файл")
        return

    path = f"uploads/{document.file_name}"
    file = await bot.get_file(file_id=document.file_id)
    await bot.download_file(file_path=file.file_path, destination=path)

    try:
        sources = await parse_excel(file_path=path)

        await msg.reply("Содержимое файла:")

        for source in sources:
            await msg.reply(f"title: {source.title}\nurl: {source.url}\nxpath: {source.xpath}")

        async with async_session() as session:
            await create_source(sources=sources, session=session)

        await msg.reply("Данные успешно сохранены в БД")
    except Exception as e:
        await msg.reply(f"Ошибка при обработке файла: {e}")
