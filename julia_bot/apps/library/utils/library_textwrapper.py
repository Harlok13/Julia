from collections import namedtuple
from typing import Dict


def _text_wrapper(text: str, start: int, page_size: int) -> 'PageText':  # type: ignore
    """
    Split text into pages.

    :param text: text to be paginated
    :param start: index from which to start dividing per page
    :param page_size: maximum page size
    :return: a named tuple that stores the index of the last
     character of the page and the text of the page itself
    """
    symbols: str = ',.!?:;'
    end_of_page: int = max(text[start: page_size + start].rfind(symbol)
                           for symbol in symbols)
    PageText: namedtuple = namedtuple('PageText', ['page', 'text'])
    page_with_text: PageText = PageText(page=end_of_page + 1,
                                        text=text[start: end_of_page + start + 1])
    return page_with_text


# ref
def get_dict(text, size):
    d = {}
    cursor = 0
    page = 1
    while cursor < len(text) - 1:
        if len(text[cursor:]) > size:
            t = text_wrapper2(text, cursor, size)
            d.setdefault(page, t[1])
            cursor += t[0]
            page += 1
        else:
            d.setdefault(page, text[cursor:])
            break
    return d
