import asyncio

from aiogram import Bot, Router, F
from aiogram.filters import CommandObject, Command
from aiogram.types import Message

from lariska_bot.utils.db_connect import Request


async def add_trigger(message: Message, command: CommandObject, request: Request, bot: Bot) -> None:
    name_trigger = command.args.replace(' ', '_')
    print('command args ', command.args)
    value_trigger = message.reply_to_message.message_id
    await request.db_add_trigger(name_trigger, value_trigger)
    await message.answer(f'Триггер "{name_trigger}" успешно добавлен для пользователя '
                         f'"{message.from_user.first_name}"')
    await asyncio.sleep(3)
    # получаем сообщение бота
    message_for_del = message.message_id + 1
    await bot.delete_message(chat_id=message.chat.id, message_id=message_for_del)


async def get_trigger(message: Message, request: Request):
    msg = await request.db_get_triggers()
    await message.answer(msg, parse_mode='MARKDOWN')


async def get_value(message: Message, request: Request, bot: Bot):
    values = await request.db_get_values(message.text.replace('#', ''))
    list_values = values.split('\r\n')

    for value in list_values:
        await bot.copy_message(message.chat.id, message.chat.id, int(value))


def register_trigger_message_handler(r: Router):
    r.message.register(add_trigger, Command(commands='add_trigger', magic=F.args), F.reply_to_message)
    r.message.register(get_trigger, Command(commands='get_triggers'))
    r.message.register(get_value, F.text.startswith('#'))
