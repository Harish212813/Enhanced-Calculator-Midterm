from pathlib import Path

import pandas as pd

from app.calculation import Calculation


class CalculationHistory:
    def __init__(self):
        self.calculations = []

    def add(self, calculation):
        self.calculations.append(calculation)

    def get_all(self):
        return self.calculations

    def clear(self):
        self.calculations.clear()

    def save_to_csv(self, file_path):
        data = [calculation.to_dict() for calculation in self.calculations]
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(file_path, index=False)

    def load_from_csv(self, file_path):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("History file was not found")

        try:
            dataframe = pd.read_csv(file_path)
        except pd.errors.ParserError as error:
            raise ValueError("History file could not be read") from error

        required_columns = {
            "operation",
            "operand_a",
            "operand_b",
            "result",
            "timestamp",
        }

        if not required_columns.issubset(dataframe.columns):
            raise ValueError("History file is missing required columns")

        self.calculations.clear()

        for _, row in dataframe.iterrows():
            calculation = Calculation(
                row["operation"],
                row["operand_a"],
                row["operand_b"],
            )
            calculation.result = row["result"]
            calculation.timestamp = pd.to_datetime(row["timestamp"]).to_pydatetime()
            self.calculations.append(calculation)