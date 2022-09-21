from typing import List
import pytest

from md2.diophantine import solve_diophantine_eq

test_data = [
    # Lista 1 Q 28
    (43, 5, 167, [4, -1, 5, -43]),
    # Lista 1 Q 29
    (119, 272, 1700, [700, 300, 16, -7]),
    # Lista 1 Q 30
    (6643, 2873, 65000, [-80000, 185000, 221, -511])
]

params = pytest.mark.parametrize("a, b, c, expected_result", test_data)

@pytest.mark.skip
@params
def test_solve_diophantine_eq(
    a: int, b: int, c: int, 
    expected_result: List[int], 
):
    assert solve_diophantine_eq(a, b, c) == expected_result
