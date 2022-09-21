from typing import List, Tuple
import pytest

from md2.tcr import solve_congruence_sys

test_data = [
    (
        [[1, 2, 3],
         [2, 1, 5],
         [3, 2, 7]],
        (38, 105)
    ),
    (
        [[1, 3, 7],
         [1, 2, 9],
         [9, 4, 10]],
        (416, 630)
    ),
    (
        [[1, 2, 4],
         [2, 1, 7],
         [7, 8, 15],
         [1, 7122018, 11]],
        (74, 420)
    ),
]

params = pytest.mark.parametrize("system,expected_result", test_data)


@params
def test_solve_congruence_sys(system: List[List[int]], expected_result: Tuple[int, int]):
    assert solve_congruence_sys(system) == expected_result
