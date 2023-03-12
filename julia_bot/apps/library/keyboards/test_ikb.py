import random
from typing import Dict, List, Tuple, Union, Optional

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from sqlalchemy import ChunkedIteratorResult

from julia_bot.apps.library.lexicon.library_ikb_lexicon import MENU_IKB, BOOK_INFO_BUT, GO_MAIN_MENU, \
    TY_BUTTONS
from julia_bot.apps.library.utils.book_request import BookRequest


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
    book_menu_builder.add(*buttons)
    # как отрефакторить?
    book_menu_builder.row(InlineKeyboardButton(text='НАЗАД', callback_data='cat_choice_menu'))
    book_menu_builder.adjust(1)
    return book_menu_builder.as_markup(resize_keyboard=True)


def get_book_info(book_id: str, db_book_cb: str) -> InlineKeyboardMarkup:
    """Взаимодействие с книгой (отзывы, содержание и т.д.)."""
    book_info_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: List[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=tup[0],
            callback_data=f"{tup[1]}={book_id}"
        ) for tup in BOOK_INFO_BUT[:-1]
    ]
    book_info_builder.add(*buttons)
    # как отрефакторить?
    book_info_builder.row(InlineKeyboardButton(text='НАЗАД', callback_data=db_book_cb))
    book_info_builder.row(InlineKeyboardButton(text=GO_MAIN_MENU['title'], callback_data=GO_MAIN_MENU['cb_data']))
    book_info_builder.adjust(*BOOK_INFO_BUT[-1])
    return book_info_builder.as_markup(resize_keyboard=True)


def say_ty_menu(answer: str, pagination=None) -> InlineKeyboardMarkup:
    """  # , pagination: Optional[str, Dict[int, str]] = None
    Закрыть сообщение. Если текста много, то создается пагинация.
    :param pagination: give a dictionary with text to create pagination
    :param answer: required, must be 'ty_cmd' or 'praise_cmd'. responsible for button text
    :return: a button that closes the message or, if the text is long, then
     also a button with pagination
    """
    ty_menu_build: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ty_button: InlineKeyboardButton = InlineKeyboardButton(
        text=random.choice(TY_BUTTONS[answer]),
        callback_data='del_cmd'  # ref
    )
    ty_menu_build.row(ty_button)
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
