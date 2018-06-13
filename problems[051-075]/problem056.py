#! python3
"""Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?"""


def digital_sum(n):
    return sum(int(i) for i in str(n))

print(max(digital_sum(a ** b) for a in range(100) for b in range(100)))
