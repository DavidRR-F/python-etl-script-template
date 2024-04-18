from .config import env

import logging
import os


def ensure_directory_exists(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def setup_logger() -> logging.Logger:
    """Function to setup global logger"""
    ensure_directory_exists(env.log_file)
    handler = env.log_handler
    handler.setFormatter(env.log_formatter)

    logger = logging.getLogger(__name__)
    logger.setLevel(env.log_level)
    logger.addHandler(handler)

    return logger


log = setup_logger()
