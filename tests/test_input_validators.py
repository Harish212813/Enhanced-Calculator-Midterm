import pytest

from app.exceptions import ValidationError
from app.input_validators import validate_number


@pytest.mark.parametrize(
    "value,expected",
    [
        ("5", 5.0),
        ("3.5", 3.5),
        ("-10", -10.0),
        (8, 8.0),
    ],
)
def test_validate_number(value, expected):
    assert validate_number(value) == expected


def test_invalid_string_input():
    with pytest.raises(
        ValidationError,
        match="Input must be a valid number",
    ):
        validate_number("hello")


def test_none_input():
    with pytest.raises(
        ValidationError,
        match="Input must be a valid number",
    ):
        validate_number(None)


def test_input_above_maximum():
    with pytest.raises(
        ValidationError,
        match="Input must be between",
    ):
        validate_number(1001, max_input_value=1000)


def test_input_below_minimum():
    with pytest.raises(
        ValidationError,
        match="Input must be between",
    ):
        validate_number(-1001, max_input_value=1000)