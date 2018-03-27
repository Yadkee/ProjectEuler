#! python3
from os import listdir
from os.path import join

with open(join("files", "readme_preset.txt"), "rb") as f:
    preset = f.read()
with open(join("files", "index.txt")) as f:
    index = f.read().splitlines()
newLined = ["?"] * 25
cells = []
for i in range(8):
    row = []
    for j in range(4):
        row.append(newLined[:])
    cells.append(row)
problemFolders = sorted((i for i in listdir(path=".")
                         if i.startswith("problems[")), reverse=False)
for folder in problemFolders:
    problemPath = join(".", folder)
    githubPath = "/%s/" % folder
    problems = sorted(listdir(path=problemPath), reverse=False)
    for path in problems:
        n = int(path.strip(".py")[-3:]) - 1
        r, c = (n // 25) // 4, (n // 25) % 4
        cells[r][c][n % 25] = "[%s](%s%s)" % (index[n + 1], githubPath, path)


def html_list(l):
    return "\n\n".join(l)


def html_table(l):
    return "<tr>%s</tr>" % "".join("<td>\n\n%s</td>" % i for i in l)

table = "\n".join(html_table(html_list(item) for item in row)
                  for row in cells if row != cells[-1]).encode()
with open("README.md", "wb") as f:
    f.write(preset % table)
