from md2.mdc import mdc_i

def mmc_teo12(a: int, b: int) -> int:
  '''
  Segundo o Teorema 12 da Disciplina de MD2:
    
    `mmc(a,b) * mdc(a,b) = a * b`
  '''
  greatest_common_multiple = a*b
  return greatest_common_multiple/mdc_i(a, b)

def mmc_backwards(a: int, b: int) -> int:
  '''
  `possible_multiples_of_a_and_b` não é necessária. Era só tacar esse `range` lá 
  no `for`. Mas assim fica fácil de debugar.

  Assume-se que o mmc(a,b) <= a*b. Então são testados todos os números no 
  intervalo [max(a,b), a*b], do 
  '''
  ab = a * b
  greatest = max(a, b)
  possible_multiples_of_a_and_b = list(range(ab, greatest-1, -1))
  multiple_of_a_and_b = -1
  for n in possible_multiples_of_a_and_b:
    if n % a == 0 and n % b == 0:
      multiple_of_a_and_b = n
  return multiple_of_a_and_b

def mmc_backwards_2(a: int, b: int) -> int:
  ab = a * b
  greatest = max(a, b)
  possible_multiples_of_a_and_b = range(greatest, ab+1)
  multiple_of_a_and_b = greatest
  for n in possible_multiples_of_a_and_b:
    if n % a == 0 and n % b == 0:
      return n
  return multiple_of_a_and_b

def mmc_wrong(a: int, b: int) -> int:
  i = 1
  multiple_a = 1
  while True:
    multiple_a = a*i
    multiple_b = b*i
    i += 1
    if multiple_a == multiple_b:
      break
  return multiple_a

if __name__ == '__main__':
  print(mmc_teo12(15, 20))
  mmc_backwards(3, 15)