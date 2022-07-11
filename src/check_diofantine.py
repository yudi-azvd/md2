from mdc import mdc_i


def check_diofantine(a, b, c, x0, y0, t_interval=20):
  max_divisor = mdc_i(a, b)
  if c % max_divisor != 0:
    raise Exception(f'{max_divisor} does not divide {c}')

  b_max_div = b//max_divisor
  a_max_div = a//max_divisor
  print(f'x = {x0} + {b_max_div}*t')
  print(f'y = {y0} - {a_max_div}*t')
  for t in range(-t_interval, t_interval+1):
    x = x0 + b_max_div*t
    y = y0 - a_max_div*t
    result = a*x + b*y
    s = f'{a}*{x} + {b}*{y} = {c}, t = {t}'
    s += f'\n\tdiff = {result} - {c} = {result-c}'
    assert result == c, s
  print('\tparamaters are correct!')

if __name__ == '__main__':
  # L01 Q28
  # check_diofantine(43, 5, 167, 2*167, -17*167)
  # L01 Q29
  # check_diofantine(119, 272, 1700, 700, -300)
  # L01 Q30
  check_diofantine(6643, 2873, 65000, -80000, 185000)
