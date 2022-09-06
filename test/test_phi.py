import pytest

from md2.euler import phi

test_data = [
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 2),
  (5, 4),
  (6, 2),
  (7, 6),
  (8, 4),
  (11, 10),
  (15, 8),
  (64, 32),
]

params = pytest.mark.parametrize("n, expected_phi", test_data)

@pytest.mark.skip
@params
def test_phi(n: int, expected_phi: str):
  assert expected_phi == phi(n)