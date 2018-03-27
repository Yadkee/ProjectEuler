#! python3
"""Find the largest palindrome made from the product
of two 3-digit numbers."""

largest = []
for i in range(100, 1000):
    for j in range(100, 1000):
        ij = i * j
        sij = str(ij)
        if sij == sij[::-1]:
            largest.append(ij)
print(max(largest))
