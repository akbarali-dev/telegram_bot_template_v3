import asyncio
import logging
import sys

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from data.config import BOT_TOKEN, ADMINS
from loader import dp, bot
from handlers.users.start import command_start_handler
from utils.notify_admins import on_startup_admins


# All handlers should be attached to the Router (or Dispatcher)

async def on_startup():
    await on_startup_admins(bot)





async def main() -> None:
    dp.message.once = False
    await on_startup()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
