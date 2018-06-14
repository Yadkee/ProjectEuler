#! python3
"""Find the last ten digits of 28433×2^7830457+1"""

n = 28433
limit = 10 ** 10
for _ in range(7830457):
    n = (n + n) % limit
print(n + 1)
