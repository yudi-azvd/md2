from typing import Set

'''
Algoritmo das divisões sucessivas
'''
def mdc_r(a: int, b: int) -> int:
  if b == 0:
    return a
  return mdc_r(b, a % b)

def mdc_i(a: int, b: int) -> int:
  while b != 0:
    new_b = a % b
    a = b
    b = new_b
  return a

'''
Algoritmo usando a definição de MDC
'''
def mdc_set(a: int, b: int) -> int:
  a_divisors = __get_divisors(a)
  b_divisors = __get_divisors(b)
  mdc = max(a_divisors.intersection(b_divisors))
  return mdc

def __get_divisors(n: int) -> Set[int]:
  divisors = set([1])
  for i in range(2, n+1):
    if n % i == 0:
      divisors.add(i)
  return divisors

  