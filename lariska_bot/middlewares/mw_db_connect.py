from typing import Callable, Awaitable, Dict, Any
import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from lariska_bot.utils.db_connect import Request


class DbSession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        async with self.connector.acquire() as conn:
            data['request'] = Request(conn)
            return await handler(event, data)
