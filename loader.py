from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from middlewares import middleware_add
from data.config import BOT_TOKEN

dp = Dispatcher()
middleware_add(dp)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
