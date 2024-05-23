import pytest
from Easy.max_profit import *

@pytest.mark.parametrize('prices, expected_profit',[
                        ([7,1,5,3,6,4], 5),
                        ([7,6,4,3,1], 0)])
def test_max_profit(prices, expected_profit):
    assert max_profit(prices) == expected_profit

