from sqlalchemy import text, select, insert
from sqlalchemy.orm import sessionmaker

from lariska_bot.apps.trigger.utils.trigger_schemas import TriggerModel


class Request:
    def __init__(self, session: sessionmaker) -> None:
        self.session: sessionmaker = session

    async def db_add_trigger(self, name_trigger, value_trigger) -> None:
        async with self.session.begin():
            query = f"INSERT INTO triggers_table (name_trigger, value_trigger)" \
                    f" VALUES ('{name_trigger}', '{value_trigger}')" \
                    f" ON CONFLICT (name_trigger)" \
                    f" DO UPDATE SET value_trigger=triggers_table.value_trigger || '\r\n' || excluded.value_trigger"
            await self.session.execute(text(query))  # type: ignore

    async def db_get_triggers(self) -> str:
        async with self.session.begin():
            result_list: ChunkedIteratorResult = await self.session.execute(  # type: ignore
                select(TriggerModel.name_trigger)
            )
            return '\r\n'.join(f"`>{result[0]}`" for result in iter(result_list))

    async def db_get_values(self, name_trigger):
        async with self.session.begin():
            result = await self.session.execute(  # type: ignore
                select(TriggerModel.value_trigger).where(TriggerModel.name_trigger == name_trigger)
            )
            return next(result)[0]
