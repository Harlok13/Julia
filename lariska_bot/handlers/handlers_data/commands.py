from typing import Dict, List

COMMANDS: Dict[str, str] = {
    '/start': 'на время тестирования, затем будет удалена',
    '/get_triggers': 'получить список триггеров',
    '/library': 'наша сокровищница книг',
    '/help': 'справка и помощь',
    '/repo': 'наш репозиторий',
    '/youtube': 'ссылка на ютуб главдеда',
    '/aboutme': 'домик, где живет Лариска',
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



