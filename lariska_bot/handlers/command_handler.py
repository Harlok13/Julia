from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command, CommandStart

from lariska_bot.handlers.handlers_data.commands import *
from lariska_bot.handlers.handlers_data.help_message import HELP_MSG
from lariska_bot.handlers.handlers_data.messages import *
from lariska_bot.keyboards.inline_keyboard import TY_MENU
from lariska_bot.keyboards.reply_keyboard import *


async def repo_answer(message: Message) -> None:
    """Получить ссылку на репозиторий."""
    await message.delete()
    await message.answer(USER_MSG['get_repo'],
                         reply_markup=TY_MENU)


async def youtube_answer(message: Message) -> None:
    """Получить ссылку на ютуб."""
    await message.delete()
    await message.answer(USER_MSG['get_youtube'],
                         reply_markup=TY_MENU)


async def send_welcome(message: Message) -> None:
    """Отправить приветственное сообщение."""
    await message.delete()
    await message.answer(USER_MSG['get_welcome'],
                         parse_mode='MARKDOWN',
                         reply_markup=MENU_BOARD)


async def help_answer(message: Message) -> None:
    """Отправить сообщение с помощью по боту."""
    await message.delete()
    await message.answer(HELP_MSG,
                         parse_mode='MARKDOWN',
                         reply_markup=TY_MENU)


async def aboutme_answer(message: Message) -> None:
    """Отправить местоположение Лариски."""
    await message.delete()
    await message.answer(USER_MSG['about_lariska_home'],
                         parse_mode='MARKDOWN',
                         reply_markup=TY_MENU)


def register_command_handler(router: Router) -> None:
    router.message.register(repo_answer, Command(commands=get_repo_list()))
    router.message.register(youtube_answer, Command(commands=get_video_list()))
    router.message.register(help_answer, Command(commands='help'))
    router.message.register(aboutme_answer, Command(commands='aboutme'))
    router.message.register(send_welcome, CommandStart())
