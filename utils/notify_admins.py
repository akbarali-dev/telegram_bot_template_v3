import logging

from data.config import ADMINS


async def on_startup_admins(bot):
    for ADMIN in ADMINS:
        try:
            await bot.send_message(chat_id=ADMIN, text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)
