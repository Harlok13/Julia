import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

GET_PREV_DATA = 'get_prev'
TO_MENU_DATA = 'menu_cmd'

CAT_CHOICE_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='PYTHON', callback_data='python_cat'),
         InlineKeyboardButton(text='БАЗЫ ДАННЫХ', callback_data='db_cat')],
        [InlineKeyboardButton(text='GIT', callback_data='git_cat'),
         InlineKeyboardButton(text='LINUX', callback_data='linux_cat')],
        [InlineKeyboardButton(text='АЛГОРИТМЫ', callback_data='algorithms_cat'),
         InlineKeyboardButton(text='КНИГИ ДЛЯ СТАРТА', callback_data='start_cat')],
        [InlineKeyboardButton(text='РЕКОМЕНДАЦИИ', callback_data='recommendations_cat')],
        [InlineKeyboardButton(text='ЗАКРЫТЬ МЕНЮ', callback_data='close')],
    ]
)

PYTHON_CHOICE_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='КНИГИ ПО PYTHON', callback_data='pybook_cat')],
        [InlineKeyboardButton(text='ДЛЯ САМЫХ МАЛЕНЬКИХ', callback_data='kids_cat')],
        [InlineKeyboardButton(text='АСИНХРОННЫЙ PYTHON', callback_data='async_cat')],
        [InlineKeyboardButton(text='DJANGO', callback_data='django_cat')],
        [InlineKeyboardButton(text='ТЕСТИРОВАНИЕ', callback_data='tests_cat')],
        [InlineKeyboardButton(text='PANDAS', callback_data='pandas_cat')],
        [InlineKeyboardButton(text='НЕЙРОСЕТИ', callback_data='ml_cat')],
        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

BOOK_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='ПОДРОБНЕЕ О КНИГЕ', callback_data='about_cmd')],
        [InlineKeyboardButton(text='ОТЗЫВЫ ДЕДОВ', callback_data='grandfa_cmd')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_to_cat')],
        [InlineKeyboardButton(text='ГЛАВНОЕ МЕНЮ', callback_data=TO_MENU_DATA)],
    ]
)

ABOUT_BOOK_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='СПАСИБО!', callback_data='ty')]
    ]
)

TY_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='СПАСИБО!', callback_data='ty')]
    ]
)

DB_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='SQL', callback_data='sql_cat'),
         InlineKeyboardButton(text='NoSQL', callback_data='nosql_cat')],
        [InlineKeyboardButton(text='Подробнее об SQLHelper', callback_data='sql_helper')],
        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

NOSQL_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Брэдшоу - MongoDB Полное руководство', callback_data='2')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_db')],
    ]
)

SQL_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Алан Болье - Изучаем SQL', callback_data='11')],
        [InlineKeyboardButton(text='Бен Форта - Освой самостоятельно SQL за 10 минут', callback_data='31')],
        [InlineKeyboardButton(text='Моргунов - PostgreSQL Основы языка SQL', callback_data='9')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_db')],
    ]
)

GIT_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Чакон - Git для профи', callback_data='5')],
        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

START_BOOKS_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Шереметьев - Путь в программисты', callback_data='6')],
        [InlineKeyboardButton(text='Столяров - Азы программирования', callback_data='21')],
        [InlineKeyboardButton(text='Столяров - Системы и сети', callback_data='22')],
        [InlineKeyboardButton(text='Столяров - Парадигмы', callback_data='23')],
        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

ALGORITHMS_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Адитья Бхаргава - Грокаем алгоритмы', callback_data='10')],
        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

LINUX_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Уильям Шоттс - Командная строка LINUX', callback_data='17')],
        [InlineKeyboardButton(text='Шпигорь - Программирование на Bash с нуля', callback_data='20')],
        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

RECOMMEND_MENU = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='НАЗАД', callback_data=GET_PREV_DATA)],
    ]
)

PYTHON_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Свейгарт - Автоматизация рутинных задач', callback_data='3')],
        [InlineKeyboardButton(text='Свейгарт - Чистый код', callback_data='28')],
        [InlineKeyboardButton(text='Лутц - Изучаем Python 1', callback_data='16')],
        [InlineKeyboardButton(text='Лутц - Изучаем Python 2', callback_data='15')],
        [InlineKeyboardButton(text='Эрик Метиз - Изучаем Python', callback_data='27')],
        [InlineKeyboardButton(text='Бизли - Python Книга рецептов', callback_data='29')],
        [InlineKeyboardButton(text='Персиваль  - Паттерны разработки', callback_data='7')],
        [InlineKeyboardButton(text='Дауни - Основы Python', callback_data='36')],
        [InlineKeyboardButton(text='Кристиан Майер - Однострочники Pyhon', callback_data='18')],
        [InlineKeyboardButton(text='Грессер - Теория и практика', callback_data='37')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)

KIDS_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Шапошникова - Введение в программирование', callback_data='4')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)

ASYNC_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Фаулер - Asyncio и конкурентное программирование', callback_data='1')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)

DJANGO_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Персиваль - Разработка на основе тестирования', callback_data='8')],
        [InlineKeyboardButton(text='Постолит - Python, Django и PyCharm', callback_data='12')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)

TESTS_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Brian Okken - Python Testing with pytest', callback_data='13')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)

PANDAS_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Абдрахманов - Pandas Работа с данными', callback_data='14')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)

ML_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Омельяненко - Эволюционные нейросети на языке Python', callback_data='32')],
        [InlineKeyboardButton(text='Нильсен - Практический анализ временных рядов', callback_data='33')],
        [InlineKeyboardButton(text='Скиена - Наука о данных', callback_data='30')],
        [InlineKeyboardButton(text='НАЗАД', callback_data='go_python')],
    ]
)


def praise_answer():
    praise_answer = ['Это потрясающе, Лариска!',
                     'Есть над чем подумать...',
                     'Сколько же всего ты знаешь!',
                     'Это очень интересно🤔',
                     'Лариска, ты такая умная...']
    ikb_build = InlineKeyboardBuilder()
    return ikb_build.row(InlineKeyboardButton(text=random.choice(praise_answer),
                                              callback_data='compliment')).as_markup()

# PRAISE_MENU = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=random.choice(praise_answer), callback_data='compliment')],
#     ]
# )
