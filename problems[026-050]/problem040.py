#! python3
"""0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part,
find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""


def f(n):
    return int(fractional[n])

fractional = "".join(map(str, range(1000000)))
print(f(1) * f(10) * f(100) * f(1000) * f(10000) * f(100000) * f(1000000))
