from sqlalchemy import Column, Integer, TEXT, VARCHAR

from julia_bot.apps.library.utils.library_base import BaseModel


class BookModel(BaseModel):
    __tablename__ = 'books'

    book_id: Column = Column(Integer, autoincrement=True, primary_key=True)
    title: Column = Column(VARCHAR(128), nullable=False)
    description: Column = Column(TEXT, nullable=True, default='soon')
    reviews: Column = Column(TEXT, nullable=True, default='soon')
    content: Column = Column(TEXT, nullable=True, default='soon')
    # detailed_content: Column = Column(TEXT, nullable=True, default=True)
    link: Column = Column(VARCHAR(128), nullable=False)
    cb_data: Column = Column(VARCHAR(32), nullable=False)

