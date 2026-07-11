import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class CalculatorConfig:
    def __init__(self):
        self.log_dir = Path(os.getenv("CALCULATOR_LOG_DIR", "logs"))
        self.history_dir = Path(os.getenv("CALCULATOR_HISTORY_DIR", "data"))

        self.log_file = os.getenv(
            "CALCULATOR_LOG_FILE",
            "calculator.log",
        )

        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE",
            "history.csv",
        )

        self.max_history_size = int(
            os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100")
        )

        self.auto_save = (
            os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        )

        self.precision = int(
            os.getenv("CALCULATOR_PRECISION", "2")
        )

        self.max_input_value = float(
            os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000")
        )

        self.default_encoding = os.getenv(
            "CALCULATOR_DEFAULT_ENCODING",
            "utf-8",
        )

        self.validate()
        self.create_directories()

    def validate(self):
        if self.max_history_size <= 0:
            raise ValueError("Maximum history size must be greater than zero")

        if self.precision < 0:
            raise ValueError("Precision cannot be negative")

        if self.max_input_value <= 0:
            raise ValueError("Maximum input value must be greater than zero")

    def create_directories(self):
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.history_dir.mkdir(parents=True, exist_ok=True)

    @property
    def log_file_path(self):
        return self.log_dir / self.log_file

    @property
    def history_file_path(self):
        return self.history_dir / self.history_file