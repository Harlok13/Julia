from typing import Union, Dict


# ref
def text_wrapper2(text: str, start: int, width: int):
    """Разделить текст на страницы."""
    symbols = (',.!?:;')
    res = max(text[start: width + start].rfind(i) for i in symbols)
    return res + 1, text[start: res + start + 1]


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
