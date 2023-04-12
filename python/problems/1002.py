from collections import Counter
from typing import List
import pytest


# 1002. Find Common Characters
def common_chars(words: List[str]) -> List[str]:
    result = Counter(words[0])
    for word in words:
        result &= Counter(word)

    return [char for char in result for _ in range(result[char])]


@pytest.mark.parametrize('words, expected', [
    (["bella", "label", "roller"], ["e", "l", "l"]),
    (["cool", "lock", "cook"], ["c", "o"]),
])
def test_intersect(words, expected):
    assert sorted(common_chars(words)) == sorted(expected)
