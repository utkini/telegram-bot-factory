# from bot import rpa_client
# from bot_logging import LOG
#
# from telegram.ext import Filters
# from telegram.ext import CommandHandler
#
# from config import CONFIG
#
#
# def general_callback(update, context):
#     regxp = update.effective_message.text
# не понятно какой фильтр был у обработчика по сообщению. нужно повторять действие command handler
#     endpoint = CONFIG.get_command_webhook(regxp)
#     resp = rpa_client.get(endpoint)
#     LOG.info(resp)
#     context.bot.send_message(chat_id=update.effective_chat.id, text=str(resp.content))
#
#
# command_handlers = tuple(
#     [
#         CommandHandler(Filters.regex(regexp_pattern), general_callback, filters=Filters.private)
#         for regexp_pattern, _ in CONFIG.get_regexp()
#     ]
# )
#
#
# class Module:
#     name = 'regexp'
#     handlers = command_handlers
