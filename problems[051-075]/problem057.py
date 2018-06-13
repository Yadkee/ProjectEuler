#! python3
"""√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?"""

answer = 0
n, d = 3, 2
for _ in range(1000):
    if len(str(n)) > len(str(d)):
        answer += 1
    n, d = n + d + d, n + d
print(answer)
