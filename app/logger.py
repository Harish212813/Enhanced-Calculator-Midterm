import logging

from app.calculator_config import CalculatorConfig


def setup_logger(name="calculator"):
    config = CalculatorConfig()

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(
        config.log_file_path,
        encoding=config.default_encoding,
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger