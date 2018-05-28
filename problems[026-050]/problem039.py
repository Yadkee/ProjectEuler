#! python3
"""If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?"""


def squares_range(a, b):
    yield from ((a + index, i) for (index, i) in enumerate(SQUARES[a:b]))


def solutions(p):
    return sum(1 for i, i2 in squares_range(3, p // 3)
               for j, j2 in squares_range(i, (p - i) // 2 + 1)
               if i2 + j2 == SQUARES[p - i - j])

SQUARES = [i * i for i in range(1001)]
print(max(range(3, 1001), key=solutions))
