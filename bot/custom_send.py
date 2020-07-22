from bot import bot
from bot_logging import LOG


def custom_send(chat_id, text):
    LOG.info('custom send command')
    bot.sendMessage(chat_id=chat_id, text=text)
