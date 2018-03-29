#! python3
"""Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital."""


def is_pandigital(m1, m2):
    if sorted(str(m1) + str(m2) + str(m1 * m2)) == s:
        if m1 * m2 not in cache:
            cache.add(m1 * m2)
            return True

s = sorted("123456789")
cache = set()
# The only two ways to form a 9 pandigital are:
# 1 digit * 4 digit = 5 digits
# 2 digit * 3 digit = 5 digits
rs = ((range(2, 10), range(10 ** 3, 10 ** 4)),
      (range(10, 10 ** 2), range(10 ** 2, 10 ** 3)))

print(sum(i * j for a, b in rs for i in a for j in b if is_pandigital(i, j)))
