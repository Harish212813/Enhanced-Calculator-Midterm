import pytest

from app.calculator import Calculator


def test_calculator_performs_calculation():
    calculator = Calculator()

    result = calculator.calculate("add", 5, 3)

    assert result == 8
    assert len(calculator.get_history()) == 1


def test_calculator_stores_multiple_calculations():
    calculator = Calculator()

    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 4, 5)

    history = calculator.get_history()

    assert len(history) == 2
    assert history[0].result == 5
    assert history[1].result == 20


def test_calculator_clear_history():
    calculator = Calculator()

    calculator.calculate("subtract", 10, 4)
    calculator.clear_history()

    assert calculator.get_history() == []


def test_calculator_undo():
    calculator = Calculator()

    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 4, 5)

    calculator.undo()

    history = calculator.get_history()

    assert len(history) == 1
    assert history[0].result == 5


def test_calculator_redo():
    calculator = Calculator()

    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 4, 5)

    calculator.undo()
    calculator.redo()

    history = calculator.get_history()

    assert len(history) == 2
    assert history[1].result == 20


def test_undo_clear_history():
    calculator = Calculator()

    calculator.calculate("add", 5, 5)
    calculator.clear_history()

    assert calculator.get_history() == []

    calculator.undo()

    assert len(calculator.get_history()) == 1
    assert calculator.get_history()[0].result == 10


def test_save_and_load_history(tmp_path):
    calculator = Calculator()
    calculator.calculate("power", 2, 3)

    file_path = tmp_path / "history.csv"

    calculator.save_history(file_path)

    new_calculator = Calculator()
    new_calculator.load_history(file_path)

    assert len(new_calculator.get_history()) == 1
    assert new_calculator.get_history()[0].operation == "power"
    assert new_calculator.get_history()[0].result == 8


def test_invalid_operation():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.calculate("unknown", 5, 3)


def test_undo_with_no_history():
    calculator = Calculator()

    with pytest.raises(ValueError, match="Nothing to undo"):
        calculator.undo()


def test_redo_without_undo():
    calculator = Calculator()

    with pytest.raises(ValueError, match="Nothing to redo"):
        calculator.redo()