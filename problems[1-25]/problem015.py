#! python3
"""How many such routes are there through a 20×20 grid?"""


def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)

n = 20

print(f(2 * n) // (f(n) ** 2))  # 2n! / n!^2
