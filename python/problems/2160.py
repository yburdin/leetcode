import pytest


# 2160. Minimum Sum of Four Digit Number After Splitting Digits
def minimum_sum(num: int) -> int:
    sorted_digits = sorted(str(num))
    return int(sorted_digits[0] + sorted_digits[3]) + int(sorted_digits[1] + sorted_digits[2])


@pytest.mark.parametrize('num, expected', [
    (2932, 52),
    (4009, 13),
])
def test_minimum_sum(num: int, expected: int):
    assert minimum_sum(num) == expected
