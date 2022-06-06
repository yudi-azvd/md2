

import pytest

test_data = [
  (100, 'wednesday'),
  (1_000_000, 'thursday'),
  (10**100, '?')
]

params = pytest.mark.parametrize("days, expected", test_data)

@params
def test_which_weekday(days: int, expected_weekday: str):
  
  return