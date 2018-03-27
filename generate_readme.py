#! python3
from os import listdir
from os.path import join

with open("readme_preset.txt", "rb") as f:
    preset = f.read()
with open("index.txt") as f:
    index = f.read().splitlines()
text = []
for i, j in zip(range(1, 1000, 25), range(25, 1000, 25)):
    segment = "problems[%d-%d]" % (i, j)
    problemPath = join(".", segment)
    githubPath = "/%s/problem" % segment
    try:
        problems = tuple(sorted(listdir(path=problemPath), reverse=True))
    except FileNotFoundError:
        break
    for a, path in enumerate(problems):
        n = a + i
        text.append("- [%s](%s%03d.py)" % (index[n], githubPath, n))

with open("README.md", "wb") as f:
    f.write(preset % ("\n".join(text)).encode())
