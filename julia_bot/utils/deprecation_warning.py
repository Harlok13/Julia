import asyncio
import warnings
from functools import wraps


def deprecated(coroutine):
    """Сигнализирует о том, что корутина устарела"""

    @wraps(coroutine)
    async def wrapper(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)
        warnings.warn(f'a deprecated coroutine "{coroutine.__name__}" was called',
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)
        return await coroutine(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    @deprecated
    async def _cor(n):
        await asyncio.sleep(n * n)

    asyncio.run(_cor(3))
