from typing import List

from aiogram import Bot
from aiogram.types import BotCommand

from julia_bot.handlers.handlers_data.commands import COMMANDS


async def set_main_menu(bot: Bot) -> None:
    """Создание Menu с командами."""
    main_menu_commands: List[BotCommand] = [BotCommand(
        command=command,
        description=description
    ) for command, description in COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)
