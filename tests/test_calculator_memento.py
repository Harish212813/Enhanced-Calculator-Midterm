import pytest

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento, HistoryCaretaker


def test_memento_stores_calculation_state():
    calculation = Calculation("add", 2, 3)
    calculation.calculate()

    memento = CalculatorMemento([calculation])
    saved_state = memento.get_state()

    assert len(saved_state) == 1
    assert saved_state[0].result == 5


def test_memento_returns_copy():
    calculation = Calculation("multiply", 4, 5)
    calculation.calculate()

    original_state = [calculation]
    memento = CalculatorMemento(original_state)

    saved_state = memento.get_state()
    saved_state.clear()

    assert len(memento.get_state()) == 1


def test_undo_restores_previous_state():
    caretaker = HistoryCaretaker()

    first_calculation = Calculation("add", 2, 3)
    first_calculation.calculate()

    second_calculation = Calculation("multiply", 4, 5)
    second_calculation.calculate()

    calculations = [first_calculation]

    caretaker.save([])

    calculations.append(second_calculation)

    restored_state = caretaker.undo(calculations)

    assert restored_state == []


def test_redo_restores_undone_state():
    caretaker = HistoryCaretaker()

    calculation = Calculation("add", 2, 3)
    calculation.calculate()

    caretaker.save([])

    current_state = [calculation]
    undone_state = caretaker.undo(current_state)
    redone_state = caretaker.redo(undone_state)

    assert len(redone_state) == 1
    assert redone_state[0].result == 5


def test_undo_when_stack_is_empty():
    caretaker = HistoryCaretaker()

    with pytest.raises(ValueError, match="Nothing to undo"):
        caretaker.undo([])


def test_redo_when_stack_is_empty():
    caretaker = HistoryCaretaker()

    with pytest.raises(ValueError, match="Nothing to redo"):
        caretaker.redo([])


def test_new_save_clears_redo_stack():
    caretaker = HistoryCaretaker()

    calculation = Calculation("subtract", 10, 4)
    calculation.calculate()

    caretaker.save([])
    undone_state = caretaker.undo([calculation])

    caretaker.save(undone_state)

    with pytest.raises(ValueError, match="Nothing to redo"):
        caretaker.redo(undone_state)