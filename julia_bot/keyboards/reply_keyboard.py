from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, WebAppInfo

MENU_BOARD: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='выберите действие',
    keyboard=[
        [KeyboardButton(text='БИБЛИОТЕКА')],
        [KeyboardButton(text='НАША РЕПА', web_app=WebAppInfo(url='https://github.com/OldCodersClub/faq'))],

    ]
)
