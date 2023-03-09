import asyncio
from typing import List

from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from lariska_bot.apps.trigger.utils.db_connect import Request


async def add_trigger(message: Message, request: Request, bot: Bot) -> None:
    """Добавить триггер в список."""
    name_trigger: str = message.text.replace(' ', '_').replace('!', '')
    value_trigger: int = message.reply_to_message.message_id
    await request.db_add_trigger(name_trigger, value_trigger)
    await message.answer(f'Триггер "{name_trigger}" успешно добавлен для пользователя '
                         f'"{message.from_user.first_name}"')
    await asyncio.sleep(3)
    # получаем сообщение бота
    message_for_del: int = message.message_id + 1
    await bot.delete_message(chat_id=message.chat.id, message_id=message_for_del)


async def get_trigger(message: Message, request: Request) -> None:
    """Получить список всех триггеров."""
    msg: str = await request.db_get_triggers()
    if msg:
        await message.answer(msg, parse_mode='MARKDOWN')
    else:
        await message.answer('Список триггеров пуст')


async def get_value(message: Message, request: Request, bot: Bot) -> None:
    """Получить значение триггера."""
    values: str = await request.db_get_values(message.text.replace('>', ''))
    list_values: List[str] = values.split('\r\n')
    for value in list_values:
        await bot.copy_message(message.chat.id, message.chat.id, int(value))


def register_trigger_message_handler(r: Router) -> None:
    r.message.register(add_trigger, F.text.startswith('!'), F.reply_to_message)
    r.message.register(get_trigger, Command(commands='get_triggers'))
    r.message.register(get_value, F.text.startswith('>'))
