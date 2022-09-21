'''Resolvedor de Sistema de Equações de Congruência via Teorema Chinês dos Restos
Python

Executar com 

python -m md2.tcr samples/input1.csv

A entrada deve ser o caminho para um arquivo csv.
Cada linha deve ser uma equação de congruência
com ai, bi, e ni. Exemplo:

1,2,3
2,1,5
3,2,7

Teoria:
Aula 12: https://www.youtube.com/watch?v=mxJ5-ryGFjA&list=PLpizEtrJatZHsk1Ytqvaf6AMDzy8-gMz9&index=12&t=947s

Autor: Yudi Yamane, 160149410

https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
'''

import sys
from typing import List
from md2.primes import check_ai_ni_are_coprimes, check_all_n_are_coprimes
from md2.congruence import solve_congruence_sys, congruence_system_to_str


def get_system_of_eq(input_path: str) -> List[List[int]]:
    file = open(input_path, 'r')
    matrix_input = []
    for line in file:
        values_str = line.split(',')
        values_int = [int(i.rstrip()) for i in values_str]
        matrix_input.append(values_int)
    file.close()
    return matrix_input


def check_solution_exists(a_list: List[int], n_list: List[int]) -> bool:
    return check_ai_ni_are_coprimes(a_list, n_list) and check_all_n_are_coprimes(n_list)


def main():
    args = sys.argv[1::]
    input_path = args[0]

    system = get_system_of_eq(input_path)

    try:
        (x, N) = solve_congruence_sys(system)

        print('Sistema:')
        print(congruence_system_to_str(system))
        print('Solução:')
        print('x =', x)
        print('N =', N)
    except Exception as e:
        print(e.args[0])


if __name__ == '__main__':
    main()
