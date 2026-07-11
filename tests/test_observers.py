import logging

import pandas as pd

from app.calculator import Calculator
from app.observers import AutoSaveObserver, LoggingObserver


def test_logging_observer(caplog):
    calculator = Calculator()
    observer = LoggingObserver()

    calculator.register_observer(observer)

    with caplog.at_level(logging.INFO):
        calculator.calculate("add", 2, 3)

    assert "Calculation completed" in caplog.text
    assert "add" in caplog.text
    assert "5" in caplog.text


def test_auto_save_observer(tmp_path):
    file_path = tmp_path / "history.csv"

    calculator = Calculator()
    observer = AutoSaveObserver(file_path)

    calculator.register_observer(observer)
    calculator.calculate("multiply", 4, 5)

    assert file_path.exists()

    dataframe = pd.read_csv(file_path)

    assert len(dataframe) == 1
    assert dataframe.iloc[0]["operation"] == "multiply"
    assert dataframe.iloc[0]["result"] == 20


def test_multiple_observers(tmp_path, caplog):
    file_path = tmp_path / "history.csv"

    calculator = Calculator()
    logging_observer = LoggingObserver()
    auto_save_observer = AutoSaveObserver(file_path)

    calculator.register_observer(logging_observer)
    calculator.register_observer(auto_save_observer)

    with caplog.at_level(logging.INFO):
        calculator.calculate("subtract", 10, 4)

    assert "Calculation completed" in caplog.text
    assert file_path.exists()


def test_remove_observer(tmp_path):
    file_path = tmp_path / "history.csv"

    calculator = Calculator()
    observer = AutoSaveObserver(file_path)

    calculator.register_observer(observer)
    calculator.remove_observer(observer)

    calculator.calculate("add", 5, 5)

    assert not file_path.exists()


def test_remove_observer_not_registered():
    calculator = Calculator()
    observer = LoggingObserver()

    calculator.remove_observer(observer)

    assert calculator.observers == []