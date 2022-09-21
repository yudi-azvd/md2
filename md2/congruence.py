from typing import List, Tuple
from md2.primes import check_ai_ni_are_coprimes, check_all_n_are_coprimes


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

    Ninv_list = [find_inverse_mod_n(Ni, ni)
                 for (Ni, ni) in zip(N_list, n_list)]

    x = 0
    for (xi, Ni, Ni_inv) in zip(solutions, N_list, Ninv_list):
        x += xi*Ni*Ni_inv
    x %= N
    return (x, N), (solutions, N_list, Ninv_list)


def congruence_system_to_str(system: List[List[int]]) -> str:
    result = ''
    for eq in system:
        result += f'{eq[0]}x ≡ {eq[1]} (mod {eq[2]})\n'
    return result
