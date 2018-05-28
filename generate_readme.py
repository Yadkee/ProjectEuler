#! python3
from os import listdir
from os.path import join

N = 2

with open(join("files", "readme_preset.txt"), "rb") as f:
    preset = f.read()
with open(join("files", "index.txt")) as f:
    index = f.read().splitlines()
cells = [[[". " * 50] * 25 for c in range(N)] for r in range(24 // N)]
problemFolders = sorted((i for i in listdir(path=".")
                         if i.startswith("problems[")), reverse=False)
for folder in problemFolders:
    problemPath = join(".", folder)
    githubPath = "/%s/" % folder
    problems = sorted(listdir(path=problemPath), reverse=False)
    for path in problems:
        n = int(path.strip(".py")[-3:]) - 1
        r, c = (n // 25) // N, (n // 25) % N
        name = "%d.- %s" % (n + 1, index[n + 1].split("\t", 1)[1])
        cells[r][c][n % 25] = "[%s](%s%s)" % (name, githubPath, path)


def html_list(l):
    return "\n\n".join(l)


def html_table(l):
    td = "<td width=%d%s>\n\n%s</td>" % (100 // N, "%%", "%s")
    return "<tr width>%s</tr>" % "".join(td % i for i in l)

table = "\n".join(html_table(html_list(item) for item in row)
                  for row in cells if row != cells[-1]).encode()
with open("README.md", "wb") as f:
    f.write(preset % table)
