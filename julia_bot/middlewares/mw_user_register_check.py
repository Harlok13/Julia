import datetime
import logging
from typing import Any, Callable, Dict, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aioredis import Redis
from sqlalchemy import select, ScalarResult, update
from sqlalchemy.orm import sessionmaker

from julia_bot.data.schemas.user import User
from julia_bot.data.user_register import is_user_exists, register_user

logger = logging.getLogger(__name__)


class UserRegisterCheck(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data['session_maker']
        redis: Redis = data['redis']

        if await is_user_exists(
                event.from_user.id,
                event.from_user.first_name,
                redis
        ):
            pass
        else:
            await register_user(
                session_maker,
                event.from_user.id,
                event.from_user.username,
                event.from_user.first_name,
                redis
            )

        return await handler(event, data)
