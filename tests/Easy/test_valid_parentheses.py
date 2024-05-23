import pytest
from Easy.valid_parentheses import is_valid_parentheses


@pytest.mark.parametrize("s, expected",[
                         ("()", True),
                         ("()[]{}", True),
                         ("(]", False)
                         ])
def test_valid_parentheses(s:str, expected:bool):
    assert is_valid_parentheses(s) == expected