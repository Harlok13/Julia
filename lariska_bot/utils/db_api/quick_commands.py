import logging
from typing import List

from asyncpg import UniqueViolationError

from lariska_bot.utils.db_api.db_gino import db
from lariska_bot.utils.db_api.schemas.user import User


async def pg_add_user(user_id: int, name: str, update_name: str) -> None:
    """Добавить пользователя."""
    logger = logging.getLogger(__name__)
    try:
        user: User = User(user_id=user_id, name=name, update_name=update_name)
        await user.create()
    except UniqueViolationError:
        logger.error('user is not created')
        print('Пользователь не добавлен')


async def pg_select_all_users() -> List[User]:
    """Выбрать всех пользователей."""
    users: List[User] = await User.query.gino.all()
    return users


async def pg_count_users() -> int:
    """Получить число всех пользователей в бд."""
    count: int = await db.func.count(User.user_id).gino.scalar()
    return count


async def pg_select_user(user_id: int) -> User:
    """Выбрать одного пользователя по айди."""
    user: User = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def pg_update_user_name(user_id: int, new_name: str) -> None:
    """Обновить имя пользователя."""
    user: User = await pg_select_user(user_id)
    await user.update(update_name=new_name).apply()
