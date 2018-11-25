import logging
import sys
from colorlog import ColoredFormatter


LOGFORMAT = '%(log_color)s %(asctime)s%(reset)s - %(log_color)s%(levelname)s%(reset)s: %(log_color)s%(message)s%(reset)s'

LOG_LEVEL = logging.DEBUG
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
logger = logging.getLogger('pythonConfig')
logger.setLevel(LOG_LEVEL)
logger.addHandler(stream)


# logger = logging.getLogger(LOGFORMAT)
# logger.setLevel(logging.DEBUG)


# ch = logging.StreamHandler(sys.stdout)
# ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter()
# ch.setFormatter(formatter)
# logger.addHandler(ch)
