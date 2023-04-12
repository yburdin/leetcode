import pytest


def count_vowel_strings(n: int) -> int:
    n_vowels = 5

    if n < 2:
        return n_vowels

    dp = [[0 for _ in range(4)] + [1] for _ in range(n)]
    dp[0] = [5, 4, 3, 2, 1]
    for i in range(1, n):
        for j in range(3, -1, -1):
            dp[i][j] = dp[i-1][j] + dp[i][j + 1]

    return dp[-1][0]


@pytest.mark.parametrize('n, expected', [
    (1, 5),
    (2, 15),
    (33, 66045),
])
def test_count_vowel_strings(n: int, expected: int):
    assert count_vowel_strings(n) == expected
