from typing import Dict, List, Tuple, Union

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from sqlalchemy import ChunkedIteratorResult

from lariska_bot.apps.library.lexicon.library_ikb_lexicon import MENU_IKB, OTHER_BUTTONS, BOOK_INFO_BUT
from lariska_bot.apps.library.utils.book_request import BookRequest



def main_menu(ikb_data: str) -> InlineKeyboardMarkup:
    """Выбор категорий."""
    main_menu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    menu: List[Union[Tuple[str, str], Tuple[int]]] = MENU_IKB[ikb_data]
    buttons: List[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=tup[0],
            callback_data=tup[1]
        ) for tup in menu[:-1]
    ]
    # if ikb_data != 'cat_choice_menu':
    #     get_prev_but = InlineKeyboardButton(
    #         text='НАЗАД',
    #         callback_data=get_prev
    #     )
    #     main_menu_builder.add(get_prev_but)

    main_menu_builder.add(*buttons)
    main_menu_builder.adjust(*menu[-1])
    return main_menu_builder.as_markup(resize_keyboard=True)


def choice_book(books_list: List[Tuple[str, int]], cb_data: str) -> InlineKeyboardMarkup:
    """Выбор книг."""
    book_menu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: List[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=title,
            callback_data=id_book
        ) for title, id_book in books_list
    ]
    print(buttons[0].callback_data, 'inodnlkdnnkldjhfkjnldkkdl;hr;k')
    book_menu_builder.add(*buttons)
    book_menu_builder.adjust(1)
    ############# хардкод ###############
    # if cb_data not in ('sql_cat', 'python_cat', 'nosql_cat'):
    #     get_prev_button: InlineKeyboardButton = InlineKeyboardButton(
    #         text='НАЗАД',
    #         callback_data='cat_choice_menu'
    #     )
    #     book_menu_builder.add(get_prev_button)
    # else:
    #     get_prev_button: InlineKeyboardButton = InlineKeyboardButton(
    #         text='ГЛАВНОЕ МЕНЮ',
    #         callback_data='cat_choice_menu'
    #     )
    #     book_menu_builder.add(get_prev_button)
    #######################################
    return book_menu_builder.as_markup(resize_keyboard=True)


def get_book_info(about_book: str) -> InlineKeyboardMarkup:

    book_info_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: List[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=tup[0],
            callback_data=f"{tup[1]}={about_book}"
        ) for tup in BOOK_INFO_BUT[:-1]
    ]
    book_info_builder.add(*buttons)
    book_info_builder.adjust(*BOOK_INFO_BUT[-1])
    return book_info_builder.as_markup(resize_keyboard=True)


def say_ty_menu():
    # если текста очень много, то создается дополнительно
    # кнопка с пагинацией
    ...


# from typing import Dict, List, Tuple, Union
#
# from aiogram.types import InlineKeyboardMarkup
# from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
# from sqlalchemy import ChunkedIteratorResult
#
# from lariska_bot.apps.library.lexicon.library_ikb_lexicon import MENU_IKB, OTHER_BUTTONS
#
#
# def library_menu_ikb(data: Dict[str, List[str]]) -> None:
#     menu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#
#
# def main_menu(ikb_data: str, get_prev: str) -> InlineKeyboardMarkup:
#     main_menu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     menu: List[Union[Tuple[str, str], Tuple[int]]] = MENU_IKB[ikb_data]
#     buttons: List[InlineKeyboardButton] = [
#         InlineKeyboardButton(
#             text=tup[0],
#             callback_data=tup[1]
#         ) for tup in menu[:-1]
#     ]
#     if ikb_data != 'cat_choice_menu':
#         get_prev_but = InlineKeyboardButton(
#             text='НАЗАД',
#             callback_data=get_prev
#         )
#         main_menu_builder.add(get_prev_but)
#
#     main_menu_builder.add(*buttons)
#     main_menu_builder.adjust(*menu[-1])
#     return main_menu_builder.as_markup(resize_keyboard=True)
#
#
# def choice_book(book_data: ChunkedIteratorResult, get_prev: str) -> InlineKeyboardMarkup:
#     print(book_data, 'choice_book func')
#     book_menu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     books: List[str] = [name[0] for name in book_data]
#     print(books)
#     buttons: List[InlineKeyboardButton] = [
#         InlineKeyboardButton(
#             text=name,
#             callback_data='some'
#         ) for name in books
#     ]
#     get_prev_but = InlineKeyboardButton(
#         text
#     )
#     print(buttons, 'buttons')
#     book_menu_builder.add(*buttons)
#     book_menu_builder.row()
#     return book_menu_builder.as_markup(resize_keyboard=True)
