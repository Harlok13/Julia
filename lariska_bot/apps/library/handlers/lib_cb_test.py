from typing import List, Tuple

import aiohttp
from aiogram import Router, F
from aiogram.types import CallbackQuery

from lariska_bot.apps.library.filters.library_filter import library_menu_filter, book_list_filter, \
    book_interaction_filter, book_choice_filter
from lariska_bot.apps.library.keyboards.lybrary_inline_kb import praise_answer
from lariska_bot.apps.library.keyboards.test_ikb import main_menu, choice_book, get_book_info
from lariska_bot.apps.library.lexicon.library_menu_lexicon import MENU_LEXICON
from lariska_bot.apps.library.utils.book_request import BookRequest


async def library_menu_cb(callback: CallbackQuery, ikb_data: str) -> None:
    """Меню выбора категории."""
    await callback.message.edit_text(text=MENU_LEXICON[ikb_data],
                                     reply_markup=main_menu(ikb_data))


async def book_menu_cb(callback: CallbackQuery, request: BookRequest) -> None:
    """Меню выбора книги."""
    books_list: List[Tuple[str, int]] = await request.db_get_books_list()
    cb_data: str = request.cb_data
    await callback.message.edit_text(text=MENU_LEXICON[callback.data],
                                     reply_markup=choice_book(books_list, cb_data))


async def book_info_cb(callback: CallbackQuery, request: BookRequest) -> None:
    """Получить книгу."""
    book: str = await request.db_get_book_link()
    about_book: str = request.cb_data
    print(book, 'book_info_cb')
    await callback.message.edit_text(text=f'Ваша книга: \n{book}',
                                     reply_markup=get_book_info(about_book))


async def book_interaction_cb(callback: CallbackQuery, request: BookRequest) -> None:
    """Взаимодействие с книгой (описание, отзывы, содержание и пр.)."""
    field, title = request.cb_data.split('=')
    action: str = await request.db_book_interaction(field, title)
    await callback.message.answer(text=action)


# это вынести отдельно. разделить сессию и апишку
async def close_menu_cb(callback: CallbackQuery) -> None:  # тут должна быть цитата
    """Закрыть меню."""
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=ru') as resp:
            quote = await resp.json()
    await callback.message.answer(text=quote['quoteText'],
                                  reply_markup=praise_answer())
    await callback.message.delete()


def register_library_cb_handler(router: Router) -> None:
    router.callback_query.register(library_menu_cb, library_menu_filter)
    router.callback_query.register(book_menu_cb, book_list_filter)
    router.callback_query.register(book_interaction_cb, book_interaction_filter)
    router.callback_query.register(close_menu_cb, F.data == 'close')
    router.callback_query.register(book_info_cb, book_choice_filter)
