from aiogram.types import CallbackQuery


def book_filter(callback: CallbackQuery) -> bool:
    """Фильтр книг для redis."""
    try:
        return True if int(callback.data) else 'да что угодно'
    except ValueError:
        return False
