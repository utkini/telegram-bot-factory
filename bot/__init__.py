from telegram.ext import Updater

from bot.client import BaseClient
from config import CONFIG

service_client = BaseClient(login=CONFIG.login, password=CONFIG.password, base_url=CONFIG.base_url)
updater = Updater(token=CONFIG.bot_token, use_context=True)
dispatcher = updater.dispatcher
bot = updater.bot
