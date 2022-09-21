from math import sqrt
from typing import List
from md2.mdc import mdc_i


def is_prime(n: int) -> bool:
    '''
    Apenas para números positivos.
    '''
    if n <= 1:
        return False
    square_root_of_n = int(sqrt(n))
    for i in range(2, square_root_of_n+1):
        if n % i == 0:
            return False
    return True


def prime_factors_of(n: int) -> List[int]:
    raise Exception('not implemented')
    return [1]


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


class PrimeGenerator():
    __current_prime = 2

    def __init__(self, starting_number=2) -> None:
        if starting_number <= 0:
            raise Exception(f'Not allowed numbers less than 0.')

        if not is_prime(starting_number):
            raise Exception(f'{starting_number} is not prime.'
                            '`starting_number` must be a prime.')

        self.__current_prime = starting_number

    def get_current(self):
        return self.__current_prime

    def get_next(self):
        i = self.__current_prime+1
        while not is_prime(i):
            i += 1
        self.__current_prime = i
        return self.__current_prime
