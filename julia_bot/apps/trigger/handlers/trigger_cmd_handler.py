import asyncio
from typing import List

from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from julia_bot.apps.trigger.utils.trigger_request import Request
from julia_bot.keyboards.inline_keyboard import TY_MENU


async def add_trigger(message: Message, request: Request, bot: Bot) -> None:
    """Добавить триггер в список."""
    name_trigger: str = message.text.replace(' ', '_').replace('!', '')
    value_trigger: int = message.reply_to_message.message_id
    user_id: int = message.from_user.id
    await request.db_add_trigger(name_trigger, value_trigger, user_id)
    await message.answer(f'Заметка "{name_trigger}" успешно добавлена для пользователя '
                         f'"{message.from_user.first_name}"')
    await asyncio.sleep(3)
    # получаем сообщение бота
    message_for_del: int = message.message_id + 1
    await bot.delete_message(chat_id=message.chat.id, message_id=message_for_del)


async def get_trigger(message: Message, request: Request) -> None:
    """Получить список всех триггеров."""
    msg: str = await request.db_get_triggers()
    await message.delete()
    if msg:
        await message.answer(f'Список заметок:\n{msg}\n`______________________`\n'
                             f'Удаление заметки: \n!название',  # ref
                             parse_mode='MARKDOWN',
                             reply_markup=TY_MENU)  # ref
    else:
        await message.answer('Список заметок пуст',
                             reply_markup=TY_MENU)


async def get_value(message: Message, request: Request, bot: Bot) -> None:
    """Получить значение триггера."""
    values: str = await request.db_get_values(message.text.replace('>', ''))
    list_values: List[str] = values.split('\r\n')
    await message.delete()
    for value in list_values:
        await bot.copy_message(message.chat.id, message.chat.id, int(value),
                               reply_markup=TY_MENU)


async def del_trigger(message: Message, request: Request, bot: Bot) -> None:
    """Удалить триггер."""
    name: str = message.text.replace('!', '').replace(' ', '_')
    await request.db_del_trigger(name)
    # fix cuz removes non-existent triggers
    await message.answer(f'Заметка "{name}" для пользователя '
                         f'"{message.from_user.first_name}" удалена!')
    await asyncio.sleep(3)
    message_for_del: int = message.message_id + 1
    await bot.delete_message(message.chat.id, message_for_del)


def register_trigger_message_handler(r: Router) -> None:
    r.message.register(add_trigger, F.text.startswith('!'), F.reply_to_message)
    r.message.register(get_trigger, Command(commands='get_notes'))
    r.message.register(get_value, F.text.startswith('>'))
    r.message.register(del_trigger, F.text.startswith('!'))
