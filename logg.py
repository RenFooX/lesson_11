import logging


def create_logger():

    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    console_hangler = logging.StreamHandler()
    file_hangler = logging.FileHandler("logs/basic.txt")

    logger.addHandler(console_hangler)
    logger.addHandler(file_hangler)

    formatter_one = logging.Formatter("%(asctime)s : %(message)s")

    console_hangler.setFormatter(formatter_one)
    file_hangler.setFormatter(formatter_one)