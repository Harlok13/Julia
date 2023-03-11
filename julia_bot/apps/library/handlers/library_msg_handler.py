from aiogram import Router, F
from aiogram.types import Message

from julia_bot.apps.library.keyboards.lybrary_inline_kb import CAT_CHOICE_MENU
from julia_bot.apps.library.lexicon.library_menu_lexicon import MENU_LEXICON


async def get_library_menu(message: Message) -> None:
    """Открыть меню библиотеки."""
    await message.delete()
    await message.answer(text=MENU_LEXICON['main_menu'],
                         reply_markup=CAT_CHOICE_MENU)


def register_library_msg_handlers(router: Router) -> None:
    router.message.register(get_library_menu, F.text == 'БИБЛИОТЕКА')
