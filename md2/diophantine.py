from md2.mdc import mdc_i


def check_diophantine(a, b, c, x0, y0, t_interval=20):
    max_divisor = mdc_i(a, b)
    if c % max_divisor != 0:
        raise Exception(f'{max_divisor} does not divide {c}')

    b_max_div = b//max_divisor
    a_max_div = a//max_divisor
    print(f'x = {x0} + {b_max_div}*t')
    print(f'y = {y0} - {a_max_div}*t')
    for t in range(-t_interval, t_interval+1):
        x = x0 + b_max_div*t
        y = y0 - a_max_div*t
        result = a*x + b*y
        s = f'{a}*{x} + {b}*{y} = {c}, t = {t}'
        s += f'\n\tdiff = {result} - {c} = {result-c}'
        assert result == c, s
    print('\tparamaters are correct!')


def calculate_successive_divisions(a: int, b: int):
    divisions = []
    bigger = max(a, b)
    smaller = min(a, b)
    a, b = bigger, smaller
    while b != 0:
        new_b = a % b
        quocient = a // b
        divisions.append([a, (b, quocient), new_b])
        a = b
        b = new_b
    return divisions


def rollback_successive_divisions(successive_divisions: list[list[int]]):
    for division in successive_divisions:
        print(division)
    return 0


def solve_diophantine_eq(a: int, b: int, c: int) -> list[int] | None:
    '''Resolve equação diofantina

    ax + by = c

    d = mdc(a, b)

    retorna:
        (x0, y0),
        (b//d, -a//d)
    '''
    mdc_ab = mdc_i(a, b)
    if c % mdc_ab != 0:
        return None
    x0 = a
    y0 = b
    return [x0, y0, b//mdc_ab, -a//mdc_ab]


if __name__ == '__main__':
    # L01 Q28
    # check_diophantine(43, 5, 167, 2*167, -17*167)
    # L01 Q29
    # check_diophantine(119, 272, 1700, 700, -300)
    # L01 Q30
    # check_diophantine(6643, 2873, 65000, -80000, 185000)
    divs = calculate_successive_divisions(43, 5)
    for d in divs:
        print(d)
