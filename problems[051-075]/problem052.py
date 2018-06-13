#! python3
"""It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits."""
from itertools import count

for i in count(125874):
    s = sorted(str(i))
    for j in range(2, 7):
        if sorted(str(i * j)) != s:
            break
    else:
        break
print(i)
