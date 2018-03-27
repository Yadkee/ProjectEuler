#! python3
from os import listdir
from os.path import join

with open(join("files", "readme_preset.txt"), "rb") as f:
    preset = f.read()
with open(join("files", "index.txt")) as f:
    index = f.read().splitlines()
text = []
problemFolders = sorted((i for i in listdir(path=".")
                         if i.startswith("problems[")), reverse=False)
for folder in problemFolders:
    problemPath = join(".", folder)
    githubPath = "/%s/" % folder
    problems = sorted(listdir(path=problemPath), reverse=False)
    for path in problems:
        n = int(path.strip(".py")[-3:])
        text.append("- [%s](%s%s)" % (index[n], githubPath, path))

with open("README.md", "wb") as f:
    f.write(preset % ("\n".join(text)).encode())
