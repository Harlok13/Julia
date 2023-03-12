import logging

from aiogram.types import Message
from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart

from julia_bot.handlers.handlers_data.commands import *
from julia_bot.handlers.handlers_data.help_message import HELP_MSG
from julia_bot.handlers.handlers_data.messages import *
from julia_bot.keyboards.inline_keyboard import TY_MENU
from julia_bot.keyboards.reply_keyboard import *


async def commands_answer(message: Message) -> None:
    """Ответить на команды."""
    await message.delete()
    await message.answer(text=COMMANDS_ANSWER[message.text.strip('/')],
                         # parse_mode='HTML',
                         reply_markup=TY_MENU)  # ref kb?


async def help_answer(message: Message) -> None:
    """Отправить сообщение с помощью по боту."""
    await message.delete()
    await message.answer(HELP_MSG,
                         # parse_mode='MARKDOWN',
                         reply_markup=TY_MENU)

async def feedback_answer(message: Message, bot: Bot) -> None:
    """Отправить сообщение с помощью по боту."""
    logging.basicConfig(
        level='INFO',
        filename='feedback.log'
    )
    logger = logging.getLogger(__name__)
    logger.info(message.text)
    await message.answer(f"Спасибо, {message.from_user.first_name}, ваше сообщение успешно отправлено!",
                         # parse_mode='MARKDOWN',
                         reply_markup=TY_MENU)


def register_command_handler(router: Router) -> None:
    router.message.register(feedback_answer, Command(commands=['feedback', 'f'], magic=F.args))  # ref filter
    router.message.register(commands_answer, Command(commands=list(COMMANDS_ANSWER.keys())))  # ref filter
    router.message.register(help_answer, Command(commands='help'))  # ref filter
