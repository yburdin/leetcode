import pytest


# 1221. Split a String in Balanced Strings
def balanced_string_split(s: str) -> int:
    result = 0
    cur_r = 0
    cur_l = 0

    for char in s:
        if char == 'R':
            cur_r += 1
        elif char == 'L':
            cur_l += 1

        if cur_r == cur_l:
            result += 1
            cur_r = 0
            cur_l = 0

    return result


@pytest.mark.parametrize('s, expected', [
    ("RLRRLLRLRL", 4),
    ("RLRRRLLRLL", 2),
    ("LLLLRRRR", 1)
])
def test_balanced_string_split(s, expected):
    assert balanced_string_split(s) == expected
