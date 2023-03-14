from sqlalchemy import text, select, delete
from sqlalchemy.orm import sessionmaker

from julia_bot.apps.trigger.utils.trigger_schemas import TriggerModel


class Request:  # NoteRequest
    def __init__(self, session: sessionmaker) -> None:
        self.session: sessionmaker = session

    async def db_add_trigger(self, name_trigger: str, value_trigger: int) -> None:
        """Добавить триггер."""
        async with self.session.begin():
            query = f"INSERT INTO triggers_table (name_trigger, value_trigger)" \
                    f" VALUES ('{name_trigger}', '{value_trigger}')"
            await self.session.execute(text(query))  # type: ignore

    async def db_get_triggers(self) -> str:
        """Получить список триггеров."""
        async with self.session.begin():
            result_list: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                select(TriggerModel.name_trigger)
            )
            return '\r\n'.join(f"`>{result[0]}`" for result in iter(result_list))

    async def db_get_values(self, name_trigger: str) -> str:
        """Получить значение триггера."""
        async with self.session.begin():
            result: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                select(TriggerModel.value_trigger).where(TriggerModel.name_trigger == name_trigger)
            )
            return next(result)[0]

    async def db_del_trigger(self, name_trigger: str) -> None:
        """Удалить триггер."""
        async with self.session.begin():
            query: CursorResult = await self.session.execute(  # type: ignore
                delete(TriggerModel).where(TriggerModel.name_trigger == name_trigger)
            )
            # если такого триггера нет, то предупреждать пользователя

    async def db_upd_trigger(self, name_trigger: str) -> None:
        """Обновить название триггера."""
        ...
