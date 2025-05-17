from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from settings.loader import SQL_LITE_URL

engine = create_async_engine(SQL_LITE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)
