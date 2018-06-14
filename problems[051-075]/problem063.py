#! python3
"""How many n-digit positive integers exist which are also an nth power?"""
from itertools import count

answer = 0
for i in range(1, 10):
    for j in count(1):
        ln = len(str(i ** j))
        if ln == j:
            answer += 1
        elif j > ln:
            break
print(answer)
