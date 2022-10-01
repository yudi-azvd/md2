import pytest

from md2.congruence import solve_congruence_sys

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
         [7, 8, 15]],
        (74, 420)
    ),
]

params = pytest.mark.parametrize("system,expected_result", test_data)


@params
def test_solve_congruence_sys(system: list[list[int]], expected_result: tuple[int, int]):
    sol, _ = solve_congruence_sys(system)
    assert sol == expected_result
