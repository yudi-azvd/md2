from typing import List, Optional
import pytest

from tcr import solve_congruence_eq

test_data = [
    (2, 5, 12, None),
    (4, 8, 12, [2, 3])
]

params = pytest.mark.parametrize("a,b,n,expected_result", test_data)
@params
def test_solve_congruence_eq(a: int, b: int, n: int, expected_result: Optional[List[int]]):
    assert solve_congruence_eq(a, b, n) == expected_result
