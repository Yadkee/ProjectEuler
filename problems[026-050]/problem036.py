#! python3
"""Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2."""

print(sum(i for i in range(10 ** 6) if str(i) == str(i)[::-1] and
      bin(i)[2:] == bin(i)[2:][::-1]))
