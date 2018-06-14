#! python3
from math import ceil
from itertools import count

fractions = []
for d in range(2, 10 ** 6):
    n = (3 * d - 1) // 7  # Immediately to the left of 3 / 7
    try:
        if d % n:
            fractions.append((n, d))
    except ZeroDivisionError:
        pass
print(max(fractions, key=lambda x: x[0] / x[1]))
