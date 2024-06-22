import pandas as pd
import pytest

from src.amazing import amaze

BASIC_NAME = "John"
EXPECTED_MIDDLE_LINE = "\nI'm going to add the first and second operands you provided."


def create_expected_name_line(name) -> str:
    return f"Hello {name}. See how amazing I am!"


def create_expected_addition_line(op1, op2) -> str:
    """
    This is probably as complicated as we should get with our test logic.
    """
    return f"\n{op1} + {op2} = {op1 + op2}"


def create_operands(op1, op2) -> pd.DataFrame:
    return pd.DataFrame({"op1": [op1], "op2": [op2]})


def test_amazing_happy():
    """
    For a function under test this simple, this may be enough.
    Ideally, we should:
    1. extract out code we'll be repeating (once we find ourselves creating more/similar tests/setup)
    2. separate testing of the two different arguments
    3. remove any print statements when done debugging
    """
    name = "John"
    first = 2
    second = 3
    data = pd.DataFrame({"op1": [first], "op2": [second]})
    result = amaze(name, data)
    print("result:", result)
    assert result.startswith(create_expected_name_line(BASIC_NAME))
    assert "\nI'm going to add the first and second operands you provided." in result
    assert result.endswith(create_expected_addition_line(first, second))


@pytest.mark.parametrize(
    "name",
    [
        "Jane",
        "!@#$%^&*()-=_+",
        1,
        " ",
        None,
        "Bobby tables",
    ]
)
def test_name_parameterized(name):
    data = create_operands(1, 2)
    result = amaze(name, data)
    expected = create_expected_name_line(name) + EXPECTED_MIDDLE_LINE
    assert result.startswith(expected)
