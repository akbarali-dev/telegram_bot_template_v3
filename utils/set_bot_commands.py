from aiogram import types
from aiogram import Bot


async def set_default_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Botni ishga tushurish"),
        types.BotCommand(command="/help", description="Yordam"),
        types.BotCommand(command="/menu", description="Menu")
    ]
    await bot.set_my_commands(commands=commands)
