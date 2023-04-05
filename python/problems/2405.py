import pytest


# 2405. Optimal Partition of String
def partition_string(s: str) -> int:
    sub_str = ''
    result = 0

    for char in s:
        if char in sub_str:
            result += 1
            sub_str = char
        else:
            sub_str += char

    if len(sub_str) > 0:
        result += 1

    return result


@pytest.mark.parametrize('s, expected', [
    ('abacaba', 4),
    ('ssssss', 6)
])
def test_partition_string(s, expected):
    assert partition_string(s) == expected
