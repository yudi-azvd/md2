import pytest
from primes import PrimeGenerator

def test_should_return_2_as_current_prime_given_no_args():
  sut = PrimeGenerator()
  assert 2 == sut.get_current()


def test_should_accept_valid_prime_number_as_starting_number():
  return None != PrimeGenerator(2)


def test_should_throw_exception_if_starting_number_is_not_prime():
  with pytest.raises(Exception) as e:
    PrimeGenerator(4)
  assert 'is not prime' in str(e.value)
  
def test_should_throw_exception_if_starting_number_is_not_positive():
  with pytest.raises(Exception) as e:
    PrimeGenerator(-3)
  assert 'Not allowed numbers less than 0' in str(e.value)

def test_should_calculate_next_prime():
  sut = PrimeGenerator(2)
  assert 3 == sut.get_next()


def test_should_return_13_given_5_as_starting_number():
  sut = PrimeGenerator(5)
  assert 7 == sut.get_next()