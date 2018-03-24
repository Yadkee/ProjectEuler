#! python3
"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

for c in range(1000 - 2, 1, -1):
    for b in range(1, 1000 - c - 1):
        a = 1000 - b - c
        if c ** 2 == a ** 2 + b ** 2:
            print(a * b * c)
            break
