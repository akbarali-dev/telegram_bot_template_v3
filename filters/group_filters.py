from aiogram import types
from aiogram.filters import Filter
from aiogram.enums.chat_type import ChatType


from aiogram import types
from aiogram.filters import Filter
from aiogram.types import Message

from data.config import ADMINS


class IsGroup(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type in (
            ChatType.GROUP,
            ChatType.SUPERGROUP,
        )
