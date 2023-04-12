import pytest
from collections import Counter


# 383. Ransom Note
def can_construct(ransomNote: str, magazine: str) -> bool:
    counter_r = Counter(ransomNote)
    counter_m = Counter(magazine)

    for char in counter_r:
        if counter_r[char] > counter_m[char]:
            return False

    return True


@pytest.mark.parametrize('ransom_note , magazine, expected', [
    ('a', 'b', False),
    ('aa', 'ab', False),
    ('aa', 'aab', True),
])
def test_first_uniq_char(ransom_note, magazine, expected):
    assert can_construct(ransom_note, magazine) == expected
