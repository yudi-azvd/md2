import pytest

from mdc import mdc

test_data = [
  (15, 20, 5)
]

params = pytest.mark.parametrize("a, b, expected_mdc", test_data)


@params
def test_mdc_1(a: int, b: int, expected_mdc: int):
  result_mdc = mdc(a, b)
  assert expected_mdc == result_mdc