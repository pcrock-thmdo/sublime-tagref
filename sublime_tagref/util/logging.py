import logging


# thanks to https://github.com/SublimeText/PackageDev/blob/master/_logging.py


DEFAULT_LOG_LEVEL = logging.DEBUG


def init(package_name: str):
    package_logger = logging.getLogger(package_name)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="[{name}] {levelname}: {message}", style='{')
    handler.setFormatter(formatter)
    package_logger.addHandler(handler)

    package_logger.setLevel(DEFAULT_LOG_LEVEL)
    package_logger.propagate = False  # prevent root logger from catching this


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
