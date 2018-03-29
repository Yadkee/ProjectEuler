#! python3
"""Find the sum of all numbers which are equal to the sum of the factorial of
their digits. Note: as 1! = 1 and 2! = 2 are not sums they are not included."""
# If anyone is interested -> http://mathworld.wolfram.com/Factorion.html

fact = dict(zip("0123456789", (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)))
print(sum(i for i in range(3, fact["9"]) if sum(fact[j] for j in str(i)) == i))
