# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
# Aula 12

from typing import List
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
    for i in range(n):
        if (a*i - 1) % n == 0:
            return i
    return None



def main():
    # Saída esperada para input1.csv
    print('x =', 38)
    print('N =', 105)

    matrix_input = get_input(input_path)
    a_list = [row[0] for row in matrix_input]
    b_list = [row[1] for row in matrix_input]
    n_list = [row[2] for row in matrix_input]
    k = len(matrix_input)

    # print(n_list)
    # all_n_are_coprimes = verify_all_n_are_coprimes(n_list)
    print(check_ai_ni_are_coprimes(a_list, n_list))
    # print('all_n_are_coprimes', all_n_are_coprimes)
    # print(k)
    # print(matrix_input)
    # print(a_list)
    # print(b_list)
    '''
    0 0 0
    0 0 0
    0 0 0
    '''


if __name__ == '__main__':
    main()
