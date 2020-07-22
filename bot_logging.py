import logging
import sys

log_level = logging.INFO
bot_logger = 'BOTLogger'
LOGGING_FORMAT = '[%(levelname)s] %(asctime)s %(filename)s:%(funcName)s:%(lineno)s: %(message)s'

LOG = logging.getLogger(bot_logger)

formatter = logging.Formatter(LOGGING_FORMAT)
LOG.setLevel(log_level)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.set_name('console_handler')
console_handler.setLevel(log_level)
console_handler.setFormatter(formatter)
LOG.addHandler(console_handler)
LOG.propagate = False
