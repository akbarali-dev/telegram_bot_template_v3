from aiogram import BaseMiddleware
from aiogram.types import Message
import time


class RateLimitMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 3, interval: int = 1):
        self.limit = limit
        self.interval = interval
        self.requests = {}

    async def __call__(self, handler, event: Message, data: dict):
        user_id = event.from_user.id
        current_time = time.time()

        if user_id not in self.requests:
            self.requests[user_id] = []

        self.requests[user_id] = [t for t in self.requests[user_id] if current_time - t < self.interval]

        if len(self.requests[user_id]) >= self.limit:
            return await event.answer("Too Many Requests")

        self.requests[user_id].append(current_time)
        return await handler(event, data)
