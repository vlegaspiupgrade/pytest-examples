
def test_amazing():
    from src.amazing import amaze
    import pandas as pd

    name = "John"
    data = pd.DataFrame({"op1": [2], "op2": [3]})
    result = amaze(name, data)
    print("result:", result)
    assert result == "Hello John. See how amazing I am!\nI'm going to add the first and second operands you provided.\n2 + 3 = 5"
