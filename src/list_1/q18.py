# python -m src.list_1.q18

from ..mdc import get_divisors

if __name__ ==  '__main__':
  divisors_of_8 = get_divisors(8)
  divisors = [i -1 for i in divisors_of_8]

  for n in divisors:
    print((n*n - 7*n)/(n+1))

