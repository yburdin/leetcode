import pytest


# 387. First Unique Character in a String
def first_uniq_char(s: str) -> int:
    char_dict = {}
    visited = set()

    for i, char in enumerate(s):
        if char not in char_dict and char not in visited:
            visited.add(char)
            char_dict[char] = i
        elif char in char_dict:
            del char_dict[char]

    if len(char_dict) > 0:
        return min(char_dict.values())
    else:
        return -1


@pytest.mark.parametrize('s, expected', [
    ('leetcode', 0),
    ('loveleetcode', 2),
    ('aabb', -1),
])
def test_first_uniq_char(s, expected):
    assert first_uniq_char(s) == expected