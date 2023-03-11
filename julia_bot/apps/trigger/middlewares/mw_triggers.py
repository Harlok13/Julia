import logging
from typing import Awaitable, Any, Dict, Callable

from aiogram import BaseMiddleware
from aiogram.filters import CommandObject
from aiogram.types import Message, TelegramObject
from sqlalchemy.orm import sessionmaker

from julia_bot.apps.trigger.utils.db_connect import Request


class Trigger(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        logger = logging.getLogger(__name__)
        session_maker: sessionmaker = data['session_maker']
        async with session_maker() as session:
            data['request'] = Request(session)

            return await handler(event, data)
