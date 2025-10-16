# copy of the given file

with open("problem7.txt") as f:
    content = f.read()


with open("problem7_copy.txt", "w") as f:
    f.write(content)