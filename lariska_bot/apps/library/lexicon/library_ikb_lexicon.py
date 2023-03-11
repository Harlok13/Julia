from typing import Dict, List, Tuple, Union

# или сделать списком?
# кнопка закрытия цитаты
PRAISE_ANSWER: Dict[str, str] = {
    'Это потрясающе, Лариска!': 'compliment',
    'Есть над чем подумать...': 'compliment',
    'Сколько же всего ты знаешь!': 'compliment',
    'Это очень интересно🤔': 'compliment',
    'Лариска, ты такая умная...': 'compliment',
    'Лариска умняша': 'compliment', }

GET_PREV_DATA = 'cat_choice_menu'
TO_MENU_DATA = 'menu_cmd'

# кортеж с числами отвечает за расположение кнопок в ряду
MENU_IKB: Dict[str, List[Union[Tuple[str, str], Tuple[int]]]] = {
    'cat_choice_menu':
        [('PYTHON', 'python_cat'),
         ('БАЗЫ ДАННЫХ', 'db_cat'),
         ('GIT', 'git_cat'),
         ('LINUX', 'linux_cat'),
         ('АЛГОРИТМЫ', 'algorithms_cat'),
         ('КНИГИ ДЛЯ СТАРТА', 'start_cat'),
         ('РЕКОМЕНДАЦИИ', 'recommendations_cat'),
         ('ЗАКРЫТЬ МЕНЮ', 'close'),
         (2, 2, 2, 1)],

    'db_cat':
        [('SQL', 'sql_cat'),
         ('NoSQL', 'nosql_cat'),
         ('Подробнее об SQLHelper', 'sql_helper'),
         ('НАЗАД', GET_PREV_DATA),
         (2, 1)],

    'python_cat':
        [('КНИГИ ПО PYTHON', 'pybook_cat'),
         ('ДЛЯ САМЫХ МАЛЕНЬКИХ', 'kids_cat'),
         ('АСИНХРОННЫЙ PYTHON', 'async_cat'),
         ('DJANGO', 'django_cat'),
         ('ТЕСТИРОВАНИЕ', 'tests_cat'),
         ('PANDAS', 'pandas_cat'),
         ('НЕЙРОСЕТИ', 'ml_cat'),
         ('НАЗАД', GET_PREV_DATA),
         (1,)],
}
# изменить на кортеж
BOOK_IKB = {
    'sql_cat': [],

    'nosql_cat': [],

    'pybook_cat': [],

    'kids_cat': [],

    'async_cat': [],

    'django_cat': [],

    'tests_cat': [],

    'pandas_cat': [],

    'ml_cat': [],

    'linux_cat': [],

    'algorithms_cat': [],

    'git_cat': [],

    'start_cat': [],

    'recommendations_cat': []
}

OTHER_BUTTONS = {
    'get_prev': ('НАЗАД', 'get_prev'),
    'ty_cmd': 'СПАСИБО!'
}

# cb data должна называться так же как и поля в бд
BOOK_INFO_BUT = [
    ('ПОДРОБНЕЕ О КНИГЕ', 'description'),
    ('ОТЗЫВЫ ДЕДОВ', 'reviews'),
    ('СОДЕРЖАНИЕ', 'content'),
    ('НАЗАД', 'go_to_cat'),
    ('ГЛАВНОЕ МЕНЮ', TO_MENU_DATA),
    (1,)
]
