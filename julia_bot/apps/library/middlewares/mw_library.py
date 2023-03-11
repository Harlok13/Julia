import logging
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from sqlalchemy.orm import sessionmaker

from julia_bot.apps.library.lexicon.library_ikb_lexicon import MENU_IKB, BOOK_IKB
from julia_bot.apps.library.utils.book_request import BookRequest


class LibraryMenu(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        logger = logging.getLogger(__name__)
        session_maker: sessionmaker = data['session_maker']

        # генерация категорий меню
        if event.data in list(MENU_IKB.keys()):
            try:
                data['ikb_data'] = event.data
                logger.info(f"{data['ikb_data']}")
                print(data['ikb_data'], 'mw_library')
            except AttributeError as exc:
                logger.error(exc)

        # генерация меню с книгами
        elif event.data in list(BOOK_IKB.keys()):
            async with session_maker() as session:
                data['request'] = BookRequest(session, event.data)

        # сработает в случае, если cb data будет названием книги
        elif event.data.isdigit():
            async with session_maker() as session:
                data['request'] = BookRequest(session, event.data)
                # data['about_book_mw'] = event.data
        return await handler(event, data)  # type: ignore
