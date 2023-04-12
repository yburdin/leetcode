import pytest


def simplify_path(path: str) -> str:
    result_path = '/'
    directories = path.split('/')
    stack = []
    for directory in directories:
        if len(directory) == 0:
            continue

        if directory == '..' and len(stack) > 0:
            stack.pop()
        elif directory != '..' and directory != '.':
            stack.append(directory)

    result_path += '/'.join(stack)
    return result_path


@pytest.mark.parametrize('path, expected', [
    ("/home/", "/home"),
    ("/../", "/"),
    ("/home//foo/", "/home/foo"),
    ("/a/./b/../../c/", "/c"),
])
def test_simplify_path(path, expected):
    assert simplify_path(path) == expected


