#! python3
"""Find the sum of the digits in the number 100!"""


def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)

print(sum(int(i) for i in str(f(100))))