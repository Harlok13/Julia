from aiogram import Router, types, F, Bot
from aiogram.filters import Text
from aiogram.types import Message

from lariska_bot.handlers.handlers_data.messages import *
from lariska_bot.keyboards.lybrary_inline_kb import *
# from lariska_bot.text_recogn_start import *

r = Router()


async def get_library(message: types.Message):
    await message.answer(text='Выберите категорию:',
                         reply_markup=CAT_CHOICE_MENU)
    await message.delete()


async def skirmish_reply(message: Message):
    await message.reply(user_mes['dont_skirmish'])


async def call_names_reply(message: Message):
    await message.reply(user_mes['dont_call_names'])


async def attack_reply(message: Message):
    await message.reply(user_mes['get_attack_reply'])


async def hello_where_to_reply(message: Message):
    await message.reply(user_mes['get_hello'])
    await message.answer(user_mes['get_start_here'])
    await message.answer(user_mes['get_start_video'])
    await message.answer('Там много полезных ссылок под видео.')


async def hello_reply(message: Message):
    await message.reply(user_mes['get_hello'])


async def where_to_begin(message: Message):
    await message.reply(user_mes['get_start_here'])
    await message.answer(user_mes['get_start_video'])
    await message.answer(user_mes['about_links'])


async def our_repository_reply(message: Message):
    await message.reply(user_mes['get_repo'])


async def our_repo_reply(message: Message):
    await message.reply(user_mes['get_repo'])


async def lariska_bot_reply(message: Message):
    await message.reply(user_mes['get_lariska_bot'])
    await message.answer(user_mes['get_forks'])


# aiogram2
# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# @dp.throttled(flood_controlling, rate=5)
# async def text_reply(message: types.Message):
#     username = message.from_user.username
#     user_dict = users.get(username)
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


def register_message_handlers(r: Router):
    r.message.register(get_library, F.text == 'БИБЛИОТЕКА')

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
