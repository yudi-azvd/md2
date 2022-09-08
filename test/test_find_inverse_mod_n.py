import pytest

from md2.tcr import find_inverse_mod_n
# python -m pytest -k "mod_n[1-13-1]"
test_data = [
    (2, 3, 2),
    (3, 4, 3),
    (3, 4, 3),
    # (mod 13)
    (1, 13, 1),
    (2, 13, 7),
    (3, 13, 9),
    (4, 13, 10),
    (5, 13, 8),
    (6, 13, 11),
    (7, 13, 2),
    (8, 13, 5),
    (9, 13, 3),
    (10, 13, 4),
    (11, 13, 6),
    (12, 13, 12),
]

params = pytest.mark.parametrize("a,n,expected_result", test_data)


@params
def test_find_inverse_mod_n(a: int, n: int, expected_result: int | None):
    assert find_inverse_mod_n(a, n) == expected_result
