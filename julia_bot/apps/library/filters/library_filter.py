from aiogram.types import CallbackQuery

from julia_bot.apps.library.lexicon.library_ikb_lexicon import MENU_IKB, BOOK_IKB


def book_filter(callback: CallbackQuery) -> bool:
    """Фильтр книг для redis."""
    try:
        return True if int(callback.data) else 'да что угодно'
    except ValueError:
        return False


def library_menu_filter(callback: CallbackQuery) -> bool:
    """Фильтрация callback-ов, относящихся к меню."""
    return callback.data in list(MENU_IKB.keys())


def book_list_filter(callback: CallbackQuery) -> bool:
    """Фильтрация callback-ов, относящихся к списку книг"""
    return callback.data in list(BOOK_IKB.keys())


def book_interaction_filter(callback: CallbackQuery) -> bool:
    return '=' in callback.data


def book_choice_filter(callback: CallbackQuery) -> bool:
    return callback.data.isdigit()
