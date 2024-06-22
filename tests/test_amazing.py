import pandas as pd
import pytest

from src.amazing import amaze

BASIC_NAME = "John"
EXPECTED_MIDDLE_LINE = "\nI'm going to add the first and second operands you provided."


def create_operands(op1, op2) -> pd.DataFrame:
    return pd.DataFrame({"op1": [op1], "op2": [op2]})


def create_expected_name_line(name) -> str:
    return f"Hello {name}. See how amazing I am!"


def create_expected_addition_line(op1, op2, result) -> str:
    """ Notice we don't dynamically create the expected result, but pass it in implicitly. """
    return f"\n{op1} + {op2} = {result}"


def test_amazing_happy():
    """
    First basic, happy path test. It's not using any of the helper functions.
    For a function under test this simple, this may be enough.
    (This is what I've seen a lot of - we could do better.)
    Ideally, we should:
    1. extract out code we'll be repeating (once we find ourselves creating more/similar tests/setup)
      * or re-use existing helper functions
    2. separate testing of the two different arguments
    3. remove any print statements when done debugging
    """
    name = "John"
    first = 2
    second = 3
    data = pd.DataFrame({"op1": [first], "op2": [second]})

    result = amaze(name, data)
    print("result:", result)

    expected_start = f"Hello {name}. See how amazing I am!"
    expected_middle = "\nI'm going to add the first and second operands you provided."
    expected_end = f"\n{first} + {second} = 5"
    assert result == expected_start + expected_middle + expected_end


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
    """
    Notice we are not bothering to test the operands here.
    However, we are providing basic operands since they are required arguments.
    """
    operands = create_operands(1, 2)
    # If we tried to also test the operands and did something funky with it...
    # and we set it up wrong?
    # We may think it's a problem with the code under test, or the 'name' parameter
    # operands = create_operands(1, "2")
    result = amaze(name, operands)

    # Yes, in this example, we are testing the "middle line" here:
    # * it's not foreseen that it would change
    # * better to validate it's in the middle by expecting it right after the first line
    # * it's the same setup as testing the name - all required arguments are provided
    expected = create_expected_name_line(name) + EXPECTED_MIDDLE_LINE
    assert result.startswith(expected)


operand_parameters = [
    (5, 4, 9),
    (-1, 3, 2),
    (1_000, 599, 1_599),
    (0, 0, 0),
    (70, -200, -130),
]


@pytest.mark.parametrize(
    "first, second, expected_result",
    operand_parameters
)
def test_operands_parameterized(first, second, expected_result):
    """
    Notice we are not bothering to test the name parameter here.
    """
    operands = create_operands(first, second)
    result = amaze(BASIC_NAME, operands)
    assert result.endswith(create_expected_addition_line(first, second, expected_result))
