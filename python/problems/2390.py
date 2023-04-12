import pytest


def remove_stars(s: str) -> str:
    stack = []
    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


@pytest.mark.parametrize('s, expected', [
    ("leet**cod*e", 'lecoe'),
    ("erase*****", ''),
])
def test_remove_stars(s, expected):
    assert remove_stars(s) == expected
