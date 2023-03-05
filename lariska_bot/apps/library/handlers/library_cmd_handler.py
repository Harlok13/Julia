from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from lariska_bot.apps.library.keyboards.lybrary_inline_kb import CAT_CHOICE_MENU
from lariska_bot.apps.library.lexicon.library_cmd_lexicon import get_library
from lariska_bot.apps.library.lexicon.library_menu_lexicon import MENU_LEXICON


async def library_answer(message: Message) -> None:
    """Открыть меню библиотеки."""
    await message.delete()
    await message.answer(MENU_LEXICON['main_menu'],
                         reply_markup=CAT_CHOICE_MENU)


def register_library_cmd_handlers(router: Router) -> None:
    router.message.register(library_answer, Command(commands=get_library()))
