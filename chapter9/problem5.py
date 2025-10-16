words = ["hello", "goal", "doing", "how", "try"]

with open("problem5.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("problem5.txt", "w") as f:
    f.write(content)