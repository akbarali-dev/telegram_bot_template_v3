from aiogram import types
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.enums.chat_type import ChatType


class IsPrivate(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE
