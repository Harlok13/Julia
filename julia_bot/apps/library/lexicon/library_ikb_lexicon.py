from typing import Dict, List, Tuple, Union

GET_PREV_DATA: str = 'cat_choice_menu'
TO_MENU_DATA: str = 'cat_choice_menu'
GO_DB: str = 'db_cat'
GO_PYTHON: str = 'python_cat'

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

BOOK_IKB: Dict[str, str] = {
    'sql_cat': GO_DB,
    'nosql_cat': GO_DB,
    'pybook_cat': GO_PYTHON,
    'kids_cat': GO_PYTHON,
    'async_cat': GO_PYTHON,
    'django_cat': GO_PYTHON,
    'tests_cat': GO_PYTHON,
    'pandas_cat': GO_PYTHON,
    'ml_cat': GO_PYTHON,
    'linux_cat': GET_PREV_DATA,
    'algorithms_cat': GET_PREV_DATA,
    'git_cat': GET_PREV_DATA,
    'start_cat': GET_PREV_DATA,
    'recommendations_cat': GET_PREV_DATA
}

TY_BUTTONS: Dict[str, Tuple[str]] = {  # type: ignore
    'ty_cmd': ('СПАСИБО!',
               'ПОНЯТНО!',
               'ХОРОШО!',
               'БЛАГОДАРЮ!'),
    'praise_cmd': ('Это потрясающе, Julia!',
                   'Есть над чем подумать...',
                   'Сколько же всего ты знаешь!',
                   'Это очень интересно🤔',
                   'Julia, ты такая умная...')
}

# cb data должна называться так же как и поля в бд
BOOK_INFO_BUT = (
    ('ПОДРОБНЕЕ О КНИГЕ', 'description'),
    ('ОТЗЫВЫ ДЕДОВ', 'reviews'),
    ('СОДЕРЖАНИЕ', 'content'),
    (1,)
)

GO_MAIN_MENU: Dict[str, str] = {
    'title': 'ГЛАВНОЕ МЕНЮ',
    'cb_data': TO_MENU_DATA
}

PAGINATION_BUT: Dict[str, str] = {
    'backward': '<<',
    'forward': '>>'
}
