import pytest

from app.operations import OperationFactory


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 5, 3, 8),
        ("subtract", 5, 3, 2),
        ("multiply", 5, 3, 15),
        ("divide", 10, 2, 5),
        ("power", 2, 3, 8),
        ("root", 9, 2, 3),
        ("modulus", 10, 3, 1),
        ("int_divide", 10, 3, 3),
        ("percent", 25, 100, 25),
        ("abs_diff", 5, 10, 5),
    ],
)
def test_operations(operation, a, b, expected):
    calculator_operation = OperationFactory.create_operation(operation)
    assert calculator_operation.execute(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "operation",
    ["divide", "modulus", "int_divide"],
)
def test_division_by_zero(operation):
    calculator_operation = OperationFactory.create_operation(operation)

    with pytest.raises(ValueError):
        calculator_operation.execute(10, 0)


def test_percentage_with_zero():
    calculator_operation = OperationFactory.create_operation("percent")

    with pytest.raises(ValueError):
        calculator_operation.execute(10, 0)


def test_zero_root():
    calculator_operation = OperationFactory.create_operation("root")

    with pytest.raises(ValueError):
        calculator_operation.execute(9, 0)


def test_even_root_of_negative_number():
    calculator_operation = OperationFactory.create_operation("root")

    with pytest.raises(ValueError):
        calculator_operation.execute(-16, 2)


def test_odd_root_of_negative_number():
    calculator_operation = OperationFactory.create_operation("root")

    assert calculator_operation.execute(-8, 3) == pytest.approx(-2)


def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.create_operation("invalid")