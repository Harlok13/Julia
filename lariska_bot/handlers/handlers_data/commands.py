from typing import Dict, List

COMMANDS: Dict[str, str] = {
    '/start': 'на время тестирования, затем будет удалена',
    '/library': 'наша сокровищница книга',
    '/help': 'справка и помощь',
    '/repo': 'наш репозиторий',
    '/youtube': 'ссылка на ютуб главдеда'
}


def get_repo_list() -> List[str]:
    """Фильтр команды для получения ссылки на репозиторий."""
    return [
        'repo',
        'repository',
        'репа',
        'репозиторий',
    ]


def get_video_list() -> List[str]:
    """Фильтр команды для получения ссылки на ютуб."""
    return [
        'ютуб',
        'youtube',
        'video',
    ]


def get_library() -> str:
    """Фильтр команды для открытия меню библиотеки."""
    return 'library'
