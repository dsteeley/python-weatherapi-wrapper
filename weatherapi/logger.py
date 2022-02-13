import logging

# Basic logger for weatherapi

logger = logging.getLogger("main")
f_handler = logging.FileHandler("weatherapi.log")
f_format = logging.Formatter(
    "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
)
f_handler.setFormatter(f_format)
logger.setLevel(logging.DEBUG)
logger.addHandler(f_handler)
