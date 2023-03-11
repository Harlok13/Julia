import logging

import aiohttp
from aiogram import F, Router
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from aioredis import Redis

from julia_bot.apps.library.filters.library_filter import book_filter
from julia_bot.apps.library.keyboards.lybrary_inline_kb import *
from julia_bot.apps.library.lexicon.library_menu_lexicon import MENU_LEXICON

redis = Redis()


async def callback_get_prev(callback: CallbackQuery) -> None:
    """Кнопка назад."""
    # prev = await redis.get('back')
    await callback.message.edit_text(text=MENU_LEXICON['main_menu'],
                                     reply_markup=CAT_CHOICE_MENU)


async def callback_back_to_menu(callback: CallbackQuery) -> None:
    """Кнопка вернуться в меню."""
    await callback.message.edit_text(text=MENU_LEXICON['main_menu'],
                                     reply_markup=CAT_CHOICE_MENU)


async def callback_python_cat_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории PYTHON."""
    logger = logging.getLogger(__name__)
    await callback.message.edit_text(text=MENU_LEXICON['choice_python'],
                                     reply_markup=PYTHON_CHOICE_MENU)


async def callback_db_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории БАЗЫ ДАННЫХ"""
    logger = logging.getLogger(__name__)
    await callback.message.edit_text(text=MENU_LEXICON['choice_db'],
                                     reply_markup=DB_MENU)


async def callback_nosql_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории NoSQL."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_nosql'],
                                     reply_markup=NOSQL_MENU)


async def callback_sql_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории SQL."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_sql'],
                                     reply_markup=SQL_MENU)


async def callback_sql_helper(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории SQL."""
    await callback.message.answer(text=MENU_LEXICON['choice_sql_helper'],
                                  reply_markup=TY_MENU)


async def callback_back_to_db(callback: CallbackQuery) -> None:
    """Кнопка возврата к категории БАЗЫ ДАННЫХ."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_db'],
                                     reply_markup=DB_MENU)


async def callback_back_to_pyhon(callback: CallbackQuery) -> None:
    """Кнопка возврата к категории КНИГИ ПО PYTHON."""
    await callback.message.edit_text(text=MENU_LEXICON['back_python'],
                                     reply_markup=PYTHON_CHOICE_MENU)


async def callback_git_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории GIT."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_git'],
                                     reply_markup=GIT_MENU)


async def callback_start_book_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории КНИГИ ДЛЯ СТАРТА."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_for_starts'],
                                     reply_markup=START_BOOKS_MENU)


async def callback_algorithms_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории АЛГОРИТМЫ."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_algorithms'],
                                     reply_markup=ALGORITHMS_MENU)


async def callback_linux_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории LINUX."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_linux'],
                                     reply_markup=LINUX_MENU)


async def callback_python_books_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории КНИГИ ПО PYTHON."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_python_book'],
                                     reply_markup=PYTHON_MENU)


async def callback_kids_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории ДЛЯ САМЫХ МАЛЕНЬКИХ."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_kids'],
                                     reply_markup=KIDS_MENU)


async def callback_async_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории АСИНХРОННЫЙ PYTHON."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_async'],
                                     reply_markup=ASYNC_MENU)


async def callback_django_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории DJANGO."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_django'],
                                     reply_markup=DJANGO_MENU)


async def callback_tests_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории ТЕСТИРОВАНИЕ."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_tests'],
                                     reply_markup=TESTS_MENU)


async def callback_pandas_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории PANDAS."""
    await callback.message.edit_text(text='Выберите книгу по PANDAS',
                                     reply_markup=PANDAS_MENU)


async def callback_ml_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории НЕЙРОСЕТИ."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_ml'],
                                     reply_markup=ML_MENU)


async def callback_recommendations_info(callback: CallbackQuery) -> None:
    """Кнопка для выбора категории РЕКОМЕНДАЦИИ."""
    await callback.message.edit_text(text=MENU_LEXICON['choice_recommendation'],
                                     reply_markup=RECOMMEND_MENU)
    # await callback.message.edit_text(text='Выберите книгу из рекомендаций',
    #                                  reply_markup=RECOMMEND_MENU)


async def callback_get_book(callback: CallbackQuery) -> None:
    """Получить книгу из redis."""
    call = await redis.get(callback.data)
    await redis.set('save_book', f'd{callback.data}')
    await callback.message.edit_text(text=f'{callback.data} Ваша книга :)\n{str(call).strip("b")}'.replace("'", ''),
                                     reply_markup=BOOK_MENU)


async def callback_grandfa_reviews(callback: CallbackQuery) -> None:
    """Получить отзыв от дедов."""
    # call = await redis.get(callback.data)
    await callback.message.answer(text='деды явно знают больше\nждем от них ревью :)',
                                  reply_markup=TY_MENU)


async def callback_about_book(callback: CallbackQuery) -> None:
    """Получить описание книги."""
    await callback.message.answer(text='описание в процессе)',
                                  reply_markup=ABOUT_BOOK_MENU)


async def callback_say_ty(callback: CallbackQuery) -> None:
    """Сказать спасибо и удалить сообщение."""
    await callback.message.delete()


async def close_menu(callback: CallbackQuery) -> None:  # тут должна быть цитата
    """Закрыть меню."""
    async with aiohttp.ClientSession() as session:
        async with session.get(
                'http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=ru') as resp:
            quote = await resp.json()
    await callback.message.answer(text=quote['quoteText'],
                                  reply_markup=praise_answer())
    await callback.message.delete()


async def callback_get_compliment(callback: CallbackQuery) -> None:
    """Похвалить Лариску и удалить сообщение."""
    await callback.message.delete()


async def callback_go_to_cat(callback: CallbackQuery) -> None:
    """
    Назад к категориям (из ссылки на книгу).
    хардкод вариант
    """
    print(callback.message.text)
    if callback.message.text.split()[0] in ('2',):
        await callback_nosql_info(callback)
    elif callback.message.text.split()[0] in ('11', '31', '9'):
        await callback_sql_info(callback)
    elif callback.message.text.split()[0] in ('5',):
        await callback_git_info(callback)
    elif callback.message.text.split()[0] in ('6', '21', '22', '23'):
        await callback_start_book_info(callback)
    elif callback.message.text.split()[0] in ('10',):
        await callback_algorithms_info(callback)
    elif callback.message.text.split()[0] in ('17', '20'):
        await callback_linux_info(callback)
    elif callback.message.text.split()[0] in ('3', '7', '16', '15', '18', '27',
                                              '28', '29', '36', '37'):
        await callback_python_books_info(callback)
    elif callback.message.text.split()[0] in ('4',):
        await callback_kids_info(callback)
    elif callback.message.text.split()[0] in ('1',):
        await callback_async_info(callback)
    elif callback.message.text.split()[0] in ('8', '12'):
        await callback_django_info(callback)
    elif callback.message.text.split()[0] in ('13',):
        await callback_tests_info(callback)
    elif callback.message.text.split()[0] in ('14',):
        await callback_pandas_info(callback)
    elif callback.message.text.split()[0] in ('32', '33', '30'):
        await callback_ml_info(callback)


def register_library_cb_handlers(r: Router) -> None:
    r.callback_query.register(callback_db_info, F.data == 'db_cat')
    r.callback_query.register(callback_nosql_info, F.data == 'nosql_cat')
    r.callback_query.register(callback_sql_info, F.data == 'sql_cat')
    r.callback_query.register(callback_sql_helper, F.data == 'sql_helper')
    r.callback_query.register(callback_git_info, F.data == 'git_cat')
    r.callback_query.register(callback_start_book_info, F.data == 'start_cat')
    r.callback_query.register(callback_algorithms_info, F.data == 'algorithms_cat')
    r.callback_query.register(callback_linux_info, F.data == 'linux_cat')
    r.callback_query.register(callback_python_cat_info, F.data == 'python_cat')
    r.callback_query.register(callback_python_books_info, F.data == 'pybook_cat')
    r.callback_query.register(callback_kids_info, F.data == 'kids_cat')
    r.callback_query.register(callback_async_info, F.data == 'async_cat')
    r.callback_query.register(callback_tests_info, F.data == 'tests_cat')
    r.callback_query.register(callback_django_info, F.data == 'django_cat')
    r.callback_query.register(callback_pandas_info, F.data == 'pandas_cat')
    r.callback_query.register(callback_ml_info, F.data == 'ml_cat')
    r.callback_query.register(close_menu, F.data == 'close')

    r.callback_query.register(callback_recommendations_info, F.data == 'recommendations_cat')

    r.callback_query.register(callback_get_prev, F.data == GET_PREV_DATA)
    r.callback_query.register(callback_back_to_menu, F.data == TO_MENU_DATA)

    r.callback_query.register(callback_back_to_db, F.data == 'go_db')
    r.callback_query.register(callback_back_to_pyhon, F.data == 'go_python')

    r.callback_query.register(callback_grandfa_reviews, F.data == 'grandfa_cmd')
    r.callback_query.register(callback_about_book, F.data == 'about_cmd')
    r.callback_query.register(callback_say_ty, F.data == 'ty')
    r.callback_query.register(callback_get_compliment, F.data == 'compliment')
    r.callback_query.register(callback_go_to_cat, F.data == 'go_to_cat')

    r.callback_query.register(callback_get_book, book_filter)  # должен быть последним
