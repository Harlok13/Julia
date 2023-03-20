import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE, Boolean, BigInteger

from julia_bot.data.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    # tlg user_id
    user_id: Column = Column(BigInteger, unique=True, autoincrement=True, nullable=False, primary_key=True)
    # tlg username
    username: Column = Column(VARCHAR(64), unique=True, nullable=True)
    # name of user
    user_nickname: Column = Column(VARCHAR(64), unique=False, nullable=False)
    admin: Column = Column(Boolean, default=False)
    register_date: Column = Column(DATE, default=datetime.date.today)
    update_date: Column = Column(DATE, onupdate=datetime.datetime.utcnow)

    def __str__(self) -> str:
        return f'<User: {self.user_id}>'
