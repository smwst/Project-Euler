"""https://projecteuler.net/problem=3"""

from typing import List

import pytest  # type: ignore


def is_prime(n: int) -> bool:
    """Determine if `n` is prime."""
    if n < 2 or str(n)[-1] in [0, 2, 4, 5, 6, 8]:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):  # n ** 0.5 == sqrt(n)
        if n % divisor == 0:
            return False
    return True

def prime_factors(n: int) -> List[int]:
    """Prime factors of `n` in ascending order."""
    if n < 2:
        return []
    if is_prime(n):
        return [n]
    divisor, factors = 2, []
    while True:
        quotient, remainder = divmod(n, divisor)
        if remainder:
            divisor += 1
        else:
            factors.append(divisor)
            n = quotient
            if is_prime(n):
                factors.append(n)
                break
    return factors

#####

@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])  # type: ignore
def test_is_prime(num: int) -> None:
    """Expected: True"""
    assert is_prime(num)

@pytest.mark.parametrize("num, factors", [  # type: ignore
    (22, [2, 11]),
    (333, [3, 3, 37]),
    (4444, [2, 2, 11, 101]),
    (55555, [5, 41, 271]),
    (666666, [2, 3, 3, 7, 11, 13, 37]),
    (7777777, [7, 239, 4649]),
    (88888888, [2, 2, 2, 11, 73, 101, 137]),
    (999999999, [3, 3, 3, 3, 37, 333667])
])
def test_prime_factors(num: int, factors: List[int]) -> None:
    """Expected: Correct prime factors"""
    assert prime_factors(num) == factors

def test_p003() -> None:
    """Expected: 6857"""
    assert prime_factors(600851475143)[-1] == 6857
