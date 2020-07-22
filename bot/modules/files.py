from bot import service_client
from bot.utils import parse_args
from bot_logging import LOG
from telegram.ext import Filters
from telegram.ext import MessageHandler

from config import CONFIG


def files_callback(update, context):
    file = context.bot.getFile(update.message.document.file_id)
    file_path = CONFIG.tmp_path / update.effective_message.document.file_name
    file.download(file_path)

    text = update.effective_message.caption
    file_ext = update.effective_message.document.mime_type
    file_type = CONFIG.get_file_type(file_ext)
    url = CONFIG.get_webhook(file_type)
    chat_id = update.effective_chat.id
    params = parse_args(text)
    data = {
        'chat_id': chat_id,
        'params': params
    }
    with open(str(file_path), 'rb') as f:
        resp = service_client.post(url=url, body=data, file=f)
    LOG.info(resp)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(resp.content))


matcher = dict()
supported_handlers = list()
for extensions, endpoint in CONFIG.get_files():
    filters = None
    for extension in extensions:
        if filters is None:
            filters = Filters.document.mime_type(extension)
        else:
            filters |= Filters.document.mime_type(extension)
    matcher[endpoint] = filters
    supported_handlers.append(MessageHandler(filters, files_callback))


class Module:
    name = 'files'
    handlers = supported_handlers
