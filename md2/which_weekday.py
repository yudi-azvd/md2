'''
Qual será o dia da semana daqui a

a) 100 dias
b) 1.000.000 dias
b) 10^100 dias

?

0, 1
1, 3
14, 2
142, 6
1428, 4
14285, 5
142857, 1
1428571, 3
14285714, 2
142857142, 6
1428571428, 4
'''

map_exp_to_dias_a_mais = {
  0: 1,
  1: 3,
  4: 2,
  2: 6,
  8: 4,
}

# precisa do dia inicial
def which_weekday(total_days: int) -> str:
  remainder = total_days % 7
  pass

if __name__ == '__main__':
  days = [10**d for d in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]]
  for d in days:
    print(f'{d // 7}, {d % 7}')
