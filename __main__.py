from aiohttp import web

from bot_logging import LOG, init_logger
import importlib

from bot import updater
from bot import dispatcher
from bot.modules import supported_modules

from server import routes


def add_module_handlers(module_name):
    try:
        module = importlib.import_module(f'bot.modules.{module_name}').Module
        LOG.info(f'module imported - {module.name} (handlers: {len(module.handlers)})')
        for handler in module.handlers:
            dispatcher.add_handler(handler)
    except Exception as e:
        LOG.error(e)


def initialize_bot():
    for modname in supported_modules:
        add_module_handlers(modname)

    updater.start_polling(clean=True)
    # updater.idle()


init_logger()
initialize_bot()
app = web.Application()
app.add_routes(routes)
web.run_app(app)
