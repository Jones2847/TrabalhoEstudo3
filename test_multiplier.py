# test_multiplier
# from module import function_name
from multiplier import multiplier

def test01():
    TEST_VALUES = [1, 2, 3]
    EXPECTED_RESULT = 6

    bOK:bool =\
    EXPECTED_RESULT == multiplier(TEST_VALUES)

    assert (bOK)
# def test01

#test01() # DO NOT DO THIS IF USING PYTEST

