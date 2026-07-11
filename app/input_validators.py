from app.exceptions import ValidationError


def validate_number(value, max_input_value=1000000):
    try:
        number = float(value)
    except (TypeError, ValueError) as error:
        raise ValidationError("Input must be a valid number") from error

    if abs(number) > max_input_value:
        raise ValidationError(
            f"Input must be between {-max_input_value} and {max_input_value}"
        )

    return number