import pandas as pd
import pytest

from app.calculation import Calculation
from app.history import CalculationHistory


def test_add_calculation_to_history():
    history = CalculationHistory()
    calculation = Calculation("add", 2, 3)
    calculation.calculate()

    history.add(calculation)

    assert len(history.get_all()) == 1
    assert history.get_all()[0].result == 5


def test_clear_history():
    history = CalculationHistory()
    calculation = Calculation("multiply", 4, 5)
    calculation.calculate()
    history.add(calculation)

    history.clear()

    assert history.get_all() == []


def test_save_history_to_csv(tmp_path):
    history = CalculationHistory()
    calculation = Calculation("subtract", 10, 4)
    calculation.calculate()
    history.add(calculation)

    file_path = tmp_path / "history.csv"
    history.save_to_csv(file_path)

    dataframe = pd.read_csv(file_path)

    assert len(dataframe) == 1
    assert dataframe.iloc[0]["operation"] == "subtract"
    assert dataframe.iloc[0]["result"] == 6


def test_load_history_from_csv(tmp_path):
    history = CalculationHistory()

    data = {
        "operation": ["add"],
        "operand_a": [5],
        "operand_b": [3],
        "result": [8],
        "timestamp": ["2026-07-10T12:00:00"],
    }

    file_path = tmp_path / "history.csv"
    pd.DataFrame(data).to_csv(file_path, index=False)

    history.load_from_csv(file_path)

    assert len(history.get_all()) == 1
    assert history.get_all()[0].operation == "add"
    assert history.get_all()[0].result == 8


def test_load_missing_file():
    history = CalculationHistory()

    with pytest.raises(FileNotFoundError):
        history.load_from_csv("missing_history.csv")


def test_load_file_with_missing_columns(tmp_path):
    history = CalculationHistory()

    file_path = tmp_path / "invalid.csv"
    pd.DataFrame({"operation": ["add"]}).to_csv(file_path, index=False)

    with pytest.raises(ValueError):
        history.load_from_csv(file_path)