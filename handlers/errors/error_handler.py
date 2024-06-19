import logging
from aiogram.exceptions import (TelegramAPIError,
                                )

from loader import dp


@dp.errors()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
