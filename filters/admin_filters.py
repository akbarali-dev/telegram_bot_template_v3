from aiogram import types
from aiogram.filters import Filter
from aiogram.types import Message

from data.config import ADMINS


class AdminFilter(Filter):
    def __init__(self):
        self.admin_ids = ADMINS

    async def __call__(self, message: Message) -> bool:
        print(self.admin_ids)
        print(message.from_user.id in self.admin_ids)
        return str(message.from_user.id) in self.admin_ids



