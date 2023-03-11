from aiogram import Router, F
from aiogram.types import CallbackQuery


async def callback_say_ty_main(callback: CallbackQuery) -> None:
    """Сказать спасибо и удалить сообщение."""
    await callback.message.delete()


def register_callback_handlers(router: Router) -> None:
    router.callback_query.register(callback_say_ty_main, F.data == 'ty_main')
