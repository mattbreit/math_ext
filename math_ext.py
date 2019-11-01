import sys
import math
import unittest
from functools import lru_cache, reduce
from itertools import combinations, chain
import operator


""" The golden ratio."""
phi = (1.0 + math.sqrt(5.0)) / 2.0

""" Pi to 100 digits."""
pi_100 = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"


@lru_cache(maxsize=None)
def prime_factors(n):

    f = [n]
    d = 2

    while d < f[0]:
        if f[0] % d == 0:
            f[0] = f[0] // d
            f.append(d)
        else:
            d += 1

    return tuple(sorted(f))


def test_prime_factors():
    assert prime_factors(1) == (1,)
    assert prime_factors(2) == (2,)
    assert prime_factors(3) == (3,)
    assert prime_factors(4) == (2, 2)
    assert prime_factors(5) == (5,)
    assert prime_factors(6) == (2, 3)
    assert prime_factors(7) == (7,)
    assert prime_factors(8) == (2, 2, 2)
    assert prime_factors(9) == (3, 3)
    assert prime_factors(10) == (2, 5)
    assert prime_factors(210) == (2, 3, 5, 7)
    assert prime_factors(1024) == (2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
    assert prime_factors(2310) == (2, 3, 5, 7, 11)
    assert prime_factors(2019) == (3, 673)
    assert prime_factors(2020) == (2, 2, 5, 101)


def intify(n):
    return int(n) if int(n) == n else n


def div(n, d):
    if n % d == 0:
        return n // d
    else:
        return n / d


def sqrt(n):
    r = math.sqrt(n)
    if int(r) ** 2 == n:
        return int(r)
    else:
        return r


def triangular(n):
    return div(n * (n + 1), 2)


def test_triangular():
    assert triangular(3) == 6
    assert triangular(5) == 15
    assert triangular(6) == 21
    assert triangular(8) == 36
    assert triangular(36) == 666
    assert triangular(66) == 2211
    assert triangular(666) == 222111


def triangular_root(n):
    return div(sqrt(8 * n + 1) - 1, 2)


def test_triangular_root():
    assert triangular_root(6) == 3
    assert triangular_root(15) == 5
    assert triangular_root(21) == 6
    assert triangular_root(36) == 8
    assert triangular_root(666) == 36
    assert triangular_root(888) == 41.64558102577303
    assert triangular_root(2211) == 66
    assert triangular_root(222111) == 666


def triads(n, m):
    for a in range(n, m+1):
        for b in range(a+1, m+1):
            c2 = math.sqrt(a**2 + b**2)
            if int(c2) == c2:
                yield a, b, int(c2)


def triads2(n, m):
    for a, b in combinations(range(n, m + 1), 2):
        c2 = math.sqrt(a**2 + b**2)
        if int(c2) == c2:
            yield a, b, int(c2)


""" Prove that this is equivalent to reduce(math.gcd, numbers)."""
def hcf(numbers):
    #import pdb; pdb.set_trace()
    factors = [prime_factors(n) for n in numbers]
    #print(factors)

    answer = 1

    done = False
    while not done:
        done = True
        for val in set(chain(*factors)):
            positions = [(f.index(val) if val in f else None) for f in factors]
            #print(val, positions)

            if all(pos is not None for pos in positions):
                for i, pos in enumerate(positions):
                    factors[i] = factors[i][:pos] + factors[i][pos + 1:]
                answer *= val
                done = False
                break

    return answer


def test_hcf():
    assert hcf([60,80,100]) == 20


def product(numbers):
    return reduce(operator.mul, numbers)


def lcm(numbers):
    return div(product(numbers), hcf(numbers))


def test_lcm():
    assert lcm([6,8,12]) == 24


def convert_base(value, base):
    places = []
    try:
        power = int(math.log(value) / math.log(base))
        while value > 0:
            scale = base ** power
            if scale == 0:
                break
            place_value = int(value / scale)
            places.append((place_value, power))
            value -= place_value * scale
            power -= 1
        return places
    except Exception:
        print([p[0] for p in places])
        raise


def test_convert_base():
    assert convert_base(666, 60) == [(11,1),(6,0)]

    # this is not true pi base 60, but the truncated math.pi, which only has
    # about 15 digits, converted to base 60, which will have a lot more digits,
    # but beyond about 8 digits it is all garbage
    digits = convert_base(math.pi, 60)

    for precision in range(1, 13):
        values = [d[0] * 60 ** d[1] for d in digits[:precision]]
        print(','.join('%02d' % d[0] for d in digits[:precision]))
        print(precision, values)
        print(sum(values))


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def digits(n):
    assert n >= 0
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n = n // 10
    return digits


def add_digits(n):
    return sum(digits(n))


def digital_root(n):
    while n >= 10:
        n = add_digits(n)
    return n


def _trace_profile(frame, event, arg):
    argnames = frame.f_code.co_varnames[:frame.f_code.co_argcount]
    argdict = {k: frame.f_locals[k] for k in argnames}
    print(frame, 'args:', argdict, 'event:', event, 'arg:', arg)


def test_trace_profile():
    sys.setprofile(_trace_profile)
    print(prime_factors(6))
    sys.setprofile(None)


def primes(max):
    nums = list(range(1,max+1))
    for n in range(2, int(math.sqrt(max))):
        for m in range(n, max):
            p = m * n
            if p in nums:
                nums.remove(p)
    return nums
