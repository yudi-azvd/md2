from md2.primes import is_prime, prime_factors_of

def phi(n) -> int:
  if is_prime(n):
      return n-1
  
  factors = prime_factors_of(n)
  result = 1
  for f in factors:
    result *= (f-1)
  return result