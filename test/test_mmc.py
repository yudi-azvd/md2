import pytest

from mmc import mmc

test_data = [
  (15, 20, 60),
]

params = pytest.mark.parametrize("a, b, expected_mmc", test_data)

@pytest.mark.skip
@params
def test_mmc(a: int, b: int, expected_mmc: int):
  result_mmc = mmc(a, b)
  assert expected_mmc == result_mmc
