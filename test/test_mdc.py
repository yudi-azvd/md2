import pytest

from mdc import mdc_i, mdc_r, mdc_set

test_data = [
  (15, 20, 5),
  (19, 9, 1),
  (18, 9, 9),
  (48, 18, 6),
  (48, 18, 6),
]

params = pytest.mark.parametrize("a, b, expected_mdc", test_data)

@params
def test_mdc_r(a: int, b: int, expected_mdc: int):
  result_mdc = mdc_r(a, b)
  assert expected_mdc == result_mdc

@params
def test_mdc_i(a: int, b: int, expected_mdc: int):
  result_mdc = mdc_i(a, b)
  assert expected_mdc == result_mdc

@params
def test_mdc_set(a: int, b: int, expected_mdc: int):
  result_mdc = mdc_set(a, b)
  assert expected_mdc == result_mdc