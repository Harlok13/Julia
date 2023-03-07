from typing import List

import asyncpg
from asyncpg import Record


class Request:
    def __init__(self, connector: asyncpg.pool.Pool) -> None:
        self.connector: asyncpg.pool.Pool = connector

    async def db_add_trigger(self, name_trigger, value_trigger) -> None:
        query = f"INSERT INTO triggers_table (name_trigger, value_trigger) VALUES ('{name_trigger}', '{value_trigger}') ON CONFLICT (name_trigger) DO UPDATE SET value_trigger=triggers_table.value_trigger || '\r\n' || excluded.value_trigger"
        await self.connector.execute(query)

    async def db_get_triggers(self) -> str:
        query = f"SELECT name_trigger FROM triggers_table ORDER BY name_trigger"
        result_list: List[Record] = await self.connector.fetch(query)
        return '\r\n'.join(f"`#{result.get('name_trigger')}`" for result in result_list)

    async def db_get_values(self, name_trigger):
        query = f"SELECT value_trigger FROM triggers_table WHERE name_trigger='{name_trigger}'"
        return await self.connector.fetchval(query)


