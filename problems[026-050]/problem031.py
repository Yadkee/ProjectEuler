#! python
"""England coints: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
How many different ways can £2 be made using any number of coins?"""
# I tried other methods than recursion but it is clearly the best way

print(sum(1 for a in range(0, 201, 200)
          for b in range(0, 201 - a, 100)
          for c in range(0, 201 - a - b, 50)
          for d in range(0, 201 - a - b - c, 20)
          for e in range(0, 201 - a - b - c - d, 10)
          for f in range(0, 201 - a - b - c - d - e, 5)
          for g in range(0, 201 - a - b - c - d - e - f, 2)))
