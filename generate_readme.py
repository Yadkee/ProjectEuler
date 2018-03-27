#! python3
from os import listdir
from os.path import join

with open(join("files", "readme_preset.txt"), "rb") as f:
    preset = f.read()
with open(join("files", "index.txt")) as f:
    index = f.read().splitlines()
text = []
for i, j in zip(range(1, 1000, 25), range(25, 1000, 25)):
    segment = "problems[%d-%d]" % (i, j)
    problemPath = join(".", segment)
    githubPath = "/%s/" % segment
    try:
        problems = tuple(sorted(listdir(path=problemPath), reverse=False))
    except FileNotFoundError:
        break
    for path in problems:
        n = int(path.strip(".py")[-3:])
        text.append("- [%s](%s%s)" % (index[n], githubPath, path))

with open("README.md", "wb") as f:
    f.write(preset % ("\n".join(text)).encode())
