from bot import service_client
from bot_logging import LOG

from telegram.ext import Filters
from telegram.ext import CommandHandler

from config import CONFIG


def command_callback(update, context):
    command = update.effective_message.text
    endpoint = CONFIG.get_webhook(command.replace('/', ''))
    resp = service_client.get(endpoint)
    LOG.info(resp)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(resp.content))


command_handlers = tuple(
    [
        CommandHandler([command], command_callback, filters=Filters.private)
        for command, _ in CONFIG.get_commands()
    ]
)


class Module:
    name = 'command'
    handlers = command_handlers
