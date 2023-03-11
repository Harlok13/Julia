from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TY_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='СПАСИБО!', callback_data='ty_main')]
    ]
)
