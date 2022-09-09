# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# Aula 12

'''
Yudi Yamane
160149410

Python

Executar com 

python -m md2.tcr samples/input1.csv

A entrada deve ser o caminho para um arquivo csv.
Cada linha deve ser uma equação de congruência
com ai, bi, e ni. Exemplo:

1,2,3
2,1,5
3,2,7
'''

from typing import List, Tuple
from md2.mdc import mdc_i
import sys

args = sys.argv[1::]
input_path = args[0]


def get_system_of_eq(input_path: str) -> List[List[int]]:
    file = open(input_path, 'r')
    matrix_input = []
    for line in file:
        values_str = line.split(',')
        values_int = [int(i.rstrip()) for i in values_str]
        matrix_input.append(values_int)
    return matrix_input


def check_all_n_are_coprimes(n_list: List[int]) -> bool:
    n_list_size = len(n_list)
    for i in range(n_list_size):
        for j in range(i+1, n_list_size):
            if mdc_i(n_list[i], n_list[j]) != 1:
                return False
    return True


def check_ai_ni_are_coprimes(a_list: List[int], n_list: List[int]) -> bool:
    for ai, ni in zip(a_list, n_list):
        if mdc_i(ai, ni) != 1:
            return False
    return True


def check_solution_exists(a_list: List[int], n_list: List[int]) -> bool:
    return check_ai_ni_are_coprimes(a_list, n_list) and check_all_n_are_coprimes(n_list)


def find_inverse_mod_n(a: int, n: int) -> int | None:
    '''
    Encontrar i : a.i ≡ 1 (mod n)
    '''
    for i in range(1, n):
        if (a*i - 1) % n == 0:
            return i
    return None

def _try_brute_force(a: int, b: int, n: int) -> int | None:
    for x in range(1, n):
        if (a*x - b) % n == 0:
            return x
    return None

def solve_congruence_eq(a: int, b: int, n: int) -> int | None:
    '''
    ax ≡ b (mod n)
    x ≡ b.i (mod n), i inv a (mod n)
    '''
    i = find_inverse_mod_n(a, n)
    if i == None:
        return _try_brute_force(a, b, n)
    x = b*i
    x = x % n
    return x

def solve_congruence_sys(system: List[List[int]]) -> Tuple[int, int]:
    a_list = [row[0] for row in system]
    n_list = [row[2] for row in system]

    if not (check_ai_ni_are_coprimes(a_list, n_list) and check_all_n_are_coprimes(n_list)):
        raise Exception('Não é possível aplicar TCR')
    
    solutions = [solve_congruence_eq(eq[0], eq[1], eq[2]) for eq in system]
    
    N = 1
    for ni in n_list:
        N *= ni
    N_list = [N//ni for ni in n_list]

    Ninv_list = [find_inverse_mod_n(Ni, ni) for (Ni, ni) in zip(N_list, n_list)]

    x = 0
    for (xi, Ni, Ni_inv) in zip(solutions, N_list, Ninv_list):
        x += xi*Ni*Ni_inv
    return (x % N, N)

def congruence_system_to_str(system: List[List[int]]) -> str:
    result = ''
    for eq in system:
        result += f'{eq[0]}x ≡ {eq[1]} (mod {eq[2]})\n'
    return result


def main():
    system = get_system_of_eq(input_path)

    (x, N) = solve_congruence_sys(system)

    print('Sistema:')
    print(congruence_system_to_str(system))
    print('Solução:')
    print('x =', x)
    print('N =', N)

if __name__ == '__main__':
    main()
