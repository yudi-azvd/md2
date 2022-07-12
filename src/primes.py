from math import sqrt

def is_prime(n: int) -> bool:
  '''
  Apenas para números positivos.
  '''
  if n <= 1:
    return False
  square_root_of_n = int(sqrt(n))
  for i in range(2, square_root_of_n+1):
    if n % i == 0:
      return False
  return True