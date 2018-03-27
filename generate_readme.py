#! python3
from os import listdir
from os.path import join

with open(join("files", "readme_preset.txt"), "rb") as f:
    preset = f.read()
with open(join("files", "index.txt")) as f:
    index = f.read().splitlines()
cells = [[[], [], [], []],
         [[], [], [], []],
         [[], [], [], []],
         [[], [], [], []],
         [[], [], [], []],
         [[], [], [], []]]
problemFolders = sorted((i for i in listdir(path=".")
                         if i.startswith("problems[")), reverse=False)
for folder in problemFolders:
    problemPath = join(".", folder)
    githubPath = "/%s/" % folder
    problems = sorted(listdir(path=problemPath), reverse=False)
    for path in problems:
        n = int(path.strip(".py")[-3:])
        r, c = (n // 25) // 4, (n // 25) % 4
        cells[r][c].append("[%s](%s%s)" % (index[n], githubPath, path))
voidRow = [[]] * 4


def html_list(l):
    return "\n\n".join(l)


def html_table(l):
    return "<tr>%s</tr>" % "".join("<td>\n\n%s</td>" % i for i in l)

with open("README.md", "wb") as f:
    f.write(preset % ("\n".join(html_table(html_list(item) for item in row)
                                for row in cells if row != voidRow)).encode())
