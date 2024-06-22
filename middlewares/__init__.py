from aiogram import Dispatcher, Bot
from . import throttling
from . import check_sub


def middleware_add(dp: Dispatcher, bot: Bot):
    dp.message.middleware(throttling.RateLimitMiddleware())
    dp.message.middleware(check_sub.CheckSubscriptionMiddleware(bot))
