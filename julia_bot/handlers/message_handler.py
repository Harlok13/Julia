import asyncio
from pprint import pprint

from aiogram import Router, types, F, Bot
from aiogram.filters import Text
from aiogram.types import Message

from julia_bot.handlers.handlers_data.messages import *


# from lariska_bot.text_recogn_start import *


async def skirmish_reply(message: Message):
    await message.reply(USER_MSG['dont_skirmish'])


async def call_names_reply(message: Message):
    await message.reply(USER_MSG['dont_call_names'])


async def attack_reply(message: Message):
    await message.reply(USER_MSG['get_attack_reply'])


async def hello_where_to_reply(message: Message):
    await message.reply(USER_MSG['get_hello'])
    await message.answer(USER_MSG['get_start_here'])
    await message.answer(USER_MSG['get_start_video'])
    await message.answer(USER_MSG['about_links'])


async def hello_reply(message: Message, bot: Bot):
    await message.reply(USER_MSG['get_hello'])
    print(message.chat.id)
    await asyncio.sleep(5)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id+1)


async def where_to_begin(message: Message):
    await message.reply(USER_MSG['get_start_here'])
    await message.answer(USER_MSG['get_start_video'])
    await message.answer(USER_MSG['about_links'])


async def our_repository_reply(message: Message):
    await message.reply(USER_MSG['get_repo'])


async def our_repo_reply(message: Message):
    await message.reply(USER_MSG['get_repo'])


async def lariska_bot_reply(message: Message):
    await message.reply(USER_MSG['get_lariska_bot'])
    await message.answer(USER_MSG['get_forks'])


# aiogram2
# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# @dp.throttled(flood_controlling, rate=5)
# async def text_reply(message: types.Message):
#     username = message.from_user.username
#     user_dict = USERS.get(username)
#
#     tz = pytz.timezone('Europe/Moscow')
#     present_date = datetime.now(tz)
#     present_date += timedelta(hours=5)
#     present_day = present_date.day
#
#     if user_dict and user_dict['day'] != present_day:
#         user_dict['day'] = present_day
#         await message.reply(random.choice(user_dict['greetings']))


async def photo_reply(message: types.Message, bot: Bot):
    await bot.download(message.photo[-1].file_id, 'img.jpg')
    model = keras.models.load_model('emnist_letters.h5')
    s_out = img_to_str(model, "img.jpg")
    s_out = str(s_out)
    try:
        if s_out[0].isalpha() or s_out[0].isdigit():
            await message.reply('Красивенько 😍')
    except IndexError:
        await message.reply('тут пусто')


def register_message_handlers(r: Router) -> None:
    r.message.register(skirmish_reply, Text(contains=['говно'], ignore_case=True))
    r.message.register(call_names_reply, Text(contains=['лариска', 'дура'], ignore_case=True))
    r.message.register(attack_reply, Text(contains=['лариска', 'фас'], ignore_case=True))
    r.message.register(hello_where_to_reply, Text(contains=['привет', 'с чего начать'], ignore_case=True))
    r.message.register(hello_reply, Text(contains=['привет'], ignore_case=True))
    r.message.register(where_to_begin, Text(contains=['с чего начать'], ignore_case=True))
    r.message.register(our_repository_reply, Text(contains=['наш репозиторий'], ignore_case=True))
    r.message.register(our_repo_reply, Text(contains=['наша репа'], ignore_case=True))
    r.message.register(lariska_bot_reply, Text(contains=['лариска', 'бот'], ignore_case=True))
    r.message.register(where_to_begin, Text(contains=['с чего начать'], ignore_case=True))
    r.message.register(photo_reply, F.photo)
