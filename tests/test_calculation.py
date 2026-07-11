import pytest

from app.calculation import Calculation


def test_create_calculation():
    calculation = Calculation("add", 5, 3)

    assert calculation.operation == "add"
    assert calculation.operand_a == 5
    assert calculation.operand_b == 3
    assert calculation.result is None
    assert calculation.timestamp is not None


def test_calculate_result():
    calculation = Calculation("multiply", 4, 5)

    result = calculation.calculate()

    assert result == 20
    assert calculation.result == 20


def test_calculation_to_dict():
    calculation = Calculation("subtract", 10, 4)
    calculation.calculate()

    calculation_data = calculation.to_dict()

    assert calculation_data["operation"] == "subtract"
    assert calculation_data["operand_a"] == 10
    assert calculation_data["operand_b"] == 4
    assert calculation_data["result"] == 6
    assert calculation_data["timestamp"] is not None


def test_invalid_calculation_operation():
    calculation = Calculation("unknown", 5, 3)

    with pytest.raises(ValueError):
        calculation.calculate()


def test_calculation_division_by_zero():
    calculation = Calculation("divide", 10, 0)

    with pytest.raises(ValueError):
        calculation.calculate()