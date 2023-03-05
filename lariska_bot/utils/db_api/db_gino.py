from typing import List

import sqlalchemy as sa
from aiogram import Dispatcher
from gino import Gino

from lariska_bot.data import config_data

db = Gino()


class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_keys_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_keys_columns
        }
        values_str = ' '.join(f'{name}={value!r}' for name, value in values.items())
        return f'<{model} {values_str}>'


class TimedBaseModel(BaseModel):
    __abstarct__ = True

    created_at: db.Column = db.Column(db.DateTime(True),  # type: ignore
                                      server_default=db.func.now())  # type: ignore
    updated_at: db.Column = db.Column(  # type: ignore
        db.DateTime(True),  # type: ignore
        default=db.func.now(),  # type: ignore
        onupdate=db.func.now(),  # type: ignore
        server_default=db.func.now(),  # type: ignore
    )


async def on_startup(dp: Dispatcher):
    print('Установка связи с PG')
    await db.set_bind(config_data.POSTGRES_URI)
