import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aioredis import Redis

from lariska_bot.config_reader import config


async def main():
    logging.basicConfig(
        level='INFO',
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    bot = Bot(config.bot_token, parse_mode='HTML')

    if config.fsm_mode == 'redis':
        dp = Dispatcher(storage=RedisStorage.from_url(config.redis_dsn))
    else:
        dp = Dispatcher(storage=MemoryStorage())

    # register mw

    # register router

    # register bot cmd

    try:
        if not config.webhook_domain:
            await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
        else:
            aiohttp_logger = logging.getLogger('aiohttp.access')
            aiohttp_logger.setLevel(level='FATAL')

            await bot.set_webhook(
                url=f'{config.webhook_domain}{config.webhook_path}',
                allowed_updates=dp.resolve_used_update_types(),
                drop_pending_updates=True
            )

            # aiohttp app

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
