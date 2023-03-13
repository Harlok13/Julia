import random
from pprint import pprint
from typing import Dict, List, Tuple, Union, Optional

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from julia_bot.apps.library.lexicon.library_ikb_lexicon import MENU_IKB, BOOK_INFO_BUT, GO_MAIN_MENU, \
    TY_BUTTONS


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


def choice_book(books_list: List[Tuple[str, int]], prev: str) -> InlineKeyboardMarkup:
    """Выбор книг."""
    # если в списке больше 6 книг, то добавить пагинацию
    book_menu_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: List[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=title,
            callback_data=id_book
        ) for title, id_book in books_list
    ]
    book_menu_builder.add(*buttons)
    # как отрефакторить?
    book_menu_builder.row(InlineKeyboardButton(text='НАЗАД', callback_data=prev))
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


# ref
def say_ty_menu(answer: str, pagination=None) -> InlineKeyboardMarkup:
    """  # , pagination: Optional[str, Dict[int, str]] = None
    Закрыть сообщение. Если текста много, то создается пагинация.
    :param pagination: give a dictionary with text to create pagination
    :param answer: required, must be 'ty_cmd' or 'praise_cmd'. responsible for button text
    :return: a button that closes the message or, if the text is long, then
     also a button with pagination
    """
    pprint(pagination)
    ty_menu_build: InlineKeyboardBuilder = InlineKeyboardBuilder()
    ty_button: InlineKeyboardButton = InlineKeyboardButton(
        text=random.choice(TY_BUTTONS[answer]),
        callback_data='del_cmd'  # ref
    )
    ty_menu_build.row(ty_button)
    # если текста очень много, то создается дополнительно
    # кнопка с пагинацией

    text_but = {  #ref
        'backward': '<<',
        'forward': '>>'
    }
    if len(pagination) > 1:
        prev = InlineKeyboardButton(text=text_but['backward'], callback_data='2')
        next = InlineKeyboardButton(text=text_but['forward'], callback_data='2')
        count = InlineKeyboardButton(text=f'1/{len(pagination)}', callback_data='2')
        ty_menu_build.row(prev).add(count).add(next)

    return ty_menu_build.as_markup(resize_keyboard=True)
