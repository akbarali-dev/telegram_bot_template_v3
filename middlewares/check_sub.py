from aiogram import BaseMiddleware, methods
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message
from aiogram.enums import ChatMemberStatus
from aiogram import Bot
import logging


class CheckSubscriptionMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel_ids = [-1001582550273, -1001752250778]  # bu yerda a'zao bo'lishi kerak bo'gan kanallar mavjud
        super().__init__()

    async def __call__(self, handler, event: Message, data: dict):
        # if not hasattr(event, 'message') or event.message is None:
        #     return await handler(event, data)

        user_id = event.from_user.id

        try:
            non_member_channels = []
            # Bu yerda user a'zo bo'lmagan kanallar ro'yxati olingan
            for ch_id in self.channel_ids:
                member = await self.bot.get_chat_member(chat_id=ch_id, user_id=user_id)
                if member.status in [ChatMemberStatus.LEFT, ChatMemberStatus.KICKED]:
                    non_member_channels.append(ch_id)
            # Bu yerda esa qaysi kanallarga a'zo bo;ishi kerakligi keltirilgan
            if len(non_member_channels) != 0:
                msg = ''
                for ch_id in non_member_channels:
                    channel = await self.bot.export_chat_invite_link(ch_id)
                    msg += f"👉 <a href='{channel}'>bu kanalga</a>\n"
                msg += "Yuqoridagi kanallarga obuna bo'ling"
                return await event.answer(msg)
            # Bu yerda hamma kanalga a'zo bo'lgandan so'ng keyingi qadamga o'tkazilgan
            return await handler(event, data)

        except TelegramBadRequest as e:
            logging.error(f"Telegram bad request: {e}")
            return await event.answer("Noto'g'ri so'rov!")
