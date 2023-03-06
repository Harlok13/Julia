from typing import Union

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

#
# def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
#     return _create_async_engine(url=url, echo=True, pool_pre_ping=True)
#
#
# async def proceed_schemas(engine: AsyncEngine, metadata: MetaData) -> None:
#     """
#
#     :param engine:
#     :param metadata:
#     :return:
#     """
#     # with engine.connect() as conn:
#     #     conn.run_sync(metadata.create_all())
#     ...
#
#
# def get_session_maker(engine: AsyncEngine) -> sessionmaker:
#     return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
def create_async_engine(url: Union[URL, str]) -> AsyncEngine:
    return _create_async_engine(url=url, echo=True, pool_pre_ping=True)


async def proceed_schemas(engine: AsyncEngine, metadata: MetaData) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)
