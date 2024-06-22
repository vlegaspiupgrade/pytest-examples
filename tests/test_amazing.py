import pandas as pd

from src.amazing import amaze


def test_amazing_happy():
    """
    First basic, happy path test.
    For a function under test this simple, this may be enough.
    (I see a lot of this. We could do better.)
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

    expected = (
        f"Hello {name}. See how amazing I am!"
        "\nI'm going to add the first and second operands you provided."
        f"\n{first} + {second} = 5"
    )
    assert result == expected
