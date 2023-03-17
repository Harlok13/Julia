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
    PageText: namedtuple = namedtuple('PageText', ['page_end', 'text'])
    page_with_text: PageText = PageText(page_end=end_of_page + 1,
                                        text=text[start: end_of_page + start + 1])
    return page_with_text


def get_pages_dict(text: str, page_size: int, field: str) -> Dict[str, str]:
    """
    Get a dictionary with page numbers and the text of those pages.

    :param text: text to be paginated
    :param page_size: maximum allowable page size
    :param field: the name of db field, then this name will be used as callback data
    :return: dictionary with page numbers and the text of those pages
    """
    pages_dict: Dict[str, str] = {}
    cursor_start, page = 0, 1
    while cursor_start < len(text) - 1:
        if len(text[cursor_start:]) > page_size:
            page_with_text: 'PageText' = _text_wrapper(text, cursor_start, page_size)  # type: ignore
            pages_dict.setdefault(f'{field}{page}', page_with_text.text)
            cursor_start += page_with_text.page_end
            page += 1
        else:
            pages_dict.setdefault(f'{field}{page}', text[cursor_start:])
            break
    return pages_dict
