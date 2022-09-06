import pytest

from md2.mmc import mmc_backwards, mmc_backwards_2, mmc_teo12

test_data = [
  (15, 20, 60),
  (2, 7, 14),
  (3, 15, 15),
  (4, 6, 12),
]

params = pytest.mark.parametrize("a, b, expected_mmc", test_data)

@params
def test_mmc_teo12(a: int, b: int, expected_mmc: int):
  result_mmc = mmc_teo12(a, b)
  assert expected_mmc == result_mmc

@params
def test_mmc_backwards(a: int, b: int, expected_mmc: int):
  result_mmc = mmc_backwards(a, b)
  assert expected_mmc == result_mmc

@params
def test_mmc_backwards_2(a: int, b: int, expected_mmc: int):
  result_mmc = mmc_backwards_2(a, b)
  assert expected_mmc == result_mmc
