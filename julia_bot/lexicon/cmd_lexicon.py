from typing import Dict, List

COMMANDS: Dict[str, str] = {
    '/start': 'на время тестирования, затем будет удалена',
    '/get_triggers': 'получить список триггеров',
    '/library': 'наша сокровищница книг',
    '/help': 'справка и помощь',
    '/repo': 'наш репозиторий',
    '/youtube': 'ссылка на ютуб главдеда',
    '/julia': 'домик, где живет Julia',
    '/changelog': 'логи последних изменений'
}

COMMANDS_ANSWER: Dict[str, str] = {
    'start': 'Привет, я Julia - помощница для чата "Old Coders Club", '
              'написанная энтузиастом - самоучкой под ником Harlok. '
              'Если у вас будут какие-то вопросы или предложения, или обнаружите '
              'баг, то для связи с разработчиком можете оставить свое сообщение '
              'начав его с команды /feedback и после пробела написав свое '
              'сообщение. '
              'Вы также можете использовать меня как хранилище полезной информации, '
              'потому что у меня есть очень удобная система заметок. Подробнее можно '
              'узнать отправив команду /help',
    'repo': 'https://github.com/OldCodersClub',
    'youtube': 'https://www.youtube.com/@oldcoders',
    'julia': 'Я бот и поэтому мой домик здесь:\n'
              'https://github.com/Harlok13/Julia\n'
              'А здесь живет моя сестра:\n'
              'https://github.com/OldCodersClub/LariskaBot'
}

CHANGELOG_ANSWER: str = """

"""

HELP_ANSWER: Dict[str, str] = {
    '/help': """
    
    
    """
}
