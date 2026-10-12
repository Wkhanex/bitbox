# tool: divisors
# description: List all positive divisors of a positive integer
# author: @Wkhanex
# example: divisors "12" -> "1,2,3,4,6,12"

import math


def run(*args) -> str:
    """Return positive divisors in ascending order without repeating square roots."""
    if len(args) != 1:
        raise ValueError("expected one positive integer")
    n = int(args[0])
    if n <= 0:
        raise ValueError("n must be a positive integer")
    small, large = [], []
    for candidate in range(1, math.isqrt(n) + 1):
        if n % candidate == 0:
            small.append(candidate)
            quotient = n // candidate
            if quotient != candidate:
                large.append(quotient)
    return ",".join(str(value) for value in small + large[::-1])
