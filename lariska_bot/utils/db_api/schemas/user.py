from sqlalchemy import Column, BigInteger, String

from lariska_bot.utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id: Column = Column(BigInteger, primary_key=True)
    name: Column = Column(String(200), primary_key=True)
    update_name: Column = Column(String(50), primary_key=True)
