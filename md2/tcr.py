# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# Aula 12

from functools import reduce
from typing import List, Tuple
from md2.mdc import mdc_i
import sys

args = sys.argv[1::]
input_path = args[0]


def get_input(input_path: str) -> List[List[int]]:
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
        raise Exception('Não existe solução')
    
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


def main():
    # Saída esperada:
    # input1: x = 38, N = 105
    # input2: x = 416, N = 630
    # input3: x = 74, N = 420 (vídeo L03Q02)

    system = get_input(input_path)

    (x, N) = solve_congruence_sys(system)
    print('Solução:')
    print('x =', x)
    print('N =', N)

if __name__ == '__main__':
    main()
