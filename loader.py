from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

# dp = Dispatcher(storage=MemoryStorage())
from data import config
from data.config import BOT_TOKEN

dp = Dispatcher()

# bot = Bot(token=config.BOT_TOKEN)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# storage = MemoryStorage()
