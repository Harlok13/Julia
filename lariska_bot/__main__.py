import asyncio
import logging
import os
from dotenv import load_dotenv, find_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.redis import RedisStorage
from aioredis import Redis
from sqlalchemy import URL

from lariska_bot.data import config_data
from lariska_bot.data.base import BaseModel
from lariska_bot.data.engine import create_async_engine, get_session_maker, proceed_schemas
from lariska_bot.middlewares.mw_user_register_check import UserRegisterCheck
# Импорт настроек apps. Должен быть выше остальных импортов.
from lariska_bot.settings import *

# from lariska_bot.config_reader import config

if library:
    from lariska_bot.apps.library.handlers.library_cb_handler import register_library_cb_handlers
    from lariska_bot.apps.library.handlers.library_msg_handler import register_library_msg_handlers
    from lariska_bot.apps.library.handlers.library_cmd_handler import register_library_cmd_handlers

from lariska_bot.handlers.callback_handlers import register_callback_handlers
from lariska_bot.handlers.message_handler import register_message_handlers
from lariska_bot.handlers.command_handler import register_command_handler

from lariska_bot.keyboards.set_menu import set_main_menu

logger: logging.Logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level='INFO',
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('is started')

    load_dotenv(find_dotenv())
    # bot = Bot(config.bot_token, parse_mode='HTML')
    bot: Bot = Bot(os.getenv('BOT_TOKEN'), parse_mode='HTML')

    # if config.fsm_mode == 'redis':
    #     dp = Dispatcher(storage=RedisStorage.from_url(config.redis_dsn))
    # else:
    #     dp = Dispatcher(storage=MemoryStorage())

    dp: Dispatcher = Dispatcher(storage=RedisStorage.from_url(os.getenv('REDIS_DSN')))

    # register mw
    dp.message.middleware(UserRegisterCheck())
    dp.callback_query.middleware(UserRegisterCheck())

    # register router
    register_callback_handlers(dp)
    register_message_handlers(dp)
    register_command_handler(dp)

    if library:
        register_library_cb_handlers(dp)
        register_library_msg_handlers(dp)
        register_library_cmd_handlers(dp)

    # register bot cmd
    await set_main_menu(bot)

    # register postgres
    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=os.getenv("PG_USER"),
        host=os.getenv('IP'),
        database=os.getenv("DATABASE"),
        port=int(os.getenv("") or 0),
        password=os.getenv('PG_PASSWORD')
    )
    # async_engine = create_async_engine(postgres_url)
    # session_maker = get_session_maker(async_engine)

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)


    # try:
    #     if not config.webhook_domain:
    #         await bot.delete_webhook(drop_pending_updates=True)
    #         await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    #     else:
    #         aiohttp_logger = logging.getLogger('aiohttp.access')
    #         aiohttp_logger.setLevel(level='FATAL')
    #
    #         await bot.set_webhook(
    #             url=f'{config.webhook_domain}{config.webhook_path}',
    #             allowed_updates=dp.resolve_used_update_types(),
    #             drop_pending_updates=True
    #         )
    #
    #         # aiohttp app
    #
    # finally:
    #     await bot.session.close()
    #
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), session_maker=session_maker)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('stopped')
