#! python3
"""What is the index of the first term in the
Fibonacci sequence to contain 1000 digits?"""


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = a + b, a

for a, i in enumerate(fib()):
    if len(str(i)) == 1000:
        print(a + 2)
        break
