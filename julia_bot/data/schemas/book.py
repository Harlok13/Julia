from sqlalchemy import Column, Integer, VARCHAR, TEXT

from julia_bot.data.base import BaseModel


class Book(BaseModel):
    __tablename__ = 'books'

    book_id: Column = Column(Integer, unique=True, nullable=False, autoincrement=True, primary_key=True)
    name: Column = Column(VARCHAR(200), nullable=False)
    description: Column = Column(TEXT, default='description')
    grandfa_desc: Column = Column(TEXT, default='grandfather description')
    content: Column = Column(TEXT, default='soon')
    detailed_content: Column = Column(TEXT, default='soon')
