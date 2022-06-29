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
  