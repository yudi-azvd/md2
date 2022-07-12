from primes import is_prime

def test_primes():
  assert is_prime(2)
  assert is_prime(3)
  assert is_prime(5)
  assert is_prime(13)
  assert is_prime(31)
  assert is_prime(37)
  assert is_prime(151)

def test_not_primes():
  assert not is_prime(4)
  assert not is_prime(6)
  assert not is_prime(10)
  assert not is_prime(12)