def mmc(a: int, b: int) -> int:
  '''
  Por definição

  Sim, ainda está erradão
  '''
  i = 1
  multiple_a = 1
  while True:
    multiple_a = a*i
    multiple_b = b*i
    i += 1
    if multiple_a == multiple_b:
      break
  return multiple_a
