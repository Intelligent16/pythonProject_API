import sys

import colorlog


def get_logger(name):
    logger = colorlog.getLogger(name)
    logger.setLevel(colorlog.DEBUG)
    stream_handler = colorlog.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s [%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S'))
    logger.addHandler(stream_handler)
    return logger
