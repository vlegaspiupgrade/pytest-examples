import pandas as pd


def amaze(name: str, data: pd.DataFrame) -> str:
    """
    My amazing function!
    It greets you, then does math for you!
    """
    result = f"Hello {name}. See how amazing I am!"
    result += "\nI'm going to add the first and second operands you provided."

    first = data.op1.iloc[0]
    second = data.op2.iloc[0]

    result += f"\n{first} + {second} = {first + second}"
    return result
