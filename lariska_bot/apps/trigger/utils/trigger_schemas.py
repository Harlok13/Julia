from sqlalchemy import Column, TEXT

from lariska_bot.apps.trigger.utils.trigger_base import BaseModel


class TriggerModel(BaseModel):
    __tablename__ = 'triggers_table'

    id: Column = Column()
    name_trigger: Column = Column(TEXT)
    value_trigger: Column = Column(TEXT)
