#! python3
"""Find the maximum total from top to bottom in triangle.txt,
a 15K text file containing a triangle with one-hundred rows."""
from os.path import join

with open(join("..", "files", "p067_triangle.txt")) as f:
    triangle = f.read()

with open(join("..", "problems[1-25]", "problem018.py")) as f:
    exec(f.read().split("\n\n\n")[1])

print(solve(triangle))