from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from julia_bot.apps.library.keyboards.lybrary_inline_kb import main_menu
from julia_bot.apps.library.lexicon.library_cmd_lexicon import get_library
from julia_bot.apps.library.lexicon.library_menu_lexicon import MENU_LEXICON


async def library_answer(message: Message) -> None:
    """Открыть меню библиотеки."""
    await message.delete()
    await message.answer(MENU_LEXICON['cat_choice_menu'],
                         reply_markup=main_menu('cat_choice_menu'))


def register_library_cmd_handlers(router: Router) -> None:
    router.message.register(library_answer, Command(commands=get_library()))
