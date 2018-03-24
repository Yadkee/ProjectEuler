#! python3
"""By considering the terms in the Fibonacci sequence whose values do
not exceed four million, find the sum of the even-valued terms."""


def fib_until(m):
    a, b = 1, 1
    while a < m:
        yield a
        a, b = a + b, a

print(sum(i for i in fib_until(4 * 10 ** 6) if not i & 1))
