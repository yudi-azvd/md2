import pytest

from md2.tcr import solve_congruence_eq

test_data = [
    (3, 1, 4, 3),
    (4, 8, 12, 2),
    (2021, 9, 13, 8),
    (1, 3, 7, 3),
    (1, 2, 9, 2),
    (2, 1, 3, 2),
    # 3x === 2 (mod 4), x = 2
    (3, 2, 4, 2),
    (2, 5, 12, None),
    (4, 6, 8, None),
]

params = pytest.mark.parametrize("a,b,n,expected_result", test_data)


@params
def test_solve_congruence_eq(a: int, b: int, n: int, expected_result: int | None):
    assert solve_congruence_eq(a, b, n) == expected_result
