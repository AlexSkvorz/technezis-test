from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemes.source_schemes import CreateSourceSchema
from database.models import Source


async def create_source(sources: list[CreateSourceSchema], session: AsyncSession):
    await session.execute(insert(Source), [s.model_dump(mode="json") for s in sources])
    await session.commit()
