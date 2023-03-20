from sqlalchemy import Column, TEXT, Integer, ForeignKey, BigInteger

from julia_bot.apps.trigger.utils.trigger_base import BaseModel


class TriggerModel(BaseModel):
    __tablename__ = 'triggers_table'

    trigger_id: Column = Column(Integer, autoincrement=True, primary_key=True)
    name_trigger: Column = Column(TEXT)
    value_trigger: Column = Column(TEXT)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))
