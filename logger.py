import logging


def logging_it():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_handler = logging.FileHandler("logs/basic.txt", encoding="utf-8")
    logger.addHandler(file_handler)
    # %(pathname)s >> %(funcName)s
    formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s  ")
    file_handler.setFormatter(formatter)
    return logger
