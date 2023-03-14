from typing import List, Tuple

import aiohttp
from aiogram import Router, F
from aiogram.types import CallbackQuery

from julia_bot.apps.library.filters.library_filter import (
    library_menu_filter,
    book_list_filter,
    book_interaction_filter,
    book_choice_filter)
from julia_bot.apps.library.keyboards.lybrary_inline_kb import main_menu, choice_book, get_book_info, say_ty_menu, \
    get_pagination_ikb
from julia_bot.apps.library.lexicon.library_menu_lexicon import MENU_LEXICON, PAGINATION
from julia_bot.apps.library.utils.book_request import BookRequest
from julia_bot.apps.library.utils.library_textwrapper import get_pages_dict


async def library_menu_cb(callback: CallbackQuery, ikb_data: str) -> None:
    """Меню выбора категории."""
    await callback.message.edit_text(text=MENU_LEXICON[ikb_data],
                                     reply_markup=main_menu(ikb_data))


async def book_menu_cb(callback: CallbackQuery, request: BookRequest, prev: str) -> None:
    """Меню выбора книги."""
    books_list: List[Tuple[str, int]] = await request.db_get_books_list()
    await callback.message.edit_text(text=MENU_LEXICON[callback.data],
                                     reply_markup=choice_book(books_list, prev))


async def book_info_cb(callback: CallbackQuery, request: BookRequest) -> None:
    """Получить книгу."""
    book: str = await request.db_get_book_link()
    book_id: str = request.cb_data
    db_book_cb: str = await request.db_get_prev(callback.data)
    await callback.message.edit_text(text=f'Ваша книга: \n{book}',
                                     reply_markup=get_book_info(book_id, db_book_cb))


async def book_interaction_cb(callback: CallbackQuery, request: BookRequest) -> None:
    """Взаимодействие с книгой (описание, отзывы, содержание и пр.)."""
    field, book_id = request.cb_data.split('=')
    action: str = await request.db_book_interaction(field, book_id)
    global dict_with_pages
    max_size_page: int = 500
    dict_with_pages = get_pages_dict(action, max_size_page, field[0])
    await callback.message.answer(text=dict_with_pages[f'{field[0]}1'],
                                  reply_markup=say_ty_menu('ty_cmd', field[0], dict_with_pages))


# ref
async def get_pagination_cb(callback: CallbackQuery) -> None:
    """Управление пагинацией."""
    global dict_with_pages
    if callback.data != 's999' and callback.data != 's0':
        try:
            await callback.message.edit_text(text=dict_with_pages[callback.data],
                                             reply_markup=get_pagination_ikb(callback, dict_with_pages))
        except KeyError:
            await callback.answer(PAGINATION['error'])
    elif callback.data == 's0':
        await callback.answer(PAGINATION['count_pages'])
    else:
        await callback.answer(PAGINATION['last_page'])


# это вынести отдельно. разделить сессию и апишку
async def close_menu_cb(callback: CallbackQuery) -> None:
    """Закрыть меню."""
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=ru') as resp:
            quote = await resp.json()
    await callback.message.answer(text=f"{quote['quoteText']} 👱🏻‍♀",
                                  reply_markup=say_ty_menu('praise_cmd'))
    await callback.message.delete()


async def del_message_cb(callback: CallbackQuery) -> None:
    """Удалить сообщение, нажав на кнопку."""
    await callback.message.delete()


async def about_sql_helper_cb(callback: CallbackQuery):
    """Подробнее о мобильном приложении."""
    await callback.message.answer(text=MENU_LEXICON[callback.data],
                                  reply_markup=say_ty_menu('ty_cmd'))


def register_library_cb_handlers(router: Router) -> None:
    router.callback_query.register(library_menu_cb, library_menu_filter)
    router.callback_query.register(book_menu_cb, book_list_filter)
    router.callback_query.register(book_interaction_cb, book_interaction_filter)
    router.callback_query.register(close_menu_cb, F.data == 'close')  # ref
    router.callback_query.register(del_message_cb, F.data == 'del_cmd')  # ref
    router.callback_query.register(book_info_cb, book_choice_filter)
    router.callback_query.register(about_sql_helper_cb, F.data == 'sql_helper')  # ref
    router.callback_query.register(get_pagination_cb)  # ref
