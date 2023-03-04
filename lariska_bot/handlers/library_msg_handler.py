from aiogram import Router, F
from aiogram.types import Message

from lariska_bot.keyboards.lybrary_inline_kb import CAT_CHOICE_MENU


async def get_library(message: Message):
    await message.answer(text='Выберите категорию:',
                         reply_markup=CAT_CHOICE_MENU)
    await message.delete()


def register_library_msg_handlers(router: Router):
    router.message.register(get_library, F.text == 'БИБЛИОТЕКА')
