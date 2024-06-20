from aiogram import Dispatcher
from . import throttling


def middleware_add(dp: Dispatcher):
    dp.message.middleware(throttling.RateLimitMiddleware())
