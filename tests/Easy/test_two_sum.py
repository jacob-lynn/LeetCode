import pytest
from Easy.two_sum import two_sum

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([2, 5, 5, 11], 10, [1, 2]),
    ([0, 4, 3, 0], 0, [0, 3]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
])
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected