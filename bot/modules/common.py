from bot_logging import LOG

from telegram.ext import Filters
from telegram.ext import CommandHandler

from config import CONFIG


def start_message(update, context):
    LOG.info('/start command')
    ans_msg = f'{CONFIG.start_description}\n your chat_id is: {update.effective_chat.id}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=ans_msg)


def help_message(update, context):
    LOG.info('/help command')
    context.bot.send_message(chat_id=update.effective_chat.id, text=CONFIG.help_description)


class Module:
    name = 'common'
    handlers = (
        CommandHandler(['help'], help_message, filters=Filters.chat(chat_id=CONFIG.allow_chat_ids)),
        CommandHandler(['start'], start_message, filters=Filters.private),
    )
