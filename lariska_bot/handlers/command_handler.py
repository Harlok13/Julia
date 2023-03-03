from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command

from lariska_bot.handlers.handlers_data.commands import *
from lariska_bot.handlers.handlers_data.messages import *
from lariska_bot.keyboards.reply_keyboard import *

router = Router()


async def repo_answer(message: Message):
    await message.answer(get_repo())


async def youtube_answer(message: Message):
    await message.answer(get_youtube())


async def send_welcome(message: Message):
    await message.delete()
    await message.answer(get_welcome(),
                         parse_mode='MARKDOWN',
                         reply_markup=MENU_BOARD)


def register_command_handler(router: Router):
    router.message.register(repo_answer, Command(commands=get_repo_list()))
    router.message.register(youtube_answer, Command(commands=get_video_list()))
    router.message.register(send_welcome, Command(commands=['start', 'help']))
