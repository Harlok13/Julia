import logging
from pprint import pprint
from typing import Any, Callable, Dict, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import sessionmaker

from julia_bot.data.schemas.user import User


class UserRegisterCheck(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        logger = logging.getLogger(__name__)
        session_maker: sessionmaker = data['session_maker']
        async with session_maker() as session:
            async with session.begin():
                result: ScalarResult = await session.execute(  # type: ignore
                    select(User).where(User.user_id == event.from_user.id))  # type: ignore
                user: User = result.one_or_none()

                if user is not None:
                    logger.info(f'Пользователь {event.from_user.username} уже зарегистрирован')
                else:
                    user: User = User(
                        user_id=event.from_user.id,
                        username=event.from_user.username,
                        user_nickname=event.from_user.first_name
                    )
                    await session.merge(user)
                    logger.info(f'Пользователь {event.from_user.username} зарегистрирован')

        return await handler(event, data)
