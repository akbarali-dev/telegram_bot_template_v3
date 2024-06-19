from loader import dp
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html

from aiogram.filters import Command
from filters.admin_filters import AdminFilter
from aiogram import types


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
