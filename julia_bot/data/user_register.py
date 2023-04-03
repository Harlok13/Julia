import logging

from aioredis import Redis
from sqlalchemy.orm import sessionmaker

from julia_bot.data.schemas.user import User

logger: logging.Logger = logging.getLogger(__name__)


async def register_user(
        session_maker: sessionmaker,
        user_id: int,
        username: str,
        first_name: str,
        redis: Redis
) -> None:
    async with session_maker() as session:
        async with session.begin():
            user: User = User(
                user_id=user_id,
                username=username,
                user_nickname=first_name
            )
            await session.merge(user)
            logger.info(f'Пользователь {first_name} зарегистрирован')
            await redis.set(name=str(user_id), value=1)


async def is_user_exists(
        user_id: int,
        first_name: str,
        redis: Redis
) -> bool:
    user_exists: bytes = await redis.get(name=str(user_id))
    if user_exists:
        logger.info(f'Пользователь {user_id} уже зарегистрирован')

        # sql_res = await session.execute(
        #     update(User).where(User.user_id == event.from_user.id).values(
        #         update_date=datetime.datetime.today())
        # )

        return True
    return False
